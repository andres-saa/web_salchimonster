import axios from "axios";
import { URI } from "../conection";
import { usecartStore } from "../../store/shoping_cart";
import { useSitesStore } from "../../store/site";
const store = useSitesStore()
export const categoriesService = {
    
    async getCategories() {
      
        const site_id = store.location.site.site_id
        if(site_id){
            try {
                const response = await axios.get(`${URI}/categories/${site_id}/1`);
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
        }else return []
        
    },


    // const getCategories = async () => {
    //     try {
    //         let siteId = currentCity.value.currenSiteId; // Asegúrese de que esta es la forma correcta de obtener el site_id
    //         let response = await fetch(`${URI}/site/${siteId}/active-categories`);
    //         if (!response.ok) {
    //             throw new Error(`HTTP error! status: ${response.status}`);
    //         }
    //         let data = await response.json();
    //         categories.value = data;
    //     } catch (error) {
    //         console.error('Error fetching data: ', error);
    //     }
    // }









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
