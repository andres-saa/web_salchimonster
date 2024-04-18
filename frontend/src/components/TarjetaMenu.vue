<template>
 
<!-- {{ store.currentProduct }} -->

    <div class="container p-shadow col-12" style="border-radius: 0.5rem;height: 100%;position: relative;">
    <div class="imagen">
      
            <img class="" style="width: 100%;height: 100%; background-color: rgb(255, 255, 255);object-fit: contain; border-radius: 0.2rem;" :src="`https://backend.salchimonster.com/read-product-image/300/${props.product.product_name}`" alt="" @click="open(props.product)">
     
            
        </div>

        <div class="texto" style="">
            <div style="display: flex;gap: 1rem; height: 100%; flex-direction: column;justify-content: space-between;">

                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>
                    <b style="text-transform: uppercase;">
                        {{props.product.product_name}}
                    </b>
                </span>
                <Button text style="color: black;" icon="pi pi-ellipsis-v p-0 text-xl" />




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
import { computed } from 'vue';
import {usecartStore} from '../store/shoping_cart'

const store = usecartStore()

const addToCart = (productToAdd) => {

  store.addProductToCart(productToAdd) 

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

/* Responsive adjustments */
@media (max-width: 576px) {
    .container {
    grid-template-columns: 1fr 2fr;
    width: 100%; /* 1:2 ratio for image to details */
        /* Stack elements vertically on smaller screens */
    }

    .imagen, .texto {
        width: 100%; /* Ensure full width on smaller screens */
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

/* Add additional styles for buttons, text, etc., as needed */
</style>


