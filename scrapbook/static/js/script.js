console.log("Script loaded.");

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

document.addEventListener('DOMContentLoaded', function() {
    const shareForm = document.getElementById('shareForm');

    if (shareForm) {
        shareForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('usernameShareField').value;

            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch('/share/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken
                },
                body: `username=${username}`
            })
            .then(response => response.json())
            .then(data => {
                const errorElement = document.getElementById('shareError');
                const successElement = document.getElementById('shareSuccess');

                if (data.status === 'success') {
                    successElement.textContent = data.message;
                    errorElement.textContent = '';
                } else {
                    errorElement.textContent = data.message;
                    successElement.textContent = ''
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    } else {
        console.log("Did not find shareForm.");  
    }
});
