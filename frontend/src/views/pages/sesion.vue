<template>
    


<div class="grid  xl:col-10 xl:m-auto p-4 " style="; border-radius:2rem; margin-bottom: 5rem;">

<div  v-for="product in menuGlobal[`${ruta.params.menu_name.toLowerCase()}`].products" class="" :class="product.id == 55 || product.id == 56? 'xl:col-3 lg:col-4 md:p-3 col-6 p-2 m-0 ':'xl:col-3 lg:col-4 md:p-3 col-6 p-2 m-0 '">

<div>
    <TarjetaMenu style="width: 100%;" class="" :product="product"></TarjetaMenu>
</div>   
    <!-- <TarjetaMenu class=""></TarjetaMenu> -->

   
</div>
</div>


</template>

<script setup>

import { menuGlobal } from '@/service/menu/menu';
import TarjetaMenu from '@/components/TarjetaMenu.vue';
import router from '@/router/index.js'
import {ref} from 'vue'

const ruta = ref(router.currentRoute)



</script>


