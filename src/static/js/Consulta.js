window.addEventListener("load", function (){
    let periodoSelect = document.getElementById("periodo");
    let periodoParam = GetURLParameter("periodo").split(",");
    if(periodoParam != ""){
        if(periodoParam.length > 0){
            for(let i = 0; i < periodoParam.length; i++)
                periodoSelect.options[periodoParam[i]].selected = "selected";
        }
    }

    let cidadeSelect = document.getElementById("cidade");
    let cidadeParam = GetURLParameter("cidade").split(",");
    if(cidadeParam != ""){
        if(cidadeParam.length > 0){
            for(let i = 0; i < cidadeParam.length; i++)
                cidadeSelect.options[cidadeParam[i]].selected = "selected";
        }
    }

    let tipoValorSelect = document.getElementById("tipoValor");
    let tipoValorParam = GetURLParameter("tipoValor");
    if(tipoValorParam != "")
        tipoValorSelect.selectedIndex = tipoValorParam;

    let tipoSelect = document.getElementById("tipo");
    let tipoSelectParam = GetURLParameter("tipo");
    if(tipoSelectParam != "")
        tipoSelect.selectedIndex = tipoSelectParam;

    let subTipoSelect = document.getElementById("subTipo");
    let subTipoParam = GetURLParameter("subTipo").split(",");
    if(subTipoParam != ""){
        if(subTipoParam.length > 0){
            for(let i = 0; i < subTipoParam.length; i++)
                subTipoSelect.options[subTipoParam[i]].selected = "selected";
        }
    }

    let porcentagemCheckbox = document.getElementById("porcentagem");
    let porcentagemParam = GetURLParameter("porcentagem");
    if(porcentagemParam != "" && porcentagemCheckbox.checked.toString() !== porcentagemParam)
        porcentagemCheckbox.click();

    UpdatesubTipos(document.getElementById("tipo"));
});

function Search(){
    let periodoSelect = document.getElementById("periodo");
    let cidadeSelect = document.getElementById("cidade");
    let tipoValorSelect = document.getElementById("tipoValor");
    let tipoSelect = document.getElementById("tipo");
    let subTipoSelect = document.getElementById("subTipo");
    let porcentagemCheckbox = document.getElementById("porcentagem");

    let forgot = false;
    let forgotMsg = "Você esqueceu de selecionar as opções:";

    if(!periodoSelect.selectedOptions.length){
        forgotMsg += "\nPeriodo";
        forgot = true;
    }
    if(!cidadeSelect.selectedOptions.length){
        forgotMsg += "\nCidade";
        forgot = true;
    }
    if(!tipoValorSelect.selectedOptions.length){
        forgotMsg += "\nValor";
        forgot = true;
    }
    if(!tipoSelect.selectedOptions.length){
        forgotMsg += "\nTipo";
        forgot = true;
    }
    if(!subTipoSelect.selectedOptions.length){
        forgotMsg += "\nSub Tipo";
        forgot = true;
    }
    if(forgot){
        alert(forgotMsg);
        return;
    }
    
    window.location.href = "consulta?periodo=" + Array.from(periodoSelect.selectedOptions).map(option => option.index) +
        "&cidade=" + Array.from(cidadeSelect.selectedOptions).map(option => option.index) +
        "&tipoValor=" + tipoValorSelect.selectedIndex +
        "&tipo=" + tipoSelect.selectedIndex +
        "&subTipo=" + Array.from(subTipoSelect.selectedOptions).map(option => option.index) +
        "&porcentagem=" + porcentagemCheckbox.checked;
}

function ShowSelect(selectID, btn){
    select = document.getElementById(selectID);
    if (select.style.display == "inline-block"){
        btn.firstChild.data = "Mostrar";
        select.style.display = "none";

        btn.style.width = "117px";
        btn.style.height = "40px";
    }
    else{
        btn.firstChild.data = "Esconder";
        select.style.display = "inline-block";

        btn.style.width = "100%";
        btn.style.height = "20px";
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
