import { extendObservable, action, observable } from "mobx";

class SlotsStore {
    constructor() {
        extendObservable(this, {
            _store: observable.map(),
        })
    }

    get slots() {
        return this._store.values()
    }

    getById = id => this._store.get(id)

    setSlots = action(slots =>{
        slots.map(slot => {
            this._store.set(slot.id, slot)
        })
    })
}

export default new SlotsStore();
