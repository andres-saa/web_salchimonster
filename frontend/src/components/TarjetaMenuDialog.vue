<template>
 

    <div  class="container shadow-3 col-12"   style="border-radius: 0.5rem; height: 100%;position: relative;display: flex;flex-direction: column;align-items: center;">
    
        

    <h4 class="text-center m-0 p-3" style="background-color: var(--primary-color);color: white;width: min-content;position:absolute;z-index: 2; border-radius: 10rem;"><b>
        NUEVO
    </b>

    </h4>
        
    
    
    <div class="imagen" style="display: flex;align-items: center;z-index: 1;min-width: 100%; " @click="open(props.product)">
  
        <transition name="fade">
        <img  v-show="loaded" @load="see" :class="loaded? 'cargado': 'sin-cargar'" style="width: 100%; aspect-ratio: 1 / 1 ; border-radius: 1rem;min-width: 100%; background-color: rgb(255, 255, 255);object-fit: contain; border-radius: 0.5rem;" :src="`https://backend.salchimonster.com/read-product-image/300/${props.product.product_name}`" alt="" >
    </transition>
    
        <div v-if="!loaded" style="width: 100%;display: flex;justify-content: center; align-items: center; aspect-ratio: 1 / 1; background-color: rgb(255, 255, 255);object-fit: contain; border-radius: 0.5rem;">
        
            <ProgressSpinner   style="width: 60px; height: 60px" strokeWidth="8" 
            animationDuration=".2s" aria-label="Custom ProgressSpinner" />
        
        </div>
  
    </div>

    <div class="texto" style="width: 100%;">
        <div style="display: flex;gap: 1rem; height: 100%; flex-direction: column;justify-content: space-between;">

            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span>
                <b style="text-transform: uppercase;">
                    {{props.product.product_name}}
                </b>
            </span>
            <!-- <Button text style="color: black;" icon="pi pi-ellipsis-v p-0 text-xl" /> -->
            <img  class="character" style="width:4rem;"  :src="`/images/characters/${props.index}.png`" alt="">





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


    <Button  style="position: absolute; right: -1rem; top:-1rem;" @click="reportStore.visible.show_new_product = false" severity="danger"  rounded icon="pi pi-times text-xl fw-100"/>

    <Button  style="width: 100%;font-weight: bold; border-radius: .5rem;" @click="addToCart(props.product)" severity="danger"    label="LO QUIERO" icon="pi pi-shopping-cart" />


</div>


</template>

<script setup>

import  {formatoPesosColombianos} from '../service/formatoPesos'
import { computed,ref,onMounted } from 'vue';
import {usecartStore} from '../store/shoping_cart'
import { useReportesStore } from '../store/ventas';

const reportStore = useReportesStore()

const store = usecartStore()

const addToCart = (productToAdd) => {

  store.addProductToCart(productToAdd) 
  reportStore.visible.show_new_product = false

}



const loaded = ref(false)

const see = () => {
    loaded.value = true
}

const open = (product) => {



    store.setCurrentProduct(product)
    store.setVisible('currentProduct',true)
    // speak()

}





function speak() {
    var text = props.product.price
    var msg = new SpeechSynthesisUtterance(text);

    // Obtiene todas las voces disponibles
    var voices = window.speechSynthesis.getVoices();
    
    // Filtra para encontrar una voz femenina en español
    var femaleVoice = voices.find(voice => voice.lang === 'es-ES' && voice.gender === 'female');

    // Si no encuentra una voz femenina específica, intenta al menos una en español
    if (!femaleVoice) {
        femaleVoice = voices.find(voice => voice.lang === 'es-ES');
    }

    // Asigna la voz encontrada al mensaje
    if (femaleVoice) {
        msg.voice = femaleVoice;
    } else {
        console.log('No se encontró una voz femenina en español.');
    }

    // Establece el idioma (aunque ya debería ser el correcto si la voz es correcta)
    msg.lang = 'es-ES';
    msg.rate = 1.2

    window.speechSynthesis.speak(msg);
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


onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        loaded.value[img.dataset.index] = true; // Marca como cargado
        observer.unobserve(img); // Detiene la observación una vez cargada la imagen
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('img.lazy').forEach((img, index) => {
    img.dataset.index = index; // Asigna un índice a cada imagen para controlar su estado
    observer.observe(img);
  });
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


