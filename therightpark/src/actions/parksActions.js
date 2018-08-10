import { Action, ActionFirst } from "controlled-actions";
import parksStore from "../store/parksStore";
import { parksEndpoint } from "./endpoints/endpoints";

export const fetchParks = new ActionFirst(
    async ({resolve, reject}) => {
        try {
            const { data } = await parksEndpoint.get()
            resolve(data)
        } catch (error) {
            reject(error)
        }
    }
)

export const fetchAndSaveParks = new Action(
    async ({resolve, reject}) => {
        try {
            const parks = fetchParks.execute()
            parksStore.setParks(parks);
            resolve(parks)
        } catch (error) {
            reject(error)
        }
    }
)

export const startParksPolling = new Action(
    ({resolve, reject}) => {
        const intervalId = window.setInterval(async ()=> {
            await fetchAndSaveParks.execute();
        }, 2000)
        resolve(()=> window.clearInterval(intervalId))
    }
)