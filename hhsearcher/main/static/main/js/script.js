const image = document.querySelector(".intro__phones");

// image.addEventListener("mouseenter", () => {
//   image.src = "main/img/colored.png";
// });
//
// image.addEventListener("mouseleave", () => {
//   image.src = "main/img/image.png";
// });

const openMenu = document.querySelector(".header__menu-button");
const closeMenu = document.querySelector(".close__menu");
const headerMenu = document.querySelector(".header__menu-container");
const menuElements = document.querySelectorAll(".header__menu-item");

openMenu.addEventListener("click", (e) => {
  headerMenu.classList.toggle("active");
});

closeMenu.addEventListener("click", (e) => {
  headerMenu.classList.toggle("active");
});

menuElements.forEach((el) =>
  el.addEventListener("click", () => headerMenu.classList.toggle("active"))
);
