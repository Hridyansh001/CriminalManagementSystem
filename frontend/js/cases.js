// Case Management Logic (Police Only)

let caseList = [];
let firList = [];
let courtList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("cases");
    loadCases();

    // Check if firId passed in query parameters
    const urlParams = new URLSearchParams(window.location.search);
    const firIdParam = urlParams.get("firId");
    if (firIdParam) {
        setTimeout(() => {
            openAddModalForFir(parseInt(firIdParam));
        }, 300);
    }
});

async function loadCases() {
    const casesTbody = document.getElementById("casesTableBody");
    const courtFirsTbody = document.getElementById("courtFirsTableBody");
    casesTbody.innerHTML = `<tr><td colspan="8" class="no-data">Querying court cases...</td></tr>`;
    courtFirsTbody.innerHTML = `<tr><td colspan="8" class="no-data">Checking court-referred FIRs...</td></tr>`;

    try {
        const [casesRes, firsRes, courtsRes] = await Promise.allSettled([
            fetch(`${API_BASE_URL}/cases`),
            fetch(`${API_BASE_URL}/firs`),
            fetch(`${API_BASE_URL}/courts`)
        ]);

        if (casesRes.status === "fulfilled" && casesRes.value.ok) {
            caseList = await casesRes.value.json();
        } else {
            caseList = [];
        }

        if (firsRes.status === "fulfilled" && firsRes.value.ok) {
            firList = await firsRes.value.json();
        } else {
            firList = [];
        }

        if (courtsRes.status === "fulfilled" && courtsRes.value.ok) {
            courtList = await courtsRes.value.json();
        } else {
            courtList = [];
        }

        renderTable(caseList);
        renderCourtFirsTable();
    } catch (error) {
        console.error("Error loading cases:", error);
        casesTbody.innerHTML = `<tr><td colspan="8" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        courtFirsTbody.innerHTML = `<tr><td colspan="8" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch case records.");
    }
}

function getFirInfo(firId) {
    if (!firId) return null;
    return firList.find(f => f.fir_id === firId);
}

function getCourtInfo(courtId) {
    if (!courtId) return null;
    return courtList.find(c => c.courtId === courtId);
}

