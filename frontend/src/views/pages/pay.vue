<template>

    <p class="col-12 md:col-7 p-1 text-center text-4xl m-auto mb-5 lg:col-7 md:col-12 sm:col-12 m-auto mb-8" style="border-radius: 2rem; font-weight: bold; color: white; background-color: black;" > <i class="text-4xl pr-3 p-0" :class="PrimeIcons.SHOPPING_CART" style="color: white;"></i>FINALIZAR COMPRA </p>

    <!-- {{ domici }} -->
    <div class=" col-12 grid container lg:col-10 xl:col-8  m-auto mb-8 p-0 md:p-4" style="background-color: white; border-radius: 2rem;   box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);" v-if="products.length>0">

       <div class="col-12 xl:col-6 p-0 md:p-3 " style="background-color: ;"> 

        <div class=" col-12 p-4  "
            style="position: relative; border-radius: 1rem;height:max-content;  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2); ; ;padding:0 1rem ;background-color: white; ">

            <p class="text-2xl" style="font-weight: bold;">RESUMEN </p>

            <!-- <input style="border-radius: 20px; " class="col-12 " type="text" name="" id=""> -->

            <div class="productos">
                <div class="producto" v-for="product in products"
                    style="display: flex; justify-content: space-between; align-items:center ; flex-direction: column;">



                    <div class="col-12 p-0" style="display: flex; justify-content: space-between; align-items:center ;">
                        <p class=""
                            style="font-weight: bold; text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.5rem 0">
                            <span>{{ product.quantity }}</span> <span>{{ product.product.name
                            }}</span>
                        </p>


                        <p style="font-weight: bold;height: ;">{{ formatoPesosColombianos(product.quantity *
                            calcularPrecioTotal(product.product)) }}
                        </p>
                    </div>

           



                    <!-- {{ product.product.salsas }} -->

                    <p v-if="product.product.adiciones.length > 0" class="col-12 p-0 pl-2 mb-0" style="font-weight: bold ;">ADICIONES</p>
                    <div class="col-12 p-0 pl-1 "
                        style="display: flex; justify-content: space-between; align-items:center ;"
                        v-for="adicion in product.product.adiciones">

                        <!-- <button @click="eliminarAdicionDelCarrito(adicion, product.product)"
                            style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                            <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.TIMES"></i></button> -->
                        <p class="pl-2"
                            style="text-transform: uppercase; min-width: ;margin: 0; padding: 0.1rem 0;width: 100%">
                            <span>{{ adicion.name
                            }}</span>
                        </p>




                        <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(adicion.price) }}
                        </p>



                    </div>

                   <div style="width: 100%; background-color:gray;padding-bottom: 0.1rem; " class="m-0 mt-2 mb-2"></div>
















                </div>
            </div>


            <!-- <div style="width: 100%; border-bottom: 2px solid; margin-top:0rem;"></div> -->
            <div class="text-l" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

                <span style="font-weight: bold;"> SUBTOTAL </span>
                <span style="font-weight: bold;"> {{ formatoPesosColombianos(calcularTotalCarrito()) }} </span>

                </div>

                <div class="text-l" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

                <span style="font-weight: bold; text-transform: uppercase;"> DOMICILIO A {{ domicilio.name }}</span>
                <span style="font-weight: bold;"> {{ formatoPesosColombianos(domicilio.deliveryPrice) }} </span>

                </div>

                <div class="text-xl" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

<span style="font-weight: bold;"> TOTAL </span>
<span style="font-weight: bold;"> {{ formatoPesosColombianos(calcularTotalCarrito() +
    domicilio.deliveryPrice) }} </span>

</div>

            <p class="text-2xl mt-4" style="font-weight: bold;">NOTAS DE TU PEDIDO</p>

            <textarea v-model="order_notes" style=" min-height:5rem ;margin-bottom: 2rem; border;" class="col-12 " type="text" name="" id="dynamicTextarea" ></textarea>
            
            <!-- <textarea cla style=" font-size: 1.5rem; resize: none; height: max-content;" class="col-12 text-xl" name="" id="" cols="30" rows="10"></textarea> -->


        </div>

       </div>
       <div class="col-12 xl:col-6 p-0 md:p-3" style="height: 100%;">

        <div class=" col-12 p-4 md:p-0   "
            style="position: relative; border-radius: 1rem;height:max-content;  ; ;padding:0 1rem ;background-color: white; ">

            
            <label for="year">NOMBRE</label>
           
           
            <InputText type="text" class="col-12 p-1  mb-4" v-model="user_data.user_name" />

            <label for="year">BARRIO (click para modificar)</label>
            <InputText @click="showSiteDialog = !showSiteDialog" :value="currenNeigborhood" type="text" readonly class="col-12 p-1  mb-4" v-model="user_data.barrio" />
        
            <label for="year">DIRECCION</label>
            <InputText type="text" class="col-12 p-1  mb-4" v-model="user_data.user_address" />
            <label for="year">TELEFONO</label>
            <InputText type="text" class="col-12 p-1  mb-4" v-model="user_data.user_phone" />
            </div>

            <div class="col-12 p-6 d-flex justify-content-center">
                <button @click="send_order()" class="col-6 "
                        style=" width: 100%;border:none; background-color: var(--primary-color); color: white; border-radius: 0.6rem; padding: 0.5rem;">
                        <span class="text-xl" style="font-weight: bold;margin-top: 5rem;">FINALIZAR COMPRA</span></button>

            </div>
            
       </div>


       

    </div>

    <div class="col-12 m-auto d-flex" v-else style="display: flex; flex-direction: column; justify-content: center; text-align: center; height: 80vh; align-items: center; ">
        <i class="col-12" style="font-size: 30vh;" :class="PrimeIcons.SHOPPING_CART"></i>
        <i class="col-12" style="font-size: 5vh;"> Tu carrito esta vacio </i>
    
    </div>

</template>


<script setup>

import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { PrimeIcons } from 'primevue/api';
import { useCart,domicilio, eliminarAdicionDelCarrito,agregarAdicionAlCarrito, products, updateCart, contarObjetosRepetidos, quitarElementos } from '../../service/cart';
import { useRoute } from 'vue-router';
import { calcularPrecioTotal, calcularTotalCarrito, showSiteDialog } from '../../service/state';
import { adiciones } from '../../service/menu/adiciones/adiciones';
import { send_order,order_notes,user_data } from '../../service/order';


const currenNeigborhood = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood.name







const payMethod = ref('')
const payMethods = ref(["Recoger en local", "Efectivo", "Pago con tarjeta (datafono)"])






















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