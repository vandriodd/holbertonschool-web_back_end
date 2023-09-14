// Script that Changes header color on click of #red_header to red

const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');

redHeader.onclick = () => {
  header.style.color = '#FF0000';
};
