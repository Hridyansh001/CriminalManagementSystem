// Police Management Logic (Police/Admin Access)

let policeList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("police");
    loadPolice();
});

async function loadPolice() {
    const tbody = document.getElementById("policeTableBody");
    tbody.innerHTML = `<tr><td colspan="8" class="no-data">Querying police roster...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/police`);
        if (!response.ok) throw new Error("Failed to fetch police");
        policeList = await response.json();
        renderTable(policeList);
    } catch (error) {
        console.error("Error loading police:", error);
        tbody.innerHTML = `<tr><td colspan="8" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch police records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("policeTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">No police records found.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(p => `
        <tr>
            <td>${p.policeId}</td>
            <td><strong>${p.name || "-"}</strong></td>
            <td><span class="badge badge-info">${p.badgeNumber || "-"}</span></td>
            <td>${p.policeRank || "-"}</td>
            <td>Station #${p.stationId ?? "-"}</td>
            <td>${p.email || "-"}</td>
            <td>${p.phone || "-"}</td>
            <td class="actions">
                <button class="btn btn-primary btn-sm" onclick="viewPoliceDetails(${p.policeId})">[ VIEW ]</button>
                <button class="btn btn-sm" onclick="openEditModal(${p.policeId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deletePolice(${p.policeId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = policeList.filter(p => {
        return (
            (p.name && p.name.toLowerCase().includes(query)) ||
            (p.badgeNumber && p.badgeNumber.toLowerCase().includes(query)) ||
            (p.policeRank && p.policeRank.toLowerCase().includes(query)) ||
            (p.email && p.email.toLowerCase().includes(query)) ||
            (p.stationId && String(p.stationId).includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "REGISTER POLICE OFFICER";
    document.getElementById("policeForm").reset();
    document.getElementById("policeId").value = "";
    document.getElementById("password").required = true;
    document.getElementById("policeModal").style.display = "block";
}

function openEditModal(id) {
    const p = policeList.find(item => item.policeId === id);
    if (!item) return;

    document.getElementById("modalTitle").textContent = "EDIT OFFICER DETAILS";
    document.getElementById("policeId").value = p.policeId;
    document.getElementById("name").value = p.name || "";
    document.getElementById("badgeNumber").value = p.badgeNumber || "";
    document.getElementById("policeRank").value = p.policeRank || "";
    document.getElementById("stationId").value = p.stationId || "";
    document.getElementById("email").value = p.email || "";
    document.getElementById("phone").value = p.phone || "";
    document.getElementById("password").value = p.password || "";

    document.getElementById("policeModal").style.display = "block";
}

function viewPoliceDetails(id) {
    const p = policeList.find(item => item.policeId === id);
    if (!p) return;

    const list = document.getElementById("policeDetailsContent");
    list.innerHTML = `
        <li><strong>Officer ID:</strong> <span>${p.policeId}</span></li>
        <li><strong>Name:</strong> <span>${p.name || "-"}</span></li>
        <li><strong>Badge Number:</strong> <span>${p.badgeNumber || "-"}</span></li>
        <li><strong>Rank:</strong> <span>${p.policeRank || "-"}</span></li>
        <li><strong>Station ID:</strong> <span>Station #${p.stationId ?? "-"}</span></li>
        <li><strong>Email:</strong> <span>${p.email || "-"}</span></li>
        <li><strong>Phone:</strong> <span>${p.phone || "-"}</span></li>
    `;

    document.getElementById("viewModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function savePolice(e) {
    e.preventDefault();

    const id = document.getElementById("policeId").value;
    const policeData = {
        name: document.getElementById("name").value.trim(),
        badgeNumber: document.getElementById("badgeNumber").value.trim(),
        policeRank: document.getElementById("policeRank").value.trim(),
        stationId: parseInt(document.getElementById("stationId").value),
        email: document.getElementById("email").value.trim() || null,
        phone: document.getElementById("phone").value.trim() || null,
        password: document.getElementById("password").value
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/police/${id}` : `${API_BASE_URL}/police`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(policeData)
        });

        if (!response.ok) throw new Error("Failed to save officer");

        showAlert("success", isEdit ? "Officer record updated." : "Officer registered.");
        closeModal("policeModal");
        loadPolice();
    } catch (error) {
        console.error("Save police error:", error);
        showAlert("danger", "Could not save officer. Check Badge # uniqueness and Station ID.");
    }
}

async function deletePolice(id) {
    if (!confirm("Are you sure you want to delete this officer record?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/police/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "Officer record deleted.");
        loadPolice();
    } catch (error) {
        console.error("Delete police error:", error);
        showAlert("danger", "Could not delete officer record.");
    }
}
