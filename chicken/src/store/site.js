import { defineStore } from "pinia";
import { URI,URI_SOCKET } from "../service/conection";
import axios from "axios";




export const useSitesStore = defineStore('site', {
   
    persist: {
       
                key: 'site', 
                storage: localStorage,
                paths:[
                    'location'

                    ]
    },
    state: () => {

        return {

            location: {
                site:{},
                neigborhood:{}
            },
            visibles: {
                currentSite: false
            },
            current_delivery:0,
            webSocket: null,
            status:'closed'


        }
    },

    getters: {
        fucion: (state) => {
            return 0
        }
    },

   

    actions: {

        async func() {
            return func
        },

        setLocation(location){
            this.connectWebSocket(location.site.site_id)
            this.location = location
        },
        setVisible(item,status){
            this.visibles[item]=status
        },
        async connectWebSocket(siteId) {

            if (this.webSocket !== null) {
                this.webSocket.close// Make sure to close any existing connections
            }

            this.webSocket = new WebSocket(`wss://${URI_SOCKET}/ws/${siteId}`);
            this.webSocket.onopen = () =>
                this.webSocket.onmessage = (message) => {
                    console.log('new mesagge')
                    


                };
            this.webSocket.onclose = async () => {
                console.log("WebSocket disconnected");


                const site_id = this.location.site.site_id

                if (site_id) {
                    this.connectWebSocket(site_id);
                } else {
                    // router.push('/login')
                }
                this.webSocket = null;
                // location.reload() // Clean up the reference to the WebSocket
            };
            this.webSocket.onerror = (error) => console.error("WebSocket error:", error);
        },
        async setNeighborhoodPrice(){
       
                try {
                    const response = await axios.get(`${URI}/neighborhood/${this.location.neigborhood.neighborhood_id}/`);
                    if (response.status === 200) {
                        this.location.neigborhood = response.data
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
        async setNeighborhoodPriceCero(){
       
           this.location.neigborhood.delivery_price = 0
    }




    },


})


