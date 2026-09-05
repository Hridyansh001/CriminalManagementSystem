// Evidence Management Logic (Police Only)

let evidenceList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("evidence");
    loadEvidences();
});

async function loadEvidences() {
    const tbody = document.getElementById("evidenceTableBody");
    tbody.innerHTML = `<tr><td colspan="8" class="no-data">Querying evidence records...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/evidences`);
        if (!response.ok) throw new Error("Failed to fetch evidences");
        evidenceList = await response.json();
        renderTable(evidenceList);
    } catch (error) {
        console.error("Error loading evidences:", error);
        tbody.innerHTML = `<tr><td colspan="8" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch evidence records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("evidenceTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">No evidence records logged.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(item => `
        <tr>
            <td>${item.evidenceId}</td>
            <td>FIR #${item.firId}</td>
            <td>${item.evidenceType || "-"}</td>
            <td>${item.storageLocation || "-"}</td>
            <td>${formatDate(item.collectedDate)}</td>
            <td>Officer #${item.collectedBy}</td>
            <td><span class="badge ${getEvidenceStatusClass(item.status)}">${item.status || "IN CUSTODY"}</span></td>
            <td class="actions">
                <button class="btn btn-primary btn-sm" onclick="viewEvidenceDetails(${item.evidenceId})">[ VIEW ]</button>
                <button class="btn btn-sm" onclick="openEditModal(${item.evidenceId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deleteEvidence(${item.evidenceId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function getEvidenceStatusClass(status) {
    if (!status) return "badge-secondary";
    const s = status.toUpperCase();
    if (s.includes("CUSTODY")) return "badge-info";
    if (s.includes("LAB")) return "badge-warning";
    if (s.includes("COURT")) return "badge-success";
    if (s.includes("DISPOSED") || s.includes("RELEASED")) return "badge-danger";
    return "badge-secondary";
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = evidenceList.filter(item => {
        return (
            (item.evidenceType && item.evidenceType.toLowerCase().includes(query)) ||
            (item.storageLocation && item.storageLocation.toLowerCase().includes(query)) ||
            (item.description && item.description.toLowerCase().includes(query)) ||
            (item.status && item.status.toLowerCase().includes(query)) ||
            (item.firId && String(item.firId).includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "LOG EVIDENCE ITEM";
    document.getElementById("evidenceForm").reset();
    document.getElementById("evidenceId").value = "";
    document.getElementById("collectedDate").value = new Date().toISOString().split("T")[0];
    document.getElementById("evidenceModal").style.display = "block";
}

function openEditModal(id) {
    const item = evidenceList.find(e => e.evidenceId === id);
    if (!item) return;

    document.getElementById("modalTitle").textContent = "EDIT EVIDENCE RECORD";
    document.getElementById("evidenceId").value = item.evidenceId;
    document.getElementById("firId").value = item.firId || "";
    document.getElementById("collectedBy").value = item.collectedBy || "";
    document.getElementById("evidenceType").value = item.evidenceType || "";
    document.getElementById("collectedDate").value = item.collectedDate || "";
    document.getElementById("storageLocation").value = item.storageLocation || "";
    document.getElementById("status").value = item.status || "IN CUSTODY";
    document.getElementById("description").value = item.description || "";

    document.getElementById("evidenceModal").style.display = "block";
}

function viewEvidenceDetails(id) {
    const item = evidenceList.find(e => e.evidenceId === id);
    if (!item) return;

    const list = document.getElementById("evidenceDetailsContent");
    list.innerHTML = `
        <li><strong>Evidence ID:</strong> <span>${item.evidenceId}</span></li>
        <li><strong>Linked FIR:</strong> <span>FIR #${item.firId}</span></li>
        <li><strong>Evidence Type:</strong> <span>${item.evidenceType || "-"}</span></li>
        <li><strong>Storage Location:</strong> <span>${item.storageLocation || "-"}</span></li>
        <li><strong>Collected Date:</strong> <span>${formatDate(item.collectedDate)}</span></li>
        <li><strong>Collected By:</strong> <span>Officer #${item.collectedBy}</span></li>
        <li><strong>Custody Status:</strong> <span><span class="badge ${getEvidenceStatusClass(item.status)}">${item.status || "IN CUSTODY"}</span></span></li>
        <li><strong>Description:</strong> <span>${item.description || "None"}</span></li>
    `;

    document.getElementById("viewModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveEvidence(e) {
    e.preventDefault();

    const id = document.getElementById("evidenceId").value;
    const evidenceData = {
        firId: parseInt(document.getElementById("firId").value),
        collectedBy: parseInt(document.getElementById("collectedBy").value),
        evidenceType: document.getElementById("evidenceType").value.trim(),
        collectedDate: document.getElementById("collectedDate").value || null,
        storageLocation: document.getElementById("storageLocation").value.trim() || null,
        status: document.getElementById("status").value,
        description: document.getElementById("description").value.trim() || null
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/evidences/${id}` : `${API_BASE_URL}/evidences`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(evidenceData)
        });

        if (!response.ok) throw new Error("Failed to save evidence");

        showAlert("success", isEdit ? "Evidence record updated." : "Evidence logged successfully.");
        closeModal("evidenceModal");
        loadEvidences();
    } catch (error) {
        console.error("Save evidence error:", error);
        showAlert("danger", "Could not save evidence. Check FIR ID and Officer ID.");
    }
}

async function deleteEvidence(id) {
    if (!confirm("Are you sure you want to delete this evidence record?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/evidences/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "Evidence item deleted.");
        loadEvidences();
    } catch (error) {
        console.error("Delete evidence error:", error);
        showAlert("danger", "Could not delete evidence record.");
    }
}
