window.addEventListener("load", function(){
    carousels = document.getElementsByClassName("carousel");

    for(let i = 0; i < carousels.length; i++){
        for(let j = 1; j < carousels[i].children.length - 1; j++)
            console.log(carousels[i].children[j].style.display = "none");
        carousels[i].children[1].style.display = "inline-block";

        carousels[i].children[0].innerText = "<1/"+(carousels[i].children.length-2).toString()
        carousels[i].children[carousels[i].children.length-1].innerText = "1/"+(carousels[i].children.length-2).toString()+">"
    }
});

function RollCarousel(carousel, roll){
    let current = 1;
    for(let i = 1; i < carousel.children.length - 1; i++){
        if(carousel.children[i].style.display == "inline-block"){
            current = i;
            carousel.children[current].style.display = "none";
        }
    }

    current += roll;
    if(current >= carousel.children.length - 1)
        current = 1;
    else if(current < 1)
        current = carousel.children.length - 2;

    carousel.children[current].style.display = "inline-block"

    carousel.children[0].innerText = "<"+current.toString()+"/"+(carousel.children.length-2).toString()
    carousel.children[carousel.children.length-1].innerText = current.toString()+"/"+(carousel.children.length-2).toString()+">"
}