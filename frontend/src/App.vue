<script setup>

import barra from './components/barra.vue';
import siteDialog from './components/siteDialog.vue';
// import siteDialog from './components/siteDialog.vue';
import VistaProducto from './components/VistaProducto.vue'
import restauranteCerrado from './components/restauranteCerrado.vue';
import Loading from './components/Loading.vue'
// import { eliminarAdicionDelCarrito } from './service/cart';
import { eliminarProductosDelCarrito } from './service/order';
import { URI } from './service/conection';
import { onMounted } from 'vue';
import { useSitesStore } from './store/site';
import { useRoute } from 'vue-router';

const siteStore = useSitesStore()
const route = useRoute()

// onMounted(()=>{
//   // if(!siteStore.location.site.site_id && route.path == '/'){
//   //   alert(route.fullPath)
//   //   siteStore.setVisible("currentSite", true)
//   // }
// eliminarProductosDelCarrito()
// })

</script>

<template>

<restauranteCerrado>

</restauranteCerrado>


        <RouterView></RouterView>



<siteDialog></siteDialog>


<VistaProducto> </VistaProducto>



<barra></barra>

  <!-- <div v-if="showProductDialog" class="full-before col-12 p-0 m-0" style="top: 0;left: 0; position: fixed; background-color: black;height: 100vh;opacity: 0.1;"> </div> -->
</template>

<style scoped> 

.fade-enter-active,.fade-leave-active {
  transition: all ease  .5s;
  
}



/* .fade-enter-to  {
  opacity: 0;
  transform: translateX(20rem);
 
} */


/* .fade-leave-from  {
  opacity: 1;
  transform: translateY(20rem);

} */
 /*
*/

 .fade-enter-from {
  opacity: 1;
  transform: translateY(-20rem);
  filter: blur(10px);
  /* filter: blur(0); */
  
}



.fade-enter-to {
  opacity: 1;
  /* filter: blur(0); */
  /* transform: translateY(0); */

  
} 



</style>


