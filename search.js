function preload(){
    console.log("Inside search js")
    var a = localStorage.getItem("NGOs");
    allNgos = a.split(',');
    console.log(allNgos);
    for (let i = 1; i < allNgos.length; i++){
        $.post("http://127.0.0.1:8000/ngo/ngoDetails/",
        {
            cphil: allNgos[i],
        },function(data){
            cardContainer = document.getElementById("cardCont")
            let card = document.createElement('div');
            card.className = "card";
            let cardBody = document.createElement('div');
            cardBody.className = 'card-body';
            let title = document.createElement('h4');
            title.className = 'card-title';
            var t = document.createTextNode(data['name']);
            title.appendChild(t);
            let details = document.createElement('p');
            details.className = 'card-text';
            var p = document.createTextNode(data['goal']);
            let link = document.createElement('a');
            var z = document.createTextNode("See Profile");
            link.className = "btn btn-primary";
            link.href = "http://127.0.0.1:8000/ngo/fakepage/";
            link.appendChild(z);
            details.appendChild(p);
            cardBody.appendChild(title);
            cardBody.appendChild(details);
            cardBody.appendChild(link);
            card.appendChild(cardBody);
            cardContainer.appendChild(card);
        });
    }
}