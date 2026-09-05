// Police Station Management Logic (Police Only)

let stationList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("stations");
    loadStations();
});

async function loadStations() {
    const tbody = document.getElementById("stationTableBody");
    tbody.innerHTML = `<tr><td colspan="7" class="no-data">Querying police stations...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/policestations`);
        if (!response.ok) throw new Error("Failed to fetch police stations");
        stationList = await response.json();
        renderTable(stationList);
    } catch (error) {
        console.error("Error loading stations:", error);
        tbody.innerHTML = `<tr><td colspan="7" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch police station records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("stationTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" class="no-data">No police stations registered.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(s => `
        <tr>
            <td>${s.stationId}</td>
            <td><strong>${s.stationName || "-"}</strong></td>
            <td>${s.city || "-"}</td>
            <td><span class="badge badge-info">${s.jurisdiction || "-"}</span></td>
            <td>${s.address || "-"}</td>
            <td>${s.phone || "-"}</td>
            <td class="actions">
                <button class="btn btn-sm" onclick="openEditModal(${s.stationId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deleteStation(${s.stationId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = stationList.filter(s => {
        return (
            (s.stationName && s.stationName.toLowerCase().includes(query)) ||
            (s.city && s.city.toLowerCase().includes(query)) ||
            (s.jurisdiction && s.jurisdiction.toLowerCase().includes(query)) ||
            (s.address && s.address.toLowerCase().includes(query)) ||
            (s.phone && s.phone.toLowerCase().includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "ADD POLICE STATION";
    document.getElementById("stationForm").reset();
    document.getElementById("stationId").value = "";
    document.getElementById("stationModal").style.display = "block";
}

function openEditModal(id) {
    const item = stationList.find(s => s.stationId === id);
    if (!item) return;

    document.getElementById("modalTitle").textContent = "EDIT POLICE STATION";
    document.getElementById("stationId").value = item.stationId;
    document.getElementById("stationName").value = item.stationName || "";
    document.getElementById("city").value = item.city || "";
    document.getElementById("jurisdiction").value = item.jurisdiction || "";
    document.getElementById("address").value = item.address || "";
    document.getElementById("phone").value = item.phone || "";

    document.getElementById("stationModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveStation(e) {
    e.preventDefault();

    const id = document.getElementById("stationId").value;
    const stationData = {
        stationName: document.getElementById("stationName").value.trim(),
        city: document.getElementById("city").value.trim(),
        jurisdiction: document.getElementById("jurisdiction").value.trim() || null,
        address: document.getElementById("address").value.trim() || null,
        phone: document.getElementById("phone").value.trim() || null
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/policestations/${id}` : `${API_BASE_URL}/policestations`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(stationData)
        });

        if (!response.ok) throw new Error("Failed to save station");

        showAlert("success", isEdit ? "Station record updated." : "Station added successfully.");
        closeModal("stationModal");
        loadStations();
    } catch (error) {
        console.error("Save station error:", error);
        showAlert("danger", "Could not save police station.");
    }
}

async function deleteStation(id) {
    if (!confirm("Are you sure you want to delete this police station?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/policestations/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "Police station removed.");
        loadStations();
    } catch (error) {
        console.error("Delete station error:", error);
        showAlert("danger", "Could not delete police station.");
    }
}
