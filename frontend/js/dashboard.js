// Terminal Dashboard Logic

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard();
    if (!role) return;

    renderNavbar("dashboard");

    if (role === "police") {
        document.getElementById("policeDashboardView").style.display = "block";
        loadPoliceDashboard();
    } else {
        document.getElementById("userDashboardView").style.display = "block";
        document.getElementById("userWelcomeName").textContent = getUserName();
        loadUserDashboard();
    }
});

async function loadPoliceDashboard() {
    try {
        const response = await fetch(`${API_BASE_URL}/dashboard`);
        if (!response.ok) throw new Error("Dashboard fetch failed");

        const data = await response.json();
        document.getElementById("stat-firs").textContent = data.totalFirs ?? 0;
        document.getElementById("stat-criminals").textContent = data.totalCriminals ?? 0;
        document.getElementById("stat-investigations").textContent = data.totalInvestigations ?? 0;
        document.getElementById("stat-cases").textContent = data.totalCases ?? 0;
        document.getElementById("stat-police").textContent = data.totalPolice ?? 0;
        document.getElementById("stat-users").textContent = data.totalUsers ?? 0;
    } catch (error) {
        console.error("Police dashboard error:", error);
        showAlert("danger", "Could not query dashboard stats from backend.");
    }
}

async function loadUserDashboard() {
    const tbody = document.getElementById("userRecentFirsBody");
    const currentUserId = getUserId();

    try {
        const response = await fetch(`${API_BASE_URL}/firs`);
        if (!response.ok) throw new Error("FIR fetch failed");

        const allFirs = await response.json();
        const myFirs = allFirs.filter(f => f.userid === currentUserId);

        if (myFirs.length === 0) {
            tbody.innerHTML = `<tr><td colspan="5" class="no-data">No FIR records found under your account.</td></tr>`;
            return;
        }

        tbody.innerHTML = myFirs.slice(0, 5).map(f => `
            <tr>
                <td><strong>${f.firnumber || "-"}</strong></td>
                <td>${f.crimetype || "-"}</td>
                <td>${formatDate(f.date_filed)}</td>
                <td><span class="badge ${getStatusBadge(f.status)}">${f.status || "REGISTERED"}</span></td>
                <td><a href="fir.html" class="btn btn-sm">[ VIEW ]</a></td>
            </tr>
        `).join("");
    } catch (error) {
        console.error("User dashboard error:", error);
        tbody.innerHTML = `<tr><td colspan="5" class="no-data" style="color:#f48771;">Server query failed.</td></tr>`;
    }
}

function getStatusBadge(status) {
    if (!status) return "badge-secondary";
    const s = status.toUpperCase();
    if (s.includes("CLOSED") || s.includes("RESOLVED")) return "badge-success";
    if (s.includes("INVESTIGATION")) return "badge-warning";
    if (s.includes("REGISTERED")) return "badge-info";
    if (s.includes("CHARGESHEET")) return "badge-danger";
    return "badge-secondary";
}
