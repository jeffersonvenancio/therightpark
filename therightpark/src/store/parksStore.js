import { extendObservable, action, observable } from "mobx";
import moment from "moment";

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

    parksOfASlot = slot => Array.from(this.parks).filter(park => park.slot.label === slot.label)

    isSlotOcupied = slot => {
        const now = moment();
        this.parksOfASlot(slot).filter(park => {
            console.log()
        });
        
        const parks = this.parksOfASlot(slot).filter(park => moment(park.dateOut, "DD/MM/YYYY HH:mm:ss").subtract(3, 'hours').isAfter(now) || park.dateOut === null || park.dateOut === undefined);
        return parks.length > 0
    }

    setParks = action(parks =>{
        parks.map(park => {
            this._store.set(park.id, park)
        })
    })
}

export default new ParksStore();
