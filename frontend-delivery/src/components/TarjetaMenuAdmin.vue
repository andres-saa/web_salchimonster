<template>
    <div class="cont">
        <router-link :to="`product/${props.product.id}` " @click="changeProduct(product)">

            <div class="imagen-cont">
                <img class="imagen" @error="imagenError" :src="`${URI}/read_product_image/${props.product.id}`" alt="">
            </div>
           

        </router-link>
        <!-- <img class="imagen" src="src/images/iconos menu/salchipapa-icono.png" alt=""> -->

        
        <div>
            <div style="display: flex;  ">
                <p style="font-size: 20px; "> {{ props.product.name }}</p>
                
            </div>

            
            
        </div>
        <div class="info">
            
            <div style="font-size: 20px; font-weight: bold;"> {{props.product.price}}</div>
            <button class="me-lo-llevo"><i style="font-size: 20px; " class="icono" :class="PrimeIcons.PENCIL"> </i>  </button>
            <!-- <button class="mas-detalles"> + </button> -->
            <!-- <button class="me-lo-llevo"><i style="font-size: 20px; " class="icono" :class="PrimeIcons.SHOPPING_CART"> </i>  </button> -->
            <!-- <button class="mas-detalles"> + </button> -->
        </div>
    </div>
</template>

<script setup>
import { PrimeIcons } from 'primevue/api';
import { changeProduct } from '../service/productServices';
import {URI} from '@/service/conection'

const props = defineProps({
    product: {
        type: Object,
        default: {}
    },


});

const imagenError = (Event) => {
    Event.target.src = 'https://novatocode.online/assets/logo-f2daca0e.png'
}
</script>
<style scoped>
.info {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-attachment: fixed;
    gap: 20px;

    /* padding: 20px; */
}



.mas-detalles{
    transition: all  0.2s ease;
    border: 2px solid var(--primary-color);
    padding: 10px 40px;
    font-size: 20px;
    background-color: transparent;
    border-radius: 10px;
}

.mas-detalles:hover {
    /* background-color: var(--primary-color); */
    transform: scale(1.1);

    
    /* color: #fff; */
}


.mas-detalles:hover > .icono {

    /* color: #fff; */
    transform: translateX(1px);
}



.me-lo-llevo{
    transition: all  0.2s ease;
    border: 2px solid var(--primary-color);
    padding: 10px 20px;
    font-size: 20px;
    background-color: var(--primary-color);
    border-radius: 10px;
    color: #fff;
}

.me-lo-llevo .icono{

    color: #fff;
}

.me-lo-llevo:hover {
    /* background-color: var(--primary-color); */
    /* transform: scale(1.4); */
    /* filter: brightness(1.4); */
    /* box-shadow: 0px 0px 4px rgb(255, 0, 0); */


    
    /* color: #fff; */
}


.me-lo-llevo:hover > .icono {

    color: #fff;
    transform: translateX(0px) scale(1.3);
}


.icono{
    transition: all  0.2s ease;
    color: var(--primary-color);
    /* transform: translateX(-15px); */
    font-weight: bold;
}
.cont {
    /* border: 1px solid gray; */
    border-radius: 20px;
    box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.2);
    margin: 20px;
}
.cont:hover .imagen{
    filter: brightness(1.3);
    transform: scale(1.1) rotate(3deg);
}

.cont:hover .me-lo-llevo{
    
    /* transform: translateY(-10px); */
}
.cont:hover {
    /* filter: brightness(1.3); */
    box-shadow: 0px 0px 30px var(--primary-color);
}
.imagen{
    width: 100%;
    object-fit: cover;
    transition: all ease .3s;
    /* background-image: url('https://i.ytimg.com/vi/yvIhfmAfsck/maxresdefault.jpg'); */
    height: 30vh;
    /* background-color: red; */
}

.imagen-cont{
    width: 100%;
    overflow: hidden;
    border-radius: 20px;
    height: 100%;

}
</style>