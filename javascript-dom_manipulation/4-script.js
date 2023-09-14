// Script that adds a li element on ul element when clicking #add_item

const ulElement = document.querySelector('ul');
const addItem = document.getElementById('add_item');

addItem.onclick = () => {
  const newElement = document.createElement('li');
  newElement.innerHTML = 'Item';
  ulElement.appendChild(newElement);
};
