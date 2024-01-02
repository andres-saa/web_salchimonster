<template>

    <!-- {{ domici }} -->
    <div class=" col-12  grid container lg:col-10 xl:col-8 mt-8  m-auto mb-8  md:p-4" style="background-color: white; border-radius: 2rem;   box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);" v-if="products.length>0">


  

            <div class=" col-12 xl:col-6  mt-4 ">
                <div 
                style="position: relative; border-radius: 2rem; padding:0 1rem ;background-color: white;box-shadow: 0 0 10px rgba(0, 0, 0, 0.188); ">
                <!-- <div class="notch"
                    style="display: flex; align-items: center; width: 30%; background-color: black; border-radius: 0 0 1rem 1rem; height: 2rem; position: sticky; top: 0; left: 35%;">
                    <div class="led"
                        style="position:absolute ;right: 1rem; width: 0.7rem; height: 0.7rem; background-color: var(--primary-color); border-radius: 50%;: 1rem">
                    </div>

                </div> -->
                <p class="text-2xl text-center pt-4" style="font-weight: bold;">RESUMEN </p>

                <!-- <input style="border-radius: 20px; " class="col-12 " type="text" name="" id=""> -->

                <div class="productos">
                    <div class="producto" v-for="product in products"
                        style="display: flex; justify-content: space-between; align-items:center ; flex-direction: column;">



                        <div class="col-12 p-0 "
                            style="display: flex; justify-content: space-between; align-items:center ;">
                            <p class="col p-0"
                                style="font-weight: bold; text-transform: uppercase; min-width:;margin: 0; padding: 0.5rem 0">
                                <span>{{ product.quantity }}</span> <span>{{ product.product.name
                                }}</span>
                            </p>
                            
                            <div style="display: flex;gap: 1rem; justify-content: end;width: min-content; " class="col p-0 text-right">

                                <!-- sin adiciones
                                <p style="font-weight: bold;height: ;">{{ formatoPesosColombianos(product.quantity *
                                    product.product.price) }}
                                </p> -->


                                <p style="font-weight: bold;height: ;">{{ formatoPesosColombianos(product.quantity *
                                    calcularPrecioTotal(product.product)) }}
                                </p>
                            </div>
                        </div>

              





                        <!-- {{ product.product.salsas }} -->

                        <p v-if="product.product.adiciones.length > 0" class="col-12 p-0 pl-4 mb-1" style="font-weight: bold;">
                            ADICIONES</p>
                        <div class="col-12 p-0 pl-4 "
                            style="display: flex; justify-content: space-between; align-items:center ;"
                            v-for="adicion in product.product.adiciones">

                            <!-- <button @click="eliminarAdicionDelCarrito(adicion, product.product)"
                            style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                            <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.TIMES"></i></button> -->
                            <p class=""
                                style="text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.1rem 0;width: 100%">
                                <span>{{ adicion.name
                                }}</span>
                            </p>




                            <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(adicion.price) }}
                            </p>



                        </div>














                        <div class="col-12 p-0 pl-4 pt-1 "
                            style="display: flex; justify-content: space-between; align-items:center ;">


                            <!-- <button @click="showAditions[product.product.name] = !showAditions[product.product.name]"
                            style="background-color: rgb(41, 255, 123); border: none;border-radius: 0.5rem; color: white;">
                            <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.PLUS"></i></button>
                        <p class="pl-2"
                            style="text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.1rem 0;width: 100%">


                            <span> {{ product.product.adiciones.length < 1 ? 'METELE ADICIONES' : 'METELE MAS ADICIONES'
                            }}</span>
                        </p> -->



                        </div>


                        <p v-if="product.product.salsas.length > 0" class="col-12 p-0 pl-4 mt-1 mb-1" style="font-weight: bold;">
                            SALSAS</p>
                        <div class="col-12 p-0 pl-4 "
                            style="display: flex; justify-content: space-between; align-items:center ;"
                            v-for="salsa in product.product.salsas">

                            <!-- <button @click="eliminarSalsaDelCarrito(salsa, product.product)"
                            style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                            <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.TIMES"></i></button> -->
                            <p class=""
                                style="text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.1rem 0;width: 100%">
                                <span>{{ salsa
                                }}</span>
                            </p>




                            <!-- <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(adicion.price) }}
                        </p> -->




                        </div>



                        <!-- <div class="col-12 p-0 pl-4 pt-1 "
                        style="display: flex; justify-content: space-between; align-items:center ;">


                        <button @click="showSalsas[product.product.name] = !showSalsas[product.product.name]"
                            style="background-color: rgb(41, 255, 123); border: none;border-radius: 0.5rem; color: white;">
                            <i v-if="product.product.salsas[0] != 'TODAS LAS SALSAS'"
                                style="color: white; border-radius: 1rem;" :class="PrimeIcons.PLUS"></i>

                            <i v-else style="color: white; border-radius: 1rem;" :class="PrimeIcons.MINUS"></i>


                        </button>
                        <p class="pl-2"
                            style="text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.1rem 0;width: 100%">


                            <span> {{
                                product.product.salsas.length < 1 ? 'METELE SALSAS' :
                                product.product.salsas[0] == 'TODAS LAS SALSAS' ? 'QUITALE SALSAS' : 'METELE MAS SALSAS'
                            }}</span>
                        </p>



                    </div> -->



















                    </div>

                </div>




                <div style="width: 100%; border-bottom: 2px solid; margin-top:0rem;"></div>



                <div class="text-l p-0" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

                    <span style="font-weight: bold;"> SUBTOTAL </span>
                    <span style="font-weight: bold;"> {{ formatoPesosColombianos(subtotal)  }} </span>

                </div>

                <div class="text-l p-0 col-12" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

                    <span style="font-weight: bold; text-transform: uppercase;"> DOMICILIO A <span @click="setShowDialog()"
                            style="margin-right: 1rem; cursor: pointer; color: var(--primary-color);">{{ domicilio.name
                            }}</span> </span>
                    <span style="font-weight: bold;"> {{ formatoPesosColombianos(domicilio.deliveryPrice)
                    }}
                    </span>

                </div>


                <div class="text-xl" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

                    <span style="font-weight: bold;"> TOTAL </span>
                    <span style="font-weight: bold;"> {{ formatoPesosColombianos(calcularTotalCarrito() +
                        domicilio.deliveryPrice) }} </span>

                </div>

                <p class="text-2xl mt-4" style="font-weight: bold; border-radius: 1rem;">NOTAS DE TU PEDIDO</p>

                <!-- <input style=" border-radius: ; height:20rem;margin-bottom: 2rem; border;" class="col-12 " type="text" name=""
                id=""> -->
                <textarea v-model="order_notes" style=" min-height:5rem ;margin-bottom: 2rem; border-radius: 1rem;" class="col-12 "
                    type="text" name="" id="dynamicTextarea"></textarea>



                <!-- <textarea cla style=" font-size: 1.5rem; resize: none; height: max-content;" class="col-12 text-xl" name="" id="" cols="30" rows="10"></textarea> -->


            </div>
            </div>

       <div class="col-12 xl:col-6  p-0 md:p-3 " style="height: 100%;">

        <div class=" col-12 p-4 md:p-0   "
            style="position: relative; border-radius: 1rem;height:max-content;  ; ;padding:0 1rem ;background-color: white; ">

            <div style="font-weight: bold;" class="col-12 pl-0 text-center text-xl">
                DATOS DE USUARIO
            </div>
            <label for="year">NOMBRE</label> 
            <InputText type="text" class="col-12 p-1  mb-4" v-model="user_data.user_name" />
            <label for="year">BARRIO (click para modificar)</label>
            <InputText @click="showSiteDialog = !showSiteDialog" :value="currenNeigborhood" type="text" readonly class="col-12 p-1  mb-4" v-model="user_data.barrio" />
            <label for="year">DIRECCION</label>
            <InputText type="text" class="col-12 p-1  mb-4" v-model="user_data.user_address" />
            <label for="year">TELEFONO</label>
            <InputText  max="10" type="Number" class="col-12 p-1  mb-4" v-model="user_data.user_phone" />
            <label for="year">METODO DE PAGO</label>
            <Dropdown class="col-12 p-0"  v-model.trim="payMethod" :options="payMethods" placeholder=""
                            required="true" :class="{ 'p-invalid': submitted && !currentUser.position }" />


        
        
        </div>

            <div class="col-12 p-6 d-flex justify-content-center">
                <button @click="send_order()" class="col "
                        style=" width: 100%;border:none; background-color: var(--primary-color); color: white; border-radius: 0.6rem; padding: 0.5rem;">
                        <span class="text-xl" style="min-width:max-content; font-weight: bold;margin-top: 5rem;">FINALIZAR COMPRA</span></button>

            </div>
            
       </div>


       

    </div>

    <div class="col-12 m-auto d-flex" v-else style="display: flex; flex-direction: column; justify-content: center; text-align: center; height: 80vh; align-items: center; ">
        <i class="col-12" style="font-size: 30vh;" :class="PrimeIcons.SHOPPING_CART"></i>
        <i class="col-12" style="font-size: 5vh;"> Tu carrito esta vacio </i>
    
    </div>





