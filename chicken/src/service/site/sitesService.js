import axios from "axios";
import { URI } from "../conection";

export const sitesService = {
    async getSiteById(site_id) {
        try {
            const response = await axios.get(`${URI}/site/${site_id}`);
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

    // async createIngredient(ingredientData) {
    //     try {
    //         const response = await axios.post(`${URI}/ingredient`, ingredientData);
    //         if (response.status === 200) { // Asumiendo que 201 Created es el código de estado para una creación exitosa
    //             return response.data;
    //         } else {
    //             console.error('An error occurred while creating the ingredient:', response.status);
    //             return null;
    //         }
    //     } catch (error) {
    //         console.error('An error occurred while creating the ingredient:', error);
    //         return null;
    //     }
    // },

    // async deleteIngredient(ingredientId) {
    //     try {
    //         const response = await axios.delete(`${URI}/ingredient/${ingredientId}`);
    //         if (response.status === 200) { // Asumiendo que 200 OK es el código de estado para una eliminación exitosa
    //             console.log('Ingredient deleted successfully');
    //             return true;
    //         } else {
    //             console.error('An error occurred while deleting the ingredient:', response.status);
    //             return false;
    //         }
    //     } catch (error) {
    //         console.error('An error occurred while deleting the ingredient:', error);
    //         return false;
    //     }
    // }
};
