from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import date
from database.db import fetch_all, fetch_one, insert_and_get_id, execute_query

police_bp = Blueprint('police', __name__)

def login_required_police():
    return session.get('role') == 'police' and 'police_id' in session

@police_bp.route('/police/dashboard')
def dashboard():
    if not login_required_police():
        flash('Please login as a Police Officer to access the police portal.', 'warning')
        return redirect(url_for('auth.login'))

    police_id = session['police_id']

    try:
        # Officer details
        officer = fetch_one(
            """
            SELECT p.*,
                   COALESCE(ps.Station_Name, 'Central Police Station') as Station_Name,
                   COALESCE(ps.City, 'Metropolitan') as City,
                   COALESCE(ps.Jurisdiction, 'Central District') as Station_Jurisdiction
            FROM Police p
            LEFT JOIN PoliceStation ps ON p.Station_ID = ps.Station_ID
            WHERE p.Police_ID = %s
            """,
            (police_id,)
        )

        if not officer:
            officer = {
                'Name': session.get('name', 'Officer'),
                'police_rank': session.get('police_rank', 'Inspector'),
                'Badge_Number': session.get('badge_number', 'N/A'),
                'Station_Name': session.get('station_name', 'Central Command'),
                'Station_Jurisdiction': 'City Wide'
            }

        # Metrics
        res_assigned = fetch_one("SELECT COUNT(*) as count FROM Investigation WHERE Police_ID = %s", (police_id,))
        assigned_count = res_assigned['count'] if res_assigned else 0

        res_active = fetch_one("SELECT COUNT(*) as count FROM Investigation WHERE Police_ID = %s AND (Status IS NULL OR Status != 'Completed')", (police_id,))
        active_count = res_active['count'] if res_active else 0

        res_completed = fetch_one("SELECT COUNT(*) as count FROM Investigation WHERE Police_ID = %s AND Status = 'Completed'", (police_id,))
        completed_count = res_completed['count'] if res_completed else 0

        res_court = fetch_one(
            """
            SELECT COUNT(*) as count
            FROM Investigation i
            JOIN FIR f ON i.FIR_ID = f.FIR_ID
            WHERE i.Police_ID = %s AND f.Status IN ('Case In Court', 'Under Trial', 'Chargesheet Filed')
            """,
            (police_id,)
        )
        court_cases_count = res_court['count'] if res_court else 0

        # Assigned FIRs table
        assigned_firs = fetch_all(
            """
            SELECT f.FIR_ID, f.FIR_Number, f.Crime_Type, f.Date_Filed, f.Status as FIR_Status, f.Last_Updated,
                   u.Name as Complainant_Name, u.Phone as Complainant_Phone,
                   i.Investigation_ID, i.Status as Investigation_Status, i.Start_Date, i.Findings
            FROM Investigation i
            JOIN FIR f ON i.FIR_ID = f.FIR_ID
            JOIN User u ON f.User_ID = u.User_ID
            WHERE i.Police_ID = %s
            ORDER BY f.FIR_ID DESC
            """,
            (police_id,)
        ) or []

        # Also get other station / unassigned FIRs in officer's jurisdiction
        other_firs = fetch_all(
            """
            SELECT f.FIR_ID, f.FIR_Number, f.Crime_Type, f.Date_Filed, f.Status as FIR_Status, f.Jurisdiction,
                   u.Name as Complainant_Name,
                   i.Investigation_ID, p.Name as Assigned_Officer
            FROM FIR f
            JOIN User u ON f.User_ID = u.User_ID
            LEFT JOIN Investigation i ON f.FIR_ID = i.FIR_ID
            LEFT JOIN Police p ON i.Police_ID = p.Police_ID
            WHERE i.Police_ID != %s OR i.Police_ID IS NULL
            ORDER BY f.FIR_ID DESC
            LIMIT 10
            """,
            (police_id,)
        ) or []

        metrics = {
            'assigned_count': assigned_count,
            'active_count': active_count,
            'completed_count': completed_count,
            'court_cases_count': court_cases_count
        }

        return render_template(
            'police_dashboard.html',
            officer=officer,
            assigned_firs=assigned_firs,
            other_firs=other_firs,
            metrics=metrics
        )

    except Exception as e:
        flash(f"Error loading police dashboard: {str(e)}", 'danger')
        fallback_officer = {
            'Name': session.get('name', 'Officer'),
            'police_rank': session.get('police_rank', 'Inspector'),
            'Badge_Number': session.get('badge_number', 'N/A'),
            'Station_Name': session.get('station_name', 'Central Command'),
            'Station_Jurisdiction': 'City Wide'
        }
        return render_template('police_dashboard.html', officer=fallback_officer, assigned_firs=[], other_firs=[], metrics={'assigned_count': 0, 'active_count': 0, 'completed_count': 0, 'court_cases_count': 0})


