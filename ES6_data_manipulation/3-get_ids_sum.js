export default function getStudentIdsSum(arrayStudents) {
  return arrayStudents.reduce((total, student) => total + student.id, 0);
}
