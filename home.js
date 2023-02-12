function preload(){
    console.log("hello");
    let ngoNames;
    let temp;
    var max;
    var a = localStorage.getItem("user");
    document.getElementById("userid").innerHTML = "Welcome, " + a;
    console.log(a);
    var x = ["heading","goal"]
    console.log("goodbye")
    $.post("http://127.0.0.1:8000/ngo/getfav/",
    {
        cphil: a,
    },function(data){
        ngoNames = data.split(",");
        for (let i = 0; i < 3; i++){
            $.post("http://127.0.0.1:8000/ngo/ngoDetails/",
            {
                cphil: ngoNames[i+1],
            },function(data){
                document.getElementById(x[0] + (i+1)).innerHTML = data['name'];
                document.getElementById(x[1] + (i+1)).innerHTML = data['goal'];
            });
        }
    });
}
