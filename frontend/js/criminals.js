// Criminal Management Logic (Police Only)

let criminalList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("criminals");
    loadCriminals();
});

async function loadCriminals() {
    const tbody = document.getElementById("criminalTableBody");
    tbody.innerHTML = `<tr><td colspan="8" class="no-data">Querying criminal records...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/criminals`);
        if (!response.ok) throw new Error("Failed to fetch criminals");
        criminalList = await response.json();
        renderTable(criminalList);
    } catch (error) {
        console.error("Error loading criminals:", error);
        tbody.innerHTML = `<tr><td colspan="8" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch criminal records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("criminalTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">No criminal records found.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(c => `
        <tr>
            <td>${c.criminalId}</td>
            <td><strong>${c.name || "-"}</strong></td>
            <td>${c.nationalId || "-"}</td>
            <td>${c.aliases || "-"}</td>
            <td>${c.levelOfCrime || "-"}</td>
            <td><span class="badge ${getCriminalStatusClass(c.status)}">${c.status || "UNKNOWN"}</span></td>
            <td>${c.livingStatus || "ALIVE"}</td>
            <td class="actions">
                <button class="btn btn-primary btn-sm" onclick="viewCriminalDetails(${c.criminalId})">[ VIEW ]</button>
                <button class="btn btn-sm" onclick="openEditModal(${c.criminalId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deleteCriminal(${c.criminalId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function getCriminalStatusClass(status) {
    if (!status) return "badge-secondary";
    const s = status.toUpperCase();
    if (s.includes("WANTED") || s.includes("LARGE")) return "badge-danger";
    if (s.includes("CUSTODY") || s.includes("CONVICTED")) return "badge-warning";
    if (s.includes("ACQUITTED") || s.includes("BAIL")) return "badge-info";
    return "badge-secondary";
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = criminalList.filter(c => {
        return (
            (c.name && c.name.toLowerCase().includes(query)) ||
            (c.nationalId && c.nationalId.toLowerCase().includes(query)) ||
            (c.aliases && c.aliases.toLowerCase().includes(query)) ||
            (c.levelOfCrime && c.levelOfCrime.toLowerCase().includes(query)) ||
            (c.status && c.status.toLowerCase().includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "ADD CRIMINAL RECORD";
    document.getElementById("criminalForm").reset();
    document.getElementById("criminalId").value = "";
    document.getElementById("criminalModal").style.display = "block";
}

function openEditModal(id) {
    const c = criminalList.find(item => item.criminalId === id);
    if (!c) return;

    document.getElementById("modalTitle").textContent = "EDIT CRIMINAL RECORD";
    document.getElementById("criminalId").value = c.criminalId;
    document.getElementById("name").value = c.name || "";
    document.getElementById("nationalId").value = c.nationalId || "";
    document.getElementById("aliases").value = c.aliases || "";
    document.getElementById("levelOfCrime").value = c.levelOfCrime || "";
    document.getElementById("status").value = c.status || "IN CUSTODY";
    document.getElementById("livingStatus").value = c.livingStatus || "ALIVE";

    document.getElementById("criminalModal").style.display = "block";
}

function viewCriminalDetails(id) {
    const c = criminalList.find(item => item.criminalId === id);
    if (!c) return;

    const list = document.getElementById("criminalDetailsContent");
    list.innerHTML = `
        <li><strong>Criminal ID:</strong> <span>${c.criminalId}</span></li>
        <li><strong>Full Name:</strong> <span>${c.name || "-"}</span></li>
        <li><strong>National ID:</strong> <span>${c.nationalId || "-"}</span></li>
        <li><strong>Aliases:</strong> <span>${c.aliases || "None"}</span></li>
        <li><strong>Crime Level:</strong> <span>${c.levelOfCrime || "-"}</span></li>
        <li><strong>Custody Status:</strong> <span><span class="badge ${getCriminalStatusClass(c.status)}">${c.status || "UNKNOWN"}</span></span></li>
        <li><strong>Living Status:</strong> <span>${c.livingStatus || "ALIVE"}</span></li>
    `;

    document.getElementById("viewModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveCriminal(e) {
    e.preventDefault();

    const id = document.getElementById("criminalId").value;
    const criminalData = {
        name: document.getElementById("name").value.trim(),
        nationalId: document.getElementById("nationalId").value.trim() || null,
        aliases: document.getElementById("aliases").value.trim() || null,
        levelOfCrime: document.getElementById("levelOfCrime").value.trim() || null,
        status: document.getElementById("status").value,
        livingStatus: document.getElementById("livingStatus").value
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/criminals/${id}` : `${API_BASE_URL}/criminals`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(criminalData)
        });

        if (!response.ok) throw new Error("Failed to save criminal record");

        showAlert("success", isEdit ? "Criminal record updated." : "Criminal record added.");
        closeModal("criminalModal");
        loadCriminals();
    } catch (error) {
        console.error("Save criminal error:", error);
        showAlert("danger", "Could not save criminal record. Check National ID uniqueness.");
    }
}

async function deleteCriminal(id) {
    if (!confirm("Are you sure you want to delete this criminal record?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/criminals/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "Criminal record removed.");
        loadCriminals();
    } catch (error) {
        console.error("Delete criminal error:", error);
        showAlert("danger", "Could not delete criminal record.");
    }
}
