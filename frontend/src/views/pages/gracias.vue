<template>



    <div class="p-2 col-12" style=" height: 90vh; display: flex; justify-content: center; align-items: center;">
        <div class="shadow-3 p-4 " style="border-radius: 0.5rem; max-width: 300px;">
            <P class="text-4xl text-center my-5" style="font-weight: bold;"> MUCHAS GRACIAS POR TU COMPRA !</P>

            <P class="text-4xl text-center my-5" style="font-weight: bold;text-transform: uppercase;">ID DEL PEDIDO #{{store.last_order  }}</P>


            
        <P class="text-3xl text-center my-5" style="font-weight: bold; border-radius: .5rem; background-color: var(--primary-color);color: white;"> Hemos recibido tu pedido y en breve será despachado</P>
   
        <router-link to="/">
            <Button icon="pi pi-arrow-left" severity="danger" style="font-weight: bold; background-color: black;border: none;width: 100%;" label="VOLVER AL MENU"></Button>
        </router-link>
        </div>
     </div>


</template>



<script setup>


import sesion_main from './sesion_main.vue';
import { usecartStore } from '../../store/shoping_cart';

const store = usecartStore()

</script>