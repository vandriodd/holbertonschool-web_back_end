export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      /* eslint-disable comma-dangle */
      throw new Error(
        'Class extending Building must override evacuationWarningMessage'
      );
      /* eslint-enable */
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
