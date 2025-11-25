function validateForm() {
    let valid = true;

    // Inputs
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    // Error fields
    const nameError = document.getElementById("nameError");
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");

    // Name Validation
    if (name === "") {
        nameError.style.display = "block";
        valid = false;
    } else {
        nameError.style.display = "none";
    }

    // Email Validation (simple regex)
    let emailPattern = /\S+@\S+\.\S+/;
    if (!emailPattern.test(email)) {
        emailError.style.display = "block";
        valid = false;
    } else {
        emailError.style.display = "none";
    }

    // Password Validation
    if (password.length < 6) {
        passwordError.style.display = "block";
        valid = false;
    } else {
        passwordError.style.display = "none";
    }

    return valid;
}
