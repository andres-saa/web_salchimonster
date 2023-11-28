<template>
    <div style="padding-bottom: 10rem;">




  
    <CarouselBanner></CarouselBanner>
    <!-- <CarouselBanner></CarouselBanner>
    <CarouselBanner></CarouselBanner>
    <CarouselSites></CarouselSites> -->
    <!-- <gridCombo></gridCombo> --> 
    <!-- <carouselCombo></carouselCombo> -->


    <div class="col-12 xl:text-7xl text-3xl  p-8">

<p style="text-align: center;
  width: 100%;
  
  font-weight: bold;
">


  <span>MENÚ</span>
</p>


</div>
    <carrouselCategory  :category="menuGlobal[0]"></carrouselCategory>
    <carrouselCategory :category="menuGlobal[1]"></carrouselCategory>
    <carrouselCategory :category="menuGlobal[3]"></carrouselCategory>
    <!-- <carrouselCategory :category="menuGlobal[4]"></carrouselCategory> -->
    <carrouselCategory :category="menuGlobal[2]"></carrouselCategory>




    </div>
</template>

<script setup>
import CarouselBanner from '@/components/CarouselBanner.vue'
// import CarouselSites from '../../components/CarouselSites.vue';
// import gridCombo from './gridCombo.vue';
import carrouselCategory from '../../components/carrouselCategory.vue';
import { menuGlobal } from '../../service/menu/menu';
// import carouselCombo from '../../components/carouselCombo.vue';
import carouselCombo from '../../components/carouselCombo.vue';




</script>

<style  scoped>
    
</style>