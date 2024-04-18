<template>
    <div @click="open" class="col-12 p-0" style="background-color: rgba(255, 255, 255, 0.506);border-radius: 0.5rem;cursor: pointer;">

        <div style="display: flex; align-items: center;justify-content: space-between;">
            <div style=" display: flex;align-items: center;">
                <b style="min-width: max-content;color: black;">
        #{{props.order?.order_id}}
            </b>


            </div>

            
            
            <span style="display: flex; gap: 1rem;align-items: center;">
                <b style="min-width: max-content;">
            {{format_date(props.order?.latest_status_timestamp) }}
            </b>
            
            
                <b style="color: black;">
                    {{formatoPesosColombianos(props.order.total_order_price)  }}

                </b>
                
       
           

          

            </span>
            
            
        </div>
        
       

    </div>
    
</template>

<script setup>

import { formatoPesosColombianos } from '../../service/formatoPesos';
import { useOrderStore } from '../../store/order';


const store = useOrderStore()


const open = () => {
    store.setVisible('currentOrder',true)
    store.setOrder(props.order)
}


const icons = {
    generada: 'warning',
    "en preparacion": 'info',
    enviada:'success',
    cancelada:'danger'
}

const props = defineProps({
    order: {
        type: Object,
        default: {}
    },


});

const format_date = (date) => {
   const new_date = new Date(date)

    const timeFormatter = new Intl.DateTimeFormat('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
    })

    const formatedDate = timeFormatter.format(new_date)
    return formatedDate

}



</script>