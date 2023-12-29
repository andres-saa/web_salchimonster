<template>
    <div style="max-width: 1024px;" class="m-auto ">
        <p class="text-6xl text-center mt-6" style="font-weight: bold; color: var(--primary-color)">
        Muchas gracias {{thanks_data.user_data.user_name}}!
    </p>
    <p class="text-3xl text-center mt-0 mb-0" style="font-weight:bold ; color:;">
        Hemos recibido tu pedido y en breve ser'a despachado.
    </p>


    <p class="text-3xl text-center mt-0 mb-6" style="font-weight: ; color:;">
        Pedido#  <span style="font-weight: bold;"> {{ thanks_data.order_id }} </span > <span class="text-md">con este codigo puedes consultar el estado de  tu pedido 
            
        <router-link to="/rastrear-pedido">
            <button style="color: var(--primary-color); border: none; background-color: transparent;" >aqui</button>
        </router-link> 
        
        
        
        </span>
    </p>

    <!-- {{ thanks_data }} -->

    
    <div class="grid  px-4">


        <div class="grid  col  " style="border-radius:2rem; ;max-width: 1024px; max-height: min-content;">
        <div  v-for="product in thanks_data.order_products" :key="product.id" class=" col-6 md:col-3 lg:col ">
            <TarjetaMenu v-if="product.state=='active'"  style="width: 100%;  "  :product="product"></TarjetaMenu>
            <!-- {{ currentCity }}jj -->
        </div>
      

        
    </div>



    </div>
    <div class="col p-0 m-0 m-auto " style="">
            <resumenGracias class="col-12 m-0 md:col m-auto   " style="min-width: 400px; max-width:40rem;"></resumenGracias>

    </div>

    
    </div>


    <!-- <resumen></resumen> -->



</template>



<script setup>

import { onBeforeMount, onMounted, watch } from 'vue';
import { send_order,thanks_data } from '../../service/order';
import router from '../../router';
import TarjetaMenu from '../../components/TarjetaMenu.vue';
import resumen from './resumen.vue';
import resumenGracias from './resumen-gracias.vue';


onBeforeMount(() => {
    if (!thanks_data.value.user_data){
        router.push('/')
    }
})


</script>