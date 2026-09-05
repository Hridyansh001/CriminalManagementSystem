// Judgment Management Logic (Police Only)

let judgmentList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("judgments");
    loadJudgments();
});

async function loadJudgments() {
    const tbody = document.getElementById("judgmentsTableBody");
    tbody.innerHTML = `<tr><td colspan="6" class="no-data">Querying court judgments...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/judgments`);
        if (!response.ok) throw new Error("Failed to fetch judgments");
        judgmentList = await response.json();
        renderTable(judgmentList);
    } catch (error) {
        console.error("Error loading judgments:", error);
        tbody.innerHTML = `<tr><td colspan="6" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch judgment records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("judgmentsTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="6" class="no-data">No judgments recorded.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(j => `
        <tr>
            <td>${j.judgmentId}</td>
            <td>Case #${j.caseId}</td>
            <td>${formatDate(j.judgmentDate)}</td>
            <td><span class="badge ${getDecisionBadgeClass(j.decision)}">${j.decision || "N/A"}</span></td>
            <td>${j.sentence || "-"}</td>
            <td class="actions">
                <button class="btn btn-primary btn-sm" onclick="viewJudgmentDetails(${j.judgmentId})">[ VIEW ]</button>
                <button class="btn btn-sm" onclick="openEditModal(${j.judgmentId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deleteJudgment(${j.judgmentId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function getDecisionBadgeClass(decision) {
    if (!decision) return "badge-secondary";
    const d = decision.toUpperCase();
    if (d.includes("GUILTY") || d.includes("CONVICTED")) return "badge-danger";
    if (d.includes("ACQUITTED") || d.includes("NOT GUILTY")) return "badge-success";
    if (d.includes("SETTLED") || d.includes("DISMISSED")) return "badge-info";
    return "badge-secondary";
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = judgmentList.filter(j => {
        return (
            (j.decision && j.decision.toLowerCase().includes(query)) ||
            (j.sentence && j.sentence.toLowerCase().includes(query)) ||
            (j.basis && j.basis.toLowerCase().includes(query)) ||
            (j.remarks && j.remarks.toLowerCase().includes(query)) ||
            (j.caseId && String(j.caseId).includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "RECORD COURT JUDGMENT";
    document.getElementById("judgmentForm").reset();
    document.getElementById("judgmentId").value = "";
    document.getElementById("judgmentDate").value = new Date().toISOString().split("T")[0];
    document.getElementById("judgmentModal").style.display = "block";
}

function openEditModal(id) {
    const item = judgmentList.find(j => j.judgmentId === id);
    if (!item) return;

    document.getElementById("modalTitle").textContent = "EDIT JUDGMENT RECORD";
    document.getElementById("judgmentId").value = item.judgmentId;
    document.getElementById("caseId").value = item.caseId || "";
    document.getElementById("judgmentDate").value = item.judgmentDate || "";
    document.getElementById("decision").value = item.decision || "GUILTY / CONVICTED";
    document.getElementById("sentence").value = item.sentence || "";
    document.getElementById("basis").value = item.basis || "";
    document.getElementById("remarks").value = item.remarks || "";

    document.getElementById("judgmentModal").style.display = "block";
}

function viewJudgmentDetails(id) {
    const item = judgmentList.find(j => j.judgmentId === id);
    if (!item) return;

    const list = document.getElementById("judgmentDetailsContent");
    list.innerHTML = `
        <li><strong>Judgment ID:</strong> <span>${item.judgmentId}</span></li>
        <li><strong>Linked Case ID:</strong> <span>Case #${item.caseId}</span></li>
        <li><strong>Judgment Date:</strong> <span>${formatDate(item.judgmentDate)}</span></li>
        <li><strong>Decision Verdict:</strong> <span><span class="badge ${getDecisionBadgeClass(item.decision)}">${item.decision || "N/A"}</span></span></li>
        <li><strong>Sentence / Fine:</strong> <span>${item.sentence || "None"}</span></li>
        <li><strong>Legal Basis:</strong> <span>${item.basis || "None"}</span></li>
        <li><strong>Remarks:</strong> <span>${item.remarks || "None"}</span></li>
    `;

    document.getElementById("viewModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveJudgment(e) {
    e.preventDefault();

    const id = document.getElementById("judgmentId").value;
    const judgmentData = {
        caseId: parseInt(document.getElementById("caseId").value),
        judgmentDate: document.getElementById("judgmentDate").value,
        decision: document.getElementById("decision").value,
        sentence: document.getElementById("sentence").value.trim() || null,
        basis: document.getElementById("basis").value.trim() || null,
        remarks: document.getElementById("remarks").value.trim() || null
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/judgments/${id}` : `${API_BASE_URL}/judgments`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(judgmentData)
        });

        if (!response.ok) throw new Error("Failed to save judgment");

        showAlert("success", isEdit ? "Judgment updated." : "Judgment recorded.");
        closeModal("judgmentModal");
        loadJudgments();
    } catch (error) {
        console.error("Save judgment error:", error);
        showAlert("danger", "Could not save judgment. Ensure Case ID is valid.");
    }
}

async function deleteJudgment(id) {
    if (!confirm("Are you sure you want to delete this judgment record?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/judgments/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "Judgment record deleted.");
        loadJudgments();
    } catch (error) {
        console.error("Delete judgment error:", error);
        showAlert("danger", "Could not delete judgment record.");
    }
}
