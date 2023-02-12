function loadprofile(){
    var a = localStorage.getItem("user");
    document.getElementById("userprofilename").innerHTML = a;
    $.post("http://127.0.0.1:8000/ngo/prof/",
    {
        cphil: a,
    },function(data){
        document.getElementById("em").innerHTML = data['e'];
        document.getElementById("ph").innerHTML = data['ph'];
        let x = data['i'].split(",");
        for(let i = 1; i < 5; i++){
            console.log("Inside")
            contain = document.getElementById("intrestBox")
            let para = document.createElement('p');
            para.innerHTML = x[i];
            contain.appendChild(para);
        }
    });
}