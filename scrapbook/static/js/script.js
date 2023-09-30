function toggleDeleteMode() {
    var checkboxes = document.querySelectorAll(".photo-checkbox");
    var cancelButton = document.getElementById("cancelButton")
    var deleteButton = document.getElementById("deleteButton");

    checkboxes.forEach(function(checkbox) {
        checkbox.classList.toggle("d-none");
    });

    cancelButton.classList.toggle("d-none");

    if (deleteButton.innerText = "Delete") {
        deleteButton.innerText = "Delete Selected";
    } else {
        deleteButton.innerText = "Delete";
        document.getElementById("deleteForm").submit();
    }
}

function toggleCancelButton() {
    var checkboxes = document.querySelectorAll(".photo-checkbox");
    var cancelButton = document.getElementById("cancelButton")
    var deleteButton = document.getElementById("deleteButton");

    checkboxes.forEach(function(checkbox) {
        checkbox.classList.toggle("d-none");
    });

    cancelButton.classList.toggle("d-none");

    if (deleteButton.innerText = "Delete Selected") {
        deleteButton.innerText = "Delete";
    }
}