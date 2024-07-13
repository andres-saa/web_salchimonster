<script setup>

import barra from './components/barra.vue';
import siteDialog from './components/siteDialog.vue';
import VistaProducto from './components/VistaProducto.vue'
import restauranteCerrado from './components/restauranteCerrado.vue';
import { verCerrado } from '@/service/state';
import { onMounted, watch } from 'vue';
import { useSitesStore } from './store/site';
import { URI } from './service/conection';
import validate from './views/pages/validate.vue';
const siteStore  = useSitesStore()


const obtenerstatus = async () => {

const siteId = siteStore.location.site.site_id  

if(!siteId){
  alert()
    return
    
}

  try {
    const response = await fetch(`${URI}/site/${siteId}/status`);
    const data = await response.json();
    
    if (data.status === 'closed') {
      siteStore.status = 'cerrado';
    } else {
      siteStore.status = 'abierto';
   
    }
  } catch (error) {
    console.error('Error al obtener el status:', error);
    siteStore.status = 'cerrado';
     
  }
};

watch(() => siteStore.location.site.site_id , async() => {
  await obtenerstatus()
  if (siteStore.status == 'cerrado') {
      verCerrado.value = true
    }
})

onMounted(async() => {
  await obtenerstatus()
  if (siteStore.status == 'cerrado') {
      verCerrado.value = true
    }
})

</script>
<template>
  <restauranteCerrado>
  </restauranteCerrado>
  <RouterView  class="p-0" style="min-height: 90vh;"/>
  <siteDialog />
  <VistaProducto />
  <validate/>
  <barra />
</template>
<style scoped></style>
