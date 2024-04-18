<template>

    

<Dialog  v-model:visible="verCerrado" style="background-color:rgb(255, 255, 255);border-radius: 1rem;" maximizable modal header="Header" :style="{ width: '30rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
    <div style="background-color: rgba(76, 0, 0, 0); border-radius: 1rem;">
        <p class="m-0 py-8 text-2xl" style="color: rgb(0, 0, 0)">
        Esta restaurante esta cerrado abrimos a las {{estado.next_opening_time?.split(':')[0]   }}:{{estado.next_opening_time?.split(':')[1]   }}
    </p>

    <Button @click="verCerrado = false" style="position: absolute;right: -1rem;border: none; top: -1rem; background-color: var(--primary-color);display: flex;align-items: center;justify-content: center; border-radius: 50%; aspect-ratio: 1 / 1;">  <i class="text-2xl" style="font-weight: bold;" :class="PrimeIcons.TIMES"></i></Button>


    </div>
   
</Dialog>


</template>

<script setup>

import { PrimeIcons } from 'primevue/api';
import {verCerrado} from '@/service/state'
import {URI} from '@/service/conection'
import {ref, onMounted,onUnmounted} from 'vue'




const estado = ref({})
const visible = ref(true)


const obtenerEstado = async () => {
    
    };





    // Llamar a obtenerEstado cuando el componente se monta
    onMounted(obtenerEstado);

    // Limpiar el intervalo cuando el componente se desmonta para evitar fugas de memoria
    onUnmounted(() => clearInterval(intervalId));
</script>