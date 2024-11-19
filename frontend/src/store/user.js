import { defineStore } from "pinia";
import { URI } from "../service/conection";


export const useUserStore = defineStore('user', {
   
    persist: {
       
                key: 'user', 
                storage: localStorage,
                paths:[
                    'user'

                    ]
    },
    state: () => {

        return {

            user: {
                name:'',
                neigborhood:'',
                address:'',
                phone_number:'',
                payment_method_option:'',
                was_reserva:false,
            },
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

    },


})


