var periodos = [
    "2019",
    "2020",
    "2021",
    "2022"
];

var current = 0;

window.addEventListener("load", function(){
    let graficos = document.getElementById("carousel-graficos");

    graficos.children[0].style.display = "inline-block";
    for(let i = 1; i < graficos.children.length; i++)
        graficos.children[i].style.display = "none";

    document.getElementById("carousel-button-r").children[0].innerText = periodos[current+1];
    document.getElementById("carousel-button-l").children[0].innerText = periodos[graficos.children.length-1];
});

function RollCarousel(carousel, roll){
    let graficos = document.getElementById("carousel-graficos");
    graficos.children[current].style.display = "none";

    current += roll;
    if(current < 0)
        current = graficos.children.length-1;
    else if (current >= graficos.children.length)
        current = 0;

    graficos.children[current].style.display = "inline-block";

    document.getElementById("carousel-button-r").children[0].innerText = periodos[(current+1 >= graficos.children.length ? 0 : current+1)];
    document.getElementById("carousel-button-l").children[0].innerText = periodos[(current-1 < 0 ? graficos.children.length-1 : current-1)];
}