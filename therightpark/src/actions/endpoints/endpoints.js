import axios from "axios";
import EndpointFactory from "axios-endpoints";

const axiosInstance = axios.create({
    baseURL: "http://therightparking.appspot.com/api"
});

const Endpoint = EndpointFactory(axiosInstance);

export const slotsEndpoint = new Endpoint("/slots/"); 
export const parksEndpoint = new Endpoint("/parks/"); 

