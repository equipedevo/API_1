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

function UpdateSubtipos(tipo){
    subtipoSelect = document.getElementById("subtipo");
    
    selectedTipo = tipo.options[tipo.selectedIndex].value;

    for (let i = 0; i < subtipoSelect.options.length; i++) {
        if (subtipoSelect.options[i].value != selectedTipo)
            subtipoSelect.options[i].style.display = "none";
        else subtipoSelect.options[i].style.display = "block";
    }
}