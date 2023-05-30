var periodos = [
    "2019",
    "2020",
    "2021",
    "2022"
];

window.addEventListener("load", function(){
    let graficos = document.getElementsByClassName("carousel-graficos");
    for(let i = 0; i < graficos.length; i++){
        graficos[i].children[0].style.display = "inline-block";
        for(let j = 1; j < graficos[i].children.length; j++)
            graficos[i].children[j].style.display = "none";
    }

    let buttons = document.getElementsByClassName("carousel-button");
    for(let i = 0; i < buttons.length; i++){
        switch(buttons[i].className[buttons[i].className.length-1]){
            case 'r':
                buttons[i].children[0].innerText = periodos[1];
            break;
            case 'l':
                buttons[i].children[0].innerText = periodos[3];
            break;
        }
    }
});

function RollCarousel(carousel, roll){
    let graficos = document.getElementById(carousel+"-carousel-graficos");

    let current = 0;
    for(let i = 0; i < graficos.children.length; i++){
        if(graficos.children[i].style.display == "inline-block"){
            current = i;
            break;
        }
    }
    graficos.children[current].style.display = "none";

    current += roll;
    if(current < 0)
        current = graficos.children.length-1;
    else if (current >= graficos.children.length)
        current = 0;

    graficos.children[current].style.display = "inline-block";

    document.getElementById(carousel+"-button-r").children[0].innerText = periodos[(current+1 >= graficos.children.length ? 0 : current+1)];
    document.getElementById(carousel+"-button-l").children[0].innerText = periodos[(current-1 < 0 ? graficos.children.length-1 : current-1)];
}