<template>
    <div class="cont">

        <!-- <img class="imagen" src="https://th.bing.com/th/id/R.054de7c0b15c69122bcd61901081e0f9?rik=F4gV5g9nGLmGBw&riu=http%3a%2f%2fimages5.fanpop.com%2fimage%2fphotos%2f25200000%2fGoku-goku-25227865-1024-640.png&ehk=DuvCzT0Y5DtjAFDi8%2fgLWbnoZGURAXgTyy4oecctujs%3d&risl=&pid=ImgRaw&r=0" alt=""> -->

        <div class="imagen-cont">
            <img class="imagen" @error="imagenError" :src="`${URI}/read_product_image/300/${props.combo.id}`" alt="">

            <!-- <Dialog  v-if="!img_id" v-model:visible="menuOptions" modal header="Header" :style="{ width: '20vw' }" :breakpoints="{ '960px': '75vw', '641px': '100vw' }">
                    <ProgressSpinner style="width: 100%; color: #fff; height: 50px" strokeWidth="10"
                    animationDuration=".2s" aria-label="Custom ProgressSpinner" />
            </Dialog > -->
        </div>

        <div>
            <div style="display: flex; justify-content: space-between; padding: 1rem; align-items: center;">
                <div class="lg:text-2xl text-xl" style=" font-weight:  bold; text-transform: uppercase;"> {{ combo.name }}
                </div>
                <div class="lg:text-2xl text-xl" style=" font-weight: bold;"> {{formatoPesosColombianos(combo.price)  }}</div> 
            </div>

            <!-- <RouterLink to="/combo/1"> -->
            <div class="text-xl text-justify"
                style=" padding: 20px;justify-content: space-between;background-color: rgb(255, 255, 255)">


                <!-- <div style="background-color: ;">
                    <button class="mas-detalles text-xl xl:text-4xl "><i style="font-weight: bold;padding-right: 0.5rem; " class="text-xl xl:text-4xl " :class="PrimeIcons.SHOPPING_CART">
                    </i> AGREGAR AL CARRITO</button>

                    

                </div> -->
                

                <!-- Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam possimus ipsum voluptate repellat illum a assumenda sunt dolor corporis quod aliquid voluptas voluptatem, fugiat iure porro unde et delectus voluptates? -->
            </div>
            <!-- </RouterLink> -->

        </div>
        <div class="info">

            <!-- <button class="me-lo-llevo"><i style="font-size: 20px; " class="" :class="PrimeIcons.SHOPPING_CART"> </i>Agregar al carrito</button> -->
            <!-- <button class="mas-detalles"><i style="font-size: 20px; " class="" :class="PrimeIcons.ANGLE_DOUBLE_RIGHT"> </i> Mas detalles</button> -->
        </div>




    </div>
</template>

<script setup>
import { PrimeIcons } from 'primevue/api';
import { ref } from 'vue';
import {URI} from '@/service/conection'
import  {formatoPesosColombianos} from '../service/formatoPesos'

const props = defineProps({
    // img_id: {
    //     type: Number,
    //     // default: 0
    // },
    combo: {
        type: Object,
        // default: 0
    },


});

const errorImage = ref(false)
const imagenNoCargada = (event) => {
    event.target.src = 'https://novatocode.online/assets/logo-f2daca0e.png'
}
</script>
<style scoped>
.info {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    background-attachment: fixed;
    /* gap: 20px; */

    /* padding: 20px; */
}


.add-cart-btn{
    /* transition: all  0.2s ease; */
    border: none;
    padding: 0.1rem 1rem;
    font-size: 20px;
    background-color: var(--primary-color);
    border-radius: 10px;
    color: #fff;
}

.add-cart-btn .icono{

    color: #fff;
}


.mas-detalles {
    /* transition: all  0.2s ease; */
    /* border: 2px solid var(--primary-color); */
    /* padding: 10px 40px; */
    font-size: 20px;
    color: white;
    border: none;
    background-color: var(--primary-color);
    border-radius: 30px;
    padding: 0.5rem 1rem;
    transition: all .3s ease;
    width: 100%;
    height: 100%;
}

.mas-detalles:hover {
    /* background-color: var(--primary-color); */
    /* transform: scale(1.1); */
    /* background-color: black; */
    /* cursor: pointer;
    width: 100%;
    height: 100%; */


    /* color: #fff; */
}

.mas-detalles:focus{
    border: none;
    outline: none;
}
.mas-detalles:hover>.icono {

    color: #fff;
    transform: translateX(1px);
}



.me-lo-llevo {
    transition: all 0.2s ease;
    border: 2px solid var(--primary-color);
    padding: 10px 40px;
    font-size: 10px;
    background-color: var(--primary-color);
    border-radius: 10px;
    color: #fff;
}

.me-lo-llevo .icono {

    color: #fff;
}

.me-lo-llevo:hover {
    background-color: var(--primary-color);
    transform: scale(1.1);


    color: #fff;
}


.me-lo-llevo:hover>.icono {

    color: #fff;
    transform: translateX(1px);
}


.icono {
    transition: all 0.2s ease;
    color: var(--primary-color);
    transform: translateX(-15px);
    font-weight: bold;
}

.cont {
    /* border: 1px solid gray; */
    border-radius: 2rem;
    /* box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2); */
    border: 2px solid rgb(255, 0, 0);
    overflow: hidden;
    margin: 0;
    background-color: white;
    box-shadow: 0px 0px 50px rgb(255, 0, 0);
    /* margin: 1rem; */
    /* transition:  all ease 0.3s; */
    /* width: 100%; */
    /* background-color: red; */
}

.cont:hover {
    /* border: 5px solid rgba(255, 0, 0, 1); */
    /* box-shadow: 0px 0px 20px #ff6200; */
}

.imagen {
    /* border-radius:20px  20px 0 0; */
    width: 100%;
    height: 100%;
    object-fit: contain;
    /* transition:   ease .3s ; */

}



.imagen-cont {
    /* border-radius:20px  20px 0 0; */
    width: 100%;
    /* height: 30vw; */
    object-fit: contain;
    /* transition:  all ease .5s ; */
    overflow: hidden;


}</style>