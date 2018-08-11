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
            console.log(
                moment(park.dateOut, "DD/MM/YYYY HH:mm:ss").format(),
                moment(park.dateOut, "DD/MM/YYYY HH:mm:ss").subtract(3, 'hours').format(),
                now.format(),
                moment(park.dateOut, "DD/MM/YYYY HH:mm:ss").subtract(3, 'hours').isAfter(now) 
            )
        });
        
        const parks = this.parksOfASlot(slot).filter(park =>  park.dateOut === null || park.dateOut === undefined);
        parks[0] && console.log(parks[0].car.plate);
        return { 
            occupied: parks.length > 0, 
            regular: parks[0] && parks[0].regular,
            carplate: parks[0] && parks[0].car.plate,
        }
    }

    setParks = action(parks =>{
        parks.map(park => {
            this._store.set(park.id, park)
        })
    })
}

export default new ParksStore();
