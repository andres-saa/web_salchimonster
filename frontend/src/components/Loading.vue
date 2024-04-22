<template>


    <div v-if="store.loading.visible" class="col-12" v style="display: flex;flex-direction: column; pointer-events: none; align-items: center; justify-content: center; position: fixed;z-index: 100;left: 0;top: 0; height: 100vh;">

<div class="p-5" style="height: min-content;display: flex;flex-direction: column;align-items: center;justify-content: center;


border-radius: 1rem;;">



<div style="display: flex;">

    
        <ProgressSpinner   style="width: 100px; height: 100px" strokeWidth="4" 
        animationDuration=".1s" aria-label="Custom ProgressSpinner" />

    </div>
</div>
</div>



</template>


<script setup>
import {useReportesStore} from '@/store/ventas.js'
import {onUnmounted} from 'vue'
const store = useReportesStore()

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
