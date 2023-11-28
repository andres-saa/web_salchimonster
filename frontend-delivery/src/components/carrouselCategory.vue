<template >



    






    




<div v-if="isSmallScreen" style=" ; width: auto; position: relative">
  <div  class="container" ref="scrollContainer"  style="background-color: #fff; position: ; display: flex;gap:1rem ; overflow-x: auto;padding-left:0.1rem">

<div   style="margin:0 0 2rem 0;" v-for="product in category.products" class="item col-6 p-0">
  <TarjetaMenu   style="   ;width: ;"    :product="product"></TarjetaMenu>     


</div>
<a style="width: auto; position: absolute; left: -2rem; ; padding: 0; transform: translateX(); "
  class="carousel-control-prev"  role="button" data-slide="prev">
  <span style="color: var(--primary-color); transform: ;font-size: 2rem ;" :class="PrimeIcons.ANGLE_DOUBLE_LEFT"
    aria-hidden="true"></span>
  <span class="sr-only">Previous</span>
</a>
<a style="width: auto; position: absolute; right: -2rem; padding: 0; transform: translateX(); "
  class="carousel-control-next"  role="button" data-slide="next">
  <span style="background-color: ; color: var(--primary-color); ;font-size: 2rem ;" :class="PrimeIcons.ANGLE_DOUBLE_RIGHT"
    aria-hidden="true"></span>
  <span class="sr-only">Next</span>
</a>

</div>

</div>
    

  <div class="col-12 md:col-12 lg:col-10 xl:col-9 mr-auto ml-auto p-0 m-0 grid p-0 mb-8" v-if="!isSmallScreen" style="gap: ; margin-top: 4rem; position: relative;display: flex;"> 

   
    <img v-if="screenWidth>767" class="  " style="    filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 0, 0)); right: 96%;top: 1rem; position:absolute;height: 78%; object-fit: contain" :src="'/images/fire_left.png'" alt="">
    <img v-if="screenWidth>767" class="  " style="    filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 0, 0)); left:96%;top: 1rem; position:absolute;height: 78%; object-fit: contain" :src="'/images/fire_right.png'" alt="">
  
    <div class=" col-12 m-auto p-0">
      <Carousel  circular   class= ""   :responsiveOptions="responsiveOptions"  style="; border-bottom:  2rem solid  black;background-color:var(--primary-color);  ;overflow: hidden; border-radius: 2rem ; height:max-content; padding-top:;margin: 0;z-index:20; box-shadow: 0px 0px 50px rgb(255, 0, 0);  z-index: ;" :value="category.products" :numVisible="category.products[3]? 4: 3" :numScroll="1"  >
        <template #item="slotProps" >
   
            <div class=" m-3  ">
                 <TarjetaMenu  style="   ;width: 100%;"    :product="slotProps.data"></TarjetaMenu>
 
            </div>
         
        </template>
    </Carousel>  


    <p class="  m-auto text-center text-2xl p-1" style="border-radius: 0 0 10rem 10rem ; left: 50%;top: 0; width: 20rem; color: white; background-color: black;z-index: 1; ; position: ; font-weight: bold; height:min-content  ">
 
 {{ category.category.name.toUpperCase() }}</p>
    </div>

    

  </div>



    </template>
    
    <script setup>
import { menuGlobal } from '../service/menu/menu';
import TarjetaMenu from './TarjetaMenu.vue';
import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { PrimeIcons } from 'primevue/api';
import setProductDialog


















const screenWidth = ref(window.innerWidth);

const isSmallScreen = computed(() => screenWidth.value < 580);

const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreenWidth);
});

const responsiveOptions = [
                {
                    breakpoint: '1400px',
                    numVisible: 4,
                    numScroll: 1
                },
                {
                    breakpoint: '1250px',
                    numVisible: 3,
                    numScroll: 1
                },
                {
                    breakpoint: '767px',
                    numVisible: 2,
                    numScroll: 1
                },
                {
                    breakpoint: '575px',
                    numVisible: 1,
                    numScroll: 1
                }
            ]
        
    
     const images = [
        'https://static.wikia.nocookie.net/p__/images/8/81/Goku_Super_Hero_Infobox.png/revision/latest?cb=20220220034848&path-prefix=protagonist',
        'https://static.wikia.nocookie.net/p__/images/8/81/Goku_Super_Hero_Infobox.png/revision/latest?cb=20220220034848&path-prefix=protagonist',
        'https://static.wikia.nocookie.net/p__/images/8/81/Goku_Super_Hero_Infobox.png/revision/latest?cb=20220220034848&path-prefix=protagonist',
        'https://static.wikia.nocookie.net/p__/images/8/81/Goku_Super_Hero_Infobox.png/revision/latest?cb=20220220034848&path-prefix=protagonist',
        
     ]

     const props = defineProps({
    category: {
        type: Array,
        default: {}
    },


});
    
    </script>
    
    <style scoped>
    .imagen{
        height: 90vh;
        object-fit: cover;
    }



body {
    font-family: var(--font-family);
    font-weight: normal;
    /* background: var(--surface-ground); */
    color: var(--text-color);
    padding: 1rem;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}



p {
    line-height: 1.75;
}



::-webkit-scrollbar {
  width: 12px; /* Ancho de la barra de desplazamiento */
}

/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {
  background-color: var(--primary-color); /* Color del pulgar de la barra de desplazamiento */
  border-radius: 6px; /* Radio de esquinas del pulgar */
}

   
    </style>