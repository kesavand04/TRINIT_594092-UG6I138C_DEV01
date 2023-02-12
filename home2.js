function searchFunction(){
    var searchedFor = document.getElementById("search").value;
    $.post("http://127.0.0.1:8000/ngo/searchNgos/",
    {
        cphil: searchedFor,
    },function(data){
        localStorage.setItem("NGOs", data);
        window.location.href = "http://127.0.0.1:8000/ngo/search/";
    });
}

function profilepage(){
    window.location.href = "http://127.0.0.1:8000/ngo/profile/";
}