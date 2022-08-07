
function show() {
    document.querySelector(".main_img").src=this.src;
}

window.onload = function(){
    let t = document.querySelectorAll(".mini_img");
    for(let i = 0; i < t.length; i++){
        t[i].onmouseover=show;
    }
}