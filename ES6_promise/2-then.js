export default function handleResponseFromAPI(promise) {
  return promise
  .then((success) => {
    return {
      status: 200,
      body: success
    };
  })
  .catch(() => {
    return new Error();
  })
  .finally(() => {
    console.log('Got a response from the API')
  })
}
