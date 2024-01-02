<template>

    <div class="col-12">

        <p style="
    text-align: center;
    width: 100%;
    font-size: 36px;
    font-weight: bold;
">

 <span >COMBOS</span></p>


    </div>
    <div class="grid   xl:col-10 xl:m-auto p-0 m-0">

        <div v-for="i in [1,2,3,4]" class=" mb-4 lg:col-6">
          <TarjetaCombo :img_id="i" class="tarjeta"></TarjetaCombo>  

        </div>
    </div>
</template>

<script setup>
import CarouselBanner from '@/components/CarouselBanner.vue'
// import CarouselSites from '../../components/CarouselSites.vue';
import TarjetaCombo from '../../components/TarjetaCombo.vue';
</script>

<style  scoped>

</style>