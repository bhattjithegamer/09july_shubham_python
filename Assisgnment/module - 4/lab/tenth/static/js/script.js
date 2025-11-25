function validateForm() {
    let user = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let pass = document.getElementById("password").value;
    let error = document.getElementById("error");

    if (user.trim() === "") {
        error.innerHTML = "Username is required!";
        return false;
    }

    if (email.indexOf("@") === -1) {
        error.innerHTML = "Invalid email!";
        return false;
    }

    if (pass.length < 6) {
        error.innerHTML = "Password must be 6 characters!";
        return false;
    }

    error.innerHTML = "";
    alert("Form Submitted Successfully!");
    return true;
}
