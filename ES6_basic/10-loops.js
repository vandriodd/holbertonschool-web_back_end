export default function appendToEachArrayValue(array, appendString) {
  const arr = [];
  for (let elem of array) {
    arr.push(appendString + elem);
  }
  return arr;
}
