from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import date
from database.db import fetch_all, fetch_one, insert_and_get_id, execute_query

user_bp = Blueprint('user', __name__)

def login_required_user():
    return session.get('role') == 'user' and 'user_id' in session

@user_bp.route('/dashboard')
def dashboard():
    if not login_required_user():
        flash('Please login as a Citizen / User to access this page.', 'warning')
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    
    try:
        # Fetch user details
        user = fetch_one("SELECT * FROM User WHERE User_ID = %s", (user_id,))

        # Fetch metrics
        res_total = fetch_one("SELECT COUNT(*) as count FROM FIR WHERE User_ID = %s", (user_id,))
        total_firs = res_total['count'] if res_total else 0

        res_active = fetch_one(
            "SELECT COUNT(*) as count FROM FIR WHERE User_ID = %s AND Status NOT IN ('Case Closed', 'Closed')",
            (user_id,)
        )
        active_firs = res_active['count'] if res_active else 0

        res_court = fetch_one(
            "SELECT COUNT(*) as count FROM FIR WHERE User_ID = %s AND Status IN ('Case In Court', 'Under Trial')",
            (user_id,)
        )
        court_firs = res_court['count'] if res_court else 0

        res_closed = fetch_one(
            "SELECT COUNT(*) as count FROM FIR WHERE User_ID = %s AND Status IN ('Case Closed', 'Closed')",
            (user_id,)
        )
        closed_firs = res_closed['count'] if res_closed else 0

        # Fetch all FIRs filed by this user
        firs = fetch_all(
            """
            SELECT f.FIR_ID, f.FIR_Number, f.Crime_Type, f.Date_Filed, f.Location, f.Jurisdiction, f.Status, f.Last_Updated,
                   i.Investigation_ID, i.Status as Investigation_Status,
                   p.Name as Officer_Name,
                   c.Case_Number, c.Status as Case_Status
            FROM FIR f
            LEFT JOIN Investigation i ON f.FIR_ID = i.FIR_ID
            LEFT JOIN Police p ON i.Police_ID = p.Police_ID
            LEFT JOIN `Case` c ON f.FIR_ID = c.FIR_ID
            WHERE f.User_ID = %s
            ORDER BY f.FIR_ID DESC
            """,
            (user_id,)
        ) or []

        # Determine active pipeline stage for standard lifecycle timeline
        active_stage = 1
        if firs:
            latest_status = (firs[0].get('Status') or '').lower()
            if 'closed' in latest_status or 'judgment' in latest_status:
                active_stage = 6
            elif 'court' in latest_status or 'trial' in latest_status:
                active_stage = 5
            elif 'investigation' in latest_status or 'evidence' in latest_status or 'chargesheet' in latest_status:
                active_stage = 4
            elif 'registered' in latest_status:
                active_stage = 3
            else:
                active_stage = 2

        metrics = {
            'total_firs': total_firs,
            'active_firs': active_firs,
            'court_firs': court_firs,
            'closed_firs': closed_firs
        }

        return render_template('user_dashboard.html', user=user, firs=firs, metrics=metrics, active_stage=active_stage)

    except Exception as e:
        flash(f"Error loading dashboard: {str(e)}", 'danger')
        return render_template('user_dashboard.html', user={}, firs=[], metrics={'total_firs': 0, 'active_firs': 0, 'court_firs': 0, 'closed_firs': 0}, active_stage=1)


@user_bp.route('/my-firs')
@user_bp.route('/firs')
def my_firs():
    if not login_required_user():
        flash('Please login to view your FIR records.', 'warning')
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    try:
        firs = fetch_all(
            """
            SELECT f.*, i.Status as Investigation_Status, p.Name as Officer_Name,
                   c.Case_Number, c.Status as Case_Status
            FROM FIR f
            LEFT JOIN Investigation i ON f.FIR_ID = i.FIR_ID
            LEFT JOIN Police p ON i.Police_ID = p.Police_ID
            LEFT JOIN `Case` c ON f.FIR_ID = c.FIR_ID
            WHERE f.User_ID = %s
            ORDER BY f.FIR_ID DESC
            """,
            (user_id,)
        )
    except Exception:
        firs = []
    return render_template('user_dashboard.html', firs=firs, show_firs_only=True)


@user_bp.route('/my-cases')
def my_cases():
    if not login_required_user():
        flash('Please login to view your judicial cases.', 'warning')
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    try:
        cases = fetch_all(
            """
            SELECT c.*, f.FIR_Number, f.Crime_Type, ct.Court_Name, ct.Judge_Name
            FROM `Case` c
            JOIN FIR f ON c.FIR_ID = f.FIR_ID
            JOIN Court ct ON c.Court_ID = ct.Court_ID
            WHERE f.User_ID = %s
            ORDER BY c.Case_ID DESC
            """,
            (user_id,)
        )
    except Exception:
        cases = []
    return render_template('courts_list.html', cases=cases, citizen_mode=True)


@user_bp.route('/fir/new', methods=['GET', 'POST'])
def file_fir():
    if not login_required_user():
        flash('Please login to report a crime or file an FIR.', 'warning')
        return redirect(url_for('auth.login'))

    user_id = session['user_id']

    if request.method == 'POST':
        crime_type = request.form.get('crime_type', '').strip()
        description = request.form.get('description', '').strip()
        location = request.form.get('location', '').strip()
        jurisdiction = request.form.get('jurisdiction', '').strip()

        if not crime_type or not description or not location or not jurisdiction:
            flash('All fields are required to register an FIR.', 'danger')
            return redirect(url_for('user.file_fir'))

        try:
            today = date.today()
            current_year = today.year

            # Generate unique FIR Number automatically
            last_fir = fetch_one("SELECT MAX(FIR_ID) as max_id FROM FIR")
            next_num = ((last_fir['max_id'] if last_fir else 0) or 0) + 1
            fir_number = f"FIR-{current_year}-{next_num:03d}"

            # 1. Insert into FIR
            fir_id = insert_and_get_id(
                """
                INSERT INTO FIR (FIR_Number, User_ID, Date_Filed, Crime_Type, Description, Location, Jurisdiction, Status, Last_Updated)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (fir_number, user_id, today, crime_type, description, location, jurisdiction, 'FIR Registered', today)
            )

            # 2. Insert into FIR_Status_History
            insert_and_get_id(
                """
                INSERT INTO FIR_Status_History (FIR_ID, Status, Updated_Date, Updated_By, Remarks)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (fir_id, 'FIR Registered', today, session.get('name', 'Citizen'), 'FIR registered online via Citizen Portal.')
            )

            flash(f'FIR {fir_number} successfully registered and queued for police review.', 'success')
            return redirect(url_for('fir.fir_details', fir_id=fir_id))

        except Exception as e:
            flash(f"Failed to register FIR: {str(e)}", 'danger')

    # Available jurisdictions from PoliceStation
    jurisdictions = []
    try:
        jurisdictions = fetch_all("SELECT DISTINCT Jurisdiction FROM PoliceStation ORDER BY Jurisdiction")
    except Exception:
        pass

    return render_template('file_fir.html', jurisdictions=jurisdictions)


@user_bp.route('/user/firs', methods=['GET'])
def get_user_firs_api():
    """API endpoint to get user's FIRs in JSON format."""
    if not login_required_user():
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        user_id = session['user_id']
        firs = fetch_all(
            "SELECT FIR_ID, FIR_Number, Crime_Type, Date_Filed, Location, Jurisdiction, Status, Last_Updated FROM FIR WHERE User_ID = %s ORDER BY FIR_ID DESC",
            (user_id,)
        )
        return jsonify({'firs': firs})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
