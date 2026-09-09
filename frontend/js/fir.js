// Terminal FIR Logic (Dual Role Aware)

let firList = [];
let userRole = "user";
let currentUserId = null;

document.addEventListener("DOMContentLoaded", () => {
    userRole = checkRoleGuard();
    if (!userRole) return;

    currentUserId = getUserId();
    renderNavbar("fir");

    if (userRole === "user") {
        document.getElementById("pageHeading").textContent = "MY FILED FIRs";
        document.getElementById("addNewFirBtn").textContent = "[ + FILE NEW FIR ]";
        document.getElementById("thUser").style.display = "none";
        document.getElementById("statusGroup").style.display = "none";
        document.getElementById("lastUpdatedGroup").style.display = "none";
        document.getElementById("userIdGroup").style.display = "none";
    }

    loadFirs();

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get("action") === "new") {
        openAddModal();
    }
});

async function loadFirs() {
    const tbody = document.getElementById("firTableBody");
    tbody.innerHTML = `<tr><td colspan="8" class="no-data">Querying FIR records...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/firs`);
        if (!response.ok) throw new Error("Failed to fetch FIRs");

        const allFirs = await response.json();

        if (userRole === "user") {
            firList = allFirs.filter(f => f.userid === currentUserId);
        } else {
            firList = allFirs;
        }

        renderTable(firList);
    } catch (error) {
        console.error("Error loading FIRs:", error);
        tbody.innerHTML = `<tr><td colspan="8" class="no-data" style="color: #f48771;">Backend connection error.</td></tr>`;
        showAlert("danger", "Could not fetch FIR records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("firTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">${userRole === "user" ? "You have not filed any FIRs." : "No FIR records found in database."}</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(item => `
        <tr>
            <td>${item.fir_id}</td>
            <td><strong>${item.firnumber || "-"}</strong></td>
            ${userRole === "police" ? `<td>#${item.userid ?? "-"}</td>` : ''}
            <td>${item.crimetype || "-"}</td>
            <td>${item.location || "-"}</td>
            <td>${formatDate(item.date_filed)}</td>
            <td><span class="badge ${getStatusBadge(item.status)}">${item.status || "REGISTERED"}</span></td>
            <td class="actions">
                <button class="btn btn-primary btn-sm" onclick="viewFirDetails(${item.fir_id})">[ VIEW ]</button>
                ${userRole === "police" ? `
                    <button class="btn btn-sm" onclick="openEditModal(${item.fir_id})">[ EDIT ]</button>
                    <button class="btn btn-danger btn-sm" onclick="deleteFir(${item.fir_id})">[ DEL ]</button>
                ` : ''}
            </td>
        </tr>
    `).join("");
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

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = firList.filter(item => {
        return (
            (item.firnumber && item.firnumber.toLowerCase().includes(query)) ||
            (item.crimetype && item.crimetype.toLowerCase().includes(query)) ||
            (item.location && item.location.toLowerCase().includes(query)) ||
            (item.status && item.status.toLowerCase().includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = userRole === "user" ? "FILE NEW FIR COMPLAINT" : "ADD FIR RECORD";
    document.getElementById("firForm").reset();
    document.getElementById("fir_id").value = "";
    document.getElementById("date_filed").value = new Date().toISOString().split("T")[0];

    const randNum = Math.floor(100 + Math.random() * 900);
    document.getElementById("firnumber").value = `FIR-${new Date().getFullYear()}-${randNum}`;

    if (userRole === "user") {
        document.getElementById("userid").value = currentUserId;
        document.getElementById("status").value = "FIR Registered";
    }

    document.getElementById("firModal").style.display = "block";
}

function openEditModal(id) {
    if (userRole !== "police") return;

    const item = firList.find(f => f.fir_id === id);
    if (!item) return;

    document.getElementById("modalTitle").textContent = "EDIT FIR RECORD";
    document.getElementById("fir_id").value = item.fir_id;
    document.getElementById("firnumber").value = item.firnumber || "";
    document.getElementById("userid").value = item.userid || "";
    document.getElementById("crimetype").value = item.crimetype || "";
    document.getElementById("date_filed").value = item.date_filed || "";
    document.getElementById("location").value = item.location || "";
    document.getElementById("jurisdiction").value = item.jurisdiction || "";

    const statusSelect = document.getElementById("status");
    const rawStatus = item.status || "FIR Registered";
    let matched = false;
    for (let i = 0; i < statusSelect.options.length; i++) {
        if (statusSelect.options[i].value.toLowerCase() === rawStatus.toLowerCase()) {
            statusSelect.selectedIndex = i;
            matched = true;
            break;
        }
    }
    if (!matched) {
        const opt = document.createElement("option");
        opt.value = rawStatus;
        opt.textContent = rawStatus;
        statusSelect.appendChild(opt);
        statusSelect.value = rawStatus;
    }

    document.getElementById("lastupdated").value = item.lastupdated || new Date().toISOString().split("T")[0];
    document.getElementById("description").value = item.description || "";

    document.getElementById("firModal").style.display = "block";
}

function viewFirDetails(id) {
    const item = firList.find(f => f.fir_id === id);
    if (!item) return;

    const list = document.getElementById("firDetailsContent");
    list.innerHTML = `
        <li><strong>FIR ID:</strong> <span>${item.fir_id}</span></li>
        <li><strong>FIR Number:</strong> <span>${item.firnumber || "-"}</span></li>
        <li><strong>Complainant ID:</strong> <span>#${item.userid ?? "-"}</span></li>
        <li><strong>Crime Type:</strong> <span>${item.crimetype || "-"}</span></li>
        <li><strong>Date Filed:</strong> <span>${formatDate(item.date_filed)}</span></li>
        <li><strong>Location:</strong> <span>${item.location || "-"}</span></li>
        <li><strong>Jurisdiction:</strong> <span>${item.jurisdiction || "-"}</span></li>
        <li><strong>Status:</strong> <span><span class="badge ${getStatusBadge(item.status)}">${item.status || "REGISTERED"}</span></span></li>
        <li><strong>Last Updated:</strong> <span>${formatDate(item.lastupdated)}</span></li>
        <li><strong>Description:</strong> <span>${item.description || "None"}</span></li>
    `;

    document.getElementById("viewModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveFir(e) {
    e.preventDefault();

    const id = document.getElementById("fir_id").value;
    const isEdit = Boolean(id);

    let targetUserId = currentUserId;
    if (userRole === "police") {
        targetUserId = parseInt(document.getElementById("userid").value);
    }

    const firData = {
        firnumber: document.getElementById("firnumber").value.trim(),
        userid: targetUserId,
        crimetype: document.getElementById("crimetype").value.trim(),
        date_filed: document.getElementById("date_filed").value,
        location: document.getElementById("location").value.trim() || null,
        jurisdiction: document.getElementById("jurisdiction").value.trim() || null,
        status: userRole === "police" ? document.getElementById("status").value : "REGISTERED",
        lastupdated: new Date().toISOString().split("T")[0],
        description: document.getElementById("description").value.trim()
    };

    const url = isEdit ? `${API_BASE_URL}/firs/${id}` : `${API_BASE_URL}/firs`;

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(firData)
        });

        if (!response.ok) throw new Error("Failed to save FIR");

        showAlert("success", isEdit ? "FIR record updated." : "FIR registered successfully.");
        closeModal("firModal");
        loadFirs();
    } catch (error) {
        console.error("Save FIR error:", error);
        showAlert("danger", "Failed to save FIR. Check inputs and verify user ID.");
    }
}

async function deleteFir(id) {
    if (userRole !== "police") return;
    if (!confirm("Are you sure you want to delete this FIR record?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/firs/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "FIR record removed from database.");
        loadFirs();
    } catch (error) {
        console.error("Delete FIR error:", error);
        showAlert("danger", "Could not delete FIR record.");
    }
}
