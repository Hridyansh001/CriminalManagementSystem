// Investigation Management Logic (Police Only)

let invList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("investigations");
    loadInvestigations();
});

async function loadInvestigations() {
    const tbody = document.getElementById("invTableBody");
    tbody.innerHTML = `<tr><td colspan="7" class="no-data">Querying investigation files...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/investigations`);
        if (!response.ok) throw new Error("Failed to fetch investigations");
        invList = await response.json();
        renderTable(invList);
    } catch (error) {
        console.error("Error loading investigations:", error);
        tbody.innerHTML = `<tr><td colspan="7" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch investigation records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("invTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" class="no-data">No investigation records found.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(item => `
        <tr>
            <td>${item.investigationId}</td>
            <td>FIR #${item.firId}</td>
            <td>Officer #${item.policeId}</td>
            <td>${formatDate(item.startDate)}</td>
            <td>${formatDate(item.endDate)}</td>
            <td><span class="badge ${getInvBadgeClass(item.status)}">${item.status || "OPEN"}</span></td>
            <td class="actions">
                <button class="btn btn-primary btn-sm" onclick="viewInvDetails(${item.investigationId})">[ VIEW ]</button>
                <button class="btn btn-sm" onclick="openEditModal(${item.investigationId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deleteInvestigation(${item.investigationId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function getInvBadgeClass(status) {
    if (!status) return "badge-secondary";
    const s = status.toUpperCase();
    if (s.includes("CLOSED")) return "badge-success";
    if (s.includes("PROGRESS") || s.includes("OPEN")) return "badge-info";
    if (s.includes("CHARGESHEET")) return "badge-warning";
    if (s.includes("SUSPENDED")) return "badge-danger";
    return "badge-secondary";
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = invList.filter(item => {
        return (
            (item.firId && String(item.firId).includes(query)) ||
            (item.policeId && String(item.policeId).includes(query)) ||
            (item.status && item.status.toLowerCase().includes(query)) ||
            (item.findings && item.findings.toLowerCase().includes(query)) ||
            (item.remarks && item.remarks.toLowerCase().includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "NEW INVESTIGATION FILE";
    document.getElementById("invForm").reset();
    document.getElementById("investigationId").value = "";
    document.getElementById("startDate").value = new Date().toISOString().split("T")[0];
    document.getElementById("invModal").style.display = "block";
}

function openEditModal(id) {
    const item = invList.find(i => i.investigationId === id);
    if (!item) return;

    document.getElementById("modalTitle").textContent = "EDIT INVESTIGATION FILE";
    document.getElementById("investigationId").value = item.investigationId;
    document.getElementById("firId").value = item.firId || "";
    document.getElementById("policeId").value = item.policeId || "";
    document.getElementById("startDate").value = item.startDate || "";
    document.getElementById("endDate").value = item.endDate || "";
    document.getElementById("status").value = item.status || "OPEN";
    document.getElementById("chargesheetDate").value = item.chargesheetDate || "";
    document.getElementById("findings").value = item.findings || "";
    document.getElementById("remarks").value = item.remarks || "";

    document.getElementById("invModal").style.display = "block";
}

function viewInvDetails(id) {
    const item = invList.find(i => i.investigationId === id);
    if (!item) return;

    const list = document.getElementById("invDetailsContent");
    list.innerHTML = `
        <li><strong>Investigation ID:</strong> <span>${item.investigationId}</span></li>
        <li><strong>Linked FIR:</strong> <span>FIR #${item.firId}</span></li>
        <li><strong>Lead Officer:</strong> <span>Officer #${item.policeId}</span></li>
        <li><strong>Start Date:</strong> <span>${formatDate(item.startDate)}</span></li>
        <li><strong>End Date:</strong> <span>${formatDate(item.endDate)}</span></li>
        <li><strong>Status:</strong> <span><span class="badge ${getInvBadgeClass(item.status)}">${item.status || "OPEN"}</span></span></li>
        <li><strong>Chargesheet Date:</strong> <span>${formatDate(item.chargesheetDate)}</span></li>
        <li><strong>Findings:</strong> <span>${item.findings || "None"}</span></li>
        <li><strong>Remarks:</strong> <span>${item.remarks || "None"}</span></li>
    `;

    document.getElementById("viewModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveInvestigation(e) {
    e.preventDefault();

    const id = document.getElementById("investigationId").value;
    const invData = {
        firId: parseInt(document.getElementById("firId").value),
        policeId: parseInt(document.getElementById("policeId").value),
        startDate: document.getElementById("startDate").value || null,
        endDate: document.getElementById("endDate").value || null,
        status: document.getElementById("status").value,
        chargesheetDate: document.getElementById("chargesheetDate").value || null,
        findings: document.getElementById("findings").value.trim() || null,
        remarks: document.getElementById("remarks").value.trim() || null
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/investigations/${id}` : `${API_BASE_URL}/investigations`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(invData)
        });

        if (!response.ok) throw new Error("Failed to save investigation");

        showAlert("success", isEdit ? "Investigation file updated." : "Investigation assigned successfully.");
        closeModal("invModal");
        loadInvestigations();
    } catch (error) {
        console.error("Save investigation error:", error);
        showAlert("danger", "Could not save investigation. Check FIR ID and Officer ID.");
    }
}

async function deleteInvestigation(id) {
    if (!confirm("Are you sure you want to delete this investigation record?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/investigations/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "Investigation file deleted.");
        loadInvestigations();
    } catch (error) {
        console.error("Delete investigation error:", error);
        showAlert("danger", "Could not delete investigation record.");
    }
}
