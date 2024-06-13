<template>
    <div @click="open" class="col-12 " style="background-color: rgba(255, 255, 255, 0.506);border-radius: 0.5rem;cursor: pointer;">

        <Tag class="text-l" :severity="props.order.user_phone == '1111111111'? 'danger' : 'help'"> {{props.order.user_phone == '1111111111'? 'ES UNA PRUEBA, RELAJATE' : props.order.user_name}}</Tag>


        <div style="display: flex; align-items: center;justify-content: space-between;">
            <div style=" display: flex;align-items: center;">
                <b style="min-width: max-content;color: black;">
        #{{props.order?.order_id}}
            </b>

            <div v-for="product in props.order.products.slice(0,3)" style="width: 3rem;height:100%;">
                <div style="position: relative;">
                    <img style="width: 100%;" :src="`https://backend.salchimonster.com/read-product-image/96/${product.name}`" alt="">
                    
                    <Button  severity="danger" class="p-0" rounded :label="product.quantity" style="width: 1.5rem;position: absolute;top: -.5rem;right: -.5rem;z-index: 99; height: 1.5rem;border-radius: 1rem;">

                    </Button>
                </div>
            
               

            </div>



            </div>

            
            
            <span style="display: flex; gap: 1rem;align-items: center;">
                <b style="min-width: max-content;color: black;">
            {{props.order?.latest_status_timestamp?.split('T')[1]?.split('.')[0]?.split(':').slice(0,2)?.join(':') }}
            </b>
            
            <Tag v-if="props.order.current_status != 'en preparacion'" :severity="icons[props.order.current_status]">
                
            {{props.order.current_status }}
            
            </Tag>


            <ProgressSpinner v-if="props.order.current_status == 'en preparacion'" style="width: 50px; height: 50px" strokeWidth="8"
    animationDuration=".5s" aria-label="Custom ProgressSpinner" />
           

          

            </span>
            
            
        </div>

        <Tag  v-if="props.order.calcel_sol_state != null" :severity="props.order.calcel_sol_state? 'success': 'danger'"> {{props.order.calcel_sol_state? 'REVISADO' : ' EN REVISION...' }} </Tag> <span style="font-weight: bold;" v-if="props.order.calcel_sol_state">  Y  </span>
        <Tag v-if="props.order.calcel_sol_state" :severity="props.order.calcel_sol_asnwer? 'success': 'danger'">  {{props.order.calcel_sol_asnwer? 'APROBADO': 'RECHAZADO' }} </Tag> 
        
        <P class="m-0"  v-if="props.order.calcel_sol_state "> <b>RESPONSABLE:</b>  {{props.order.cancelation_solve_responsible?.split(' ').slice(0,3).join(' ')  }} </P> 

        <span v-if="props.order.responsible_observation">
            <p> <b>OBSERVACIONES:</b> {{ props.order.responsible_observation || 'sin observaciones'}} </p> 
            
        </span>

        <Tag severity="success" v-if="props.order.responsible_id"> <i class="pi pi-whatsapp mr-2"></i>   TRANSFERENCIA APROBADA</Tag> <br> <Tag severity="success" v-if="props.order.responsible_id">  {{props.order.name}}</Tag>

    </div>
    
</template>

<script setup>

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