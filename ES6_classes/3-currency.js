export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  validate(propertyValue, property, type = 'string') {
    /* eslint-disable valid-typeof */
    if (typeof propertyValue !== type) {
      throw new TypeError(`${property} must be a ${type}`);
    }
    this[`_${property}`] = propertyValue;
    /* eslint-enable */
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }

  get code() {
    return this._code;
  }

  set code(newCode) {
    this.validate(newCode, 'code');
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this.validate(newName, 'name');
  }
}
