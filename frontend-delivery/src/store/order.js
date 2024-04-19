import { defineStore } from "pinia";
import { URI, URI_SOCKET } from "../service/conection";
import { orderService } from "../service/orderService";
import { useSitesStore } from "./site";
















export const useOrderStore = defineStore('cart', {
    persist: {
        key: 'order',
        storage: localStorage,
        paths: [

        ]

    },
    state: () => ({
        currentOrder: {},
        visibles: {
            currentOrder: false,
        },
        TodayOrders: [],
        Notification: new Audio('sound/pip.mp3'),
        webSocket: null

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


        async connectWebSocket(siteId) {
            const siteStore = useSitesStore()
            if (this.webSocket !== null) {
                this.webSocket.close// Make sure to close any existing connections
            }

            this.webSocket = new WebSocket(`ws://${URI_SOCKET}/ws/${siteId}`);
            this.webSocket.onopen = () =>
                this.webSocket.onmessage = (message) => {
                    this.Notification.play()
                    this.getTodayOrders()
                    this.Notification.addEventListener('ended', function () {
                        this.currentTime = 0;
                        this.play();
                    }, false);


                };
            this.webSocket.onclose = async () => {
                console.log("WebSocket disconnected");

                const siteStore = useSitesStore()
                const site_id = await siteStore.site.site_id

                if (site_id) {

                    this.connectWebSocket(site_id);
                } else {
                    // router.push('/login')
                }
                this.webSocket = null;
                // location.reload() // Clean up the reference to the WebSocket
            };
            this.webSocket.onerror = (error) => console.error("WebSocket error:", error);
        }

    }




});
