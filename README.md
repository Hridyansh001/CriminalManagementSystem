# Crime Record Management System (CRMS)
## College DBMS Project • Full-Stack Python Flask & MySQL

A robust, government/law-enforcement style web application for tracking First Information Reports (FIRs) and managing criminal justice lifecycles from filing to judicial verdict.

Built with **Python Flask**, **MySQL** (`mysql-connector-python`), **Vanilla HTML5, CSS3, and JavaScript**.

---

## 🏛️ Database Schema Overview (13 Tables)

The application connects directly to the existing `crimemanagementsystem` database:
1. `User` — Citizen complainants and account credentials
2. `PoliceStation` — Jurisdiction circles, stations, and locations
3. `Police` — Law enforcement officers, ranks, and badge numbers
4. `Criminal` — Registered offenders, aliases, threat levels, and statuses
5. `FIR` — First Information Reports with unique numbers (e.g., `FIR-2026-001`)
6. `FIR_Criminal` — M:N relationship between FIRs and Accused Criminals
7. `Investigation` — Officer assignments, findings, and chargesheet dates
8. `Evidence` — Physical/digital evidence catalog with storage locations
9. `FIR_Status_History` — Immutable audit ledger of status transitions
10. `Court` — District/Criminal courts and presiding judges
11. `Case` — Judicial cases committed from chargesheeted FIRs
12. `Hearing` — Court hearing schedules, next dates, and court orders
13. `Judgment` — Final judicial verdicts, sentences, and legal bases

---

## 🚀 Setup & Execution Instructions

### 1. Prerequisites
- Python 3.9+ installed
- MySQL Server running with the `crimemanagementsystem` database loaded (using `dbcreation.sql` and `mockdata.sql`).

### 2. Environment Configuration
Create a `.env` file in the project root (or copy `.env.example`):
```bash
cp .env.example .env
```
Edit `.env` with your MySQL credentials:
```ini
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=crimemanagementsystem
DB_PORT=3306
SECRET_KEY=crime-management-system-secret-key-2026
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Seed FIR-Criminal Relationships
If your `FIR_Criminal` table is empty, run:
```bash
mysql -u root -p crimemanagementsystem < seed_fir_criminal.sql
```

### 5. Launch the Application
```bash
python app.py
```
Open your browser and navigate to: **`http://localhost:5001`**

---

## 🎭 Live Demo Walkthrough (For Evaluation)

### Scenario A: Citizen Complainant Flow
1. Go to `http://localhost:5001/login`
2. Select **"Citizen / Complainant"** tab. Click on **Walter White** (`walter@gmail.com`) to quick-fill credentials.
3. View the **Citizen Dashboard** showing total FIRs, active investigations, court cases, and the table of filed complaints.
4. Click on **"Track & View"** on `FIR-2026-001` to view:
   - **Dynamic 6-Stage Visual Pipeline** (FIR Registered → Investigation Started → Evidence Collected → Chargesheet Filed → Case In Court → Judgment)
   - **Status History Audit Trail**
   - **Complainant & Investigating Officer (Jim Gordon)**
   - **Accused Criminals (The Joker)**
   - **Evidence Locker (CCTV Footage & Fingerprints)**
   - **Court Case (CASE-2026-001 at Gotham District Court)**
   - **Hearing Logs & Final Judgment (Guilty, 2 years imprisonment)**
5. Click **"+ File New FIR"**, submit a new complaint (e.g., *Armed Robbery at North Bank*).
6. Note the auto-generated unique `FIR-2026-013` and automatic initial entry in `FIR_Status_History`.

### Scenario B: Police Officer Flow
1. Log out and switch to **"Police Officer"** tab on `http://localhost:5001/login`.
2. Click on **Hank Schrader** (`HS002`) or **Frank Castle** (`raven001`).
3. View **Officer Dashboard** with assigned inquiries and station jurisdiction records.
4. Open the newly filed FIR.
5. **Update FIR Status**: Change status to *"Under Investigation"* or *"Evidence Collected"* with remarks. Notice the immutable addition to `FIR_Status_History`.
6. **Register Evidence**: Click *"+ Register Evidence"*, fill in *"CCTV Footage"*, location *"Locker F-101"*. Verify it is tagged with the officer's badge.
7. **Associate Suspect**: Select a known criminal (e.g., *Hans Gruber* or *Loki*), specify role *"Prime Accused"*.
8. Return to the Citizen Tracking view to verify that the timeline and evidence live-sync from MySQL.

---

## 🛠️ Project Structure
```
crime-management/
├── app.py                  # Flask app factory, template filters & error handlers
├── config.py               # Environment configuration settings
├── requirements.txt        # Python package dependencies
├── .env.example            # Environment variables template
├── dbcreation.sql          # Original MySQL DDL (13 tables)
├── mockdata.sql            # Original Mock Data
├── queries.sql             # Reference SQL queries
├── seed_fir_criminal.sql   # Optional accused-FIR seed data
│
├── database/
│   ├── __init__.py
│   └── db.py               # MySQL connection pool & parameterized query helpers
│
├── routes/
│   ├── __init__.py
│   ├── auth.py             # Login, Register, Logout controllers
│   ├── user.py             # Citizen dashboard & FIR filing
│   ├── police.py           # Police dashboard, status update, evidence logging
│   └── fir.py              # FIR tracking page & REST APIs
│
├── templates/
│   ├── base.html           # Layout with responsive sidebar & navy theme
│   ├── login.html          # Authentication with role toggle & quick-demo helper
│   ├── register.html       # Citizen account creation form
│   ├── user_dashboard.html # Citizen metrics and filed FIR table
│   ├── file_fir.html       # FIR registration form
│   ├── fir_details.html    # Core tracking page with dynamic pipeline
│   ├── police_dashboard.html# Officer case queue & station records
│   ├── police_fir.html     # Investigation controls & status transitions
│   ├── add_evidence.html   # Evidence registration form
│   └── criminals.html      # Known criminal directory & threat levels
│
└── static/
    ├── css/
    │   └── style.css       # Dark slate/navy theme with crimson accents
    └── js/
        └── script.js       # Client live search, status filters & demo auto-fill
```

---

## 🔒 Security & Code Standards
- **Parameterized Queries**: All SQL executions use `%s` placeholders via `mysql-connector-python` to prevent SQL injection.
- **Environment Secrets**: Database passwords and Flask secret keys are loaded from `.env`.
- **Session-Based RBAC**: Separation of Citizen and Police roles.
- **Graceful Error Handling**: Database failures produce structured flash alerts rather than crashing the application.
