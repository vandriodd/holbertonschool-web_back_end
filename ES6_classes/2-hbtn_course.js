export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  validate(propertyValue, property, type) {
    /* eslint-disable valid-typeof */
    if (type === 'array') {
      if (!Array.isArray(propertyValue)) {
        throw new TypeError(`${property} must be an ${type}`);
      }
    } else if (typeof propertyValue !== type) {
      throw new TypeError(`${property} must be a ${type}`);
    }
    this[`_${property}`] = propertyValue;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this.validate(newName, 'name', 'string');
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    this.validate(newLength, 'length', 'number');
  }

  get students() {
    return this._students;
  }

  set students(newStudent) {
    this.validate(newStudent, 'students', 'array');
  }
}
