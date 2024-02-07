<template>
 



    <div class="cont p-3" style="background-color: white; height: 100%;position: relative"  >
        <!-- <router-link :to="`product/${props.product.id}` " @click="changeProduct(product)"> -->

            <button style="position: absolute;top: -1rem;right: -1rem;background-color:red; width: 2.5rem;height: 2.5rem;border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white;z-index: 99;" @click="addcar(prepare_product(props.product))" class="add-cart-btn text-xl"><i style="font-weight: bold;"   class="icono text-2xl  p-0 m-0 " :class="PrimeIcons.PLUS"> </i>  </button>

            



            <div class="imagen-cont " style="position: ;" @click="setProductDialog(product)">
                <!-- <img class="imagen" @error="imagenError" :src="`${URI}/read_product_image/300/${props.product.id}`" alt=""> -->
                <img class="imagen" @error="imagenError" style="height: 50;" :src="`${URI}/read-product-image/300/${props.product.name}`" alt="">
                
            
            </div>
           

        <!-- </router-link> -->
        <!-- <img class="imagen" src="src/images/iconos menu/salchipapa-icono.png" alt=""> -->

        
            <div style=" display: ; " >
                <p class="nombre-producto mt-4 " style="font-weight: bold;" > {{ props.product.name }}</p>
                <p class="descripcion-producto mt-2 text-sm mb-4">{{ truncatedDescription }}</p>

                
            </div>

            
            <Toast style="box-shadow: none;"  />
       

        <div class="info col-12 " >
            <!-- {{ showEditarProducto }} -->
            
            <div class="text-l text-right" style="font-weight: bold; "> {{ formatoPesosColombianos(props.product.price) }}</div>
        </div> 


        
    </div>

</template>

<script setup>
import { PrimeIcons } from 'primevue/api';
import { changeProduct } from '../service/productServices';
import {URI} from '@/service/conection'
import {useCart} from '@/service/cart'
import { menuGlobal } from '../service/menu/menu';
import  {formatoPesosColombianos} from '../service/formatoPesos'
import { check_site, setProductDialog,showProductDialog } from '../service/state';
import { useToast } from 'primevue/usetoast';
import { comprobar_sede } from '../service/state';
import { computed } from 'vue';

const toast = useToast();



const prepare_product = (product) => {
    product.adiciones = []
    product.salsas =[]

    return product

}
const props = defineProps({
    product: {
        type: Object,
        default: {}
    },


});


const truncatedDescription = computed(() => {
  const description = props.product.description;
  return description.substring(0, 70) + '...'
});

const addcar =(product) => {

    comprobar_sede()
    useCart.add(product)  
    toast.add({ severity: 'success', summary: 'Agregado al carrito', detail: props.product.name, life: 3000 });

}


const imagenError = (Event) => {
    Event.target.src = 'https://salchimonster.com/images/logo.png'
}

</script>

<style scoped>
.info {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: end;
    background-attachment: fixed;
    position: absolute;
    bottom: 0;
    left: 0;
    padding: 5%; 
    /* gap: 20px; */
 
    /* padding: 20px; */
}


.fade-enter-active, .fade-leave-active {
    transition: opacity 2s ease-in-out;
}
.fade-enter-from, .fade-leave-to {
    opacity: 0;
}
.fade-enter-to, .fade-leave-from {
    opacity: 1;
}




.descripcion-producto, .nombre-producto{
    text-transform: lowercase;
}

.descripcion-producto::first-letter,.nombre-producto::first-letter{
    text-transform: uppercase;
}

.add-cart-btn{
    /* transition: all  0.2s ease; */
    border-radius: 50%;
    border: none;
    height: 3rem;
    width: 3rem;
    display: flex;
    align-items: center;
    justify-content: center;

    /* padding: 1rem 1rem; */
    font-size: 20px;
    background-color: rgba(251, 0, 0, 0);
    /* border-radius: 10px; */
    color: #ff0000;
}

.add-cart-btn .icono{

    color: #fff;
}




*:focus{
    outline: none;
}

.icono{
    /* transition: all  0.2s ease; */
    color: var(--primary-color);
    /* transform: translateX(-15px); */
    font-weight: bold;
}
.cont {
    /* border: 1px solid gray; */
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    /* margin: 20px; */
    /* height: max-content; */
    /* width: 100%; */
    padding: 5%;
    /* min-height: 100%; */
    /* max-height: 100%; */
    padding-bottom: 6rem;
    position: relative;
    margin: 0;


    /* margin: 0px; */
    /* width: 90%; */
    /* width: 100%; display: flex; */
    /* margin: auto; */

    /* height: 100%; */
    /* max-height: ; */
    /* background-color: red; */
    /* margin:1rem; */
}
/* .cont:hover .imagen{
    filter: brightness(1);
    transform: scale(1.1) rotate(3deg); */
    /* filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 123, 0)); */
    /* filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(0, 0, 0)); */


.cont:hover .add-cart-btn{
    
    /* transform: translateY(-10px); */
}
.cont:hover {
    filter: brightness(1.1);
    /* box-shadow: 0px 0px 30px var(--primary-color); */
    background-color: #ff620035;
}


@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.imagen{
    width: 100%;
    object-fit: contain;
    /* transition: transform ease .3s ; */

    animation: fadeIn 1s ease-in-out 0s 1 forwards;

 
    /* background-image: url('https://i.ytimg.com/vi/yvIhfmAfsck/maxresdefault.jpg'); */
    height: 100%;
    /* background-color: red; */
    /* filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 123, 0)); */
}

.imagen-cont{
    /* width: 100%; */
    overflow: hidden;
    border-radius: 20px;
    /* height: max-content; */
    /* background-color: green; */
    animation: fadeIn 1s ease;

}

</style>