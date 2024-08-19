<template>
  <div class="mt-5 mb-0 pb-0">
    <div class="col-12  mr-auto ml-auto m-0 p-0" v-for="i in [0,1,2,3,4,5,6]" style="max-width: 1024px;">
     <!-- Muestra las imágenes horizontales cuando no es un dispositivo móvil -->
     <img v-if="!isMobile" style="width: 100%;" :src="`/images/carta/${i}.jpeg`" alt="">
   </div>
 
   <div class="col-12  mr-auto ml-auto my-0 p-0" v-for="i in [0,1,2,3,4,5,6]" style="max-width: 1024px;">
     <!-- Muestra las imágenes verticales solo en dispositivos móviles -->
     <img v-if="isMobile" style="width: 100%;" :src="`/images/carta/${i}.jpeg`" alt="">
   </div>
  </div>
   
 </template>
 
 <script>
 export default {
   data() {
     return {
       isMobile: false
     };
   },
   created() {
     this.handleResize();
     window.addEventListener('resize', this.handleResize);
   },
   beforeDestroy() {
     window.removeEventListener('resize', this.handleResize);
   },
   methods: {
     handleResize() {
       // Define el punto de corte para móviles como cualquier pantalla menor a 768px
       this.isMobile = window.matchMedia("(max-width: 768px)").matches;
     }
   }
 }
 </script>
 