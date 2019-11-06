function searching() {
    var input = document.getElementById('searchBar');
    var filter = input.value.toUpperCase();
    var cards = document.getElementsByClassName("card");
    var i;
    for (i = 0; i < cards.length; i++) {
        var content = cards[i].textContent || cards[i].innerText;
        var hasText = content.indexOf(filter) !== -1;
        if (hasText) {
            cards[i].style.display = "block";
        } else {
            cards[i].style.display = "none";
        }
    }
}

function pwCheck() {
    var newPw = document.getElementById('NewPw').value;
    var conPw = document.getElementById('ConfirmPw').value;
    if (newPw != "" && conPw != "") {
        if (newPw != conPw) {
            alert("The passwords are not the same!");
        }
    } else {
        alert("Please enter the new password!");
    }
}
function closeModal() {
    // Get the modal
    var modal = document.getElementById('id01');

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

/* Searching
function searching() {
    var input = document.getElementById('searchBar');
    var filter = input.value.toUpperCase();
    var cards = document.getElementsByClassName("card");
    var i;
    for (i = 0; i < cards.length; i++) {
        removeCards(cards[i], "show");
        var content = cards[i].textContent || cards[i].innerText;
        var hasText = content.indexOf(filter) !== -1;
        if (hasText) {
            addCard(cards[i], "show");
            cards[i].style.display = "";
        }
                     cards[i].style.display = "";
                } else {
                    cards[i].style.display = "none";
                }
    }
}

function addCard(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}

function removeCards(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}  */