<Dialog class="pt-8" style="background-color: white; border-radius: 1rem;" v-model:visible="showThaks" modal header="Header" :style="{ width: '30rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">

    <div>
        <p class="text-xl" style="color: black;"> Muchas gracias <span style="text-transform: capitalize;">{{user_data.user_name}}</span>, hemos recibido tu pedido y en breve será despachado</p>
    </div>
    

    <button @click="changeThanks"
                            style="width: 3rem;height: 3rem; border: none; position: absolute; right: 2rem; top:1rem;background-color: var(--primary-color); border-radius: 50%; display: flex; align-items: center;justify-content: center; z-index: 9;">
                            <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>

                        </button>
</Dialog>





</template>


<script setup>

import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { PrimeIcons } from 'primevue/api';
import { useCart,domicilio, eliminarAdicionDelCarrito,agregarAdicionAlCarrito, products, updateCart, contarObjetosRepetidos, quitarElementos } from '../../service/cart';
import { useRoute } from 'vue-router';
import { calcularPrecioTotal, calcularTotalCarrito, showSiteDialog } from '../../service/state';
import { adiciones } from '../../service/menu/adiciones/adiciones';
import {showThaks, send_order,order_notes,user_data,payMethod,payMethods } from '../../service/order';
import { subtotal } from '../../service/state';
import router from '@/router/index.js'
const changeThanks = () =>{
    showThaks.value = false
    // router.push('/')
    location.reload()

}
const currenNeigborhood = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood.name




























// const products = ref([])


    // Crear un nuevo array con los resultados

const add = (product) => {
    useCart.add(product)
    products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
    total.value = JSON.parse(localStorage.getItem('cart')).total

}

const remove = (product) => {
    useCart.remove(product)
    products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
    total.value = JSON.parse(localStorage.getItem('cart')).total

}

const total = ref()
onMounted(() => {
    products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
    total.value = JSON.parse(localStorage.getItem('cart')).total

})
// Ejemplo de uso
const miArray = [
    { name: 'producto1', price: 2000 },
    { name: 'producto2', price: 3000 },
    { name: 'producto1', price: 2000 },
    { name: 'producto3', price: 2500 },
    { name: 'producto2', price: 3000 },
];

const resultado = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
console.log(resultado);


// const productos = ref


</script>


<style>
.container {
    /* background-color: rgb(0, 0, 0); */
}


.sumary {
    /* background-color: green; */
}

.izq {
    /* width: 100%; */

}

.cantidad {
    cursor: nomel;
}


.cantidad:focus-visible {
    outline: none;

}

i {
    font-weight: bold;
}

i:hover {
    color: var(--primary-color);
}

button:hover {
    cursor: pointer;
}
</style>