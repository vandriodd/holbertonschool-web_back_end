// Script that toggles class (red/green) on header when clicking #toggle_header

const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.onclick = () => {
  if (header.classList.contains('green')) {
    header.classList.replace('green', 'red');
  } else {
    header.classList.replace('red', 'green');
  }
};
