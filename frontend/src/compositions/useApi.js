import axios from "axios"
import { ref } from 'vue'


export function useApi(
    request,
    options,
    handleResponse = async (data) => data.data
){
    const baseURL = "http://localhost:5000/api/v1"
    const $axios = axios.create({
        baseURL,
        withCredentials: false,
        xsrfHeaderName: "X-XSRF-TOKEN",
        maxRedirects: 0
    })

    const result = ref(null);
    const isLoading = ref(false);
    const error = ref(null);
    const exec = async () => {
        isLoading.value = true;
        error.value = null;
        console.log("hello world")
        try {
            const response = await $axios(request);
            const valueResponse = await handleResponse(response)
            result.value = valueResponse;
            return valueResponse;
        } catch (e) {
            if (e.isAxiosError) {
                error.value = e
            } else {
                console.log('strange error ', e)
                error.value = e
            }
            result.value = null;
        } finally {
            isLoading.value = false;
        }
    }

    return {exec, result, error}
}

