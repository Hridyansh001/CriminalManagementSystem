// Case Management Logic (Police Only)

let caseList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("cases");
    loadCases();
});

async function loadCases() {
    const tbody = document.getElementById("casesTableBody");
    tbody.innerHTML = `<tr><td colspan="8" class="no-data">Querying court cases...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/cases`);
        if (!response.ok) throw new Error("Failed to fetch cases");
        caseList = await response.json();
        renderTable(caseList);
    } catch (error) {
        console.error("Error loading cases:", error);
        tbody.innerHTML = `<tr><td colspan="8" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch case records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("casesTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">No court cases registered.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(c => `
        <tr>
            <td>${c.caseId}</td>
            <td><strong>${c.caseNumber || "-"}</strong></td>
            <td>FIR #${c.firId}</td>
            <td>Court #${c.courtId}</td>
            <td>${c.caseType || "-"}</td>
            <td>${formatDate(c.filingDate)}</td>
            <td><span class="badge ${getCaseStatusClass(c.status)}">${c.status || "PENDING"}</span></td>
            <td class="actions">
                <button class="btn btn-primary btn-sm" onclick="viewCaseDetails(${c.caseId})">[ VIEW ]</button>
                <button class="btn btn-sm" onclick="openEditModal(${c.caseId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deleteCase(${c.caseId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function getCaseStatusClass(status) {
    if (!status) return "badge-secondary";
    const s = status.toUpperCase();
    if (s.includes("DISPOSED") || s.includes("CLOSED")) return "badge-success";
    if (s.includes("TRIAL") || s.includes("HEARING")) return "badge-warning";
    if (s.includes("PENDING")) return "badge-info";
    return "badge-secondary";
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = caseList.filter(c => {
        return (
            (c.caseNumber && c.caseNumber.toLowerCase().includes(query)) ||
            (c.caseType && c.caseType.toLowerCase().includes(query)) ||
            (c.status && c.status.toLowerCase().includes(query)) ||
            (c.firId && String(c.firId).includes(query)) ||
            (c.courtId && String(c.courtId).includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "REGISTER COURT CASE";
    document.getElementById("caseForm").reset();
    document.getElementById("caseId").value = "";
    document.getElementById("filingDate").value = new Date().toISOString().split("T")[0];
    document.getElementById("caseModal").style.display = "block";
}

function openEditModal(id) {
    const item = caseList.find(c => c.caseId === id);
    if (!item) return;

    document.getElementById("modalTitle").textContent = "EDIT COURT CASE";
    document.getElementById("caseId").value = item.caseId;
    document.getElementById("caseNumber").value = item.caseNumber || "";
    document.getElementById("firId").value = item.firId || "";
    document.getElementById("courtId").value = item.courtId || "";
    document.getElementById("caseType").value = item.caseType || "";
    document.getElementById("filingDate").value = item.filingDate || "";
    document.getElementById("status").value = item.status || "PENDING";

    document.getElementById("caseModal").style.display = "block";
}

function viewCaseDetails(id) {
    const item = caseList.find(c => c.caseId === id);
    if (!item) return;

    const list = document.getElementById("caseDetailsContent");
    list.innerHTML = `
        <li><strong>Case ID:</strong> <span>${item.caseId}</span></li>
        <li><strong>Case Number:</strong> <span>${item.caseNumber || "-"}</span></li>
        <li><strong>Linked FIR ID:</strong> <span>FIR #${item.firId}</span></li>
        <li><strong>Assigned Court:</strong> <span>Court #${item.courtId}</span></li>
        <li><strong>Case Type:</strong> <span>${item.caseType || "-"}</span></li>
        <li><strong>Filing Date:</strong> <span>${formatDate(item.filingDate)}</span></li>
        <li><strong>Status:</strong> <span><span class="badge ${getCaseStatusClass(item.status)}">${item.status || "PENDING"}</span></span></li>
    `;

    document.getElementById("viewModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveCase(e) {
    e.preventDefault();

    const id = document.getElementById("caseId").value;
    const caseData = {
        caseNumber: document.getElementById("caseNumber").value.trim(),
        firId: parseInt(document.getElementById("firId").value),
        courtId: parseInt(document.getElementById("courtId").value),
        caseType: document.getElementById("caseType").value.trim() || null,
        filingDate: document.getElementById("filingDate").value || null,
        status: document.getElementById("status").value
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/cases/${id}` : `${API_BASE_URL}/cases`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(caseData)
        });

        if (!response.ok) throw new Error("Failed to save case");

        showAlert("success", isEdit ? "Case record updated." : "Case registered successfully.");
        closeModal("caseModal");
        loadCases();
    } catch (error) {
        console.error("Save case error:", error);
        showAlert("danger", "Could not save case. Check Case Number uniqueness and foreign keys.");
    }
}

async function deleteCase(id) {
    if (!confirm("Are you sure you want to delete this case record?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/cases/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "Case record deleted.");
        loadCases();
    } catch (error) {
        console.error("Delete case error:", error);
        showAlert("danger", "Could not delete case record.");
    }
}
