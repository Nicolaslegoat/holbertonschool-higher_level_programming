/* eslint-disable */
document.addEventListener('DOMContentLoaded', function () {
    const redheader = document.querySelector("#red_header");
    redheader.addEventListener('click', function () {
        const header = document.querySelector('header');
        header.style.color = '#FF0000';
    });
});