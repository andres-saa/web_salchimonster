<template>
    


<div class="grid  xl:col-10 xl:m-auto p-4  " style="; border-radius:2rem; margin-bottom: 5rem;">

<div  v-for="product in menuGlobal.salchipapas.products" class="xl:col-3 lg:col-4 md:p-3 col-6 p-2 m-0 ">
    <TarjetaMenu style="width: 100%;" class="" :product="product"></TarjetaMenu>
    <!-- <TarjetaMenu class=""></TarjetaMenu> -->

   
</div>
</div>
{{ ruta.params.menu_name }}

</template>

<script setup>

import { menuGlobal } from '@/service/menu/menu';
import TarjetaMenu from '@/components/TarjetaMenu.vue';
import router from '@/router/index.js'
import {ref} from 'vue'

const ruta = ref(router.currentRoute)



</script>


