window.onload = function Load(){
    btnAjuda = document.getElementById("btnajuda");
    btnFontes = document.getElementById("btnfontes");
    popAjuda = document.getElementById("popupAjuda");
    popFontes = document.getElementById("popupFontes");

    console.log(btnAjuda);
}

function PopUpAjuda(btnAjuda, popAjuda){
    btnAjuda = document.getElementById("btnajuda");
    popAjuda = document.getElementById("popupAjuda");
    
    if(popAjuda.style.display == "none"){
        popAjuda.style.display = "block";
    }
    else{
        popAjuda.style.display = "none";
    }
    console.log(popAjuda.style.display);
}
