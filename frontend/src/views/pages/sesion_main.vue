<template>
    <p class="col-12 text-center text-2xl lg:text-5xl" style="font-weight: bold;" > ⚔️ BATALLA DE CIUDADES ⚔️</p>

    <div class="grid xl:col-10 xl:m-auto p-0 m-auto" style="border-radius:2rem; margin-bottom: 5rem;max-width: 1024px;">
        
        
        <div v-for="(product,index) in products.filter(product => product.state === 'active')" :key="product.id" class="xl:col-4 lg:col-4 md:p-3 col-6 my-4 ">
            <span class="text-2xl py-5  lg:text-4xl" style="color: var(--primary-color); font-weight: bold;">{{ ciudades[index] }} </span> 
            <!-- <p> divisor</p> -->
            <TarjetaMenu style="width: 100%;" :product="product"></TarjetaMenu>
            
        </div>
    </div>


    <p class="col-12 text-center text-2xl lg:text-5xl" style="font-weight: bold;" >SALCHIPAPAS </p>

    <div class="grid xl:col-10 xl:m-auto p-0 m-auto" style="border-radius:2rem; margin-bottom: 5rem;max-width: 1024px;">
        <div v-for="product in products2.filter(product => product.state === 'active')" :key="product.id" class="xl:col-3 lg:col-4 md:p-3 col-6 p-3">
            <TarjetaMenu style="width: 100%;" :product="product"></TarjetaMenu>
            
        </div>
    </div>
    
    
    
    
    </template>
    
    <script setup>
    import TarjetaMenu from '@/components/TarjetaMenu.vue';
    import { onMounted, ref, watch } from 'vue';
    import { useRoute } from 'vue-router';
    import { URI } from '../../service/conection';
    import router from '@/router/index.js';
    
    const ciudades = ['Medellín','Cali','Bogotá']
    const products = ref([]);
    const products2 = ref([]); // Definiendo la variable reactiva para almacenar los productos
    const ruta = useRoute(); // Usando useRoute para acceder a los parámetros de la ruta
    
    const getProducts = async () => {
        try {
            let response = await fetch(`${URI}/products/category/name/Batalla%20de%20ciudades/site/${currentCity.value.currenSiteId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            let data = await response.json();
            products.value = data;
        } catch (error) {
            console.error('Error fetching data: ', error);
        }
    }

    const getProducts2 = async () => {
        try {
            let response = await fetch(`${URI}/products/category/name/salchipapas/site/${currentCity.value.currenSiteId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            let data = await response.json();
            products2.value = data;
        } catch (error) {
            console.error('Error fetching data: ', error);
        }
    }
    
    onMounted(async () => {
        getProducts(ruta.params.menu_name);
        getProducts2()
    });
    
    // Opcional: Observar cambios en el parámetro de la ruta
    watch(() => ruta.params.menu_name, (newMenuName) => {
        getProducts(newMenuName);
    });
    
    
    const currentCity = ref(JSON.parse(localStorage.getItem('currentNeigborhood')));
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
        box-shadow: 0 0.5rem var(--primary-color);
        /* padding: 1rem; */
        /* font-weight: bold; */
    
    
    }
    
    .col-12 {
        width: 100vw;
        /* position: absolute; */
        left: 0;
        padding: 1.5rem;
    }</style>