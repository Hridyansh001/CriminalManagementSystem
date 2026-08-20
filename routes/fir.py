from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import date
from database.db import fetch_all, fetch_one, insert_and_get_id, execute_query

fir_bp = Blueprint('fir', __name__)

@fir_bp.route('/fir/<int:fir_id>')
def fir_details(fir_id):
    """Complete FIR Details and Tracking Page for Citizen / Police."""
    if 'user_id' not in session and 'police_id' not in session:
        flash('Please login to track FIR details.', 'warning')
        return redirect(url_for('auth.login'))

    try:
        # 1. Fetch FIR Info & Complainant
        fir = fetch_one(
            """
            SELECT f.*, u.Name as Complainant_Name, u.Email as Complainant_Email,
                   u.Phone as Complainant_Phone, u.Gender as Complainant_Gender,
                   u.Residential_Address as Complainant_Address,
                   ps.Station_Name, ps.City as Station_City, ps.Jurisdiction as Station_Jurisdiction
            FROM FIR f
            LEFT JOIN User u ON f.User_ID = u.User_ID
            LEFT JOIN PoliceStation ps ON f.Jurisdiction = ps.Jurisdiction OR f.Location LIKE CONCAT('%%', ps.City, '%%')
            WHERE f.FIR_ID = %s
            """,
            (fir_id,)
        )

        if not fir:
            flash('FIR record not found.', 'danger')
            return redirect(url_for('user.dashboard') if session.get('role') == 'user' else url_for('police.dashboard'))

        # 2. Fetch Status History for Timeline
        history = fetch_all(
            "SELECT * FROM FIR_Status_History WHERE FIR_ID = %s ORDER BY Updated_Date ASC, History_ID ASC",
            (fir_id,)
        )

        # 3. Fetch Investigation Details
        investigation = fetch_one(
            """
            SELECT i.*, p.Name as Officer_Name, p.Badge_Number, p.police_rank, p.Phone as Officer_Phone,
                   ps.Station_Name, ps.Address as Station_Address, ps.City as Station_City, ps.Jurisdiction as Station_Jurisdiction
            FROM Investigation i
            LEFT JOIN Police p ON i.Police_ID = p.Police_ID
            LEFT JOIN PoliceStation ps ON p.Station_ID = ps.Station_ID
            WHERE i.FIR_ID = %s
            """,
            (fir_id,)
        )

        # 4. Fetch Accused Criminals
        criminals = fetch_all(
            """
            SELECT c.Criminal_ID, c.Name, c.National_ID, c.Status as Criminal_Status,
                   c.Level_of_Crime, c.Aliases, c.Living_Status,
                   fc.Role, fc.Accused_Status
            FROM FIR_Criminal fc
            JOIN Criminal c ON fc.Criminal_ID = c.Criminal_ID
            WHERE fc.FIR_ID = %s
            """,
            (fir_id,)
        )

        # 5. Fetch Evidence
        evidence = fetch_all(
            """
            SELECT e.*, p.Name as Collected_By_Name, p.Badge_Number
            FROM Evidence e
            LEFT JOIN Police p ON e.Collected_By = p.Police_ID
            WHERE e.FIR_ID = %s
            ORDER BY e.Evidence_ID ASC
            """,
            (fir_id,)
        )

        # 6. Fetch Court Case
        case = fetch_one(
            """
            SELECT c.*, ct.Court_Name, ct.Court_Type, ct.Location as Court_Location, ct.Judge_Name
            FROM `Case` c
            LEFT JOIN Court ct ON c.Court_ID = ct.Court_ID
            WHERE c.FIR_ID = %s
            """,
            (fir_id,)
        )

        # 7. Fetch Hearings and Judgment if case exists
        hearings = []
        judgment = None
        if case:
            hearings = fetch_all(
                "SELECT * FROM Hearing WHERE Case_ID = %s ORDER BY Hearing_Date ASC, Hearing_Time ASC",
                (case['Case_ID'],)
            )
            judgment = fetch_one(
                "SELECT * FROM Judgment WHERE Case_ID = %s",
                (case['Case_ID'],)
            )

        # Pipeline Milestones Calculation
        pipeline_stages = [
            {'name': 'FIR Registered', 'code': 'registered'},
            {'name': 'Investigation Started', 'code': 'investigation'},
            {'name': 'Evidence Collected', 'code': 'evidence'},
            {'name': 'Chargesheet Filed', 'code': 'chargesheet'},
            {'name': 'Case In Court', 'code': 'court'},
            {'name': 'Judgment', 'code': 'judgment'}
        ]

        reached_statuses = set()
        for h in history:
            stat = h['Status'].lower()
            if 'registered' in stat:
                reached_statuses.add('registered')
            if 'investigation' in stat or 'under investigation' in stat or 'started' in stat:
                reached_statuses.add('registered')
                reached_statuses.add('investigation')
            if 'evidence' in stat:
                reached_statuses.add('registered')
                reached_statuses.add('investigation')
                reached_statuses.add('evidence')
            if 'chargesheet' in stat or 'completed' in stat:
                reached_statuses.add('registered')
                reached_statuses.add('investigation')
                reached_statuses.add('evidence')
                reached_statuses.add('chargesheet')
            if 'court' in stat or 'trial' in stat:
                reached_statuses.add('registered')
                reached_statuses.add('investigation')
                reached_statuses.add('evidence')
                reached_statuses.add('chargesheet')
                reached_statuses.add('court')
            if 'closed' in stat or 'judgment' in stat:
                reached_statuses.add('registered')
                reached_statuses.add('investigation')
                reached_statuses.add('evidence')
                reached_statuses.add('chargesheet')
                reached_statuses.add('court')
                reached_statuses.add('judgment')

        if case:
            reached_statuses.add('court')
        if judgment or fir['Status'] in ['Case Closed', 'Closed']:
            reached_statuses.add('judgment')

        return render_template(
            'fir_details.html',
            fir=fir,
            history=history,
            investigation=investigation,
            criminals=criminals,
            evidence=evidence,
            case=case,
            hearings=hearings,
            judgment=judgment,
            pipeline_stages=pipeline_stages,
            reached_statuses=reached_statuses
        )

    except Exception as e:
        flash(f"Error loading FIR details: {str(e)}", 'danger')
        return redirect(url_for('user.dashboard') if session.get('role') == 'user' else url_for('police.dashboard'))


