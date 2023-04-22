window.onload = function (){
    let periodoSelect = document.getElementById("periodo");
    let periodoParam = GetURLParameter("periodo");
    if(periodoParam.length > 0){
        for(let i = 0; i < periodoSelect.options.length; i++){
            if(i == periodoParam){
                periodoSelect.selectedIndex = i;
                break;
            }
        }
    }

    let cidadeSelect = document.getElementById("cidade");
    let cidadeParam = GetURLParameter("cidade");
    if(cidadeParam.length > 0){
        for(let i = 0; i < cidadeSelect.options.length; i++){
            if(i == cidadeParam){
                cidadeSelect.selectedIndex = i;
                break;
            }
        }
    }

    let tipovalorSelect = document.getElementById("tipovalor");
    let tipovalorParam = GetURLParameter("tipovalor");
    if(tipovalorParam.length > 0){
        for(let i = 0; i < tipovalorSelect.options.length; i++){
            if(i == tipovalorParam){
                tipovalorSelect.selectedIndex = i;
                break;
            }
        }
    }

    let tipoSelect = document.getElementById("tipo");
    let tipoParam = GetURLParameter("tipo");
    if(tipoParam.length > 0){
        for(let i = 0; i < tipoSelect.options.length; i++){
            if(i == tipoParam){
                tipoSelect.selectedIndex = i;
                break;
            }
        }
    }

    let subtipoSelect = document.getElementById("subtipo");
    let subtipoParam = GetURLParameter("subtipo");
    if(subtipoParam.length > 0){
        for(let i = 0; i < subtipoSelect.options.length; i++){
            if(i == subtipoParam){
                subtipoSelect.selectedIndex = i;
                break;
            }
        }
    }

    UpdateSubtipos(document.getElementById("tipo"));
}

function Search(){
    let periodoSelect = document.getElementById("periodo");
    let cidadeSelect = document.getElementById("cidade");
    let tipovalorSelect = document.getElementById("tipovalor");
    let tipoSelect = document.getElementById("tipo");
    let subtipoSelect = document.getElementById("subtipo");

    window.location.href = 'atualizarConsulta?periodo=' + periodoSelect.selectedIndex + '&cidade=' + cidadeSelect.selectedIndex + '&tipovalor=' + tipovalorSelect.selectedIndex + '&tipo=' + tipoSelect.selectedIndex + '&subtipo=' + subtipoSelect.selectedIndex;
}

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

function GetURLParameter(parameter){
    let url = window.location.search.substring(1);
    let variables = url.split("&");
    for(let i = 0; i < variables.length; i++){
        let variableParams = variables[i].split("=");
        if(variableParams[0] == parameter)
            return variableParams[1];
    }
    return "";
}