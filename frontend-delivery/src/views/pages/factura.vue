<template>
    <div class="col-12 p-0 m-0 xl:col-12 p-0 md:p-3 texto-negro" style="width: 100%;">


        
        <div class="col-12 p-0" style="display: flex;">
            <img class="m-auto" src="https://salchimonster.com/images/logo.png" alt=""
                style="height: 4rem; width: 4rem; object-fit: contain;">
        </div>
        <p class="text-xl col-12 text-center " style="font-weight: bold;">SALCHIMONSTER</p>
        <p class="text-xl col-12 text-center " style="font-weight: bold;">ORDEN #{{ pedido.order_id }}</p>


        <p class="text-l pl-4  p-0 p-0" style="font-weight: bold;color: white;background-color: black;">ENTREGAR</p>

    


        <!-- {{ user }} -->


<resumen></resumen>

<p v-if="pedido?.order_status?.status == 'cancelada'" class="text-xl p-2 mt-4" style="color: rgb(0, 0, 0);background-color: rgba(255, 0, 0, 0.307);">{{ pedido?.order_status.reazon}}</p>
    </div>
</template>


<script setup>

import { pedido } from '@/service/un_pedido'
// import { PrimeIcons } from 'primevue/api';


import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { calcularPrecioTotal, calcularTotalCarrito, contarObjetosRepetidos,sumarAdicionesAlProducto,sumarProductos } from '../../service/state';
import { URI } from '../../service/conection';
import resumen from '@/components/resumen.vue'
// const currenNeigborhood = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood.name

const pedidosAll = pedido

const user = ref({})



onMounted(async () => {

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
.texto-negro {
    color: black;
}

.before {
    background-color: rgba(0, 0, 0, 0.8);
    width: 100vw;
    height: 100vh;
    z-index: 999;
    position: absolute;
    top: 0;
    left: 0;
    transform: scale(2);
}

.sin-adiciones{
font-weight: bold;
}
/*  */
</style>




