<template>
    <Dialog style="background-color: ;" v-model:visible="store.visibleOrder.visible" modal header="Orden"
        :style="{ width: '40rem' }">


        <!-- {{ store.visibleOrder.order }} -->

        <div style="border-radius: 1rem; overflow: hidden;">
            <div class=" P-0 mt-0" style="background-color: var(--orange-500);">

                <div class="header p-4" style="display: flex; ;justify-content: space-between;align-items: center;">
                    <div style="display: flex">
                        <img class="p-0" src="/images/logo.png"
                            style="filter: brightness(0) invert(); width: ;height: 3rem; object-fit: contain;" alt="">
                        <span style="width: min-content;font-weight: bold;color: white;">INVERSIONES SALCHIMONSTER</span>
                    </div>

                    <div style="display: flex;flex-direction: column; max-width: 40%;">
                        <!-- <img  class="p-0" src="/images/logo.png" style="filter: brightness(0) invert(); width: ;height: 3rem; object-fit: contain;" alt=""> -->
                        <span class="text-left text-sm"
                            style="text-align: end; width: min-content;font-weight: bold;color: white;">TERMINOS Y
                            CONDICIONES </span>
                        <small class="mt-2  text-left" style="color: white; max-width: ;">Lorem ipsum dolor sit amet
                            consectetur, adipisi</small>
                    </div>

                </div>

            </div>

            <div class=" P-0" style="background-color: var(--gray-200);">

                <div class="header p-4" style="display: flex; ;justify-content: space-between;">

                    <div style="font-weight: bold; display: flex;flex-direction: column; max-width: 50%;">
                        <!-- <img  class="p-0" src="/images/logo.png" style="filter: brightness(0) invert(); width: ;height: 3rem; object-fit: contain;" alt=""> -->
                        <span class="text-xl mb-2"
                            style="width: min-content;font-weight: bold;color: rgb(0, 0, 0);">Factura</span>




                        <div style="display: flex;gap: 1rem; justify-content: space-between; ">

                            <div style="display: flex; flex-direction: column;">
                                <span> Orden No.</span>
                                <span> Sede</span>
                                <span> Fecha</span>
                                <span> Metodo de pago</span>

                            </div>

                            <div style="display: flex;font-weight: 200; flex-direction: column;">
                                <span> |</span>
                                <span> | </span>
                                <span> |</span>
                                <span> |</span>
                            </div>

                            <div style="display: flex;font-weight: 400; flex-direction: column;">
                                <span> {{ store.visibleOrder.order.order_id }}</span>
                                <span> {{ store.visibleOrder.order.site_name }}</span>
                                <span> {{ store.visibleOrder.order?.status?.timestamp.split(' ')[0] }}</span>
                                <span> {{ store.visibleOrder.order?.payment_method }}</span>
                            </div>

                        </div>


                    </div>


                    <div style="font-weight: bold; display: flex;flex-direction: column; max-width: 40%;">
                        <!-- <img  class="p-0" src="/images/logo.png" style="filter: brightness(0) invert(); width: ;height: 3rem; object-fit: contain;" alt=""> -->
                        <span class="text-xl mb-2"
                            style="width: min-content;font-weight: bold;color: rgb(0, 0, 0);">Balance</span>




                        <div style="display: flex;gap: 1rem; justify-content: space-between; ">

                            <div style="display: flex; flex-direction: column;">
                                <span> Subtotal</span>
                                <span> Domicilio</span>
                                <span class="text-2xl"> Total</span>
                            </div>

                            <div style="display: flex;font-weight: 200; flex-direction: column;">
                                <span> | </span>
                                <span> |</span>
                                <span> |</span>

                            </div>

                            <div style="display: flex; font-weight: 400; flex-direction: column;">

                                <span> {{ formatToColombianPeso(store.visibleOrder.order.total_price) }}</span>

                                <span> {{ formatToColombianPeso(store.visibleOrder.order.delivery_price) }}</span>

                                <span class="text-xl" style="font-weight: bold; border-top: 2px solid red;">
                                    {{ formatToColombianPeso(store.visibleOrder.order.total_price +
                                        store.visibleOrder.order.delivery_price) }}</span>
                            </div>

                        </div>

                        

                    </div>

                    


                </div>
                











<p class="text-xl text-center" style="font-weight: bold; color: rgb(255, 255, 255);background-color: black;">Datos de usuario</p>

                <div class="p-4" style="display: flex;gap: 1rem; justify-content: start; ">


<div style="display: flex; font-weight: 400;height: 4rem; aspect-ratio: 1 / 1; background-color: rgb(255, 255, 255);border-radius: 50%; flex-direction: column; align-items: center; justify-content: center;">
    <i class="text-2xl" :class="PrimeIcons.USER"></i>
</div>

<div style="display: flex;font-weight: 200; flex-direction: column;">
    <span> |</span>
    <span> | </span>
    <span> |</span>
</div>

