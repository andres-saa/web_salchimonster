<script setup>

import barra from './components/barra.vue';
import siteDialog from './components/siteDialog.vue';
// import siteDialog from './components/siteDialog.vue';
import VistaProducto from './components/VistaProducto.vue'




</script>

<template>


  


<router-view  class="p-0 pb-8" style="content:; background-color: rgba(0, 0, 0, 0.046); width: 100vw;left:0px;position: absolute;"/>


<siteDialog></siteDialog>


<VistaProducto> </VistaProducto>



<barra></barra>

  <!-- <div v-if="showProductDialog" class="full-before col-12 p-0 m-0" style="top: 0;left: 0; position: fixed; background-color: black;height: 100vh;opacity: 0.1;"> </div> -->
</template>