function renderTable(data) {
    const tbody = document.getElementById("casesTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">No court cases registered.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(c => {
        const fir = getFirInfo(c.firId);
        const court = getCourtInfo(c.courtId);
        const firText = fir ? `${fir.firnumber || 'FIR #' + c.firId}` : `FIR #${c.firId}`;
        const courtText = court ? court.courtName : `Court #${c.courtId}`;

        return `
            <tr>
                <td>${c.caseId}</td>
                <td><strong>${c.caseNumber || "-"}</strong></td>
                <td>${firText}</td>
                <td>${courtText}</td>
                <td>${c.caseType || "-"}</td>
                <td>${formatDate(c.filingDate)}</td>
                <td><span class="badge ${getCaseStatusClass(c.status)}">${c.status || "PENDING"}</span></td>
                <td class="actions">
                    <button class="btn btn-primary btn-sm" onclick="viewCaseDetails(${c.caseId})">[ VIEW ]</button>
                    <button class="btn btn-sm" onclick="openEditModal(${c.caseId})">[ EDIT ]</button>
                    <button class="btn btn-danger btn-sm" onclick="deleteCase(${c.caseId})">[ DEL ]</button>
                </td>
            </tr>
        `;
    }).join("");
}

function renderCourtFirsTable() {
    const tbody = document.getElementById("courtFirsTableBody");
    if (!firList || firList.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">No FIR records found.</td></tr>`;
        return;
    }

    // Filter FIRs whose status is 'Case In Court' or contains 'court'
    const courtFirs = firList.filter(f => {
        const s = (f.status || "").toLowerCase();
        return s.includes("court");
    });

    if (courtFirs.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">No FIRs currently marked as 'Case In Court'.</td></tr>`;
        return;
    }

    tbody.innerHTML = courtFirs.map(f => {
        const linkedCase = caseList.find(c => c.firId === f.fir_id);
        const locationText = `${f.location || '-'}${f.jurisdiction ? ' (' + f.jurisdiction + ')' : ''}`;

        let caseStatusBadge = "";
        let actionBtn = "";

        if (linkedCase) {
            caseStatusBadge = `<span class="badge ${getCaseStatusClass(linkedCase.status)}">${linkedCase.caseNumber} [${linkedCase.status}]</span>`;
            actionBtn = `<button class="btn btn-primary btn-sm" onclick="viewCaseDetails(${linkedCase.caseId})">[ VIEW CASE ]</button>`;
        } else {
            caseStatusBadge = `<span class="badge badge-warning">AWAITING CASE REGISTRATION</span>`;
            actionBtn = `<button class="btn btn-success btn-sm" onclick="openAddModalForFir(${f.fir_id})">[ + REGISTER CASE ]</button>`;
        }

        return `
            <tr>
                <td>${f.fir_id}</td>
                <td><strong>${f.firnumber || "-"}</strong></td>
                <td>${f.crimetype || "-"}</td>
                <td>${formatDate(f.date_filed)}</td>
                <td>${locationText}</td>
                <td><span class="badge badge-info">${f.status || "Case In Court"}</span></td>
                <td>${caseStatusBadge}</td>
                <td class="actions">
                    ${actionBtn}
                </td>
            </tr>
        `;
    }).join("");
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
        const fir = getFirInfo(c.firId);
        const court = getCourtInfo(c.courtId);
        const firText = fir ? (fir.firnumber || "").toLowerCase() : "";
        const courtText = court ? (court.courtName || "").toLowerCase() : "";

        return (
            (c.caseNumber && c.caseNumber.toLowerCase().includes(query)) ||
            (c.caseType && c.caseType.toLowerCase().includes(query)) ||
            (c.status && c.status.toLowerCase().includes(query)) ||
            (c.firId && String(c.firId).includes(query)) ||
            (c.courtId && String(c.courtId).includes(query)) ||
            firText.includes(query) ||
            courtText.includes(query)
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "REGISTER COURT CASE";
    document.getElementById("caseForm").reset();
    document.getElementById("caseId").value = "";
    document.getElementById("filingDate").value = new Date().toISOString().split("T")[0];

    const rand = Math.floor(100 + Math.random() * 900);
    document.getElementById("caseNumber").value = `CASE-${new Date().getFullYear()}-${rand}`;

    document.getElementById("caseModal").style.display = "block";
}

function openAddModalForFir(firId) {
    openAddModal();
    const fir = getFirInfo(firId);
    document.getElementById("firId").value = firId;
    if (fir && fir.crimetype) {
        document.getElementById("caseType").value = fir.crimetype;
    }
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

    const statusSelect = document.getElementById("status");
    const rawStatus = item.status || "Under Trial";
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

    document.getElementById("caseModal").style.display = "block";
}

function viewCaseDetails(id) {
    const item = caseList.find(c => c.caseId === id);
    if (!item) return;

    const fir = getFirInfo(item.firId);
    const court = getCourtInfo(item.courtId);

    const list = document.getElementById("caseDetailsContent");
    list.innerHTML = `
        <li><strong>Case ID:</strong> <span>${item.caseId}</span></li>
        <li><strong>Case Number:</strong> <span>${item.caseNumber || "-"}</span></li>
        <li><strong>Linked FIR:</strong> <span>FIR #${item.firId} ${fir ? '(' + (fir.firnumber || '') + ' - ' + (fir.crimetype || '') + ')' : ''}</span></li>
        <li><strong>Assigned Court:</strong> <span>Court #${item.courtId} ${court ? '(' + court.courtName + ' - ' + court.city + ')' : ''}</span></li>
        <li><strong>Case Type:</strong> <span>${item.caseType || "-"}</span></li>
        <li><strong>Filing Date:</strong> <span>${formatDate(item.filingDate)}</span></li>
        <li><strong>Case Status:</strong> <span><span class="badge ${getCaseStatusClass(item.status)}">${item.status || "PENDING"}</span></span></li>
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
