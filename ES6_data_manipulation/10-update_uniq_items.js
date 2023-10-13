export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw Error('Cannot process');

  for (const [key, value] of map) {
    map.set(key, value === 1 ? 100 : value);
  }
}
