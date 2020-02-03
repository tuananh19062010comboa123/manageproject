console.log("register");
$("#signup").click(async function(){
    var name = $('#name').val();
    var email = $('#email').val();
    var pass = $('#pass').val();
    var re_pass = $('#re_pass').val();

    if(re_pass != pass){
        alert(" re_pass and pass are not same")
    }
    // check email dung chua
    // if(email == "admin"){
    //     alert("email already exists")
    // }

    else{
        var data = {
            "email": email,
            "pass": pass,
            "name": name
        }
        console.log(data)
        await send_register_toUrl(data);   
        alert("You have successfully registered")
        window.location.replace("http://localhost:3000/login");
        }
  });

  const send_register_toUrl = async (data) => {
    await $.ajax({
        type: 'POST',
        url: 'http://localhost:3000/login',
        data: data,
        success: function (msg) {
            // alert('wow' + msg);
            console.log('wow' + msg)
            // document.getElementById("loading_update").style.visibility = 'hidden'; 
        }
    });
}