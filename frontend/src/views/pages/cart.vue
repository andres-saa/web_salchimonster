<template>


    <div class="col-12  my-8 md:my-8 p-0" v-if="store.cart.products.length > 0">
        <P class="text-center text-2xl my-8"><b>CARRITO DE COMPRAS</b> </P>

        <div class="grid mx-auto " style="max-width:800px;">



            <div class="col-12 text-sm md:col-6 p-3 md:px-4" style="display: flex; flex-direction: column; gap:1rem;justify-content: center;">

                <div class=" col-12 py-3 p-shadow"
                    style=" display: flex;align-items:end;position: relative; gap:1rem;border-radius: 0.3rem;"
                    v-for="product in store.cart.products">

                    <img style="width:5rem;object-fit:cover; height:5rem"
                        :src="`https://backend.salchimonster.com/read-product-image/96/${product.product.product_name}`" alt="">

                    <Button class="ml-2" @click="store.removeProductFromCart(product.product.id)" icon="pi pi-trash"
                        severity="danger" rounded
                        style="border:none;right: -.5rem;top: -.5rem; position: absolute; outline:none;width:2rem; height:2rem" />

                    <div style="display: flex; flex-direction:column;gap:0.4rem; width:100%">

                        <div style="display: flex; flex-direction:column;gap:0.3rem; width:100%">
                            <div style="display:flex;justify-content:space-between;align-items: center; width:100%;gap:1rem">
                                <span class="p-0 m-0"> {{ product.product.product_name }} </span>
                            </div>
                           <span style="text-transform: uppercase;font-weight: bold;">{{ product.product.category_name }}</span> 

                           
                            <div style="display:flex">
                                <div>

                                </div>

                                <div class="p-0 "
                                    style="box-shadow: 0 0 0.5rem rgba(0, 0, 0, 0.2); background-color:#ff620000; border-radius: 5rem;display: flex;">
                                    <Button @click="store.removeProductInstance(product.product.id)" icon="pi pi-minus"
                                        severity="danger"
                                        style="border:none;outline:none;width:2rem; height:1.5rem;border-radius: 0.4rem 0 0 0.4rem;">
                                    </Button>



                                    <InputText class="text-center"
                                        style="background-color:transparent;font-weight:bold; width:3rem;height:1.5rem;color:black ; border:none"
                                        :modelValue="product.quantity" readonly></InputText>





                                    <Button @click="store.addProductToCart(product.product)" icon="pi pi-plus "
                                        severity="danger"
                                        style="font-weight: bold; border:none;outline:none;width:2rem; height:1.5rem;border-radius:0 0.4rem   0.4rem 0;;">
                                    </Button>
                                </div>



                            </div>
                        </div>

                    </div>

                    <h5 class="p-0 m-0"> <b>{{ formatoPesosColombianos(product.total_cost) }}</b> </h5>






                </div>

                <div class="col-12 p-0 mt-1">
                    <div class="p-shadow p-3 mb-4 " v-for="(items, grupo) in agrupados" :key="grupo" style="position: relative;border-radius: 0.3rem;">
                        
                        <Button class="ml-2" @click="deleteGroup(items)" icon="pi pi-trash"
                            severity="danger" rounded
                            style="border:none;right: -.5rem;top: -.5rem; position: absolute; outline:none;width:2rem; height:2rem" />

                        <div class="mb-2">
                            <span class="mb-2 text-center">
                                <b>{{ grupo }}</b>

                            </span>
                            
                            <div class="mt-2">
                                <div v-for="item in items" :key="item.aditional_item_instance_id"
                                    style="display: flex; gap: 1rem; align-items: center;">
                                    <Button text rounded @click="deleteAd(item)" class="p-0 m-0" severity="danger"
                                        style="width: 2rem;  height: 2rem;border: none;" icon="pi pi-trash m-0"></Button>
                                        

                                    <div style="display: flex; width: 100%; gap: 1rem; justify-content: space-between;">
                                        <span class="text adicion" style="text-transform: capitalize;">{{ item.name
                                        }}</span>
                                        <span style="display: flex; align-items: center;">







                                            <span v-if="item.price > 0" class="pl-2 py-1 text-sm">
                                                <b>{{ formatoPesosColombianos(item.price * item.quantity) }}</b>
                                            </span>

                                            <div v-if="grupo != 'SALSAS'" style="box-shadow: 0 0 5px rgba(0, 0, 0, 0.411);display: flex; border-radius: 0.3rem; " class="ml-2">

                                           
                                            <Button @click="decrement(item)"  severity="danger"
                                                style="width: 2rem; height: 1.5rem;border: none; border-radius: 0.3rem 0 0 0.3rem;"
                                                icon="pi pi-minus"></Button>
                                            <InputText :modelValue="item.quantity" readonly
                                                style="width: 2rem;border: none; height: 1.5rem;" class="p-0 text-center" />
                                            <Button @click="increment(item)" severity="danger"
                                                style="width: 2rem;height: 1.5rem; border: none;border-radius:0 0.3rem 0.3rem 0;"
                                                icon="pi pi-plus"></Button>
                                            </div>
                                        </span>

                                    </div>

                                </div>

                               

                            </div>
                            
                        </div>
                        
                    </div>
                    <div  @click="store.setVisible('addAdditionToCart',true)" class="col-12 p-0 m-0" style="display: flex; justify-content: end;">
                        <Button style="width: 2rem;left: .3rem; height: 2rem;" rounded severity="danger" icon="pi pi-plus"></Button>

                    </div>

                </div>


            </div>


            <resumen class="md:col-6"></resumen>


        </div>
    </div>

    <div v-else class="col-12 " style="display: flex;justify-content: center;height: 90vh; align-items: center;">
        <img style="border-radius: 0;width: 100%; max-width: 500px;" src="/images/empty-cart.jpg" alt="">
    </div>

    <dialogAddAditions></dialogAddAditions>
