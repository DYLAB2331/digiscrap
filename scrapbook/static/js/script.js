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
    const uploadForm = document.getElementById('uploadForm');

    // Event listener for shareForm
    if (shareForm) {
        shareForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('usernameShareField').value;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch('share/', {
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
    }
});

$(document).ready(function() {
    $("#uploadForm").on('submit', function(event) {
        console.log("Inside event listener");
        event.preventDefault();

        let photoFile = $("#photoUploadField")[0].files[0];
        let photoDescription = $("#photoDescriptionField").val();
        let photoDate = $("#photoDateField").val();
        let csrfToken = $('[name="csrfmiddlewaretoken"]').val();

        let formData = new FormData();
        formData.append('photo', photoFile);
        formData.append('description', photoDescription);
        formData.append('date', photoDate);

        $.ajax({
            url: 'upload/',
            type: 'POST',
            headers: {'X-CSRFToken': csrfToken},
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                if (data.status === 'success') {
                    $("#uploadSuccess").text(data.message);
                    $("#uploadError").text('');
                } else {
                    $("#uploadError").text(data.message);
                    $("#uploadSuccess").text('');
                }
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });
});