@fir_bp.route('/cases')
@fir_bp.route('/all-firs')
def cases_list():
    """Directory of all FIR dockets in the system."""
    if 'user_id' not in session and 'police_id' not in session:
        flash('Please login to view FIR records.', 'warning')
        return redirect(url_for('auth.login'))

    try:
        q = request.args.get('q', '').strip()
        status = request.args.get('status', '').strip()

        sql = """
            SELECT f.*, u.Name as Complainant_Name, u.Email as Complainant_Email,
                   p.Name as Officer_Name, i.Status as Investigation_Status
            FROM FIR f
            LEFT JOIN User u ON f.User_ID = u.User_ID
            LEFT JOIN Investigation i ON f.FIR_ID = i.FIR_ID
            LEFT JOIN Police p ON i.Police_ID = p.Police_ID
            WHERE 1=1
        """
        params = []

        if q:
            sql += " AND (f.FIR_Number LIKE %s OR f.Crime_Type LIKE %s OR f.Location LIKE %s OR u.Name LIKE %s)"
            pattern = f"%{q}%"
            params.extend([pattern, pattern, pattern, pattern])

        if status:
            sql += " AND f.Status = %s"
            params.append(status)

        sql += " ORDER BY f.FIR_ID DESC"

        firs = fetch_all(sql, tuple(params) if params else None)
        return render_template('cases_list.html', firs=firs, q=q, status=status)

    except Exception as e:
        flash(f"Error loading FIR list: {str(e)}", 'danger')
        return render_template('cases_list.html', firs=[])


@fir_bp.route('/criminals')
def criminals_list():
    """Directory of all recorded criminals in the system."""
    try:
        q = request.args.get('q', '').strip()
        status = request.args.get('status', '').strip()

        sql = """
            SELECT c.*, COUNT(fc.FIR_ID) as Linked_FIR_Count
            FROM Criminal c
            LEFT JOIN FIR_Criminal fc ON c.Criminal_ID = fc.Criminal_ID
            WHERE 1=1
        """
        params = []
        if q:
            sql += " AND (c.Name LIKE %s OR c.Aliases LIKE %s OR c.National_ID LIKE %s)"
            pattern = f"%{q}%"
            params.extend([pattern, pattern, pattern])
        if status:
            sql += " AND c.Status = %s"
            params.append(status)

        sql += " GROUP BY c.Criminal_ID ORDER BY c.Name ASC"
        criminals = fetch_all(sql, tuple(params) if params else None)

        status_choices = ['Accused', 'Wanted', 'In Custody', 'Convicted', 'Acquitted', 'Under Investigation']
        return render_template('criminals.html', records=criminals, criminals=criminals, q=q, status=status, status_choices=status_choices)

    except Exception as e:
        flash(f"Error fetching criminals: {str(e)}", 'danger')
        return render_template('criminals.html', records=[], criminals=[], status_choices=[])


@fir_bp.route('/criminal/<int:criminal_id>')
def criminal_view(criminal_id):
    """Detailed dossier for a specific criminal."""
    try:
        criminal = fetch_one("SELECT * FROM Criminal WHERE Criminal_ID = %s", (criminal_id,))
        if not criminal:
            flash('Criminal profile not found.', 'danger')
            return redirect(url_for('fir.criminals_list'))

        linked_firs = fetch_all(
            """
            SELECT f.*, fc.Role, fc.Accused_Status
            FROM FIR_Criminal fc
            JOIN FIR f ON fc.FIR_ID = f.FIR_ID
            WHERE fc.Criminal_ID = %s
            ORDER BY f.FIR_ID DESC
            """,
            (criminal_id,)
        )

        return render_template('criminal_view.html', record=criminal, criminal=criminal, linked_firs=linked_firs)

    except Exception as e:
        flash(f"Error loading criminal dossier: {str(e)}", 'danger')
        return redirect(url_for('fir.criminals_list'))


