<template >


<div class="p-0 m-0" style="min-height: 100vh;">

    


  <CarouselBanner v-if="route.path == '/'" ></CarouselBanner>
  <!-- <img src="/images/banners/banner-1.jpeg" class="pb-6" alt="" style="width: 100%; "> -->
  <!-- <Button  style="position: sticky;top:rem;z-index: 1000; left:-0.5rem;" severity="help" text icon="pi pi-angle-left text-4xl"></Button> -->

  <BarraCategorias style=""></BarraCategorias>


<!-- <Button  style="position: absolute; right: 0rem;" severity="help" text icon="pi pi-angle-right text-4xl"></Button> -->

  <transition name="fade">
        <RouterView style="">
        
        </RouterView>
    </transition>

 



  
    
    



</div>

    









   
</template>

<script setup>
// import TarjetaCombo from '../../components/TarjetaCombo.vue';
import TarjetaMenu from '../../components/TarjetaMenu.vue'
import { menuOptions } from '../../service/menuOptions';
import {  onMounted, onBeforeUnmount, computed,watch } from 'vue';
import { PrimeIcons } from 'primevue/api';
import { curentProduct, changeProduct } from '../../service/productServices';
import { menuGlobal } from '../../service/menu/menu';
import { ableMenu } from '../../service/menuOptions';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import CarouselBanner from '../../components/CarouselBanner.vue'
import sesion from './sesion.vue';
import BarraCategorias from '../../components/BarraCategorias.vue';
import Loading from '../../components/Loading.vue';
import { useRoute } from 'vue-router';

const route = useRoute()

const siteStore = useSitesStore()


if(!siteStore.location.site.site_id){
    // alert(route.fullPath)
    siteStore.setVisible("currentSite", true)
  }

import {ref} from 'vue'
import { comprobar_sede } from '../../service/state';
import router from '@/router/index.js'
import { useSitesStore } from '../../store/site';
const ruta = ref(router.currentRoute)
const hola = ref( localStorage.getItem('currentNeigborhood') )

const screenWidth = ref(window.innerWidth);

const isSmallScreen = computed(() => screenWidth.value < 800);

const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
  comprobar_sede()
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreenWidth);
  
});


const currentSection = ref(menuOptions.value[0].menus[0])
const currentMenu = ref({})
const changesection = (section) => {
    currentSection.value = section
    console.log(section)
}


const setSection = () => {
    currentSection.value = { category: menuOptions.value[0].menus[1].category, products: menuOptions.value[0].menus[1].products }

    console.log('cambio')
}

watch(menuOptions, setSection);






onMounted(async () => {
    // changesection({category:localStorage.getItem('menu').category,products:localStorage.getItem('menu').products})
    // getMenu().then(products => currentSection.value = products[0])
    ableMenu.value = true
});

</script>

<style scoped>
.boton-menu {
    margin: 0;
    border: none;
    background-color: transparent;
    font-size: 20px;
    padding: 0 20px;
}

.menu-button {
    background-color: transparent;
    padding: 1rem;
    margin: 0 1rem;
    border: none;
    font-size: 20px;
    /* transition: all  0.3s; */
    /* font-weight: bold; */
}

.menu-button:hover {
    /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5); */
    /* transform: scale(1.1); */
    /* border-bottom:  2px red; */
    /* color: var(--primary-color); */
    /* padding:; */
    cursor: pointer;


}
*:focus{
    outline: none;
}

::-webkit-scrollbar {
  width: 12px;
  display: none;


   /* Ancho de la barra de desplazamiento */
}



/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {

  background-color: white; /* Color del pulgar de la barra de desplazamiento */
  border-radius: 6px; /* Radio de esquinas del pulgar */
  transform: translateY(40px);
  /* padding: 50px; */
  /* display: none; */
}

.selected {
    /* color: var(--primary-color); */
    box-shadow: 0 0.5rem var(--primary-color);
    /* padding: 1rem; */
    /* font-weight: bold; */


}

.col-12 {
    width: 100vw;
    /* position: absolute; */
    left: 0;
    padding: 1.5rem;
}




/* Estado Final de Salida: desvanecido y desplazado hacia la derecha */

/* Estado Inicial de Entrada: ligeramente desplazado hacia arriba y desenfocado */


/* Estado Final de Entrada: totalmente opaco, sin desplazamiento y enfocado */




.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

/* Estado Final de Salida: desvanecido y desplazado hacia la derecha */
.fade-leave-to {
  opacity: 0;
  transform: translateX(20rem);
}

/* Estado Inicial de Entrada: ligeramente desplazado hacia arriba y desenfocado */
.fade-enter-from {
  opacity: 0;
  transform: translateY(-10vh);
  filter: blur(10px);
}

/* Estado Final de Entrada: totalmente opaco, sin desplazamiento y enfocado */
.fade-enter-to {
  opacity: 1;
  transform: translateY(0);
  filter: blur(0);
}







</style>