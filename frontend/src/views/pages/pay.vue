<template>

    <!-- {{ domici }} -->
    <div class=" col-12  grid container lg:col-10 xl:col-8   m-auto mb-8  md:p-4" style="background-color: rgb(255, 255, 255); border-radius: 2rem;   " v-if="products.length>0">


  

            <resumen ></resumen>

       <div  class="col-12 xl:col-7 xl:p-5 p-0 " style="height: 100%;">

        <div class=" col-12 p-2  "
            style="position: relative; border-radius: 1rem;height:max-content;  ; ;padding:0 1rem ; ">

            <div style="font-weight: bold;" class="col-12 pl-0 text-center text-xl">
                DATOS DE USUARIO
            </div>
            <label for="year">NOMBRE</label> 
            <InputText type="text" class="col-12 p-1  mb-4  " v-model="user_data.user_name" :class="invalid.user_name? 'p-invalid': ''" />
            <!-- {{ invalid }} -->
            <label for="year">BARRIO (click para modificar)</label>
            <InputText @click="showSiteDialog = !showSiteDialog" :value="currenNeigborhood" type="text" readonly class="col-12 p-1  mb-4" v-model="user_data.barrio" />
            <label for="year">DIRECCION</label>
            <InputText type="text" class="col-12 p-1  mb-4" v-model="user_data.user_address" :class="invalid.user_address? 'p-invalid': ''" />
            <label for="year">TELEFONO</label>
            <InputText  max="10" type="Number" class="col-12 p-1  mb-4" v-model="user_data.user_phone" :class="invalid.user_phone? 'p-invalid': ''" />
            <label for="year">METODO DE PAGO</label>
            <Dropdown  class="col-12 p-0"  v-model.trim="payMethod" :options="payMethods" placeholder=""
                            required="true" :class="{ 'p-invalid': invalid.payMethod }"  />


        </div>

            <div class="col-12 p-6 d-flex justify-content-center">
                <button @click="mostrarAntojos()" class="col text-center "
                        style=" width: 100%;border:none; background-color: var(--primary-color);display: flex; justify-content: center; gap: 1rem; color: white; border-radius: 0.6rem; padding: 0.5rem;">
                        <span  class="text-xl" style="min-width:max-content;display: flex; font-weight: bold;">FINALIZAR COMPRA  
                        
                        
                            
                        
                        
                        
                        
                        </span>
                    
                        <ProgressSpinner v-if="sending_order" class="p-0 m-0"  style="width: 30px;background-color: ; height: 30px" strokeWidth="10" fill="white"
        animationDuration=".5s" aria-label="Custom ProgressSpinner" />
                    
                    
                    </button>

            </div>

          
            
       </div>


       

    </div>

    <div class="col-12 m-auto d-flex w-100" v-else
            style="display: flex; flex-direction: column; justify-content: center; text-align: center; height: 80vh; align-items: center; ">
            <img style="width: 100%; max-width: 640px;" src="/images/empty-cart.png" alt="">

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







<Dialog class="dialogo pt-6" style=" border-radius: 1rem;  overflow: ; background-color: rgb(255, 255, 255); color: rgba(0, 0, 0, 0.663)" v-model:visible="antojoVisible" modal header="name" :style="{ width: 'max-content' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">


    <span  style="border-radius: 10rem; color: black;  position:absolute ; top: 1rem;background-color: rgb(255, 255, 255); font-weight: bold;" class="text-center text-3xl px-6 py-2" > Mata el antojo</span>



    <div class="p-5" style="display: flex; align-items: center; gap:2rem; overflow-x: auto; color: black; height: 100%;">

        <div v-for="malteada in malteadas">
    
    
    <TarjetaMenu :product="malteada" style="height: 100%; width: 100%; min-width: 15rem; max-width: 15rem; box-shadow: 0 0 20px rgba(0, 0, 0, 0.227) ;"></TarjetaMenu>

    <button style="position: absolute;top: -1rem;right: -1rem;background-color:red; width: 3rem;height: 3rem;border-radius: 50%; display: flex; align-items: center;border: none; justify-content: center; color: white;z-index: 99;" @click="antojoVisible = ! antojoVisible" class="add-cart-btn text-xl"><i style="font-weight: bold;"   class="icono text-2xl  p-0 m-0 " :class="PrimeIcons.TIMES"> </i>  </button>

    <RouterLink to="/cart">
        <button style="position: absolute;top: -1rem;right: 3rem;background-color:var(--primary-color); width: 3rem;height: 3rem;border-radius: 50%; display: flex; align-items: center;border: none; justify-content: center; color: white;z-index: 99;" @click="antojoVisible = ! antojoVisible" class="add-cart-btn text-xl"><i style="font-weight: bold;"   class="icono text-2xl  p-0 m-0 " :class="PrimeIcons.SHOPPING_CART"> </i>  </button>

    </RouterLink>
    
    
