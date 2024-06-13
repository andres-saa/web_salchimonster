<template>
 

    <div  class="container shadow-3 col-12"  style="border-radius: 0.5rem; height: 100%;position: relative;">
    
        


        
    
    
    <div class="imagen" style="display: flex;align-items: center;">
  
        <img  v-show="loaded" :onload="see" :class="loaded? 'cargado': 'sin-cargar'" style="width: 100%; aspect-ratio: 1 / 1 ; border-radius: 1rem; background-color: rgb(255, 255, 255);object-fit: contain; border-radius: 0.5rem;" :src="`https://backend.salchimonster.com/read-product-image/300/${props.product.product_name}`" alt="" @click="open(props.product)">

        <div v-if="!loaded" style="width: 100%;display: flex;justify-content: center; align-items: center; aspect-ratio: 1 / 1; background-color: rgb(255, 255, 255);object-fit: contain; border-radius: 0.5rem;">
        
            <ProgressSpinner   style="width: 100px; height: 100px" strokeWidth="4" 
            animationDuration=".2s" aria-label="Custom ProgressSpinner" />
        
        </div>
  
    </div>

    <div class="texto" style="">
        <div style="display: flex;gap: 1rem; height: 100%; flex-direction: column;justify-content: space-between;">

            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span>
                <b style="text-transform: uppercase;">
                    {{props.product.product_name}}
                </b>
            </span>
            <!-- <Button text style="color: black;" icon="pi pi-ellipsis-v p-0 text-xl" /> -->
            <img class="character" style="width:6rem;" v-for="character in [1]" :src="`/images/characters/${props.index}.png`" alt="">





            </div>
            
            <span>
                    {{truncatedDescription?.toLocaleLowerCase()}} 
            </span>
            
            <div style="display: flex;justify-content: space-between; align-items: c;">

                
                <Button icon="pi pi-heart text-2xl" text rounded style="color: red;"/>
                <div style="display: flex; align-items: center;gap: 1rem;">
                    <span class="text-xl"><b>{{formatoPesosColombianos(props.product.price)  }}</b> </span>
                    
         
                </div>
                
            </div>

        </div>


    </div>


    <Button  style="position: absolute; right: -1rem; top:-1rem;" @click="addToCart(props.product)" severity="danger"  rounded icon="pi pi-plus text-xl fw-100"/>


</div>


</template>

<script setup>

import  {formatoPesosColombianos} from '../service/formatoPesos'
import { computed,ref } from 'vue';
import {usecartStore} from '../store/shoping_cart'

const store = usecartStore()

const addToCart = (productToAdd) => {

  store.addProductToCart(productToAdd) 

}



const loaded = ref(false)

const see = () => {
    loaded.value = true
}

const open = (product) => {

    store.setCurrentProduct(product)
    store.setVisible('currentProduct',true)

}


const props = defineProps({
    product: {
        type: Object,
        default: {}
    },
    index: {
        type: Number,
        default: 12
    },



});


const truncatedDescription = computed(() => {
  const description = props.product.product_description;
  return description.substring(0, 100) + '...'
});




const imagenError = (Event) => {
    Event.target.src = 'https://salchimonster.com/images/logo.png'
}

</script>



<style scoped>
.container {
    display: grid;
    gap: 1rem; /* Spacing between grid items */
    grid-template-columns: 1fr; 

    margin: 0;
    padding: 1rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 0.5rem 0.5rem 1.4rem 0.6rem;
}

.character{
    display: none;
}

/* Responsive adjustments */
@media (max-width: 576px) {
    .container {
    grid-template-columns: 1fr 2fr;
    width: 100%;
        /* Stack elements vertically on smaller screens */
    }

    .imagen, .texto {
        width: 100%;
         /* Ensure full width on smaller screens */
    }
    .character{
        display: inline;
    }
}

.imagen img {
    width: 100%;
    height: auto; /* Maintain aspect ratio */
    background-color: #fff;
    object-fit: contain;
    border-radius: 0.2rem;
}

.texto {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.rating {
    width: 1rem; /* Adjust based on your design */
}


.p-shadow{
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.25);
}


.fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
}
/* Add additional styles for buttons, text, etc., as needed */





@keyframes fadeIn {
    from {
       opacity: 0;
        transform: translateY(-100px);
        /* transform: scale(.5); */
        /* background-color: rgb(255, 255, 0); */
        /* filter: blur(1px); */
    }
    to {
        opacity: 1;
        /* filter: blur(1px); */

    }
}

.cargado {
    opacity: 0; /* Inicialmente invisible */
    animation: fadeIn .1s ease-out forwards; /* Duración de 1 segundo, 'ease-out' para desacelerar hacia el final, y 'forwards' para mantener el estado final visible */
}

</style>