</template>


<script setup>
import { useToast } from 'primevue/usetoast';
import { ref, onMounted, onBeforeUnmount, computed, watch } from 'vue';
import resumen from './resumen.vue';
import { usecartStore } from '../../store/shoping_cart';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { useSitesStore } from '../../store/site';
import { orderService } from '../../service/order/orderService'
import { adicionalesService } from '../../service/restaurant/aditionalService';
import dialogAddAditions from './dialogAddAditions.vue'
import { useUserStore } from '../../store/user';
const store = usecartStore()
const siteStore = useSitesStore()
const selectedAdditions = ref({})
const agrupados = ref({})
const user = useUserStore()


const update = () => {
    agrupados.value = store.cart.additions.reduce((acumulador, elemento) => {
        let grupo = elemento.group;

        if (!acumulador[grupo]) {
            acumulador[grupo] = [];
        }
        acumulador[grupo].push(elemento);

        return acumulador;
    }, {})
}



watch(() => store.cart.additions, () => {
    update()
},{deep:true})


const increment = (adition) => {
    const new_adition = { ...adition }
    new_adition.quantity = 1
    store.addAdditionToCart(new_adition)
}

const decrement = (adition) => {

    if(adition.quantity > 1) {
        store.removeAdditionFromCart(adition.id)
    }
}

const deleteAd = (adicion) => {
    store.removeAdditionCompletelyFromCart(adicion.id)
    update()
}

const deleteGroup = (items) => {
    items.forEach(item => {
        deleteAd(item)
    })
}

watch(() => store.visibles.addAdditionToCart, (newval)=> {
    if(newval){
        selectedAdditions.value = {}
    }
},{deep:true})

const adicionales = ref([])
onMounted(async () => {


    if (user.user.payment_method_option?.id != 7)
        siteStore.setNeighborhoodPrice()
    else {
        siteStore.setNeighborhoodPriceCero()

    }


    const product_id = 53


    if (product_id) {
        adicionales.value = await adicionalesService.getAditional(product_id)
    }


    agrupados.value = store.cart.additions.reduce((acumulador, elemento) => {
        let grupo = elemento.group;

        if (!acumulador[grupo]) {
            acumulador[grupo] = [];
        }
        acumulador[grupo].push(elemento);

        return acumulador;
    }, {})


})
// orderService.sendOrder()

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
    box-shadow: 0 .3rem 5px rgba(0, 0, 0, 0.174);
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
    text-transform: capitalize;
}

*::first-letter {
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

.p-shadow {
    box-shadow: 0 .2rem 5px rgba(0, 0, 0, 0.15);
}</style>