export default function updateStudentGradeByCity(
  arrayStudents,
  city,
  newGrades
) {
  return arrayStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.filter((grade) => grade.studentId === student.id);
      student.grade = grade[0] ? grade[0].grade : 'N/A';
      return student;
    });
}
