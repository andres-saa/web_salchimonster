<template>
  <div class="mb-6 pb-4" style="display: flex; overflow-x: auto; gap: 2rem;"  >
  


        <div v-for=" i in sedes"> 
        <div v-for="j in i">   
        
            <img style="height: 10rem;border-radius: 1rem;" src="https://lh3.googleusercontent.com/p/AF1QipO3PrbDp0lEG00ZeYZs4ovGePcJzHeAZGY_IyAo=s1360-w1360-h1020" alt="">

        
        
        </div>

    </div>


  
  </div>
<pedidos> </pedidos>






</template>

<script setup>
import pedidos from '../pedidos.vue';
import {sedes} from '@/sedes/sedes.js'


</script>

<style scope>

::-webkit-scrollbar {
    width: 0.5rem;
    /* Ancho de la barra de desplazamiento */
    /* padding-top: 1rem; */
    position: absolute;
    /* display: none; */
}

.clase {}

/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {
    background-color:var(--primary-color);
    /* Color del pulgar de la barra de desplazamiento */
    border-radius: 9px;
    /* border: 5px solid var(--primary-color); */
    height: 10rem;
    /* width: 10rem; */
    /* display: none;  */
}

</style>