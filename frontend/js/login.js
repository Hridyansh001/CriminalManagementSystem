// Terminal Login Logic

let currentSelectedRole = "police";

document.addEventListener("DOMContentLoaded", () => {
    // If already logged in, redirect to dashboard
    if (getRole()) {
        window.location.href = "dashboard.html";
        return;
    }

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get("role") === "user") {
        selectRole("user");
    }
    if (urlParams.get("registered") === "true") {
        selectRole("user");
        showAlert("success", "Registration successful. Please login with your credentials.");
    }
});

function selectRole(role) {
    currentSelectedRole = role;
    const tabCop = document.getElementById("tabCop");
    const tabUser = document.getElementById("tabUser");
    const label = document.getElementById("identifierLabel");
    const input = document.getElementById("identifier");
    const btn = document.getElementById("loginBtn");
    const formHeader = document.getElementById("formHeader");

    if (role === "police") {
        tabCop.classList.add("active");
        tabUser.classList.remove("active");
        formHeader.textContent = ">> POLICE LOGIN";
        label.textContent = "Badge Number / Officer Email:";
        input.placeholder = "Enter badge # or email";
        btn.textContent = "[ LOGIN AS POLICE ]";
    } else {
        tabUser.classList.add("active");
        tabCop.classList.remove("active");
        formHeader.textContent = ">> CITIZEN USER LOGIN";
        label.textContent = "Registered Email Address:";
        input.placeholder = "Enter email address";
        btn.textContent = "[ LOGIN AS USER ]";
    }
}

async function handleLogin(e) {
    e.preventDefault();

    const identifier = document.getElementById("identifier").value.trim();
    const password = document.getElementById("password").value.trim();
    const btn = document.getElementById("loginBtn");

    if (!identifier || !password) {
        showAlert("danger", "Identifier and password required.");
        return;
    }

    btn.disabled = true;
    btn.textContent = "[ AUTHENTICATING... ]";

    try {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ identifier, password })
        });

        const data = await response.json();

        if (response.ok && data.success) {
            const userRole = data.role ? data.role.toLowerCase() : currentSelectedRole;

            localStorage.setItem("role", userRole);
            localStorage.setItem("userId", data.id);
            localStorage.setItem("name", data.name || (userRole === "police" ? "Officer" : "User"));

            showAlert("success", "Authentication verified. Access granted.");
            setTimeout(() => {
                window.location.href = "dashboard.html";
            }, 600);
        } else {
            showAlert("danger", data.msg || "Authentication failed. Invalid credentials.");
            btn.disabled = false;
            btn.textContent = currentSelectedRole === "police" ? "[ LOGIN AS POLICE ]" : "[ LOGIN AS USER ]";
        }
    } catch (error) {
        console.error("Login error:", error);
        showAlert("danger", "Connection error. Ensure backend server is running on :8080");
        btn.disabled = false;
        btn.textContent = currentSelectedRole === "police" ? "[ LOGIN AS POLICE ]" : "[ LOGIN AS USER ]";
    }
}
