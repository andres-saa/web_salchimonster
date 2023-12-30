<template>
    <div class="   mt-4 p-0 p-0 m-0 " style="position: relative; padding:0 1rem ;background-color: white; ">
        <!-- <div class="notch"
                    style="display: flex; align-items: center; width: 30%; background-color: black; border-radius: 0 0 1rem 1rem; height: 2rem; position: sticky; top: 0; left: 35%;">
                    <div class="led"
                        style="position:absolute ;right: 1rem; width: 0.7rem; height: 0.7rem; background-color: var(--primary-color); border-radius: 50%;: 1rem">
                    </div>

                </div> -->


        <!-- <input style="border-radius: 20px; " class="col-12 " type="text" name="" id=""> -->

        <div class="productos p-0 m-0">
            <div class="producto p-0 m-0" v-for="(product, index) in contarObjetosRepetidos(pedido.order_products)"
                style="display: flex; justify-content: space-between; align-items:center ; flex-direction: column;">





                <div class="col-12 p-0 grid m-0 " style=" justify-content: space-between; align-items:center ;dis">
                    <p class="col p-0 m-0" style="font-weight: bold;display: flex;; min-width: 80%;margin: 0; gap:0.5rem">
                        <span>{{ `${product.quantity} ${product.product.name}` }}</span>
                    <p class="name-product" style="width: auto;"></p>
                    </p>

                    <div style="display: flex;gap: 0rem; justify-content: end;width: min-content; "
                        class="col p-0 text-right">



                        <p :style="
                        product.product.adiciones?.length > 0 ||
                        product.product.toppings?.length > 0 ||
                        product.product.cambios?.length > 0 ||
                        product.product.acompanantes?.length > 0? 'bold' : 'font-weight:bold'

                        " style=" ;height: ;">{{ formatoPesosColombianos(product.quantity *
                            product.product.price) }}
                        </p>
                    </div>
                </div>






                <!-- {{ product.product.salsas }} -->

                <p v-if="product.product.adiciones?.length > 0" class="col-12 p-0 pl-3 mt-1 mb-0"
                    style="font-weight: bold;">
                    ADICIONES</p>
                <div class="col-12 p-0 pl-3 m-0 "
                    style="display: flex; justify-content: space-between; align-items:center ;"
                    v-for="adicion in product.product.adiciones">

                    <!-- <button @click="eliminarAdicionDelCarrito(adicion, product.product)"
                            style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                            <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.TIMES"></i></button> -->
                    <p class="p-0 m-0" style="text-transform: uppercase; ;margin: 0; padding: 0.1rem 0;width: auto">
                        <span> {{ product.quantity }} de {{ adicion.name
                        }}</span>
                    </p>




                    <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(product.quantity * adicion.price) }}
                    </p>



                </div>

                <p v-if="product.product.cambios?.length > 0" class="col-12 p-0 pl-3 mt-1 mb-0" style="font-weight: bold;">
                    CAMBIOS</p>
                <div class="col-12 p-0 pl-3 " style="display: flex; justify-content: space-between; align-items:center ;"
                    v-for="adicion in product.product.cambios">

                    <!-- <button @click="eliminarAdicionDelCarrito(adicion, product.product)"
                            style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                            <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.TIMES"></i></button> -->
                    <p class="" style="text-transform: uppercase; ;margin: 0; padding: 0.1rem 0;width: 100%">
                        <span> {{ product.quantity }} POR {{ adicion.name
                        }}</span>
                    </p>




                    <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(product.quantity * adicion.price) }}
                    </p>



                </div>

                <p v-if="product.product.toppings?.length > 0" class="col-12 p-0 pl-3 mt-1 mb-0" style="font-weight: bold;">
                    TOPPINGS</p>
                <div class="col-12 p-0 pl-3 " style="display: flex; justify-content: space-between; align-items:center ;"
                    v-for="adicion in product.product.toppings">

                    <!-- <button @click="eliminarAdicionDelCarrito(adicion, product.product)"
                            style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                            <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.TIMES"></i></button> -->
                    <p class="" style="text-transform: uppercase; ;margin: 0; padding: 0.1rem 0;width: 100%">
                        <span> {{ product.quantity }} de {{ adicion.name
                        }}</span>
                    </p>




                    <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(product.quantity * adicion.price) }}
                    </p>



                </div>


                <p v-if="product.product.acompanantes?.length > 0" class="col-12 p-0 pl-3 mt-1 mb-0" style="font-weight: bold;">
                    ACOMPANANTES</p>
                <div class="col-12 p-0 pl-3 " style="display: flex; justify-content: space-between; align-items:center ;"
                    v-for="adicion in product.product.acompanantes">

                    <!-- <button @click="eliminarAdicionDelCarrito(adicion, product.product)"
                            style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                            <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.TIMES"></i></button> -->
                    <p class="" style="text-transform: uppercase; ;margin: 0; padding: 0.1rem 0;width: 100%">
                        <span> {{ product.quantity }}  {{ adicion.name
                        }}</span>
                    </p>




                    <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(product.quantity * adicion.price) }}
                    </p>



                </div>














                <p v-if="product.product.salsas?.length > 0" class="col-12 p-0 pl-3 mt-1 mb-0" style="font-weight: bold;">
                    SALSAS</p>
                <div class="col-12 p-0 pl-3 " style="display: flex; justify-content: space-between; align-items:center ;"
                    v-for="salsa in product.product.salsas">

                    <!-- <button @click="eliminarSalsaDelCarrito(salsa, product.product)"
                            style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                            <i style="color: white; border-radius: 1rem;" :class="PrimeIcons.TIMES"></i></button> -->
                    <p class="" style="text-transform: uppercase; ;margin: 0; padding: 0.1rem 0;width: 100%">
                        <span>{{ salsa
                        }}</span>
                    </p>




                    <!-- <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(adicion.price) }}
                        </p> -->




                </div>










                <div v-if="product.product.adiciones?.length > 0 || product.product.toppings?.length > 0 || product.product.acompanantes?.length > 0 || product.product.cambios?.length > 0"
                    class=" p-0 col-12 pl-3" style="display: flex; justify-content: space-between;border-radius: ; ">
                    <p class="text-left text-md  p-0 m-0 mb-1 " style="font-weight: bold;height: ;text-transform: ;"><b
                            style=" font-weight: bold;">TOTAL</b> {{ product.quantity }} {{ product.product.name }}
                        {{ product.product.adiciones?.length > 1 ? ' + adiciones' : '' }}
                        {{ product.product.toppings?.length > 0 ? ' + toppings' : '' }} {{ product.product.cambios?.length > 0 ?
                            ' + cambios' : '' }}
                        {{ product.product.acompanantes?.length > 0 ? ' + acompanantes' : '' }}
                    </p>
                    <p class="text-right text-md p-0  m-0 text-l " style=" font-weight: bold;height: ;">{{
                        formatoPesosColombianos(product.quantity *
                            calcularPrecioTotal(product.product)) }}
                    </p>

                </div>



                <!-- <div class="col-12 p-0 pl-3 pt-1 "
                        style="display: flex; justify-content: space-between; align-items:center ;">


                        <button @click="showSalsas[product.product.name] = !showSalsas[product.product.name]"
                            style="background-color: rgb(41, 255, 123); border: none;border-radius: 0.5rem; color: white;">
                            <i v-if="product.product.salsas[0] != 'TODAS LAS SALSAS'"
                                style="color: white; border-radius: 1rem;" :class="PrimeIcons.PLUS"></i>

                            <i v-else style="color: white; border-radius: 1rem;" :class="PrimeIcons.MINUS"></i>


                        </button>
                        <p class="pl-2"
                            style="text-transform: uppercase; ;margin: 0; padding: 0.1rem 0;width: 100%">


                            <span> {{
                                product.product.salsas.length < 1 ? 'METELE SALSAS' :
                                product.product.salsas[0] == 'TODAS LAS SALSAS' ? 'QUITALE SALSAS' : 'METELE MAS SALSAS'
                            }}</span>
                        </p>



                    </div> -->

















                <div v-if="index != contarObjetosRepetidos(pedido.order_products).length - 1"
                    class="col-12 mb-0 mt- p-0 m-2 my-2 " style="height: 2px; background-color: rgba(0, 0, 0, 0.2);">

                </div>
            </div>




        </div>




        <div class="col-12 mb-0 mt- p-0 m-0 " style="width: 100%; border-bottom: 2px solid; margin-top:0rem;"></div>



        <div class="text-md p-0 mb-0 py-0 mt-2"
            style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

            <span class=" text-md" style="font-weight: bold;"> SUBTOTAL </span>
            <span class=" text-md " style="font-weight: bold;"> {{ formatoPesosColombianos(totalOrden(pedido.order_products)
            ) }} </span>




        </div>



        <div class="text-md p-0  col-12 my-0"
            style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

            <span style="font-weight: bold; text-transform:uppercase ;"> Domicilio a <span
                    style="margin-right: 1rem; cursor: pointer;font-weight: normal; color: var(--primary-color);"><span
                        class="domi-name" style="text-transform: uppercase;">{{ pedido.user_data.user_address
                        }}</span> </span> </span>
            <span class="text-md" style="font-weight: bold;"> {{ formatoPesosColombianos(pedido.delivery_price)
            }}
            </span>

        </div>


        <div class="text-md p-0 my-0" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

            <span class="pb-1 " style="font-weight: bold;"> Total </span>
            <span class="text-md" style="font-weight: bold;"> {{ formatoPesosColombianos(totalOrden(pedido.order_products) +
                pedido.delivery_price) }} </span>




        </div>



        <!-- <div class="text-xl mt-0" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

                    <span style="font-weight: bold;"> TOTAL </span>
                    <span style="font-weight: bold;"> {{ formatoPesosColombianos(calcularTotalCarrito() +
                        pedido.deliveryPrice) }} </span>

                </div> -->

        <p class="text-l mt-2 text-l pl-3  p-0 p-0 m-0 " style="font-weight:bold ;color: white;background-color: black;">NOTAS
            DEl PEDIDO</p>

        <!-- <input style=" border-radius: ; height:20rem;margin-bottom: 2rem; border;" class="col-12 " type="text" name=""
                id=""> -->
        <div style="text-transform: lowercase;" class="col-12 mt-0 p-0  notes" type="text" name="" id="dynamicTextarea">
            {{ pedido.order_notes }}</div>






        <p class="text-l  text-l pl-3  p-0 p-0 mt-1 mb-1" style="font-weight:bold ;color: white;background-color: black;">DATOS
            DE USUARIO</p>


        <div class="col-12  grid p-0 m-0 " style="display: flex; justify-content: space-between; align-items:center ;">
            <p class="col p-0 m-0" style="text-transform: uppercase; ;margin: 0;width: 100%">
                <span> NOMBRE</span>
            </p>
            <p class="col text-right p-0 m-0" style="font-weight: ;height: ;">{{ pedido.user_data.user_name }}
            </p>
        </div>

        <div class="col-12  grid p-0 m-0 " style="display: flex; justify-content: space-between; align-items:center ;">
            <p class="col p-0 m-0" style="text-transform: uppercase; ;margin: 0;width: 100%">
                <span> Telefono</span>
            </p>
            <p class="col text-right p-0 m-0" style="font-weight: ;height: ;">{{ pedido.user_data.user_phone }}
                
            </p>
        </div>

        <div class="col-12  grid p-0 m-0 " style="display: flex; justify-content: space-between; align-items:center ;">
            <p class="col p-0 m-0" style="text-transform: uppercase; ;margin: 0;width: 100%">
                <span> direccion</span>
            </p>
            <p class="col text-right p-0 m-0" style="font-weight: ;height: ;">{{ pedido.user_data.user_address }}
                
            </p>
        </div>

        <div class="col-12  grid p-0 m-0 " style="display: flex; justify-content: space-between; align-items:center ;">
            <p class="col p-0 m-0" style="text-transform: uppercase; ;margin: 0;width: 100%">
                <span> Metodo de pago</span>
            </p>
            <p class="col text-right p-0 m-0" style="font-weight: ;height: ;">{{ pedido.payment_method }}
                
            </p>
        </div>





        <!-- <div
                    style="padding: 2rem; background-color: white; position:sticky;bottom: 0rem; display: flex;width: 100%; display: flex;align-items: center; justify-content: center;">


                   


                </div> -->
        <!-- <textarea cla style=" font-size: 1.5rem; resize: none; height: max-content;" class="col-12 text-xl" name="" id="" cols="30" rows="10"></textarea> -->


    </div>
</template>

<script setup>

import { pedido } from '../service/un_pedido';
import { calcularTotalCarrito, contarObjetosRepetidos, totalOrden } from '../service/state';
import { ref, onMounted } from 'vue';
import { formatoPesosColombianos } from '../service/formatoPesos';
import { calcularPrecioTotal } from '../service/state';
import { sumarProductos } from '../service/state'
// import { calcularTotalCarrito } from '../service/state';


// const total = ref()
// onMounted(() => {
//     products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
//     total.value = JSON.parse(localStorage.getItem('cart')).total

// })

// Ejemplo de uso



function sumarAdiciones(adiciones) {
    let suma = 0;

    for (let i = 0; i < adiciones.length; i++) {
        suma += adiciones[i].price;
    }

    return suma;
}


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


.producto {}



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

* {
    text-transform: uppercase;
}

.notes::first-letter {
    text-transform: uppercase;
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