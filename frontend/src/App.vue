<script setup>

import barra from './components/barra.vue';
import siteDialog from './components/siteDialog.vue';
import VistaProducto from './components/VistaProducto.vue'
import restauranteCerrado from './components/restauranteCerrado.vue';


</script>
<template>
  <restauranteCerrado>
  </restauranteCerrado>
  <RouterView />
  <siteDialog />
  <VistaProducto />
  <barra />
</template>
<style scoped></style>