</div>

    </div>



    <p   style="border-radius: 10rem; color: black;  position: absolute; bottom: -2rem;background-color:var(--primary-color); font-weight: bold;" class="text-center text-2xl px-4 py-1" ><button :disabled="sending_order" @click="send_order()" class="col text-center "
                        style=" width: 100%;border:none; background-color: var(--primary-color);display: flex; justify-content: center; gap: 1rem; color: white; border-radius: 0.6rem; padding: 0.5rem;">
                        <span  class="text-xl" style="min-width:max-content;display: flex; font-weight: bold;">FINALIZAR COMPRA  
                        
                        
                            
                        
                        
                        
                        
                        </span>
                    
                        <ProgressSpinner v-if="sending_order" class="p-0 m-0"  style="width: 30px;background-color: ; height: 30px" strokeWidth="10" fill="white"
        animationDuration=".5s" aria-label="Custom ProgressSpinner" />
                    
                    
                    </button> </p>
    
</Dialog>



</template>


<script setup>

import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { URI } from '../../service/conection';
import { PrimeIcons } from 'primevue/api';
import { verCerrado } from '../../service/state';
import { useCart,domicilio, eliminarAdicionDelCarrito,agregarAdicionAlCarrito, products, updateCart, contarObjetosRepetidos, quitarElementos } from '../../service/cart';
import { useRoute } from 'vue-router';
import { calcularPrecioTotal, calcularTotalCarrito, showSiteDialog,antojoVisible } from '../../service/state';
import { adiciones } from '../../service/menu/adiciones/adiciones';
import {showThaks, send_order,order_notes,user_data,payMethod,payMethods,invalid, sending_order } from '../../service/order';
import { subtotal } from '../../service/state';
import router from '@/router/index.js'
import Loading from '../../components/Loading.vue';
import resumen from './resumen.vue';
import Sesion_main from './sesion_main.vue';
import TarjetaMenu from '../../components/TarjetaMenu.vue';


import { useReportesStore } from "@/store/ventas";

const store = useReportesStore()

console.log(store)


const changeThanks = () =>{
    showThaks.value = false
    // router.push('/')
    location.reload()

}
const currentCity = ref(JSON.parse(localStorage.getItem('currentNeigborhood')));

const malteadas = ref([])
const currenNeigborhood = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood.name

onMounted(() => {


domicilio.value = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood

});

const getProducts = async (category_name) => {
    try {
        let response = await fetch(`${URI}/products/category/name/${category_name}/site/${currentCity.value.currenSiteId}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        let data = await response.json();
        malteadas.value = data;
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}














const mostrarAntojos = () => {



const estado = localStorage.getItem('estado')
if(estado && estado=='cerrado'){
    verCerrado.value = true
    return
}

const user = user_data.value

if (!user.user_name || !user.user_name.trim()) {
    alert("El nombre es obligatorio.");
    invalid.value.user_name = true
    antojoVisible.value = false
    return;
}

if (!user.user_phone || !user.user_phone.trim()) {
    alert("El teléfono es obligatorio.");
    invalid.value.user_phone = true
    antojoVisible.value = false
    return;
}

if (!user.user_address || !user.user_address.trim()) {
    invalid.value.user_address = true
    alert("La dirección es obligatoria.");
    antojoVisible.value = false
    return;
}
if (!payMethod.value){
    invalid.value.payMethod = true
    alert("Por favor seleccione un metodo de pago");
    antojoVisible.value = false
    return;

}

antojoVisible.value = true
}








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
    getProducts('malteadas')

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


.invalid{
    box-shadow: 0 0 10px red;
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