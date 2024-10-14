import axios from "axios";
import { URI } from "../service/conection";
import { useSitesStore } from "../store/site";

export const productService = {


    
    async getProductsByCategorySite(category_id,site_id,restaurant_id = 1) {
        const store = useSitesStore()
        const restaurant = store.restaurant_id
        try {
            const response = await axios.get(`${URI}/products-all/category-id/${category_id}/site/${site_id}/${restaurant}`);
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

    async updateProductInstanceStatus(product_instance_id, new_status) {
        try {
            const response = await axios.put(`${URI}/product-instance/${product_instance_id}/status`, {
                new_status: new_status // Asegurando que el valor enviado es booleano
            });
            if (response.status === 200) {
                console.log('Product instance status updated successfully:', response.data);
                return response.data;
            } else {
                console.error('Failed to update product instance status:', response.status);
                return null;
            }
        } catch (error) {
            console.error('Error updating product instance status:', error);
            return null;
        }
    }

}


