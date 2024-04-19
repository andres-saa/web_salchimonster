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
        Notification: new Audio('/sound/pip.mp3'),
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
                this.webSocket.close(); // Make sure to close any existing connections
            }

            this.webSocket = new WebSocket(`wss://${URI_SOCKET}/ws/${siteId}`);
            this.webSocket.onopen = () => {
                this.webSocket.onmessage = (message) => {
                    this.Notification.play();
                    this.getTodayOrders();
                    
                    if (Notification.permission === 'granted') {
                        const notification = new Notification('Nueva Orden en la pagina de WhatsApp', {
                            body: 'Nueva Orden en la pagina de WhatsApp',
                            icon: '/images/logo.png',
                            image: `${URI}/read-product-image/300/site-${siteId}`
                        });
                        notification.onclick = () => {
                            window.focus();
                        };
                    }

                    this.Notification.addEventListener('ended', function () {
                        this.currentTime = 0;
                        this.play();
                    }, false);
                };
            };
            this.webSocket.onclose = async () => {
                console.log("WebSocket disconnected");
                this.connectWebSocketIfDisconnected();
            };
            this.webSocket.onerror = (error) => {
                console.error("WebSocket error:", error);
            };
        },

        connectWebSocketIfDisconnected() {
            if (!this.webSocket || this.webSocket.readyState !== WebSocket.OPEN) {
                this.connectWebSocket(useSitesStore().site.site_id);
            }
        },

        startConnectionMonitor() {
            setInterval(() => {
                this.connectWebSocketIfDisconnected();
            }, 300000); // 300000 ms = 5 minutes
        }
    }

    }




);
