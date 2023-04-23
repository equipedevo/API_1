window.onload = function (){
    let periodoSelect = document.getElementById("periodo");
    let periodoParam = GetURLParameter("periodo").split(",");
    if(periodoParam.length > 0){
        for(let i = 0; i < periodoParam.length; i++)
            periodoSelect.options[periodoParam[i]].selected = "selected";
    }

    let cidadeSelect = document.getElementById("cidade");
    let cidadeParam = GetURLParameter("cidade").split(",");
    if(cidadeParam.length > 0){
        for(let i = 0; i < cidadeParam.length; i++)
            cidadeSelect.options[cidadeParam[i]].selected = "selected"
    }

    let tipoValorSelect = document.getElementById("tipoValor");
    tipoValorSelect.selectedIndex = GetURLParameter("tipoValor");

    let tipoSelect = document.getElementById("tipo");
    tipoSelect.selectedIndex = GetURLParameter("tipo");

    let subTipoSelect = document.getElementById("subTipo");
    let subTipoParam = GetURLParameter("subTipo").split(",");
    if(subTipoParam.length > 0){
        for(let i = 0; i < subTipoParam.length; i++)
            subTipoSelect.options[subTipoParam[i]].selected = "selected"
    }

    UpdatesubTipos(document.getElementById("tipo"));
}

function Search(){
    let periodoSelect = document.getElementById("periodo");
    let cidadeSelect = document.getElementById("cidade");
    let tipoValorSelect = document.getElementById("tipoValor");
    let tipoSelect = document.getElementById("tipo");
    let subTipoSelect = document.getElementById("subTipo");
    
    window.location.href = 'atualizarConsulta?periodo=' + Array.from(periodoSelect.selectedOptions).map(option => option.index) +
        '&cidade=' + Array.from(cidadeSelect.selectedOptions).map(option => option.index) +
        '&tipoValor=' + tipoValorSelect.selectedIndex +
        '&tipo=' + tipoSelect.selectedIndex +
        '&subTipo=' + Array.from(subTipoSelect.selectedOptions).map(option => option.index);
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

function UpdatesubTipos(tipo){
    subTipoSelect = document.getElementById("subTipo");
    
    selectedTipo = tipo.options[tipo.selectedIndex].value;

    for (let i = 0; i < subTipoSelect.options.length; i++) {
        if (subTipoSelect.options[i].value != selectedTipo)
            subTipoSelect.options[i].style.display = "none";
        else subTipoSelect.options[i].style.display = "block";
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