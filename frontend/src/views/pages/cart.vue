<template>
    <!-- <p class="col-12 md:col-7 p-1 text-center text-4xl m-auto mb-5 lg:col-7 md:col-12 sm:col-12 m-auto mb-8" style="border-radius: 2rem; font-weight: bold; color: white; background-color: black;" > <i class="text-4xl pr-3 p-0" :class="PrimeIcons.SHOPPING_CART" style="color: white;"></i>CARRITO DE COMPRAS </p>
     -->
    <div class="col-12 p-4 p-0 m-0">
        <div sty class=" contenedor-principal p- md:p-3 grid md:col-10 md:m-auto xl:col-8 xl:ml-auto xl:mr-auto clase"
            v-if="products.length > 0" style="margin-bottom: 5rem;overflow: hidden;height: 100%;">

            <div class=" col-12 xl:col-7 xl:p-5 " style="">
                <div class="cont-products grid p-2" style=";position: inherit; ">




                    <div v-for="product in products" class=" m-0 grid mb-5 md:pr-5 pb-6 col-12"
                        style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); height: min-content;border-radius: 1rem; overflow: hidden; position: relative; background-color: white;">


                        <img @click="setProductDialog(product.product)" class="col-2 p-1 " style=" object-fit: contain;"
                            :src="`${URI}/read-product-image/96/${product.product.name}`" alt="">

                        <div class="col-10 grid m-0 pl-5   " style="">
                            <div class="col text-left text-md p-0" style="font-weight: bold;display: flex; gap:0.5rem">
                                <p>
                            {{ `${product.quantity}  ` }}  
                                </p> <p class="name-product" style="width: auto;">{{product.product.name}}</p>

                            </div>
                            <div class="col-4 text-right text-md p-0" style="font-weight: bold;">
                                {{ formatoPesosColombianos(
                                    product.quantity * product.product.price +
                                    product.quantity * sumarAdiciones(product.product.adiciones ) +
                                    product.quantity * sumarAdiciones(product.product.toppings) +
                                    product.quantity * sumarAdiciones(product.product.cambios) +  
                                    product.quantity * sumarAdiciones(product.product.acompanantes)    ) 
                                      }}
                            </div>
                            <div class="col-12 text-left  descripcion p-0 "
                                style="font-weight:; text-transform: lowercase;">{{ product.product.description }} </div>


                            <p class="col-12 pl-0  mb-0 pb-0" style="font-weight: bold;"
                                v-if="product.product.adiciones?.length > 0">ADICIONES</p>
                            <div style="max-width: max-content;">
                                <span class="col text-left text-md descripcion p-0"
                                    style="min-width:max-content; text-transform: lowercase; "
                                    v-for="i in product.product.adiciones"> {{ i.name }} + <span style="font-weight: bold;">
                                        {{ formatoPesosColombianos(i.price) }}</span> , </span>
                            </div>

                            <p class="col-12 pl-0  mb-0 pb-0" style="font-weight: bold;"
                                v-if="product.product.adiciones?.length > 0">CAMBIOS</p>
                            <div style="max-width: max-content;">
                                <span class="col text-left text-md descripcion p-0"
                                    style="min-width:max-content; text-transform: lowercase; "
                                    v-for="i in product.product.cambios"> {{ i.name }} + <span style="font-weight: bold;">
                                        {{ formatoPesosColombianos(i.price) }}</span> , </span>
                            </div>


                            

                            <p class="col-12 pl-0  mb-0 pb-0" style="font-weight: bold;"
                                v-if="product.product.toppings?.length > 0">TOPPINGS</p>
                            <div style="max-width: max-content;">
                                <span class="col text-left text-md descripcion p-0"
                                    style="min-width:max-content; text-transform: lowercase; "
                                    v-for="i in product.product.toppings"> {{ i.name }} + <span style="font-weight: bold;">
                                        {{ formatoPesosColombianos(i.price) }}</span> , </span>
                            </div>





                            <p class="col-12 pl-0  mb-0 pb-0" style="font-weight: bold;"
                                v-if="product.product.acompanantes?.length > 0">ACOMPANANTES</p>
                            <div style="max-width: max-content;">
                                <span class="col text-left text-md descripcion p-0"
                                    style="min-width:max-content; text-transform: lowercase; "
                                    v-for="i in product.product.acompanantes"> {{ i.name }} + <span style="font-weight: bold;">
                                        {{ formatoPesosColombianos(i.price) }}</span> , </span>
                            </div>




                            
                            <p v-if="product.product.salsas?.length > 0" class="col-12 pl-0  mb-0 pb-0" style="font-weight: bold;">SALSAS</p>
                            <div style="max-width: max-content;">
                                <span class="col md:col text-left text-md descripcion p-0"
                                    style="font-weight:; text-transform: lowercase; " v-for="i in product.product.salsas">
                                    {{ i }}, </span>

                            </div>




                        </div>
                        <div class="contador col text-reignt ">

                            <button
                                style="  display: flex; align-items: center;justify-content: center;  border: none;background-color: transparent;"
                                @click="remove(product.product)"> <i :class="PrimeIcons.MINUS"> </i>

                            </button>

                            <input class="cantidad"
                                style="font-size: 1.5rem; text-align: center; width: 30px; border: 1px none;  " readonly
                                type="text" :value="product.quantity">

                            <button
                                style="  display: flex; align-items: center;justify-content: center; border: none;font-weight: bold; font-size: 3vh;background-color: transparent;"
                                @click="add(product.product)"> <i :class="PrimeIcons.PLUS"> </i> </button>


                        </div>

                    </div>
                </div>
            </div>


           <Resumen></Resumen>


        </div>



        <div class="col-12 m-auto d-flex w-100 my-8 p-0 m-0" v-else
            style="display: flex; flex-direction: column; justify-content: center; text-align: center; min-height: 80vh; align-items: center; ">
            <img style="width: 100%; max-width: 640px; margin-bottom:  5rem;" src="/images/empty-cart.png" alt="">

            <p class="text-2xl">Metele unas Salchis</p>
            <i class="text-5xl" :class=" PrimeIcons.ARROW_DOWN" style="margin:  5rem;"></i>
        
            <Sesion_main></Sesion_main>

        </div>
    </div>
