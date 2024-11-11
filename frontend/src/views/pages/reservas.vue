<template>
    <div class="col-12 px-2 my-8  p-0" style="margin-top: 6rem;">
      

      
        <p class="text-center text-2xl my-8"><b>RESERVAS PARA CUMPLEANOS</b> </p>
       
        {{ product }}

        <div>
            <img style="width: 40rem;height: 30rem;" :src="`${URI}/read-photo-product/${product.img_identifier}/600`" alt="">
        </div>

    </div>
   
</template>


<script setup>
import { useToast } from 'primevue/usetoast';
import { ref, onMounted, onBeforeUnmount, computed, watch } from 'vue';
import resumen from './resumen.vue';
import { usecartStore } from '../../store/shoping_cart';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { useSitesStore } from '../../store/site';
import {useUserStore} from '../../store/user'
import { paymentMethodService } from '../../service/restaurant/paymentMethodService';
import validate from './validate.vue';
import { useReportesStore } from '../../store/ventas';
import { URI } from '../../service/conection';
const loadinStore = useReportesStore()
const store = usecartStore()
const siteStore = useSitesStore()
const use = ref(0)
const user = useUserStore()

const payment_method_options =  ref([])
const product = ref({})


onMounted( async()=> {
    payment_method_options.value = await paymentMethodService.getPaymentMethods()

    if (user.user.payment_method_option?.id != 7)
        siteStore.setNeighborhoodPrice()
    else {
        siteStore.setNeighborhoodPriceCero()

    }

    product.value = await getProducts()

})



const getProducts = async () => {
    loadinStore.setLoading(true, 'cargando productos')
        try {
        let response = await fetch(`${URI}/products-active/category-id/${25}/site/${1}/1`);
        if (!response.ok) {
            store.setLoading(false, 'cargando productos')

            throw new Error(`HTTP error! status: ${response.status}`);

        }
        loadinStore.setLoading(false, 'cargando productos')

        let data = await response.json();
        return data[0]
    } catch (error) {
        loadinStore.setLoading(false, 'cargando productos')

        console.error('Error fetching data: ', error);
    }
    }



watch(() => user.user.payment_method_option, (new_val) => {

    if(new_val.id == 7){
        siteStore.current_delivery = siteStore.location.neigborhood.delivery_price
        siteStore.location.neigborhood.delivery_price = 0
    }else{
        siteStore.setNeighborhoodPrice()
    }
})




</script>


<style scoped>
*:focus {
    border: none;
}

.led {
    animation: cambiaColor 1s infinite;
    /* 3s de duración, animación infinita */
}

.name-product::first-letter {
    text-transform: uppercase;
}

img {
    border-radius: 50%;
}

.domi-name {
    text-transform: capitalize;
}

.descripcion::first-letter {
    text-transform: uppercase;
}

@keyframes cambiaColor {
    0% {
        background-color: rgb(0, 0, 0);
    }

    50% {
        background-color: rgb(30, 255, 0);
    }

    100% {
        background-color: var(--primary-color);
    }
}

.triangulo {
    width: 0;
    height: 0;
    border-left: 1rem solid transparent;
    border-right: 1rem solid transparent;
    border-bottom: 2rem solid #ffede1;
    /* Altura del triángulo dependiendo del ancho */
    transform: rotate(-65deg);
    position: absolute;
    top: -1rem;
    left: -1.2rem;
}


.container {
    background-color: rgb(0, 0, 0);
}

.fixed {
    position: fixed;
    width: 25%;
}

.scrollit {
    float: left;
    width: 71%
}

.sumary {
    /* background-color: green; */
}

.izq {
    /* width: 100%; */

}

*:focus {
    /* outline: none; */
}


.contenedor-producto {
    align-items: center;
    border-radius: .5rem;
    overflow: hidden;
    height: 7rem;
    position: relative;
}

@media (max-width: 991px) {
    .contenedor-producto {
        /* background-color: #ffffffea;align-items: center;border-radius: rem;overflow: hidden;height: 7rem;position: relative; */
    }
}

.nombre-sesion {
    font-weight: bold;
    /* width: auto; */
    border-radius: 5rem;
}

.contenedor-principal {
    /* border-radius: 2rem; */
    /* position: sticky */
    /* top: 100px; */
    /* margin-bottom: 10rem; */
    /* background-color: var(--primary-color); */
    /* height: auto; */
}


.producto {
    border-bottom: 2px solid #00000020;
}



.cantidad:focus-visible {
    outline: none;

}

.imagen {
    height: 100px;
    object-fit: contain;
}

.contador {
    background-color: white;
    /* height: 3rem;  */

    display: flex;
    border-radius: 0.1rem;
    padding: 0.1rem 1rem;
    /* border: 1px solid var(--primary-color); */
    border-radius: 0.5rem;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.274);
    /* bottom: 0.5rem; */
    position: absolute;
    right: 1rem;
    bottom: 1rem;
    width: 8rem;
    height: 2.5rem;

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

@media (min-width: 768px) and (max-width: 991px) {
    .clase {
        /* background-color: red; */
        min-width: 720px;
    }
}

@media (min-width: 1200px) and (max-width: 1920px) {
    .clase {
        /* background-color: red; */
        min-width: 1024px;

    }

    .productos-scroll {
        overflow-y: auto;
        border-radius: 2rem;
        /* height: 80vh; */
        overflow-y: auto;
        /* max-height: 720px */
    }
}

::-webkit-scrollbar {
    width: 1rem;
    /* Ancho de la barra de desplazamiento */
    padding-top: 1rem;
    position: absolute;
    display: none;
}

.clase {}

*:focus {
    outline: none;
}
/* 
* {
    text-transform: lowercase;
} */

*::first-letter {
    text-transform: uppercase;
}

input:focus {
    outline: none;
    border: none;
}

/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {
    background-color: rgb(255, 0, 0);
    /* Color del pulgar de la barra de desplazamiento */
    border-radius: 9px;
    border: 5px solid var(--primary-color);
    height: 10rem;
    width: 10rem;
    /* display: none;  */
}
</style>