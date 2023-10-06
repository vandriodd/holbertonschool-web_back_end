export default function getResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      const response = {
        status: 200,
        body: 'Success',
      };
      resolve(response);
    }
    reject(new Error('The fake API is not working currently'));
  });
}
