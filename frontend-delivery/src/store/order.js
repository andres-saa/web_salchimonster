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
            const siteStore = useSitesStore();
            if (this.webSocket !== null) {
              this.webSocket.close(); // Make sure to close any existing connections properly
            }
          
            this.webSocket = new WebSocket(`wss://${URI_SOCKET}/ws/${siteId}`);
            this.webSocket.onopen = () => {
              console.log("WebSocket connected");
            };
            this.webSocket.onmessage = (message) => {
              this.Notification.play();
              this.getTodayOrders();
              alert('Nueva orden');
            };
            this.webSocket.onclose = () => {
              console.log("WebSocket disconnected");
              if (siteStore.site.site_id) {
                this.connectWebSocket(siteStore.site.site_id);
              }
            };
            this.webSocket.onerror = (error) => console.error("WebSocket error:", error);
          },
          

        initNotification() {
            this.Notification.play().then(() => {
              this.Notification.pause();
              this.Notification.currentTime = 0;
            }).catch(err => console.error("Error iniciando el audio:", err));
          }
    }




});