<div style="display: flex; flex-direction: column;">
    <span style="text-transform: capitalize;">  <span style="font-weight: bold;"> Nombre :</span> {{ store.visibleOrder.order.user_data?.user_name }}</span>
    <span style="text-transform: capitalize;"> <span style="font-weight: bold;" >DIRECCION :</span>   {{ store.visibleOrder.order.user_data?.user_address }}</span>
    <span > <span style="font-weight: bold;"> TELEFONO : </span>  {{ store.visibleOrder.order.user_data?.user_phone }}</span>
</div>


</div>
























            </div>


            <div class=" P-0" style="background-color: var(--white-200);">

                <div class="header py-4" style="display: flex; ;justify-content: space-between;">

                    <div style="font-weight: bold; display: flex;flex-direction: column; width: 100%;">
                        <!-- <img  class="p-0" src="/images/logo.png" style="filter: brightness(0) invert(); width: ;height: 3rem; object-fit: contain;" alt=""> -->
                        <span class="text-xl pl-4 mb-2"
                            style="width: min-content;font-weight: bold;color: rgb(0, 0, 0);">Productos</span>

                        <div class="m-0 p-0" v-for="producto in store.visibleOrder.order.products">
                            <p class=" text-l  p-1 text-center my-2"
                                style="font-weight: bold;width: 100; background-color:var(--gray-200);color: black;">
                                {{ producto.name }} <span>{{ formatToColombianPeso(producto.price) }}</span></p>

                            <div class="px-4 py-0"
                                style="display: flex;gap: 1rem;width: 100%; justify-content: space-between; ">


                                <div style="display: flex; flex-direction: column;font-weight:500;">
                                    <span v-if="producto.salsas?.length > 0" class="" style="font-weight: bold;">
                                        Salsas</span>






                                    <span v-if="producto.salsas?.length > 0" class="ml-4" v-for="salsa in producto.salsas"> {{
                                        salsa }}</span>

                                    <span v-if="producto.adiciones?.length > 0" class="" style="font-weight: bold;">
                                        Adiciones</span>

                                    <span v-if="producto.adiciones?.length > 0" class="ml-4"
                                        v-for="adicional in producto.adiciones"> {{ adicional.name }}</span>


                                    <span v-if="producto.cambios?.length > 0" class="" style="font-weight: bold;">
                                        Cambios</span>
                                    <span v-if="producto.cambios?.length > 0" class="ml-4" v-for="cambio in producto.cambios">
                                        {{ cambio.name }}</span>

                                    <span v-if="producto.toppings?.length > 0" class="" style="font-weight: bold;">
                                        Toppings</span>
                                    <span v-if="producto.toppings?.length > 0" class="ml-4"
                                        v-for="topping in producto.toppings"> {{ topping?.name }}</span>

                                    <span v-if="producto.acompanantes?.length > 0" class="" style="font-weight: bold;">
                                        Acompanantes</span>
                                    <span v-if="producto.acompanantes?.length > 0" class="ml-4"
                                        v-for="acompanante in producto.acompanantes"> {{ acompanante.name }}</span>


                                </div>

                                <div style="display: flex;font-weight: 200; flex-direction: column;">


                                </div>

                                <div style="display: flex;font-weight: 400; flex-direction: column;">

                                    <!-- <span class="text-right" style=""> --------------</span> -->
                                    
                                    <span v-if="producto.salsas?.length > 0" class="text-right" style=""> --------------</span>


                                    <span class="ml-4 text-right" v-if="producto.salsas?.length > 0" v-for="salsa in producto.salsas"
                                        style=""> ...</span>


                                    <span v-if="producto.adiciones?.length > 0" class="text-right" style=""> --------------</span>
                                    <span class="ml-4 text-right" v-if="producto.adiciones?.length > 0"
                                        
                                        v-for="adicional in producto.adiciones"> {{ formatToColombianPeso(adicional.price)
                                        }}</span>

                                    

                                    <span v-if="producto.cambios?.length > 0" class="text-right" style=""> --------------</span>
                                    <span class="ml-4 text-right" v-for="cambio in producto.cambios">
                                        {{ formatToColombianPeso(cambio.price) }}</span>


                                    <span class="text-right" v-if="producto.topping?.length > 0" style="">
                                        --------------</span>

                                    <span class="ml-4 text-right" v-for="topping in producto.toppings">
                                        {{ formatToColombianPeso(topping?.price) }}</span>


                                    <span class="text-right" v-if="producto.acompanantes?.length > 0" style="">
                                        --------------</span>
                                    <span class="ml-4" v-for="acompanante in producto.acompanantes">
                                        {{ formatToColombianPeso(acompanante.price) }}</span>

                                </div>

                            </div>
                        </div>






                    </div>





            </div>

        </div>



    </div>
    <!-- {{ store.salesReport.total_sales.orders_info[7] }} -->



</Dialog></template>


<script setup>
import { ref } from 'vue'
import { useReportesStore } from '../store/reportes';
import { formatToColombianPeso, productoEnviado } from '../service/valoresReactivosCompartidos';
import { PrimeIcons } from 'primevue/api';
const store = useReportesStore()
const visibleDialog = ref(true)



</script>

<style scoped >* {
    text-transform: lowercase;
}

*::first-letter {
    text-transform: uppercase;
}</style>