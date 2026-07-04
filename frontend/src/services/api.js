import axios from "axios";

const api = axios.create({
  baseURL: "http://192.168.75.168:8000",
});

export default api;
