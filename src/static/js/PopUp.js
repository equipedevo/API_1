window.onload = function(){
    document.getElementById("popupAjuda").style.display = "none";
    document.getElementById("popupFontes").style.display = "none";
}

function popupToggle(id){
    popup = document.getElementById(id);
    if(popup.style.display == "none"){
        popup.style.display = "block";
        console.log("If");
    }
    else{
        popup.style.display = "none";
        console.log("Else");
    }
}

document.getElementById("popupAjuda").addEventListener("click", function(event) { popupClose(event, "popupAjuda") });
document.getElementById("popupFontes").addEventListener("click", function(event) { popupClose(event, "popupFontes") });

function popupClose(event, id){
    console.log(id);
    let larguraTela = window.innerWidth;
    let alturaTela = window.innerHeight;
    let larguraPopUp = document.getElementById(id).children[0].offsetWidth;
    let alturaPopUp = document.getElementById(id).children[0].offsetHeight;
    let divisaoTelaW = (larguraTela - larguraPopUp)/2;
    let divisaoTelaH = (alturaTela - alturaPopUp)/2;
    if(event.clientX < divisaoTelaW || event.clientX > divisaoTelaW + larguraPopUp){
        popupToggle(id);
    }
    else if(event.clientY < divisaoTelaH || event.clientY > divisaoTelaH + alturaPopUp){
        popupToggle(id);
    }
}