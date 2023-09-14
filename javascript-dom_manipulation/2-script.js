// Script that adds 'red' class to header on click of #red_header

const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');

redHeader.onclick = () => {
  header.classList.add('red');
};
