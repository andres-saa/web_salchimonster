<template>


<div class="col-12" v style="display: flex;flex-direction: column; pointer-events: none; align-items: center; justify-content: center; position: fixed;z-index: 10000;left: 0;top: 0; height: 100%;background-color: rgba(0, 0, 0, 0.5);">


<p class="text-3xl" style="font-weight: bold;text-transform: uppercase; color: white; text-shadow: 0 0 10px rgba(0, 0, 0, 0.551);">{{props.tittle   }}</p>
<div style="display: flex;">

    
        <ProgressSpinner  style="width: 100px; height: 100px" strokeWidth="4" fill="var(--surface-ground)"
        animationDuration=".5s" aria-label="Custom ProgressSpinner" />

    </div>
</div>

</template>


<script setup>


const props = defineProps({
    tittle: {
        type: String,
        default: 'CARGANDO'
    },


});




</script>