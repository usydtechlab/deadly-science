
$(document).ready(function () {
    //Login Alter
    $(".hide").click(function (event) {
        //alert("Please log in/Sign up first, thanks!");
        event.preventDefault();
        $("#id01").show();
    });

    //signup
    $("#signup").click(function () {
        /* var text = "Thanks for joinging us, " + $("#fn").val() + "!";
        text.css("color", "blue");
        alert(text); */
        alert("Thanks for joinging us, " + $("#fn").val() + "!");
    });
});
