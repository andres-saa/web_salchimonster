<template>

<!-- <Carousel class=" " :value="images" :numVisible="1" :numScroll="1" :showNavigators="true" :showIndicators="true"  circular :autoplayInterval="3000">
    <template #item="slotProps">
        <div class=" " style="overflow: hidden;">
            <div class="">
                <img :src="'https://images.pexels.com/photos/4393021/pexels-photo-4393021.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'" :alt="slotProps.data.name" class="w-12 imagen " />
            </div>
            <div>
            </div>
        </div>
    </template>
</Carousel> -->




<div  id="banner" class="carousel slide " data-ride="carousel" style="">
    
    <div class="carousel-inner  " style="width: 100%;height: ;">
      <div class="carousel-item active sm:d-none" style="width: 100%;">
        <img  style="width: 100%;height: 100%;  object-fit: cover; " :src="`/images/banners/banner-1.jpeg`" alt="">
      </div>

      
      <div v-for="i in [2,3,4,5,6,7,8]" class="carousel-item  ">
        <img  style="width: 100%;height: 80vh;  object-fit:cover;" :src="`/images/banners/banner-${i}.jpeg`" alt="">

      </div>
    </div>

    <a style="width: auto; position: absolute; left: 0; padding: 0; transform: translateX(); "
      class="carousel-control-prev" href="#banner" role="button" data-slide="prev">
      <span style="color: var(--primary-color); transform: scale(1.5);font-size: 2rem ;" :class="PrimeIcons.ANGLE_LEFT"
        aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a style="width: auto; position: absolute; right: 0; padding: 0; transform: translateX(); "
      class="carousel-control-next" href="#banner" role="button" data-slide="next">
      <span style="color: var(--primary-color); transform: scale(1.5);font-size: 2rem ;" :class="PrimeIcons.ANGLE_RIGHT"
        aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</template>

<script setup>
import { PrimeIcons } from 'primevue/api';
 const images = [
    'src/images/banners/banner-1'
    
 ]

</script>

<style scoped>
.imagen{
    /* height: 90vh */
    /* object-fit: cover; */
    width: 100vw;
}

@media (max-width: 500px) {
    .carousel-item{
        height: 50vh;
        width: 100%;
    }

    .carousel{
        /* width: 100vw; */

    }
    

}


@media (min-width: 501px) {
    .carousel-item{
        height: 80vh;
        width: 100%;
    }

    .carousel{
        /* width: 100vw; */

    }
    

}
</style>