@police_bp.route('/police/fir/<int:fir_id>')
def police_fir_view(fir_id):
    if not login_required_police():
        flash('Police login required.', 'warning')
        return redirect(url_for('auth.login'))

    police_id = session['police_id']

    try:
        # Check FIR
        fir = fetch_one(
            """
            SELECT f.*, u.Name as Complainant_Name, u.Email as Complainant_Email,
                   u.Phone as Complainant_Phone, u.Residential_Address as Complainant_Address
            FROM FIR f
            JOIN User u ON f.User_ID = u.User_ID
            WHERE f.FIR_ID = %s
            """,
            (fir_id,)
        )

        if not fir:
            flash('FIR not found.', 'danger')
            return redirect(url_for('police.dashboard'))

        # Investigation record
        investigation = fetch_one(
            """
            SELECT i.*, p.Name as Officer_Name, p.Badge_Number, p.police_rank,
                   ps.Station_Name, ps.City
            FROM Investigation i
            JOIN Police p ON i.Police_ID = p.Police_ID
            JOIN PoliceStation ps ON p.Station_ID = ps.Station_ID
            WHERE i.FIR_ID = %s
            """,
            (fir_id,)
        )

        # Status History
        history = fetch_all(
            "SELECT * FROM FIR_Status_History WHERE FIR_ID = %s ORDER BY Updated_Date ASC, History_ID ASC",
            (fir_id,)
        )

        # Evidence
        evidence = fetch_all(
            """
            SELECT e.*, p.Name as Collected_By_Name, p.Badge_Number
            FROM Evidence e
            JOIN Police p ON e.Collected_By = p.Police_ID
            WHERE e.FIR_ID = %s
            ORDER BY e.Evidence_ID ASC
            """,
            (fir_id,)
        )

        # Accused Criminals
        criminals = fetch_all(
            """
            SELECT c.*, fc.Role, fc.Accused_Status
            FROM FIR_Criminal fc
            JOIN Criminal c ON fc.Criminal_ID = c.Criminal_ID
            WHERE fc.FIR_ID = %s
            """,
            (fir_id,)
        )

        # All criminals list for associating new suspect
        all_criminals = fetch_all("SELECT * FROM Criminal ORDER BY Name ASC")

        # Court Case, Hearings, Judgment
        case = fetch_one(
            """
            SELECT c.*, ct.Court_Name, ct.Court_Type, ct.Location as Court_Location, ct.Judge_Name
            FROM `Case` c
            JOIN Court ct ON c.Court_ID = ct.Court_ID
            WHERE c.FIR_ID = %s
            """,
            (fir_id,)
        )

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

        status_choices = [
            "FIR Registered",
            "Under Investigation",
            "Evidence Collected",
            "Investigation Completed",
            "Chargesheet Filed",
            "Case In Court",
            "Under Trial",
            "Case Closed"
        ]

        return render_template(
            'police_fir.html',
            fir=fir,
            investigation=investigation,
            history=history,
            evidence=evidence,
            criminals=criminals,
            all_criminals=all_criminals,
            case=case,
            hearings=hearings,
            judgment=judgment,
            status_choices=status_choices
        )

    except Exception as e:
        flash(f"Error loading FIR details for police: {str(e)}", 'danger')
        return redirect(url_for('police.dashboard'))


