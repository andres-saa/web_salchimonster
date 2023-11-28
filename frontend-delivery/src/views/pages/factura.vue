<template>

<div class="col-12 p-0 m-0 xl:col-12 p-0 md:p-3 texto-negro" style="width: 100%;" > 

<p class="text-xl col-12 text-center " style="font-weight: bold;">SALCHIMONSTER</p>
<p class="text-xl " style="font-weight: bold;">RESUMEN PEDIDO</p>

<!-- <input style="border-radius: 20px; " class="col-12 " type="text" name="" id=""> -->
<!-- <img class="col-2" src="images/logo.png" alt=""> -->




<div class="productos">
        <div class="producto" v-for="product in contarObjetosRepetidos(pedido.order_products)"
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

            <p v-if="product.product.salsas.length > 0" class="col-12 p-0 pl-2 mb-0" style="font-weight: bold ;">SALSAS</p>
            <div class="col-12 p-0 pl-1 "
                style="display: flex; justify-content: space-between; align-items:center ;"
                v-for="salsa in product.product.salsas">

                <!-- <button @click="eliminarAdicionDelCarrito(adicion, product.product)"
                    style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                    <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.TIMES"></i></button> -->
                <p class="pl-2"
                    style="text-transform: uppercase; min-width: ;margin: 0; padding: 0.1rem 0;width: 100%">
                    <span>{{ salsa
                    }}</span>
                </p>




                <!-- <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(adicion.price) }}
                </p> -->



            </div>



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

            

           <!-- <div style="width: 100%; background-color:gray;padding-bottom: 0.1rem; " class="m-0 mt-2 mb-2"></div> -->


           
           <div style="width: 100%; border-bottom: 0.1px solid; margin-top:0rem;"></div>













        </div>
        <br>
    </div>


<!-- <div style="width: 100%; border-bottom: 1px solid; margin-top:0rem;"></div> -->
<div class="text-l" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

    <span style="font-weight: bold;"> SUBTOTAL </span>
    <span style="font-weight: bold;"> {{ formatoPesosColombianos(calcularTotalCarrito(pedido))  }} </span>

</div>

<div class="text-l" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

<span style="font-weight: bold;"> DOMICILIO </span>
<span style="font-weight: bold;"> {{ formatoPesosColombianos(pedido.delivery_price)  }} </span>

</div>

<div class="text-xl" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

    
<span style="font-weight: bold;"> TOTAL </span>
<span style="font-weight: bold;"> {{ formatoPesosColombianos(calcularTotalCarrito(pedido)+pedido.delivery_price)  }} </span>

</div>

<p class="text-xl mt-4" style="font-weight: bold;">NOTAS DEl PEDIDO</p>

<textarea :value="pedido.order_notes" readonly  style=" min-height:5rem ;margin-bottom: 2rem; border;" class="col-12 " type="text" name="" id="dynamicTextarea" ></textarea>

<!-- <textarea cla style=" font-size: 1.5rem; resize: none; height: max-content;" class="col-12 text-xl" name="" id="" cols="30" rows="10"></textarea> -->




<div class="text-l" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

<span style="font-weight: bold;"> DATOS DE USUARIO </span>
<!-- <span style="font-weight: bold;"> {{ formatoPesosColombianos(calcularTotalCarrito(pedido))  }} </span> -->

</div>

<div class="text-l" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

<span style="font-weight: bold;"> NOMBRE </span>
<span style="font-weight:;text-transform: uppercase;"> {{ user.user_name }} </span>

</div>

<div class="text-l" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

<span style="font-weight: bold;"> TELEFONO </span>
<span style="font-weight:;text-transform: uppercase;"> {{ user.user_phone }} </span>

</div>


<div class="text-l" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

<span style="font-weight: bold;"> DIRECCIÓN </span>
<span style="font-weight:;text-transform: uppercase;"> {{ user.user_address }} </span>

</div>


<!-- {{ user }} -->



</div>

</template>


<script setup>

import {pedido} from '@/service/un_pedido'
// import { PrimeIcons } from 'primevue/api';


import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { calcularPrecioTotal, calcularTotalCarrito,contarObjetosRepetidos } from '../../service/state';
import { URI } from '../../service/conection';

// const currenNeigborhood = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood.name


const user = ref({})



onMounted( async() => {
    
  const url = `${URI}/user/${pedido.value.user_id}`;

  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Error en la solicitud: ${response.status}`);
    }

    const userData = await response.json();
    user.value = userData;
  } catch (error) {
    console.error("Error en la solicitud:", error);
    // Puedes manejar el error según tus necesidades
  }
})
            
// function contarObjetosRepetidos(arr) {
//     const objetoContador = {};


//     arr.forEach((objeto) => {
//         const nombre = objeto.name;
//         if (objetoContador[nombre]) {
//             objetoContador[nombre].quantity++;
//         } else {
//             objetoContador[nombre] = {
//                 product: objeto,
//                 quantity: 1
//             };
//         }
//     });

//     // Crear un nuevo array con los resultados
//     const resultado = Object.values(objetoContador).map((item) => item);

//     return resultado;
// }

</script>

<style scoped>

.texto-negro{
    color: black;
}

.before{
    background-color: rgba(0, 0, 0, 0.8);width: 100vw;height: 100vh; z-index: 999;
    position: absolute; top: 0;left: 0;
    transform: scale(2);
}
/*  */




</style>




