// Script that updates header element when clicking #update_header

const header = document.querySelector('header');
const updateHeader = document.getElementById('update_header');

updateHeader.onclick = () => {
  header.innerHTML = 'New Header!!!';
};
