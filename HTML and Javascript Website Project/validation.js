function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    var y = document.forms["myForm"]["lname"].value;
    var z = document.forms["myForm"]["email"].value;
    if (x == "") {
        alert("First Name must be entered");
    }
    if (y == "") {
        alert("Last Name must be entered");

    }
    if (z == "") {
        alert("E-mail must be entered");
    }
    alert("Form Submitted Successfully!");
    return true;
}