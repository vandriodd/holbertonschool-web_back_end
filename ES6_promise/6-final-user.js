import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const singUpPromise = signUpUser(firstName, lastName);
  const uploadPhotoPromise = uploadPhoto(fileName);

  return Promise.allSettled([singUpPromise, uploadPhotoPromise])
    .then((results) => results.map((result, index) => (
      {
        status: result.status,
        value: index === 0 ? result.value : result.reason.toString(),
      }
    )));
}
