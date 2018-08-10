import { Action, ActionFirst } from "controlled-actions";
import slotsStore from "../store/slotsStore";

export const fetchSlots = new ActionFirst(
    async ({resolve, reject}) => {
        try {
            const { data } = await slotsEndpoint.get()
            resolve(data)
        } catch (error) {
            reject(error)
        }
    }
)

export const fetchAndSaveSlots = new Action(
    async ({resolve, reject}) => {
        try {
            const slots = fetchSlots.execute()
            slotsStore.setSlots(slots);
            resolve(slots)
        } catch (error) {
            reject(error)
        }
    }
)