</template>


<script setup>
import { useToast } from 'primevue/usetoast';
import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { PrimeIcons } from 'primevue/api';
import { order_notes } from '@/service/order.js'
import { quitarSalsas, eliminarSalsaDelCarrito, agregarSalsasAlCarrito, domicilio, useCart, eliminarAdicionDelCarrito, agregarAdicionAlCarrito, products, updateCart, contarObjetosRepetidos, quitarElementos } from '../../service/cart';
import { useRoute } from 'vue-router';
import {subtotal, calcularPrecioTotal, calcularTotalCarrito, setProductDialog, setShowDialog, sumarAdiciones } from '../../service/state';
import { adiciones } from '../../service/menu/adiciones/adiciones';
const showAditionsDialog = ref(false)
import { URI } from '../../service/conection';
import { comprobar_sede } from '../../service/state';
import Resumen from './resumen.vue';
import Sesion_main from './sesion_main.vue';
import BarraCategorias from '../../components/BarraCategorias.vue';
const existeAdicionEnProducto = (adicion, producto) => {
    return producto.adiciones && producto.adiciones.some(a => a.id === adicion.id);
}


function autoResize(textarea) {
    // Ajusta la altura del textarea en base a su contenido
    textarea.style.height = 'auto';
    textarea.style.height = (textarea.scrollHeight) + 'px';
}

const op = ref();
const showAditions = ref([]);
const showSalsas = ref([])
const toggle = (event) => {
    op.value.toggle(event);
}


// localStorage.removeItem('cart')


const screenWidth = ref(window.innerWidth);

const isSmallScreen = computed(() => screenWidth.value < 580);

const updateScreenWidth = () => {
    screenWidth.value = window.innerWidth;
};

onMounted(() => {

    window.addEventListener('resize', updateScreenWidth);
    domicilio.value = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood

});

onBeforeUnmount(() => {
    window.removeEventListener('resize', updateScreenWidth);
    comprobar_sede()
});





const add = (product) => {
    useCart.add(product)
    
    calcularTotalCarrito()
    // total.value = JSON.parse(localStorage.getItem('cart')).total

}


const remove = (product) => {
    useCart.remove(product)

    // total.value = JSON.parse(localStorage.getItem('cart')).total
    calcularTotalCarrito()


}
// localStorage.removeItem('cart')

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


<style scoped>
*:focus {
    border: none;
}

.led {
    animation: cambiaColor 1s infinite;
    /* 3s de duración, animación infinita */
}

.name-product::first-letter{
    text-transform: uppercase;
}



.domi-name{
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

*{
    text-transform:lowercase;
}

*::first-letter{
    text-transform:uppercase;
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
}</style>