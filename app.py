from flask import Flask, render_template, redirect, url_for, session, request, flash, jsonify
from config import Config
from database.db import init_db_pool, test_connection, fetch_all, fetch_one
from routes.auth import auth_bp
from routes.user import user_bp
from routes.police import police_bp
from routes.fir import fir_bp
from datetime import datetime, date, time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

STATUS_CLASS_MAP = {
    "Under Review": "st-review",
    "Pending": "st-review",
    "Verified": "st-green",
    "FIR Registered": "st-fir",
    "Registered": "st-fir",
    "Investigation": "st-investigation",
    "Under Investigation": "st-investigation",
    "Ongoing": "st-investigation",
    "Initial Investigation": "st-investigation",
    "Evidence Collected": "st-investigation",
    "Investigation Completed": "st-investigation",
    "Chargesheet Filed": "st-investigation",
    "Case In Court": "st-investigation",
    "Under Trial": "st-investigation",
    "In Custody": "st-review",
    "Wanted": "st-red",
    "Accused": "st-red",
    "Rejected": "st-red",
    "Closed": "st-closed",
    "Case Closed": "st-closed",
    "Dismissed": "st-closed",
    "Convicted": "st-red",
    "Acquitted": "st-green",
    "Released": "st-green",
    "Cleared": "st-green",
    "Completed": "st-green",
}

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Database Connection Pool
    with app.app_context():
        init_db_pool()
        connected, msg = test_connection()
        if connected:
            logger.info(f"Database status: {msg}")
        else:
            logger.warning(f"Database warning: {msg}")

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(police_bp)
    app.register_blueprint(fir_bp)

    # Context processor for current_user compatibility
    @app.context_processor
    def inject_user_context():
        role = session.get('role')
        user_name = session.get('name')
        is_auth = bool(role and ('user_id' in session or 'police_id' in session))
        
        class CurrentUserProxy:
            def __init__(self):
                self.is_authenticated = is_auth
                self.role = role
                self.Name = user_name
                self.username = user_name
                self.police_rank = session.get('police_rank')
                self.badge_number = session.get('badge_number')
                self.station_name = session.get('station_name')
                self.station_id = session.get('station_id')
                self.email = session.get('email')
                self.phone = session.get('phone')
                self.User_ID = session.get('user_id') or session.get('police_id')
                self.id = self.User_ID
        
        return {
            'current_user': CurrentUserProxy(),
            'session_role': role,
            'session_name': user_name
        }

    # Template Globals & Filters
    @app.template_global()
    @app.template_filter('status_class')
    def status_class(status):
        if not status:
            return 'st-investigation'
        return STATUS_CLASS_MAP.get(str(status).strip(), 'st-investigation')

    @app.template_global()
    def get_greeting():
        hour = datetime.now().hour
        if hour < 12:
            return "Good Morning"
        elif hour < 17:
            return "Good Afternoon"
        else:
            return "Good Evening"

    @app.template_filter('status_badge')
    def status_badge_filter(status):
        if not status:
            return 'badge-secondary'
        s = str(status).strip().lower()
        if 'registered' in s:
            return 'badge-registered'
        elif 'under investigation' in s or 'started' in s or 'initial' in s:
            return 'badge-investigating'
        elif 'evidence' in s:
            return 'badge-evidence'
        elif 'completed' in s:
            return 'badge-completed'
        elif 'chargesheet' in s:
            return 'badge-chargesheet'
        elif 'court' in s or 'trial' in s:
            return 'badge-court'
        elif 'closed' in s or 'judgment' in s or 'convicted' in s or 'guilty' in s:
            return 'badge-closed'
        return 'badge-secondary'

    @app.template_filter('format_date')
    def format_date_filter(val):
        if not val:
            return 'N/A'
        if isinstance(val, (datetime, date)):
            return val.strftime('%d %b %Y')
        try:
            d = datetime.strptime(str(val), '%Y-%m-%d')
            return d.strftime('%d %b %Y')
        except Exception:
            return str(val)

    @app.template_filter('format_time')
    def format_time_filter(val):
        if not val:
            return ''
        if isinstance(val, time):
            return val.strftime('%I:%M %p')
        return str(val)

    # ----------------------------------------------------
    # Top-Level Direct Navigation Routes & Aliases
    # ----------------------------------------------------
    @app.route('/')
    def index():
        if session.get('role') == 'user':
            return redirect(url_for('user.dashboard'))
        elif session.get('role') == 'police':
            return redirect(url_for('police.dashboard'))
        return render_template('landing.html')

    @app.route('/dashboard')
    def dashboard():
        if session.get('role') == 'user':
            return redirect(url_for('user.dashboard'))
        elif session.get('role') == 'police':
            return redirect(url_for('police.dashboard'))
        return redirect(url_for('auth.login'))

    @app.route('/login')
    def login_redirect():
        return redirect(url_for('auth.login'))

    @app.route('/register')
    def register_redirect():
        return redirect(url_for('auth.register'))

    @app.route('/logout')
    def logout_redirect():
        return redirect(url_for('auth.logout'))

    @app.route('/track')
    @app.route('/track-status')
    def track_status():
        query_id = request.args.get('q', '').strip()
        record = None
        record_type = None
        stages = []

        if query_id:
            try:
                # 1. Search FIR
                fir = fetch_one(
                    """
                    SELECT f.*, u.Name as Complainant_Name, u.Phone as Complainant_Phone
                    FROM FIR f
                    LEFT JOIN User u ON f.User_ID = u.User_ID
                    WHERE LOWER(f.FIR_Number) = LOWER(%s) OR f.FIR_ID = %s
                    """,
                    (query_id, int(query_id) if query_id.isdigit() else -1)
                )

                if fir:
                    record = fir
                    record_type = 'FIR'
                    
                    # Fetch History
                    history = fetch_all(
                        "SELECT * FROM FIR_Status_History WHERE FIR_ID = %s ORDER BY Updated_Date ASC, History_ID ASC",
                        (fir['FIR_ID'],)
                    )
                    # Investigation
                    investigation = fetch_one(
                        """
                        SELECT i.*, p.Name as Officer_Name, p.Badge_Number, p.police_rank
                        FROM Investigation i
                        LEFT JOIN Police p ON i.Police_ID = p.Police_ID
                        WHERE i.FIR_ID = %s
                        """,
                        (fir['FIR_ID'],)
                    )
                    # Case
                    case = fetch_one(
                        """
                        SELECT c.*, ct.Court_Name, ct.Judge_Name
                        FROM `Case` c
                        LEFT JOIN Court ct ON c.Court_ID = ct.Court_ID
                        WHERE c.FIR_ID = %s
                        """,
                        (fir['FIR_ID'],)
                    )

                    status_str = (fir.get('Status') or '').lower()

                    stages = [
                        {
                            'name': '1. FIR Registration',
                            'status': 'Completed',
                            'date': fir['Date_Filed'],
                            'desc': f"FIR {fir['FIR_Number']} formally registered under {fir['Crime_Type']}."
                        },
                        {
                            'name': '2. Investigation & Case Diary',
                            'status': 'Completed' if investigation and investigation.get('Status') == 'Completed' else ('In Progress' if investigation or 'investigation' in status_str else 'Pending'),
                            'date': investigation['Start_Date'] if investigation else None,
                            'desc': f"Assigned to {investigation['Officer_Name']} ({investigation['police_rank']})" if investigation and investigation.get('Officer_Name') else "Assigned to investigating officer."
                        },
                        {
                            'name': '3. Chargesheet Preparation',
                            'status': 'Completed' if (investigation and investigation.get('Chargesheet_Date')) or 'chargesheet' in status_str or 'court' in status_str or 'closed' in status_str else ('In Progress' if 'investigation completed' in status_str else 'Pending'),
                            'date': investigation['Chargesheet_Date'] if investigation else None,
                            'desc': "Chargesheet finalized and submitted for judicial trial."
                        },
                        {
                            'name': '4. Judicial Court Proceedings',
                            'status': 'Completed' if 'closed' in status_str or 'judgment' in status_str else ('In Progress' if case or 'court' in status_str or 'trial' in status_str else 'Pending'),
                            'date': case['Filing_Date'] if case else None,
                            'desc': f"Under trial at {case['Court_Name']} (Judge: {case['Judge_Name']})" if case else "Pending court trial assignment."
                        },
                        {
                            'name': '5. Final Judgment & Case Disposal',
                            'status': 'Completed' if 'closed' in status_str or 'judgment' in status_str or 'convicted' in status_str else 'Pending',
                            'date': fir['Last_Updated'],
                            'desc': f"Case final status: {fir['Status']}."
                        }
                    ]
                else:
                    flash(f"No record found matching '{query_id}'. Please verify the FIR number.", 'warning')

            except Exception as e:
                flash(f"Error querying status: {str(e)}", 'danger')

        return render_template('track_status.html', query_id=query_id, record=record, record_type=record_type, stages=stages)

    @app.route('/citizen-rights')
    @app.route('/rights')
    def citizen_rights():
        return render_template('citizen_rights.html')

    @app.route('/stations')
    def stations_list():
        try:
            stations = fetch_all(
                """
                SELECT ps.*, COUNT(p.Police_ID) as Officer_Count
                FROM PoliceStation ps
                LEFT JOIN Police p ON ps.Station_ID = p.Station_ID
                GROUP BY ps.Station_ID
                ORDER BY ps.Station_Name ASC
                """
            )
        except Exception:
            stations = []
        return render_template('stations_list.html', stations=stations)

    @app.route('/courts')
    def courts_list():
        try:
            courts = fetch_all("SELECT * FROM Court ORDER BY Court_Name ASC")
            cases = fetch_all(
                """
                SELECT c.*, f.FIR_Number, ct.Court_Name, ct.Judge_Name
                FROM `Case` c
                LEFT JOIN FIR f ON c.FIR_ID = f.FIR_ID
                LEFT JOIN Court ct ON c.Court_ID = ct.Court_ID
                ORDER BY c.Case_ID DESC
                """
            )
        except Exception:
            courts = []
            cases = []
        return render_template('courts_list.html', courts=courts, cases=cases)

    @app.route('/evidence')
    def evidence_list():
        if not session.get('role'):
            flash('Please log in to access the evidence vault.', 'warning')
            return redirect(url_for('auth.login'))
        try:
            evidences = fetch_all(
                """
                SELECT e.*, f.FIR_Number, p.Name as Collected_By_Name, p.Badge_Number
                FROM Evidence e
                LEFT JOIN FIR f ON e.FIR_ID = f.FIR_ID
                LEFT JOIN Police p ON e.Collected_By = p.Police_ID
                ORDER BY e.Evidence_ID DESC
                """
            )
        except Exception:
            evidences = []
        return render_template('evidence_list.html', evidences=evidences)

    @app.route('/profile')
    def profile():
        if not session.get('role'):
            return redirect(url_for('auth.login'))
        user_info = {}
        try:
            if session.get('role') == 'user':
                user_info = fetch_one("SELECT * FROM User WHERE User_ID = %s", (session.get('user_id'),))
            elif session.get('role') == 'police':
                user_info = fetch_one(
                    """
                    SELECT p.*, ps.Station_Name, ps.City, ps.Jurisdiction as Station_Jurisdiction, ps.Address as Station_Address
                    FROM Police p
                    LEFT JOIN PoliceStation ps ON p.Station_ID = ps.Station_ID
                    WHERE p.Police_ID = %s
                    """,
                    (session.get('police_id'),)
                )
        except Exception:
            pass
        return render_template('profile.html', user_info=user_info)

    @app.route('/settings')
    def settings():
        if not session.get('role'):
            return redirect(url_for('auth.login'))
        return render_template('profile.html', user_info={}, is_settings=True)

    # Health check route
    @app.route('/health')
    def health():
        connected, msg = test_connection()
        return {'status': 'healthy' if connected else 'degraded', 'database': msg}

    # Error Handlers
    @app.errorhandler(404)
    def not_found(e):
        return render_template('base.html', error_title="404 - Page Not Found", error_msg="The requested crime record or page does not exist."), 404

    @app.errorhandler(500)
    def internal_error(e):
        return render_template('base.html', error_title="500 - Server Error", error_msg="A database or server error occurred. Please check database connectivity."), 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