@fir_bp.route('/criminal/add', methods=['GET', 'POST'])
def criminal_add():
    if session.get('role') != 'police':
        flash('Officer access required to register new criminal records.', 'warning')
        return redirect(url_for('fir.criminals_list'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        national_id = request.form.get('national_id', '').strip() or None
        status = request.form.get('status', 'Accused').strip()
        level = request.form.get('level_of_crime', 'Medium').strip()
        aliases = request.form.get('aliases', '').strip() or None
        living_status = request.form.get('living_status', 'Alive').strip()

        if not name:
            flash('Name is required.', 'danger')
            return render_template('criminal_form.html')

        try:
            cid = insert_and_get_id(
                """
                INSERT INTO Criminal (Name, National_ID, Status, Level_of_Crime, Aliases, Living_Status)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (name, national_id, status, level, aliases, living_status)
            )
            flash(f"Criminal profile '{name}' registered successfully.", 'success')
            return redirect(url_for('fir.criminal_view', criminal_id=cid))
        except Exception as e:
            flash(f"Error adding criminal: {str(e)}", 'danger')

    return render_template('criminal_form.html')


# ==========================================
# REST API ENDPOINTS
# ==========================================

@fir_bp.route('/firs/<int:fir_id>', methods=['GET'])
def api_get_fir(fir_id):
    try:
        fir = fetch_one("SELECT * FROM FIR WHERE FIR_ID = %s", (fir_id,))
        if not fir:
            return jsonify({'error': 'FIR not found'}), 404
        return jsonify(fir)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@fir_bp.route('/firs/<int:fir_id>/status', methods=['PUT', 'POST'])
def api_update_fir_status(fir_id):
    data = request.get_json() or request.form
    new_status = data.get('status')
    remarks = data.get('remarks', 'Status updated via API')
    updated_by = session.get('name', data.get('updated_by', 'Officer'))

    if not new_status:
        return jsonify({'error': 'Status is required'}), 400

    try:
        today = date.today()
        execute_query("UPDATE FIR SET Status = %s, Last_Updated = %s WHERE FIR_ID = %s", (new_status, today, fir_id))
        insert_and_get_id(
            "INSERT INTO FIR_Status_History (FIR_ID, Status, Updated_Date, Updated_By, Remarks) VALUES (%s, %s, %s, %s, %s)",
            (fir_id, new_status, today, updated_by, remarks)
        )
        return jsonify({'message': 'FIR status updated successfully', 'status': new_status})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@fir_bp.route('/firs/<int:fir_id>/history', methods=['GET'])
def api_get_fir_history(fir_id):
    try:
        history = fetch_all("SELECT * FROM FIR_Status_History WHERE FIR_ID = %s ORDER BY Updated_Date ASC, History_ID ASC", (fir_id,))
        return jsonify({'history': history})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@fir_bp.route('/firs/<int:fir_id>/criminals', methods=['GET'])
def api_get_fir_criminals(fir_id):
    try:
        criminals = fetch_all(
            """
            SELECT c.*, fc.Role, fc.Accused_Status
            FROM FIR_Criminal fc
            JOIN Criminal c ON fc.Criminal_ID = c.Criminal_ID
            WHERE fc.FIR_ID = %s
            """,
            (fir_id,)
        )
        return jsonify({'criminals': criminals})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@fir_bp.route('/firs/<int:fir_id>/evidence', methods=['GET', 'POST'])
def api_fir_evidence(fir_id):
    if request.method == 'POST':
        data = request.get_json() or request.form
        evidence_type = data.get('evidence_type')
        description = data.get('description')
        collected_date = data.get('collected_date', str(date.today()))
        storage_location = data.get('storage_location')
        status = data.get('status', 'Under Review')
        collected_by = session.get('police_id', data.get('collected_by', 1))

        if not evidence_type or not storage_location:
            return jsonify({'error': 'Evidence Type and Storage Location are required'}), 400

        try:
            ev_id = insert_and_get_id(
                """
                INSERT INTO Evidence (FIR_ID, Evidence_Type, Description, Collected_Date, Storage_Location, Status, Collected_By)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (fir_id, evidence_type, description, collected_date, storage_location, status, collected_by)
            )
            return jsonify({'message': 'Evidence recorded', 'evidence_id': ev_id}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    try:
        evidence = fetch_all("SELECT * FROM Evidence WHERE FIR_ID = %s", (fir_id,))
        return jsonify({'evidence': evidence})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
