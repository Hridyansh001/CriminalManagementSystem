// CRMS Configuration & Terminal UI Helpers

const API_BASE_URL = "http://localhost:8080/api";

// Get logged-in role ("police" or "user")
function getRole() {
    return localStorage.getItem("role");
}

// Get logged-in user ID
function getUserId() {
    const id = localStorage.getItem("userId");
    return id ? parseInt(id) : null;
}

// Get logged-in display name
function getUserName() {
    return localStorage.getItem("name") || "User";
}

// Guard check for pages based on role
function checkRoleGuard(allowedRoles = []) {
    const role = getRole();

    // Not logged in -> go to login
    if (!role) {
        window.location.href = "index.html";
        return null;
    }

    // Role not permitted for this page -> redirect to dashboard
    if (allowedRoles.length > 0 && !allowedRoles.includes(role)) {
        window.location.href = "dashboard.html";
        return null;
    }

    return role;
}

// Render dynamic terminal navigation bar
function renderNavbar(activePage = "") {
    const role = getRole();
    const name = getUserName();
    const navContainer = document.getElementById("navbar-container");
    if (!navContainer) return;

    let linksHtml = "";

    if (role === "police") {
        // Police Navigation
        linksHtml = `
            <a href="dashboard.html" class="nav-btn ${activePage === 'dashboard' ? 'active' : ''}">[ DASHBOARD ]</a>
            <a href="fir.html" class="nav-btn ${activePage === 'fir' ? 'active' : ''}">[ FIRs ]</a>
            <a href="criminals.html" class="nav-btn ${activePage === 'criminals' ? 'active' : ''}">[ CRIMINALS ]</a>
            <a href="investigations.html" class="nav-btn ${activePage === 'investigations' ? 'active' : ''}">[ INVESTIGATIONS ]</a>
            <a href="evidence.html" class="nav-btn ${activePage === 'evidence' ? 'active' : ''}">[ EVIDENCE ]</a>
            <a href="cases.html" class="nav-btn ${activePage === 'cases' ? 'active' : ''}">[ CASES ]</a>
            <a href="courts.html" class="nav-btn ${activePage === 'courts' ? 'active' : ''}">[ COURTS ]</a>
            <a href="hearings.html" class="nav-btn ${activePage === 'hearings' ? 'active' : ''}">[ HEARINGS ]</a>
            <a href="judgments.html" class="nav-btn ${activePage === 'judgments' ? 'active' : ''}">[ JUDGMENTS ]</a>
            <a href="stations.html" class="nav-btn ${activePage === 'stations' ? 'active' : ''}">[ POLICE STATIONS ]</a>
            <button onclick="logout()" class="nav-btn logout">[ LOGOUT ]</button>
        `;
    } else {
        // User Navigation
        linksHtml = `
            <a href="dashboard.html" class="nav-btn ${activePage === 'dashboard' ? 'active' : ''}">[ DASHBOARD ]</a>
            <a href="fir.html" class="nav-btn ${activePage === 'fir' ? 'active' : ''}">[ MY FIRs ]</a>
            <a href="fir.html?action=new" class="nav-btn ${activePage === 'file-fir' ? 'active' : ''}">[ FILE FIR ]</a>
            <button onclick="logout()" class="nav-btn logout">[ LOGOUT ]</button>
        `;
    }

    navContainer.innerHTML = `
        <div class="system-header">
            <div class="system-title-row">
                <div class="logo">CRMS // CRIME RECORD MANAGEMENT SYSTEM</div>
                <div class="user-meta">
                    Logged in as: <span>${role ? role.toUpperCase() : 'GUEST'}</span> | User: <span>${name}</span>
                </div>
            </div>
            <div class="nav-bar">
                ${linksHtml}
            </div>
        </div>
    `;
}

// Logout
function logout() {
    localStorage.removeItem("role");
    localStorage.removeItem("userId");
    localStorage.removeItem("name");
    localStorage.removeItem("crms_user");
    window.location.href = "index.html";
}

// Terminal style alerts
function showAlert(type, message, timeout = 4000) {
    const alertBox = document.getElementById("alert-box");
    if (!alertBox) return;

    alertBox.className = `alert alert-${type}`;
    alertBox.textContent = `> ${message}`;
    alertBox.style.display = "block";

    if (timeout > 0) {
        setTimeout(() => {
            alertBox.style.display = "none";
        }, timeout);
    }
}

// Date formatter (YYYY-MM-DD to DD/MM/YYYY)
function formatDate(dateStr) {
    if (!dateStr) return "-";
    try {
        const parts = dateStr.split("-");
        if (parts.length === 3) {
            return `${parts[2]}/${parts[1]}/${parts[0]}`;
        }
        return dateStr;
    } catch (e) {
        return dateStr;
    }
}
