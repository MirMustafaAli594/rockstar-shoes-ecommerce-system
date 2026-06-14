let current = 0;
const slides = document.querySelectorAll('.slider-container > .slides > .slide');
const dots = document.querySelectorAll('.dots-block-fixed .dot');

function showSlide(index) {
    if (slides.length === 0 || dots.length === 0) return;
    
    slides.forEach(s => s.style.display = 'none');
    dots.forEach(d => d.classList.remove('active'));
    
    slides[index].style.display = 'flex';
    dots[index].classList.add('active');
}

function nextSlide() {
    current = (current + 1) % slides.length;
    showSlide(current);
}

if (window.sliderInterval) {
    clearInterval(window.sliderInterval);
}
window.sliderInterval = setInterval(nextSlide, 5000);

function currentSlide(index) {
    current = index;
    showSlide(current);
}

// Initial Call
showSlide(current);