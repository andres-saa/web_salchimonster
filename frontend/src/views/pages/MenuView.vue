<template >


<div class="px-0 mx-0 mt-5" style="min-height: 100vh;">

    


  <CarouselBanner v-if="route.path == '/'" />
  <!-- <img src="/images/banners/banner-1.jpeg" class="pb-6" alt="" style="width: 100%; "> -->
  <!-- <Button  style="position: sticky;top:rem;z-index: 1000; left:-0.5rem;" severity="help" text icon="pi pi-angle-left text-4xl"></Button> -->

  <BarraCategorias/>

 
        <RouterView />
        
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
import { URI } from '../../service/conection';

import { usecartStore } from '@/store/shoping_cart';
import { useReportesStore } from '@/store/ventas';
const store2 = usecartStore()
const store = useReportesStore()

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

onMounted(async() => {
  window.addEventListener('resize', updateScreenWidth);
  comprobar_sede()
  await getProducts()
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


const getProducts = async (category_name) => {
  
    const site_id = siteStore.location.site?.pe_site_id
    const category_id = route.params.category_id
    if(site_id){

        if(store2.menu?.data?.length < 1 || !store2.menu?.data ){
          store.setLoading(true, 'cargando productos')
        }
        try {
        let response = await fetch(`${URI}/get-product-integration/6149/${site_id}`);
    
        if (!response.ok) {
            store.setLoading(false, 'cargando productos')

            throw new Error(`HTTP error! status: ${response.status}`);

        }
        store.setLoading(false, 'cargando productos')

        let data = await response.json();
        store2.menu = data.data;
    } catch (error) {
        store.setLoading(false, 'cargando productos')

        console.error('Error fetching data: ', error);
    }
    }
}
  


onMounted(async () => {
    // changesection({category:localStorage.getItem('menu').category,products:localStorage.getItem('menu').products})
    // getMenu().then(products => currentSection.value = products[0])
    ableMenu.value = true
});

</script>
