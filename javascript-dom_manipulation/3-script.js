/* eslint-disable */
document.addEventListener('DOMContentLoaded', function () {
    const toggleheader = document.querySelector("#toggle_header");
    toggleheader.addEventListener('click', function () {
        const header = document.querySelector('header');
        header.classList.toggle('red');
        header.classList.toggle('green');
    });
});