<template>
    <div class="cont" style="background-color: rgb(255, 0, 0);height:max-content "  >
        <!-- <router-link :to="`product/${props.product.id}` " @click="changeProduct(product)"> -->

            <div class="imagen-cont" style="position: ;" @click="setProductDialog(product)">
                <img class="imagen" @error="imagenError" style="; object-fit: cover;" :src="`${URI}/read_product_image/300/${props.product.id}`" alt="">
                

            <!-- <div class="before"
                style="top: 0; left: 0; transform: scale(2); height: 100%; overflow: hidden; position: ;  position: absolute;">
                <img :src="props.product.img_96x96" alt=""
                    style="width: 110%; height: 110%; opacity: 0.1; object-fit:  cover; filter: blur(10px);">
            </div> -->
            </div>
           

        <!-- </router-link> -->
        <!-- <img class="imagen" src="src/images/iconos menu/salchipapa-icono.png" alt=""> -->

        
            <div style="height: 2rem; display: flex; padding-top: 1rem;" >
                <p style="font-size: 1rem;font-weight: bold;  /* Establece el ancho máximo para el párrafo */
                     /* Oculta el texto que desborda el párrafo */
                  /* Agrega puntos suspensivos (...) al final del texto truncado */ "> {{ props.product.name }}</p>
                
            </div>

            
            <Toast style="box-shadow: none;"  />
       

        <div class="info">
            
            <div class="text-xl" style="font-size: 2rem; font-weight: bold;"> {{ formatoPesosColombianos(props.product.price) }}</div>
            <button @click="addcar(prepare_product(props.product))" class="add-cart-btn text-xl"><i style="color: red;z-index: 99;"  class="icono text-5xl lg:text-6xl p-0 m-0 " :class="PrimeIcons.PLUS_CIRCLE"> </i>  </button>
            <!-- <button class="mas-detalles"> + </button> -->
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
const toast = useToast();

// console.log(menuGlobal[0].products)

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

const addcar =(product) => {

    comprobar_sede()
    useCart.add(product)  
    toast.add({ severity: 'success', summary: 'Agregado al carrito', detail: props.product.name, life: 3000 });
    check_site()
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
    justify-content: space-between;
    background-attachment: fixed;
    position: absolute;
    bottom: 0;
    left: 0;
    padding: 5%; 
    /* gap: 20px; */
 
    /* padding: 20px; */
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
.imagen{
    width: 100%;
    object-fit: contain;
    transition: transform ease .3s ;;
 
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

}
</style>