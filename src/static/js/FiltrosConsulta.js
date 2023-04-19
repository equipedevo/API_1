function ShowSelect(selectID, btn){
    select = document.getElementById(selectID);
    if (select.style.display == "inline-block"){
        btn.firstChild.data = "Mostrar";
        select.style.display = "none";
    }
    else{
        btn.firstChild.data = "Esconder";
        select.style.display = "inline-block";
    }
}