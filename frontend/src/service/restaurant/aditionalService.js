import axios from "axios";
import { URI } from "../conection";

export const adicionalesService = {
    
    async getAditional(product_instance_id) {
        try {
            const response = await axios.get(`${URI}/adicionales-new-active/${product_instance_id}`);
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
    
    async getAditionalGroup(product_instance_ids, site_id) {
        // Prepare the request body to match the expected structure: { instance_product_ids: [...] }
        const requestBody = {
            instance_product_ids: product_instance_ids,
            site_id:site_id
        };
    
        try {
            // Make a POST request with the correctly formatted data
            const response = await axios.post(`${URI}/adicionales-new-group-active/`, requestBody);
            if (response.status === 200) {
                return response.data;  // Return the received data
            } else {
                // Log and handle non-200 status responses
                console.error('An error occurred while fetching the ingredients:', response.status);
                return null;
            }
        } catch (error) {
            // Handle exceptions from the request, such as network errors
            console.error('An error occurred while fetching the ingredients:', error);
            return null;
        }
    },



};
