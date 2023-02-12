function registerUser(){
    n = document.getElementById("userName").value;
    e = document.getElementById("userEmail").value;
    p = document.getElementById("userPass").value;
    ph = document.getElementById("userPhone").value;
    // i = document.getElementById("userInterest").value;
    var intr="";
    for (let i = 1; i <= 9; i++){
        x = "check" + i;
        k = document.getElementById(x);
        if (k.checked == true){
            var lg1= document.getElementById(x).value;
            intr = intr + "," + lg1;
        }
    }
    console.log(intr);
    $.post("http://127.0.0.1:8000/ngo/register/Phil/",
    {
        "phil_name": n,
        "phil_email": e,
        "phil_pass": p,
        "phil_phoneNo": ph,
        "phil_interest": intr,
    });

}

function registerNgo(){
    n = document.getElementById("ngoName").value;
    l = document.getElementById("ngoLoc").value;
    w = document.getElementById("work").value;
    g = document.getElementById("fund").value;
    i = document.getElementById("ngoInterest").value;
    p = document.getElementById("ngoPass").value;
    ph = document.getElementById("ngoPhone").value;
    $.post("http://127.0.0.1:8000/ngo/register/Ngo/",
    {
        "ngo_name": n,
        "ngo_loc": l,
        "ngo_prevWork": w,
        "ngo_goal": g,
        "ngo_sector": i,
        "ngo_pass": p,
        "ngo_phoneNo": ph,
    });
   
}

function loginNgo(){
    window.location.href = "http://127.0.0.1:8000/ngo/philLogin/";
}

function loginUser(){
    window.location.href = "http://127.0.0.1:8000/ngo/ngoLogin/";
}