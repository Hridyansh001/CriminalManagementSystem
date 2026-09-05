// Court Management Logic (Police Only)

let courtList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("courts");
    loadCourts();
});

async function loadCourts() {
    const tbody = document.getElementById("courtTableBody");
    tbody.innerHTML = `<tr><td colspan="6" class="no-data">Querying court records...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/courts`);
        if (!response.ok) throw new Error("Failed to fetch courts");
        courtList = await response.json();
        renderTable(courtList);
    } catch (error) {
        console.error("Error loading courts:", error);
        tbody.innerHTML = `<tr><td colspan="6" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch court records.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("courtTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="6" class="no-data">No courts registered.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(c => `
        <tr>
            <td>${c.courtId}</td>
            <td><strong>${c.courtName || "-"}</strong></td>
            <td><span class="badge badge-info">${c.courtType || "-"}</span></td>
            <td>${c.location || "-"}</td>
            <td>${c.judgeName || "-"}</td>
            <td class="actions">
                <button class="btn btn-sm" onclick="openEditModal(${c.courtId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deleteCourt(${c.courtId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = courtList.filter(c => {
        return (
            (c.courtName && c.courtName.toLowerCase().includes(query)) ||
            (c.courtType && c.courtType.toLowerCase().includes(query)) ||
            (c.location && c.location.toLowerCase().includes(query)) ||
            (c.judgeName && c.judgeName.toLowerCase().includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "REGISTER COURT";
    document.getElementById("courtForm").reset();
    document.getElementById("courtId").value = "";
    document.getElementById("courtModal").style.display = "block";
}

function openEditModal(id) {
    const item = courtList.find(c => c.courtId === id);
    if (!item) return;

    document.getElementById("modalTitle").textContent = "EDIT COURT DETAILS";
    document.getElementById("courtId").value = item.courtId;
    document.getElementById("courtName").value = item.courtName || "";
    document.getElementById("courtType").value = item.courtType || "";
    document.getElementById("location").value = item.location || "";
    document.getElementById("judgeName").value = item.judgeName || "";

    document.getElementById("courtModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveCourt(e) {
    e.preventDefault();

    const id = document.getElementById("courtId").value;
    const courtData = {
        courtName: document.getElementById("courtName").value.trim(),
        courtType: document.getElementById("courtType").value.trim() || null,
        location: document.getElementById("location").value.trim() || null,
        judgeName: document.getElementById("judgeName").value.trim() || null
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/courts/${id}` : `${API_BASE_URL}/courts`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(courtData)
        });

        if (!response.ok) throw new Error("Failed to save court");

        showAlert("success", isEdit ? "Court updated." : "Court registered.");
        closeModal("courtModal");
        loadCourts();
    } catch (error) {
        console.error("Save court error:", error);
        showAlert("danger", "Could not save court record.");
    }
}

async function deleteCourt(id) {
    if (!confirm("Are you sure you want to delete this court?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/courts/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "Court record deleted.");
        loadCourts();
    } catch (error) {
        console.error("Delete court error:", error);
        showAlert("danger", "Could not delete court.");
    }
}
