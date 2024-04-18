import { defineStore } from "pinia";
import { URI } from "../service/conection";
import { orderService } from "../service/orderService";
import { useSitesStore } from "./site";

export const useOrderStore = defineStore('cart', {
    persist: {
        key: 'order',
        storage: localStorage,
        paths:[

        ]

    },
    state: () => ({
        currentOrder: {},
        visibles: {
            currentOrder: false,
        },
        TodayOrders:[],
        Notification:new Audio('sound/pip.mp3')

    }),

    getters: {


        
   },
   actions: {
    setVisible(item,status){
        this.visibles[item]=status
    },

    setOrder(order){
       this.currentOrder = order
    },
     async getTodayOrders (){
        const siteStore = useSitesStore()
        this.TodayOrders = await orderService.getOrdersBySite(siteStore.site.site_id)
    }
    
}




});
