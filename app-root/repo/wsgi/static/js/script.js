const carousel = document.querySelector('.carousel');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');
const slideWidth = document.querySelector('.slide').offsetWidth;

nextButton.addEventListener('click', () => {
  carousel.style.transform = `translateX(${slideWidth}px)`;
  carousel.appendChild(carousel.firstElementChild);
  carousel.style.transition = 'none';
  setTimeout(() => {
    carousel.style.transform = 'translateX(0)';
    carousel.style.transition = 'transform 0.5s ease-in-out';
  }, 0);
});

prevButton.addEventListener('click', () => {
  carousel.style.transform = `translateX(-${slideWidth}px)`;
  carousel.prepend(carousel.lastElementChild);
  carousel.style.transition = 'none';
  setTimeout(() => {
    carousel.style.transform = 'translateX(0)';
    carousel.style.transition = 'transform 0.5s ease-in-out';
  }, 0);
});


alert("hello")