import { extendObservable, action, observable } from "mobx";

class ParksStore {
    constructor() {
        extendObservable(this, {
            _store: observable.map(),
        })
    }

    get parks() {
        return this._store.values()
    }

    getById = id => this._store.get(id)

    setParks = action(parks =>{
        parks.map(park => {
            this._store.set(park.id, park)
        })
    })
}

export default new ParksStore();
