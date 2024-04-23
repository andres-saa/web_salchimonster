import { defineStore } from "pinia";
import { URI, URI_SOCKET } from "../service/conection";
import { orderService } from "../service/orderService";
import { useSitesStore } from "./site";
















export const useOrderStore = defineStore('cart', {
    persist: {
        key: 'order',
        storage: localStorage,
        paths: [
            'currentCountOrders'
        ]

    },
    state: () => ({
        currentOrder: {},
        visibles: {
            currentOrder: false,
        },
        TodayOrders: [],
        Notification: new Audio('/sound/pip.mp3'),
        webSocket: null,
        currentCountOrders:0,
        last_order_id:0

    }),

    getters: {



    },
    actions: {
        setVisible(item, status) {
            this.visibles[item] = status
        },

        setOrder(order) {
            this.currentOrder = order
        },
        async getTodayOrders() {
            const siteStore = useSitesStore()
            this.TodayOrders = await orderService.getOrdersBySite(siteStore.site.site_id)
        },



    }

    }




);
