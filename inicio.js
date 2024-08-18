var menuItem = document.querySelectorAll('.item-menu');

function selectLink() {
    menuItem.forEach((item) =>
        item.classList.remove('ativo')
    )
    this.classList.add('ativo')
}

menuItem.forEach((item) =>
    item.addEventListener('click', selectLink)
);

var btnExp = document.querySelector('#btn-exp');
var menuSide = document.querySelector('.menu-lateral');

btnExp.addEventListener('click', function() {
    menuSide.classList.toggle('expandir');
});

let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.carousel-images img');
    if (index >= slides.length) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = slides.length - 1;
    } else {
        currentSlide = index;
    }
    const offset = -currentSlide * 100;
    document.getElementById('carouselImages').style.transform = `translateX(${offset}%)`;
}

function moveSlide(step) {
    showSlide(currentSlide + step);
}

// Autoplay (opcional)
setInterval(() => {
    moveSlide(1);
}, 3000);

showSlide(currentSlide);

// Adiciona a classe 'rolagem' ao header quando a página é rolada
window.addEventListener("scroll", function() {
    let header = document.querySelector('header');
    header.classList.toggle('rolagem', window.scrollY > 50); // Altere o valor conforme necessário
});