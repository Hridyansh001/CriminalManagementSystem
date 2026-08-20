from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from database.db import fetch_one, insert_and_get_id, fetch_all

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form.get('role', 'user').strip().lower()
        email_or_badge = (request.form.get('email', '') or request.form.get('username', '')).strip()
        password = request.form.get('password', '').strip()

        if not email_or_badge:
            flash('Please enter your email address or badge number.', 'danger')
            return render_template('login.html')

        try:
            # Check Police first if role is police OR if input looks like police badge/email
            is_police_input = (
                role == 'police' or 
                '@police' in email_or_badge.lower() or 
                email_or_badge.upper().startswith(('HS', 'JG', 'LL', 'SH', 'JM', 'JJ', 'DD', 'RAVEN', 'POL'))
            )

            if is_police_input:
                police = fetch_one(
                    """
                    SELECT p.Police_ID, p.Name, p.Badge_Number, p.police_rank, p.Email, p.Phone, p.Station_ID,
                           COALESCE(ps.Station_Name, 'Central Police Station') as Station_Name,
                           COALESCE(ps.City, 'Metropolitan') as City,
                           COALESCE(ps.Jurisdiction, 'Central District') as Jurisdiction
                    FROM Police p
                    LEFT JOIN PoliceStation ps ON p.Station_ID = ps.Station_ID
                    WHERE LOWER(TRIM(p.Email)) = LOWER(TRIM(%s)) 
                       OR LOWER(TRIM(p.Badge_Number)) = LOWER(TRIM(%s))
                       OR LOWER(TRIM(p.Name)) = LOWER(TRIM(%s))
                    LIMIT 1
                    """,
                    (email_or_badge, email_or_badge, email_or_badge)
                )

                if police:
                    session.clear()
                    session['police_id'] = police['Police_ID']
                    session['role'] = 'police'
                    session['name'] = police['Name']
                    session['badge_number'] = police['Badge_Number']
                    session['police_rank'] = police.get('police_rank') or 'Inspector'
                    session['station_name'] = police.get('Station_Name') or 'Central Command'
                    session['station_id'] = police.get('Station_ID')
                    session['email'] = police.get('Email')
                    flash(f"Officer {police['Name']} ({police.get('police_rank', 'Officer')}) authenticated.", 'success')
                    return redirect(url_for('police.dashboard'))
                elif role == 'police':
                    flash(f"No police officer record found matching '{email_or_badge}'. Try badge 'HS002' or email 'hank@police.gov'.", 'danger')
                    return render_template('login.html')

            # Check User table
            user = fetch_one(
                """
                SELECT User_ID, Name, Email, Phone, DOB, Gender, Residential_Address, Password 
                FROM User 
                WHERE LOWER(TRIM(Email)) = LOWER(TRIM(%s)) OR LOWER(TRIM(Name)) = LOWER(TRIM(%s))
                LIMIT 1
                """,
                (email_or_badge, email_or_badge)
            )
            
            if user:
                # Accept exact password, or common demo passwords
                valid_passwords = [
                    user.get('Password'), '123456', 'demo', 'password',
                    'heisenberg@123', 'bettercall@123', 'ironman@123', 'batman@123', 'noob@123', 'spidey@123', 'elementary@123'
                ]
                if password in valid_passwords or not user.get('Password'):
                    session.clear()
                    session['user_id'] = user['User_ID']
                    session['role'] = 'user'
                    session['name'] = user['Name']
                    session['email'] = user['Email']
                    session['phone'] = user.get('Phone')
                    flash(f"Welcome back, {user['Name']}!", 'success')
                    return redirect(url_for('user.dashboard'))
                else:
                    flash(f"Invalid password for {user['Name']}. Mock password is '{user.get('Password')}' or '123456'.", 'danger')
            else:
                # Fallback: check if police was intended
                police_fallback = fetch_one(
                    """
                    SELECT p.Police_ID, p.Name, p.Badge_Number, p.police_rank, p.Email, p.Phone, p.Station_ID,
                           COALESCE(ps.Station_Name, 'Central Police Station') as Station_Name,
                           COALESCE(ps.City, 'Metropolitan') as City,
                           COALESCE(ps.Jurisdiction, 'Central District') as Jurisdiction
                    FROM Police p
                    LEFT JOIN PoliceStation ps ON p.Station_ID = ps.Station_ID
                    WHERE LOWER(TRIM(p.Email)) = LOWER(TRIM(%s)) 
                       OR LOWER(TRIM(p.Badge_Number)) = LOWER(TRIM(%s))
                       OR LOWER(TRIM(p.Name)) = LOWER(TRIM(%s))
                    LIMIT 1
                    """,
                    (email_or_badge, email_or_badge, email_or_badge)
                )
                if police_fallback:
                    session.clear()
                    session['police_id'] = police_fallback['Police_ID']
                    session['role'] = 'police'
                    session['name'] = police_fallback['Name']
                    session['badge_number'] = police_fallback['Badge_Number']
                    session['police_rank'] = police_fallback.get('police_rank') or 'Inspector'
                    session['station_name'] = police_fallback.get('Station_Name') or 'Central Command'
                    session['station_id'] = police_fallback.get('Station_ID')
                    session['email'] = police_fallback.get('Email')
                    flash(f"Officer {police_fallback['Name']} ({police_fallback.get('police_rank', 'Officer')}) authenticated.", 'success')
                    return redirect(url_for('police.dashboard'))

                flash('No user or officer account found with those credentials.', 'danger')

        except Exception as e:
            flash(f"Database error during authentication: {str(e)}", 'danger')

    # Demo quick-select accounts from database
    demo_users = []
    demo_police = []
    try:
        demo_users = fetch_all("SELECT Name, Email, Password FROM User LIMIT 5")
        demo_police = fetch_all("SELECT Name, Badge_Number, police_rank, Email FROM Police LIMIT 5")
    except Exception:
        pass

    return render_template('login.html', demo_users=demo_users, demo_police=demo_police)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        dob = request.form.get('dob', '').strip() or None
        gender = request.form.get('gender', 'Other').strip()
        residential_address = request.form.get('residential_address', '').strip()
        password = request.form.get('password', '').strip()

        if not name or not email or not password:
            flash('Name, Email, and Password are required.', 'danger')
            return render_template('register.html')

        try:
            # Check if email already exists
            existing_user = fetch_one("SELECT User_ID FROM User WHERE Email = %s", (email,))
            if existing_user:
                flash('An account with this email address already exists. Please log in.', 'warning')
                return redirect(url_for('auth.login'))

            # Insert new user
            user_id = insert_and_get_id(
                """
                INSERT INTO User (Name, Email, Phone, DOB, Gender, Residential_Address, Password)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (name, email, phone, dob, gender, residential_address, password)
            )

            flash('Account created successfully! Please log in with your credentials.', 'success')
            return redirect(url_for('auth.login'))

        except Exception as e:
            flash(f"Error creating account: {str(e)}", 'danger')

    return render_template('register.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
