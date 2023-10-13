export default function cleanSet(set, startString) {
  let result = '';

  if (typeof startString !== 'string' || startString === '') return result;

  for (const value of set) {
    if (
      value !== undefined
      && typeof value === 'string'
      && value.startsWith(startString)
    ) {
      result
        += result.length === 0
          ? value.slice(startString.length)
          : `-${value.slice(startString.length)}`;
    }
  }
  return result;
}
