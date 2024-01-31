document.addEventListener("DOMContentLoaded", () => {
    let img = document.querySelector('img')
    if (img.id == 'hardware') {
        let a = Math.round(Math.random()*3);
        img.src = `img${a}.png`;
    } else if (img.id == 'software') {
        let a = Math.round(Math.random()*2) + 4;
        img.src = `img${a}.png`;
    } else if (img.id == 'supcomp') {
        let a = Math.round(Math.random()) + 7;
        img.src = `img${a}.png`;
    }
});