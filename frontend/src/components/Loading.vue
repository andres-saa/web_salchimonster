<template>


    <div v-if="store.loading.visible" class="col-12" v style="display: flex;flex-direction: column; pointer-events: none; align-items: center; justify-content: center; position: fixed;z-index: 100;left: 0;top: 0; height: 100vh;">

<div class="p-5" style="height: min-content;display: flex;flex-direction: column;align-items: center;justify-content: center;


border-radius: 1rem;;">



<div style="display: flex;flex-direction: column;background-color: white;padding: 1rem;margin: 1rem;border-radius: 1rem;">

    
        <ProgressSpinner   style="width: 100px;justify-content: center; height: 100px" strokeWidth="4" 
        animationDuration=".3s" aria-label="Custom ProgressSpinner" />

    
       <h2 v-if="store2.menu?.data?.length < 1 || !store2.menu?.data " class="p-0 m-0 text-center" style="color: var(--primary-color);"> <strong>  CARGANDO MENU </strong> </h2> 
       <h6 v-if="store2.menu?.data?.length < 1 || !store2.menu?.data "  class="p-0 m-0 text-center" style="color: var(--primary-color);"> Solo sera' esta vez </h6> 
    </div>
</div>
</div>



</template>


<script setup>
import {useReportesStore} from '@/store/ventas.js'
import {onUnmounted} from 'vue'
import { usecartStore } from '../store/shoping_cart';

const store = useReportesStore()

const store2 = usecartStore()
const props = defineProps({
    tittle: {
        type: String,
        default: 'CARGANDO'
    },


});


onUnmounted(() => {
    store.setLoading(false);
});

</script>
