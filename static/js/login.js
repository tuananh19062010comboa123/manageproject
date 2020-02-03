console.log("login");

// email
$(".login").click(async function() {
    var email = $('.email').val();
    var password = $('.password').val();
    console.log("password: ", password);

    var data = {
        "email": email,
        "password": password
    }
    console.log(data)
    await send_login_toUrl(data);
    if (email == "admin" && password == "123") {
        window.location.replace("http://localhost:3000/main-page");
    } else {
        alert("email or password is not correct!")
    }
});

const send_login_toUrl = async(data) => {
    await $.ajax({
        type: 'POST',
        url: 'http://localhost:3000/login',
        data: data,
        success: function(msg) {
            // alert('wow' + msg);
            console.log('wow' + msg)
                // document.getElementById("loading_update").style.visibility = 'hidden'; 
        }
    });
}