<template >


    <div class="p-0 m-0" style="min-height: 100vh;">
    
        
      <!-- <img src="/images/banners/banner-1.jpeg" class="pb-6" alt="" style="width: 100%; "> -->
        
    
        <div class=" col-12 d-flex p lg:justify-content-center align-items-center mb-5 p-2 md:p-3" style="overflow-x: auto;position: sticky; z-index: 999;top:5rem; background-color: rgb(255, 255, 255);box-shadow: 0 0 1rem rgba(0, 0, 0, 0.337); ">
            <div v-for="section in menuOptions[0].menus" :key="section.category.name" class="p-0">
    
    
    
                <RouterLink :to="`/admin-products/${section.category.name}`">
                    <button class="p-1"   :class="ruta.params.menu_name == section.category.name? 'selected menu-button':
                    ruta.fullPath == '/' && section.category.name == 'Salchipapas'? 'selected menu-button': 'menu-button' " style="font-weight: bold;">
                    {{ section.category.name }}
                </button>
                </RouterLink>
                
    
            </div>
        </div>
    
    
    
        <RouterView class="pb-8" >
    
        </RouterView>
    
    
    
    
      
        
        
    
    
    
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
    import sesion from './sesion.vue';
    
    import router from '@/router/index.js'
    import {ref} from 'vue'
    import { comprobar_sede } from '../../service/state';
    
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
    
    .fade-enter-active, .fade-leave-active {
      transition: opacity 0.5s;
    }
    .fade-enter, .fade-leave-to {
      opacity: 0;
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
        box-shadow: 0 0.4rem var(--primary-color);
        padding: 1rem;
        /* font-weight: bold; */
    
    
    }
    
    .col-12 {
        width: 100vw;
        /* position: absolute; */
        left: 0;
        padding: 1.5rem;
    }</style>