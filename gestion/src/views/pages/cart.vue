<template>
    <!-- <p class="col-12 md:col-7 p-1 text-center text-4xl m-auto mb-5 lg:col-7 md:col-12 sm:col-12 m-auto mb-8" style="border-radius: 2rem; font-weight: bold; color: white; background-color: black;" > <i class="text-4xl pr-3 p-0" :class="PrimeIcons.SHOPPING_CART" style="color: white;"></i>CARRITO DE COMPRAS </p>
     -->
    <div class="col-12 p-4">
        <div sty class=" contenedor-principal p- md:p-3 grid md:col-12 xl:col-10 xl:ml-auto xl:mr-auto clase"
            v-if="products.length > 0" style="margin-bottom: 5rem;overflow: hidden;height: 100%;">

            <div class=" col-12 xl:col-7 xl:p-5 " style="">
                <div class="cont-products grid p-2" style=";position: inherit; ">




                    <div v-for="product in products" class=" m-0 grid mb-5 md:pr-5 pb-6"
                        style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); height: min-content;border-radius: 1rem; overflow: hidden; position: relative; background-color: white;">


                        <img @click="setProductDialog(product.product)" class="col-3 p-1 " style=" object-fit: contain;"
                            :src="`${URI}/read_product_image/600/${product.product.id}`" alt="">

                        <div class="col-9 grid m-0 pl-3  " style="">
                            <div class="col text-left md:text-xl p-0" style="font-weight: bold;">
                                {{ `${product.quantity} ${product.product.name} ` }}

                            </div>
                            <div class="col-4 text-right md:text-xl p-0" style="font-weight: bold;">
                                {{ formatoPesosColombianos(product.quantity * product.product.price +
                                   product.quantity * sumarAdiciones(product.product.adiciones)) }}
                            </div>
                            <div class="col-12 text-left md:text-xl descripcion p-0"
                                style="font-weight:; text-transform: lowercase;">{{ product.product.description }} </div>


                            <p class="col-12 pl-0  mb-0 pb-0" style="font-weight: bold;"
                                v-if="product.product.adiciones.length > 0">ADICIONES</p>
                            <div style="max-width: max-content;">
                                <span class="col text-left md:text-xl descripcion p-0"
                                    style="min-width:max-content; text-transform: lowercase; "
                                    v-for="i in product.product.adiciones"> {{ i.name }} + <span style="font-weight: bold;">
                                        {{ formatoPesosColombianos(i.price) }}</span> , </span>
                            </div>
                            <p v-if="product.product.salsas.length > 0" class="col-12 pl-0  mb-0 pb-0" style="font-weight: bold;">SALSAS</p>
                            <div style="max-width: max-content;">
                                <span class="col md:col text-left md:text-xl descripcion p-0"
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


            <div class=" col-12 xl:col-5  mt-4 p-5 "
                style="position: relative; border-radius: 1rem; box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);padding:0 1rem ;background-color: white; ">
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


                                <p style="font-weight: bold;height: ;">{{ formatoPesosColombianos(product.quantity * product.product.price) }}
                                </p>
                            </div>
                        </div>


                        <Dialog v-model:visible="showAditions[product.product.name]" :style="{ width: '500px' }"
                            header="Seleccion de sede" :modal="true" class="p-fluid p-3"
                            style="background-color: rgb(255, 255, 255);border:none; border-radius: 1rem;padding-top: 2rem; color: black;">


                            <!-- <button  @click="showAditions[product.product.name] = !showAditions[product.product.name]" style="width: 3rem;height: 3rem; border: none; position: absolute; right: 2rem; top:1rem;  padding: 0; background-color: var(--primary-color); border-radius: 50%; ">
                        <i :class="PrimeIcons.TIMES" style="color: white;height: 100%;width: 100%; font-weight: bold; " class="text-2xl"></i>

                        </button> -->

                            <!-- <button @click="showAditions[product.product.name] = !showAditions[product.product.name]"
                            style="width: 3rem;height: 3rem; border: none; position: absolute; right: 2rem; top:1rem;background-color: var(--primary-color); border-radius: 50%; display: flex; align-items: center;justify-content: center; z-index: 9;">
                            <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>

                        </button> -->
                            <div class="col-12 p-0" style="">
                                <div class="col-12 p-0 ">
                                    <p class="text-xl" style="color: black;font-weight: bold;">YA LE METISTE</p>
                                    <div class="col-12 p-0  "
                                        style="display: flex; justify-content: space-between; align-items:center ;"
                                        v-for="adicion in product.product.adiciones">

                                        <!-- <button @click="eliminarAdicionDelCarrito(adicion, product.product)"
                                        style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                                        <i style="color: white; border-radius: 1rem;"
                                            :class="PrimeIcons.TIMES"></i></button> -->
                                        <p class="pl-2"
                                            style="color: black;font-weight: ; text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.1rem 0;width: 100%;color: black">
                                            <span>{{ adicion.name
                                            }}</span>
                                        </p>
                                        <p style="color: black;font-weight: bold;">{{ formatoPesosColombianos(adicion.price)
                                        }}
                                        </p>



                                    </div>
                                </div>

                                <div class="col-12 p-4 pb-2 mb-4 mt-4" style="background-color: var(--primary-color);">
                                </div>

                                <div class="col-12 p-0" style="">
                                    <p class="text-xl " style="color: black;font-weight: bold;">PERO TODAVIA LE PODES METER
                                    </p>

                                    <div class=" "
                                        style="display: flex; justify-content: space-between;position: ; align-items:center ;"
                                        v-for="adicion in quitarElementos(product.product.category_id == 1 ? adiciones.salchipapas.products :
                                            product.product.category_id == 2 ? adiciones.hamburguesas.products :
                                                product.product.category_id == 3 ? adiciones.salchipapas.products :
                                                    product.product.category_id == 4 ? adiciones.topings.products :
                                                        product.product.category_id == 5 ? adiciones.almuerzos.products.concat(adiciones.acomp_almuerzos.products) :
                                                            product.product.category_id == 6 ? product.product.adiciones.products : [], product.product.adiciones) ">

                                        <button @click="agregarAdicionAlCarrito(adicion, product.product)"
                                            style="background-color: rgb(0, 177, 9); border: none;border-radius: 0.5rem; color: white;">
                                            <i style="color: white; border-radius: 1rem;"
                                                :class="PrimeIcons.PLUS"></i></button>
                                        <p class="pl-2"
                                            style="text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.1rem 0;width: 100%;color: rgb(0, 0, 0)">
                                            <span>{{ adicion.name
                                            }}</span>
                                        </p>


                                        <p style="color: black; font-weight:bold ;height: ;">{{
                                            formatoPesosColombianos(adicion.price) }}
                                        </p>
                                    </div>

                                </div>
                            </div>



                        </Dialog>




                        <Dialog v-model:visible="showSalsas[product.product.name]" :style="{ width: '500px' }"
                            header="Seleccion de sede" :modal="true" class="p-fluid p-3"
                            style="background-color: rgb(255, 255, 255);border:none; border-radius: 1rem;padding-top: 2rem; color: black;">


                            <!-- <button  @click="showAditions[product.product.name] = !showAditions[product.product.name]" style="width: 3rem;height: 3rem; border: none; position: absolute; right: 2rem; top:1rem;  padding: 0; background-color: var(--primary-color); border-radius: 50%; ">
                        <i :class="PrimeIcons.TIMES" style="color: white;height: 100%;width: 100%; font-weight: bold; " class="text-2xl"></i>

                        </button> -->

                            <button @click="showSalsas[product.product.name] = !showSalsas[product.product.name]"
                                style="width: 3rem;height: 3rem; border: none; position: absolute; right: 2rem; top:1rem;background-color: var(--primary-color); border-radius: 50%; display: flex; align-items: center;justify-content: center; z-index: 9;">
                                <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>

                            </button>

                            <div class="col-12 p-0" style="">
                                <div class="col-12 p-0 ">
                                    <p class="text-xl" style="color: black;font-weight: bold;">YA LE METISTE</p>
                                    <div class="col-12 p-0  "
                                        style="display: flex; justify-content: space-between; align-items:center ;"
                                        v-for="salsa in product.product.salsas">

                                        <button @click="eliminarSalsaDelCarrito(salsa, product.product)"
                                            style="background-color: var(--primary-color); border: none;border-radius: 0.5rem; color: white;">
                                            <i style="color: white; border-radius: 1rem;"
                                                :class="PrimeIcons.TIMES"></i></button>
                                        <p class="pl-2"
                                            style="color: black;font-weight: ; text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.1rem 0;width: 100%;color: black">
                                            <span>{{ salsa
                                            }}</span>
                                        </p>
                                        <!-- <p style="color: black;font-weight: bold;">{{ formatoPesosColombianos(salsa.price) }}
                                    </p> -->



                                    </div>
                                </div>

                                <div class="col-12 p-0 pb-2 mb-4 mt-4" style="background-color: var(--primary-color);">
                                </div>

                                <div class="col-12 p-0" style="">
                                    <p v-if="product.product.salsas[0] == 'TODAS LAS SALSAS'" class="text-xl "
                                        style="color: black;font-weight: bold;">VA CON TODO</p>
                                    <p v-else class="text-xl " style="color: black;font-weight: bold;">PERO TODAVIA LE PODES
                                        METER</p>

                                    <div class=" "
                                        style="display: flex; justify-content: space-between;position: ; align-items:center ;"
                                        v-for="salsa in product.product.salsas[0] == 'TODAS LAS SALSAS' ? [] : quitarSalsas(adiciones.salsas, product.product.salsas) ">

                                        <button @click="agregarSalsasAlCarrito(salsa, product.product)"
                                            style="background-color: rgb(0, 177, 9); border: none;border-radius: 0.5rem; color: white;">
                                            <i style="color: white; border-radius: 1rem;"
                                                :class="PrimeIcons.PLUS"></i></button>
                                        <p class="pl-2"
                                            style="text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.1rem 0;width: 100%;color: rgb(0, 0, 0)">
                                            <span>{{ salsa
                                            }}</span>
                                        </p>


                                        <!-- <p style="color: black; font-weight:bold ;height: ;">{{
                                        formatoPesosColombianos(salsa.price) }}
                                    </p> -->
                                    </div>

                                </div>
                            </div>



                        </Dialog>



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
                                <span> {{ product.quantity }} de {{ adicion.name
                                }}</span>
                            </p>




                            <p style="font-weight: ;height: ;">{{ formatoPesosColombianos(product.quantity * adicion.price) }}
                            </p>



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

                        <div class=" p-0 col-12 pl-4" style="display: flex; justify-content: space-between;">
                            <p class="text-left  p-0 pt-2" style="font-weight: bold;height: ;"><b style="font-weight: bold;">TOTAL</b> {{ product.quantity }} {{ product.product.name }} + ADICIONES
                                </p>
                                <p class="text-right text-lg p-0 pt-2 text-l pl-4" style=" font-weight: bold;height: ;">{{ formatoPesosColombianos(product.quantity *
                                    calcularPrecioTotal(product.product)) }}
                                </p>

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

                <p class="text-2xl mt-4" style="font-weight: bold;">NOTAS DE TU PEDIDO</p>

                <!-- <input style=" border-radius: ; height:20rem;margin-bottom: 2rem; border;" class="col-12 " type="text" name=""
                id=""> -->
                <textarea v-model="order_notes" style=" min-height:5rem ;margin-bottom: 2rem; border;" class="col-12 "
                    type="text" name="" id="dynamicTextarea"></textarea>



                <div
                    style="padding: 2rem; background-color: white; position:sticky;bottom: 0rem; display: flex;width: 100%; display: flex;align-items: center; justify-content: center;">


                    <RouterLink style=" width: 60%;" to="/pay"><button
                            style=" width: 100%;min-width: max-content; border:none; background-color: var(--primary-color); color: white; border-radius: 0.6rem; padding: 0.5rem;">
                            <span class="text-xl"
                                style="font-weight: bold;margin-top: 5rem;min-width: max-content;">REALIZAR
                                PEDIDO</span></button>
                    </RouterLink>


                </div>
                <!-- <textarea cla style=" font-size: 1.5rem; resize: none; height: max-content;" class="col-12 text-xl" name="" id="" cols="30" rows="10"></textarea> -->


            </div>


        </div>



        <div class="col-12 m-auto d-flex w-100" v-else
            style="display: flex; flex-direction: column; justify-content: center; text-align: center; height: 80vh; align-items: center; ">
            <img style="width: 100%; max-width: 640px;" src="/images/empty-cart.png" alt="">

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