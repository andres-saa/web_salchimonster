<template>






<div   id="banner" class="carousel slide p-0  " :interval="1000" data-ride="carousel" style=" border-radius:0.5rem ;background-color: var(--primary-color); ">
    
    <div class="carousel-inner p-0 " style=" width: 100%;height: ;">
      <div class="carousel-item active sm:d-none p-0" style="width: 100%;">
        <img class="" style="width: 100%;height: 100%;max-height: 100vh;overflow: hidden;  object-fit: COVER; " :src="`/images/banners/banner-0.jpeg`" alt="">
      </div>

      
      <div v-for="i in ['site-new',1,2,3,4]" class="carousel-item p-0 col-12 " style="">
        <img  style="width: 100%;height:100% ;top: 0;max-height: 100vh;  object-fit:cover;" :src="`/images/banners/banner-${i}.jpeg`" alt="">

        <div>
          
        </div>

      </div>
    </div>

    <a style="width: auto; position: absolute; left: 0; padding: 0; transform: translateX(); "
      class="carousel-control-prev" href="#banner" role="button" data-slide="prev">
      <span style="color: var(--primary-color);background-color: rgb(0, 0, 0);border-radius: 50%; transform: scale(2);font-size: 2rem ;" :class="PrimeIcons.ANGLE_LEFT"
        aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a style="width: auto; position: absolute; right: 0; padding: 0; transform: translateX(); "
      class="carousel-control-next" href="#banner" role="button" data-slide="next">
      <span style="color: var(--primary-color);background-color: rgb(0, 0, 0);opacity:1 !important ; border-radius: 50%; transform: scale(2);font-size: 2rem ;" :class="PrimeIcons.ANGLE_RIGHT"
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
        /* height: 50vh; */
        width: 100%;
    }

    .carousel{
        /* width: 100vw; */

    }
    

}


@media (min-width: 501px) {
    .carousel-item{
        /* height: 80vh; */
        width: 100%;
    }

    .carousel{
        /* width: 100vw; */

    }
    

}
</style>