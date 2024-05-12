import axios from "axios";
import { URI } from "./conection";
import { useOrderStore } from "../store/order";


export const orderService = {
    

    async getOrdersBySite(site_id) {
        
        try {
            const response = await axios.get(`${URI}/order-by-site/${site_id}`);
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


    async getOrderCount(site_id) {
        
        try {
            const response = await axios.get(`${URI}/get_order_count_by_site_id/${site_id}`);
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



    async is_recent_order_generated(site_id) {
        
        try {
            const response = await axios.get(`${URI}/recent-order/${site_id}`);
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




    async prepareOrder(order_id) {
        const store = useOrderStore()
        store.setVisible('currentOrder',false)

        try {
            
            const response = await axios.post(`${URI}/order/${order_id}/prepare`);
            if (response.status === 200) {
                store.Notification.pause()
                store.Notification.currentTime = 0
                store.getTodayOrders()
                return response.data;
            } else {
                console.error('An error occurred while preparing the order:', response.status);
                return null;
            }
        } catch (error) {
            console.error('An error occurred while preparing the order:', error);
            return null;
        }
    },

    async cancelOrder(order_id, reason, responsible) {
        const store = useOrderStore()
        store.Notification.pause()
        store.Notification.currentTime = 0

        store.setVisible('currentOrder',false)
        const data = {
                "reason":reason,
                "responsible": responsible 
            }

        try {
            const response = await axios.post(`${URI}/order/${order_id}/cancel`, data);
            if (response.status === 200) {
                store.getTodayOrders()
                store.setVisible('currentOrder',false)

                return response.data;
            } else {
                console.error('An error occurred while cancelling the order:', response.status);
                return null;
            }
        } catch (error) {
            console.error('An error occurred while cancelling the order:', error);
            return null;
        }
    },

    async sendOrder(order_id) {
        const store = useOrderStore()
        store.setVisible('currentOrder',false)

        try {
            const response = await axios.post(`${URI}/order/${order_id}/send`);
            if (response.status === 200) {
                store.getTodayOrders()
                store.setVisible('currentOrder',false)
                return response.data;
                
            } else {
                console.error('An error occurred while sending the order:', response.status);
                return null;
            }
        } catch (error) {
            console.error('An error occurred while sending the order:', error);
            return null;
        }
    },




    async create_cancellling_request(data) {
        const store = useOrderStore()
        store.setVisible('currentOrder',false)

        try {
            const response = await axios.post(`${URI}/insert-cancellation-order`,data);
            if (response.status === 200) {
                store.getTodayOrders()
                store.setVisible('currentOrder',false)
                return response.data;
                
            } else {
                console.error('An error occurred while sending the order:', response.status);
                return null;
            }
        } catch (error) {
            console.error('An error occurred while sending the order:', error);
            return null;
        }
    },



    async deliveryZero(order_id) {
        const store = useOrderStore()
        store.setVisible('currentOrder',false)
        try {
            const response = await axios.put(`${URI}/delivery_zero/${order_id}`);
            if (response.status === 200) {
                store.getTodayOrders()
                store.setVisible('currentOrder',false)
                return response.data;
                
            } else {
                console.error('An error occurred while sending the order:', response.status);
                return null;
            }
        } catch (error) {
            console.error('An error occurred while sending the order:', error);
            return null;
        }
    }
};


