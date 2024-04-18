import { defineStore } from "pinia";
import { URI } from "../service/conection";


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
            current_delivery:0


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
            this.location = location
        },
        setVisible(item,status){
            this.visibles[item]=status
        },



    },


})


