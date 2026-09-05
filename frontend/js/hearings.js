// Hearing Management Logic (Police Only)

let hearingList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("hearings");
    loadHearings();
});

async function loadHearings() {
    const tbody = document.getElementById("hearingsTableBody");
    tbody.innerHTML = `<tr><td colspan="8" class="no-data">Querying hearing records...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/hearings`);
        if (!response.ok) throw new Error("Failed to fetch hearings");
        hearingList = await response.json();
        renderTable(hearingList);
    } catch (error) {
        console.error("Error loading hearings:", error);
        tbody.innerHTML = `<tr><td colspan="8" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch hearing records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("hearingsTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">No hearings scheduled.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(h => `
        <tr>
            <td>${h.hearingId}</td>
            <td>Case #${h.caseId}</td>
            <td>${formatDate(h.hearingDate)}</td>
            <td>${h.hearingTime || "-"}</td>
            <td>${h.hearingType || "-"}</td>
            <td><span class="badge ${getHearingBadgeClass(h.status)}">${h.status || "SCHEDULED"}</span></td>
            <td>${formatDate(h.nextHearingDate)}</td>
            <td class="actions">
                <button class="btn btn-primary btn-sm" onclick="viewHearingDetails(${h.hearingId})">[ VIEW ]</button>
                <button class="btn btn-sm" onclick="openEditModal(${h.hearingId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deleteHearing(${h.hearingId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function getHearingBadgeClass(status) {
    if (!status) return "badge-secondary";
    const s = status.toUpperCase();
    if (s.includes("COMPLETED")) return "badge-success";
    if (s.includes("SCHEDULED")) return "badge-info";
    if (s.includes("ADJOURNED")) return "badge-warning";
    if (s.includes("CANCELLED")) return "badge-danger";
    return "badge-secondary";
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = hearingList.filter(h => {
        return (
            (h.hearingType && h.hearingType.toLowerCase().includes(query)) ||
            (h.status && h.status.toLowerCase().includes(query)) ||
            (h.remarks && h.remarks.toLowerCase().includes(query)) ||
            (h.caseId && String(h.caseId).includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "SCHEDULE COURT HEARING";
    document.getElementById("hearingForm").reset();
    document.getElementById("hearingId").value = "";
    document.getElementById("hearingDate").value = new Date().toISOString().split("T")[0];
    document.getElementById("hearingModal").style.display = "block";
}

function openEditModal(id) {
    const item = hearingList.find(h => h.hearingId === id);
    if (!item) return;

    document.getElementById("modalTitle").textContent = "EDIT HEARING DETAILS";
    document.getElementById("hearingId").value = item.hearingId;
    document.getElementById("caseId").value = item.caseId || "";
    document.getElementById("hearingDate").value = item.hearingDate || "";
    document.getElementById("hearingTime").value = item.hearingTime ? item.hearingTime.substring(0, 5) : "";
    document.getElementById("hearingType").value = item.hearingType || "";
    document.getElementById("status").value = item.status || "SCHEDULED";
    document.getElementById("nextHearingDate").value = item.nextHearingDate || "";
    document.getElementById("remarks").value = item.remarks || "";

    document.getElementById("hearingModal").style.display = "block";
}

function viewHearingDetails(id) {
    const item = hearingList.find(h => h.hearingId === id);
    if (!item) return;

    const list = document.getElementById("hearingDetailsContent");
    list.innerHTML = `
        <li><strong>Hearing ID:</strong> <span>${item.hearingId}</span></li>
        <li><strong>Linked Case ID:</strong> <span>Case #${item.caseId}</span></li>
        <li><strong>Hearing Date:</strong> <span>${formatDate(item.hearingDate)}</span></li>
        <li><strong>Hearing Time:</strong> <span>${item.hearingTime || "-"}</span></li>
        <li><strong>Hearing Type:</strong> <span>${item.hearingType || "-"}</span></li>
        <li><strong>Status:</strong> <span><span class="badge ${getHearingBadgeClass(item.status)}">${item.status || "SCHEDULED"}</span></span></li>
        <li><strong>Next Date:</strong> <span>${formatDate(item.nextHearingDate)}</span></li>
        <li><strong>Remarks:</strong> <span>${item.remarks || "None"}</span></li>
    `;

    document.getElementById("viewModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveHearing(e) {
    e.preventDefault();

    const id = document.getElementById("hearingId").value;
    const timeVal = document.getElementById("hearingTime").value;

    const hearingData = {
        caseId: parseInt(document.getElementById("caseId").value),
        hearingDate: document.getElementById("hearingDate").value,
        hearingTime: timeVal ? (timeVal.length === 5 ? `${timeVal}:00` : timeVal) : null,
        hearingType: document.getElementById("hearingType").value.trim() || null,
        status: document.getElementById("status").value,
        nextHearingDate: document.getElementById("nextHearingDate").value || null,
        remarks: document.getElementById("remarks").value.trim() || null
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/hearings/${id}` : `${API_BASE_URL}/hearings`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(hearingData)
        });

        if (!response.ok) throw new Error("Failed to save hearing");

        showAlert("success", isEdit ? "Hearing updated." : "Hearing scheduled.");
        closeModal("hearingModal");
        loadHearings();
    } catch (error) {
        console.error("Save hearing error:", error);
        showAlert("danger", "Could not save hearing. Ensure Case ID is valid.");
    }
}

async function deleteHearing(id) {
    if (!confirm("Are you sure you want to delete this hearing record?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/hearings/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "Hearing record deleted.");
        loadHearings();
    } catch (error) {
        console.error("Delete hearing error:", error);
        showAlert("danger", "Could not delete hearing record.");
    }
}
