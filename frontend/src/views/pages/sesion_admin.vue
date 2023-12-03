<template>
    


<div class="grid  xl:col-10 xl:m-auto p-4 " style="; border-radius:2rem; margin-bottom: 5rem;">

<div  v-for="product in menuGlobal[`${ruta.params.category.toLowerCase()}`].products" class="xl:col-3 lg:col-4 md:p-3 col-6 p-2 m-0 ">
    <TarjetaMenuAdmin style="width: 100%;" class="" :product="product"></TarjetaMenuAdmin>
    <!-- <TarjetaMenu class=""></TarjetaMenu> -->

   
</div>
</div>




</template>

<script setup>

import { menuGlobal } from '@/service/menu/menu';
import TarjetaMenu from '@/components/TarjetaMenu.vue';
import TarjetaMenuAdmin from '../../components/TarjetaMenuAdmin.vue';
import router from '@/router/index.js'
import {ref,onMounted} from 'vue'
import { setShowDialog } from '../../service/state';

import { showProductDialog } from '../../service/state';
const ruta = ref(router.currentRoute)

onMounted(async () => {
    // showDialog.value = false
    // changesection({category:localStorage.getItem('menu').category,products:localStorage.getItem('menu').products})
    // getMenu().then(products => currentSection.value = products[0])
});

</script>


