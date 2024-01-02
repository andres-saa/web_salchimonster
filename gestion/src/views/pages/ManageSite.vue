<script setup>

import Dock from 'primevue/dock';    
import { onMounted,onBeforeMount, ref } from 'vue';
import { useRoute } from 'vue-router';

import ShowFiles from '@/views/pages/ShowFiles.vue'

// /home/ludi/projects/salchimonster/salchimonster_frontend/src/views/pages/ShowUser.vue
// import { ref, onBeforeMount } from 'vue';


// import { useRouter } from 'vue-router';
// import Router from '@/router/index.js';

import {
    sitesDropValues,
    GenderDropValues,
    PositionDropValues,
    maritalStatusDropValues,
    epsDropValues,
    educationLevelDropValues,
    employmentContractTypeDropValues,
    pantSizesDropValues,
    shirtSizesDropValues,
    bloodTypesDropValues,
    housingTypesDropValues,
    statusDropValues,
    vehicleTypesDropValues,
    findSiteById,
    curentSite,
    getSite

} from '@/service/dropDownAux';
// import Showrecibos from './Showrecibos.vue';


const site = ref({})
const route = useRoute()
const currentSite = ref({})
const customer1 = ref(null);
const customer2 = ref(null);
const customer3 = ref(null);
const filters1 = ref(null);
const loading1 = ref(null);
const loading2 = ref(null);
const idFrozen = ref(false);
const products = ref(null);
const expandedRows = ref([]);

onMounted( () => {
   getSite(route.params.site_id)
    // console.log(curentSite)
});

onMounted(() => {
      const storedSiteData = localStorage.getItem('currentSiteFiles');
      if (storedSiteData) {
        currentSite.value = JSON.parse(storedSiteData);
      }
    });
</script>

<template>

<div cla  style="z-index: 99; max-width: 1024px;  display: flex;; align-items: center; justify-content: space-between; " class="col-12 mb-8 m-auto">
    <div>
        <h5 class=" text-4xl  ">SALCHIMONSTER {{ currentSite.site_name }}</h5> 

    <RouterLink :to="`/site/${route.params.site_id}/documentos`">
        <Button class="p-button-rounded mr-5 p-button-danger    " style="font-weight: bold;" outlined> DOCUMENTOS</Button>

    </RouterLink>

    <RouterLink :to="`/site/${route.params.site_id}/recibos`" style="border-radius: ;">
        <Button class="p-button-rounded" outlined style="font-weight: bold;"> RECIBOS</Button>
    </RouterLink>


    </div>

    


</div>
<div class="grid m-auto p-0 col-12" style="max-width: 1024px;">

    <img v-if="!$route.path.includes('recibos') && !$route.path.includes('documentos')  " class="col-12" style="opacity: 0.3;position: ; height: 60vh; object-fit: cover;" src="/images/files.jpg" alt="">

    <!-- {{ route.path }} -->
    <RouterView >

    </RouterView>

 

   </div>
</template>

<style lang="scss" scoped>

</style>
