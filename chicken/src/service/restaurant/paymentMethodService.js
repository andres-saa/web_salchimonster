import axios from "axios";
import { URI } from "../conection";

export const paymentMethodService = {
    
    async getPaymentMethods() {
        try {
            const response = await axios.get(`${URI}/payment_methods/`);
            if (response.status === 200) {
                return response.data;
            } else {
                console.error('An error occurred while fetching the ingredients:', response.status);
                return null;
            }
        } catch (error) {
            console.error('An error occurred while fetching the ingredients:', error);
            return null;
        }
    },



};
