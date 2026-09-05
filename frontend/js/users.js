// User Management Logic (Admin / Police Access)

let userList = [];

document.addEventListener("DOMContentLoaded", () => {
    const role = checkRoleGuard(["police"]);
    if (!role) return;

    renderNavbar("users");
    loadUsers();
});

async function loadUsers() {
    const tbody = document.getElementById("userTableBody");
    tbody.innerHTML = `<tr><td colspan="8" class="no-data">Querying citizen accounts...</td></tr>`;

    try {
        const response = await fetch(`${API_BASE_URL}/users`);
        if (!response.ok) throw new Error("Failed to fetch users");
        userList = await response.json();
        renderTable(userList);
    } catch (error) {
        console.error("Error loading users:", error);
        tbody.innerHTML = `<tr><td colspan="8" class="no-data" style="color: #f48771;">Database query error.</td></tr>`;
        showAlert("danger", "Could not fetch users.");
    }
}

function renderTable(data) {
    const tbody = document.getElementById("userTableBody");
    if (!data || data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="no-data">No citizen records found.</td></tr>`;
        return;
    }

    tbody.innerHTML = data.map(u => `
        <tr>
            <td>${u.userId}</td>
            <td><strong>${u.name || "-"}</strong></td>
            <td>${u.email || "-"}</td>
            <td>${u.phone || "-"}</td>
            <td>${formatDate(u.dob)}</td>
            <td>${u.gender || "-"}</td>
            <td>${u.residentialAddress || "-"}</td>
            <td class="actions">
                <button class="btn btn-primary btn-sm" onclick="viewUserDetails(${u.userId})">[ VIEW ]</button>
                <button class="btn btn-sm" onclick="openEditModal(${u.userId})">[ EDIT ]</button>
                <button class="btn btn-danger btn-sm" onclick="deleteUser(${u.userId})">[ DEL ]</button>
            </td>
        </tr>
    `).join("");
}

function filterTable() {
    const query = document.getElementById("searchInput").value.toLowerCase();
    const filtered = userList.filter(u => {
        return (
            (u.name && u.name.toLowerCase().includes(query)) ||
            (u.email && u.email.toLowerCase().includes(query)) ||
            (u.phone && u.phone.toLowerCase().includes(query)) ||
            (u.residentialAddress && u.residentialAddress.toLowerCase().includes(query))
        );
    });
    renderTable(filtered);
}

function openAddModal() {
    document.getElementById("modalTitle").textContent = "REGISTER CITIZEN ACCOUNT";
    document.getElementById("userForm").reset();
    document.getElementById("userId").value = "";
    document.getElementById("password").required = true;
    document.getElementById("userModal").style.display = "block";
}

function openEditModal(id) {
    const u = userList.find(item => item.userId === id);
    if (!u) return;

    document.getElementById("modalTitle").textContent = "EDIT CITIZEN DETAILS";
    document.getElementById("userId").value = u.userId;
    document.getElementById("name").value = u.name || "";
    document.getElementById("email").value = u.email || "";
    document.getElementById("phone").value = u.phone || "";
    document.getElementById("dob").value = u.dob || "";
    document.getElementById("gender").value = u.gender || "";
    document.getElementById("password").value = u.password || "";
    document.getElementById("residentialAddress").value = u.residentialAddress || "";

    document.getElementById("userModal").style.display = "block";
}

function viewUserDetails(id) {
    const u = userList.find(item => item.userId === id);
    if (!u) return;

    const list = document.getElementById("userDetailsContent");
    list.innerHTML = `
        <li><strong>User ID:</strong> <span>${u.userId}</span></li>
        <li><strong>Full Name:</strong> <span>${u.name || "-"}</span></li>
        <li><strong>Email Address:</strong> <span>${u.email || "-"}</span></li>
        <li><strong>Phone Number:</strong> <span>${u.phone || "-"}</span></li>
        <li><strong>Date of Birth:</strong> <span>${formatDate(u.dob)}</span></li>
        <li><strong>Gender:</strong> <span>${u.gender || "-"}</span></li>
        <li><strong>Address:</strong> <span>${u.residentialAddress || "None"}</span></li>
    `;

    document.getElementById("viewModal").style.display = "block";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

async function saveUser(e) {
    e.preventDefault();

    const id = document.getElementById("userId").value;
    const userData = {
        name: document.getElementById("name").value.trim(),
        email: document.getElementById("email").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        dob: document.getElementById("dob").value || null,
        gender: document.getElementById("gender").value,
        password: document.getElementById("password").value,
        residentialAddress: document.getElementById("residentialAddress").value.trim()
    };

    const isEdit = Boolean(id);
    const url = isEdit ? `${API_BASE_URL}/users/${id}` : `${API_BASE_URL}/users`;
    const method = isEdit ? "PUT" : "POST";

    try {
        const response = await fetch(url, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userData)
        });

        if (!response.ok) throw new Error("Failed to save user");

        showAlert("success", isEdit ? "User account updated." : "Citizen registered successfully.");
        closeModal("userModal");
        loadUsers();
    } catch (error) {
        console.error("Save user error:", error);
        showAlert("danger", "Could not save user. Ensure email is unique.");
    }
}

async function deleteUser(id) {
    if (!confirm("Are you sure you want to delete this user?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/users/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) throw new Error("Delete failed");

        showAlert("success", "User record deleted.");
        loadUsers();
    } catch (error) {
        console.error("Delete user error:", error);
        showAlert("danger", "Could not delete user. Record may be linked to active FIRs.");
    }
}
