<template>

    

<Dialog  v-model:visible="verCerrado" style="background-color:rgb(255, 255, 255);border-radius: 1rem;" maximizable modal header="Header" :style="{ width: '30rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
    <div style="background-color: rgba(76, 0, 0, 0); border-radius: 1rem;">
        <p class="m-0 py-8 text-2xl" style="color: rgb(0, 0, 0)">
        Esta restaurante esta cerrado abrimos a las {{hora?.split(':')[0]   }}:{{hora?.split(':')[1]}}
    </p>

    <Button @click="verCerrado = false" style="position: absolute;right: -1rem;border: none; top: -1rem; background-color: var(--primary-color);display: flex;align-items: center;justify-content: center; border-radius: 50%; aspect-ratio: 1 / 1;">  <i class="text-2xl" style="font-weight: bold;" :class="PrimeIcons.TIMES"></i></Button>


    </div>
   
</Dialog>


</template>

<script setup>

import { PrimeIcons } from 'primevue/api';
import {verCerrado} from '@/service/state'
import {URI} from '@/service/conection'
import {ref, onMounted,onUnmounted, watch} from 'vue'
import { useSitesStore } from '../store/site';

const siteStore = useSitesStore()


const estado = ref({})
const visible = ref(true)
const hora = ref(null)

const obtenerEstado = async () => {


const siteId = siteStore.location.site.site_id  
// alert(siteId)

if(!siteId){
    return
}

  try {
    const response = await fetch(`${URI}/site/${siteId}/status`);
    const data = await response.json();
    
    if (data.status === 'closed') {
      estado.value = 'cerrado';
      hora.value = data.next_opening_time
      localStorage.setItem('estado', 'cerrado');
    } else {
      estado.value = 'abierto';
      
      localStorage.setItem('estado', 'abierto');
    }
  } catch (error) {
    console.error('Error al obtener el estado:', error);
    estado.value = 'cerrado';
      localStorage.setItem('estado', 'cerrado');
  }
};





    // Llamar a obtenerEstado cuando el componente se monta
    onMounted(obtenerEstado);

    // Limpiar el intervalo cuando el componente se desmonta para evitar fugas de memoria
    onUnmounted(() => clearInterval(intervalId));


    watch(verCerrado , () => {
        obtenerEstado()
    })

</script>