<template>
  <div class=" col-12 p-0 m-0" style=";   ">










   <RouterView class="p-0 ">

   </RouterView>


   


  </div>
</template>

<script setup>
// import {ref}


import { ref, computed } from 'vue';
// import { curentSite,getOrders } from '../../service/un_pedido';
import { onMounted, onBeforeUnmount, watch } from 'vue'
// import { ref, computed } from 'vue';









</script>

<style  scoped>

.link-menu{
  text-decoration: none;
  color: black;
}

.selected{

  /* background-color: rgb(255, 166, 0); */
  border-radius: 1rem;background-color: rgba(255, 255, 255, 0.9); font-weight: bold;
}

.menu{
  border-radius: 1rem;background-color: rgba(255, 255, 255, 0.638); font-weight: bold;
}
</style>