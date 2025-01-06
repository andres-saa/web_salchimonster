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
import { useRoute } from 'vue-router';
import { usecartStore } from './store/shoping_cart';
import { useReportesStore } from './store/ventas';
const store2 = usecartStore()
const store = useReportesStore()
const route = useRoute()
const siteStore  = useSitesStore()


onMounted(async() => {
  // await getProducts()
  await obtenerstatus()
  if (siteStore.status == 'cerrado') {
      verCerrado.value = true
    }


})


const obtenerstatus = async () => {

const siteId = siteStore.location.site.site_id  



  try {
    const response = await fetch(`${URI}/site/${siteId}/status`);
    const data = await response.json();
    
    if (data.status === 'open') {
      siteStore.status = 'abierto';
    } else {
      siteStore.status = 'cerrado';
   
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



// const getProducts = async (category_name) => {

//     const site_id = siteStore.location.site.pe_site_id
//     const category_id = route.params.category_id
//     if(category_id && site_id){

//         if(store2.menu?.data?.length < 1 || !store2.menu?.data ){
//           store.setLoading(true, 'cargando productos')
//         }
//         try {
//         let response = await fetch(`${URI}/get-product-integration/6149/${site_id}`);
//         if (!response.ok) {
//             store.setLoading(false, 'cargando productos')

//             throw new Error(`HTTP error! status: ${response.status}`);

//         }
//         store.setLoading(false, 'cargando productos')

//         let data = await response.json();
//         store2.menu = data.data;
//     } catch (error) {
//         store.setLoading(false, 'cargando productos')

//         console.error('Error fetching data: ', error);
//     }
//     }
// }
   

</script>
<template>
  <restauranteCerrado>
  </restauranteCerrado>
  <RouterView  class="p-0" style="min-height: 90vh;"/>
  <siteDialog />
  <VistaProducto />

  <barra />
</template>
<style scoped></style>
