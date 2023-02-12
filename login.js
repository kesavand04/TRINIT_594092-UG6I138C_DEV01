function logi(){
    var e = document.getElementById("email").value;
    var p = document.getElementById("pwd").value;
    $.post("http://127.0.0.1:8000/ngo/checkData/",
    {
        "cemail": e,
        "cpwd": p,
    },function(data){
       if(data['ans'] == "right"){
            localStorage.setItem("user", data['name']);
            var a = localStorage.getItem("user");
            window.location.href = "http://127.0.0.1:8000/ngo/home/";
       }
       else{
            alert("Enter the correct username or password");
       }
    });

}