@police_bp.route('/police/fir/<int:fir_id>/status', methods=['POST'])
def update_fir_status(fir_id):
    if not login_required_police():
        flash('Police login required.', 'warning')
        return redirect(url_for('auth.login'))

    new_status = request.form.get('status', '').strip()
    remarks = request.form.get('remarks', '').strip()
    officer_name = session.get('name', 'Police Officer')
    police_id = session.get('police_id')
    today = date.today()

    if not new_status:
        flash('Please select a valid status.', 'danger')
        return redirect(url_for('police.police_fir_view', fir_id=fir_id))

    try:
        # 1. Update FIR status & Last_Updated
        execute_query(
            "UPDATE FIR SET Status = %s, Last_Updated = %s WHERE FIR_ID = %s",
            (new_status, today, fir_id)
        )

        # 2. Insert into FIR_Status_History
        insert_and_get_id(
            """
            INSERT INTO FIR_Status_History (FIR_ID, Status, Updated_Date, Updated_By, Remarks)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (fir_id, new_status, today, officer_name, remarks or f"Status updated to {new_status}")
        )

        # 3. Update or create Investigation record if needed
        existing_inv = fetch_one("SELECT Investigation_ID FROM Investigation WHERE FIR_ID = %s", (fir_id,))
        if existing_inv:
            inv_status = 'Ongoing'
            chargesheet_date = None
            if new_status in ['Investigation Completed', 'Chargesheet Filed', 'Case In Court', 'Case Closed']:
                inv_status = 'Completed'
            if new_status == 'Chargesheet Filed':
                chargesheet_date = today

            if chargesheet_date:
                execute_query(
                    "UPDATE Investigation SET Status = %s, Chargesheet_Date = %s WHERE FIR_ID = %s",
                    (inv_status, chargesheet_date, fir_id)
                )
            else:
                execute_query(
                    "UPDATE Investigation SET Status = %s WHERE FIR_ID = %s",
                    (inv_status, fir_id)
                )
        else:
            # Create investigation assignment to this officer
            insert_and_get_id(
                """
                INSERT INTO Investigation (FIR_ID, Police_ID, Start_Date, Status, Remarks)
                VALUES (%s, %s, %s, 'Ongoing', 'Investigation initiated by officer.')
                """,
                (fir_id, police_id, today)
            )

        flash(f"FIR status successfully updated to '{new_status}'.", 'success')
        return redirect(url_for('police.police_fir_view', fir_id=fir_id))

    except Exception as e:
        flash(f"Error updating status: {str(e)}", 'danger')
        return redirect(url_for('police.police_fir_view', fir_id=fir_id))


@police_bp.route('/police/fir/<int:fir_id>/evidence/add', methods=['GET', 'POST'])
def add_evidence(fir_id):
    if not login_required_police():
        flash('Police login required.', 'warning')
        return redirect(url_for('auth.login'))

    police_id = session['police_id']

    if request.method == 'POST':
        evidence_type = request.form.get('evidence_type', '').strip()
        description = request.form.get('description', '').strip()
        collected_date = request.form.get('collected_date', '').strip() or str(date.today())
        storage_location = request.form.get('storage_location', '').strip()
        status = request.form.get('status', 'Under Review').strip()

        if not evidence_type or not description or not storage_location:
            flash('Evidence Type, Description, and Storage Location are required.', 'danger')
            return redirect(url_for('police.add_evidence', fir_id=fir_id))

        try:
            # Insert into Evidence
            insert_and_get_id(
                """
                INSERT INTO Evidence (FIR_ID, Evidence_Type, Description, Collected_Date, Storage_Location, Status, Collected_By)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (fir_id, evidence_type, description, collected_date, storage_location, status, police_id)
            )

            # Also log into FIR_Status_History if not already logged
            officer_name = session.get('name', 'Police Officer')
            insert_and_get_id(
                """
                INSERT INTO FIR_Status_History (FIR_ID, Status, Updated_Date, Updated_By, Remarks)
                VALUES (%s, 'Evidence Collected', %s, %s, %s)
                """,
                (fir_id, date.today(), officer_name, f"New evidence added: {evidence_type} ({storage_location})")
            )

            flash('Evidence successfully registered and logged in FIR history.', 'success')
            return redirect(url_for('police.police_fir_view', fir_id=fir_id))

        except Exception as e:
            flash(f"Error adding evidence: {str(e)}", 'danger')

    # Fetch FIR summary for the form
    fir = fetch_one("SELECT * FROM FIR WHERE FIR_ID = %s", (fir_id,))
    return render_template('add_evidence.html', fir=fir)


@police_bp.route('/police/fir/<int:fir_id>/criminal/add', methods=['POST'])
def add_criminal_to_fir(fir_id):
    if not login_required_police():
        flash('Police login required.', 'warning')
        return redirect(url_for('auth.login'))

    criminal_id = request.form.get('criminal_id')
    role = request.form.get('role', 'Accused').strip()
    accused_status = request.form.get('accused_status', 'Under Investigation').strip()

    if not criminal_id:
        flash('Please select a criminal.', 'danger')
        return redirect(url_for('police.police_fir_view', fir_id=fir_id))

    try:
        # Check if relation already exists
        existing = fetch_one(
            "SELECT * FROM FIR_Criminal WHERE FIR_ID = %s AND Criminal_ID = %s",
            (fir_id, criminal_id)
        )
        if existing:
            execute_query(
                "UPDATE FIR_Criminal SET Role = %s, Accused_Status = %s WHERE FIR_ID = %s AND Criminal_ID = %s",
                (role, accused_status, fir_id, criminal_id)
            )
            flash('Accused criminal details updated.', 'info')
        else:
            execute_query(
                "INSERT INTO FIR_Criminal (FIR_ID, Criminal_ID, Role, Accused_Status) VALUES (%s, %s, %s, %s)",
                (fir_id, criminal_id, role, accused_status)
            )
            flash('Criminal successfully linked to FIR record.', 'success')

        return redirect(url_for('police.police_fir_view', fir_id=fir_id))

    except Exception as e:
        flash(f"Error linking criminal: {str(e)}", 'danger')
        return redirect(url_for('police.police_fir_view', fir_id=fir_id))


@police_bp.route('/police/firs', methods=['GET'])
def get_police_firs_api():
    """API endpoint to get assigned FIRs for police."""
    if not login_required_police():
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        police_id = session['police_id']
        firs = fetch_all(
            """
            SELECT f.FIR_ID, f.FIR_Number, f.Crime_Type, f.Date_Filed, f.Status as FIR_Status,
                   u.Name as Complainant_Name, i.Status as Investigation_Status
            FROM Investigation i
            JOIN FIR f ON i.FIR_ID = f.FIR_ID
            JOIN User u ON f.User_ID = u.User_ID
            WHERE i.Police_ID = %s
            ORDER BY f.FIR_ID DESC
            """,
            (police_id,)
        )
        return jsonify({'firs': firs})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
