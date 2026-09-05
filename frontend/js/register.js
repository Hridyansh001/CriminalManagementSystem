// Terminal User Registration Logic

async function handleRegister(e) {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const dob = document.getElementById("dob").value;
    const gender = document.getElementById("gender").value;
    const residentialAddress = document.getElementById("residentialAddress").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const submitBtn = document.getElementById("regSubmitBtn");

    if (!name || !email || !phone || !dob || !gender || !residentialAddress || !password) {
        showAlert("danger", "All fields are required.");
        return;
    }

    if (password !== confirmPassword) {
        showAlert("danger", "Password confirmation mismatch.");
        return;
    }

    const userData = {
        name: name,
        email: email,
        phone: phone,
        dob: dob,
        gender: gender,
        residentialAddress: residentialAddress,
        password: password
    };

    submitBtn.disabled = true;
    submitBtn.textContent = "[ REGISTERING... ]";

    try {
        const response = await fetch(`${API_BASE_URL}/users`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userData)
        });

        if (response.ok) {
            showAlert("success", "Registration successful. Redirecting to login terminal...");
            setTimeout(() => {
                window.location.href = "index.html?registered=true&role=user";
            }, 900);
        } else {
            showAlert("danger", "Registration failed. Email may already exist in database.");
            submitBtn.disabled = false;
            submitBtn.textContent = "[ REGISTER ]";
        }
    } catch (error) {
        console.error("Registration error:", error);
        showAlert("danger", "Server communication error. Ensure backend is running.");
        submitBtn.disabled = false;
        submitBtn.textContent = "[ REGISTER ]";
    }
}
