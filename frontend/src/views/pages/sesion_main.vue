<template>






  <!-- 
  <div class="mt-8" v-for="product in store2.menu.data?.filter(d => d.categoria_id == route.params.category_id)"  >
  
      <div style="display: flex;justify-content: start;align-items: center;">
  
          <TarjetaMenu style="width: 100%; max-width: 20rem;" :id="`tarjeta-${index}`" :index="index+1" :product="product"></TarjetaMenu>
  
      </div>
  
  
      <div style="border-bottom: 1px solid;height: 2px;">
  
  </div>
  </div> -->
  
  
  <div class="grid px-3 pb-8" style="max-width: 1024px;margin: auto; position:relative" >
  
  
  
     
  
  
  
  
  
  
  
      
  <div  style="position:absolute;display:flex;right:100%;gap:10rem; height:100vh;max-width:100%; justify-content:space-around; flex-direction:column;z-index: 9;">
  
  <img style="width:15vw;" v-for="character in [1,2,3,4,5]" :src="`/images/characters/line/${character}.png`" alt="">
  
  </div>
  
  
  <div  style="position:absolute;display:flex;left:100%;gap:10rem; height:100vh;max-width:100%; justify-content:space-around; flex-direction:column;z-index: 9;">
  
  <img style="width:15vw;" v-for="character in [1,2,3,4,5].reverse()" :src="`/images/characters/line/${character}.png`" alt="">
  
  </div>
      
  <p class="text-center text-3xl col-12" style="font-weight: bold;display: flex;gap: 1rem;align-items: center;">
    <div style="width: 100%;height: 5px; background-color: #ff6200">
  
    </div>
    PROMOCIONES
  
      <div style="width: 100%;height: 5px; background-color:#ff6200">
  
  </div>
      
  </p>
  
  
      <div v-for="(product, index) in products?.filter(d => d.categoria_id == 10)?.filter(p => p)" :key="product.id" class=" col-12   md:col-4 lg:col-3 sm:col-6">
  
              <TarjetaMenu style="width: 100%;" :id="`tarjeta-${index}`" :index="index+1" :product="product"></TarjetaMenu>
      </div>
  
  
  
  </div>
  
  
      
  
  
  
  </template>
  
  <script setup>
  import TarjetaMenu from '@/components/TarjetaMenu.vue';
  import { onMounted, ref, watch,nextTick  } from 'vue';
  import { useRoute } from 'vue-router';
  import { URI } from '../../service/conection';
  import router from '@/router/index.js';
  import { usecartStore } from '../../store/shoping_cart';
  import { useSitesStore } from '../../store/site';
  
  const store2 = usecartStore()
  const siteStore = useSitesStore()
  
  
  
  import { useReportesStore } from '../../store/ventas';
  const store = useReportesStore()
  const products = ref(store2.menu.data); // Definiendo la variable reactiva para almacenar los productos
  const route = useRoute(); // Usando useRoute para acceder a los parámetros de la route
  
  
  
  
  watch(
    () => route.params.categoria_id,
    async () => {
      // Limpia los productos actuales
      products.value = [];
      
      // Espera un segundo antes de asignar los nuevos productos
      setTimeout(() => {
        products.value = store2.menu.data;
      }, 1); // 1000ms = 1 segundo
    },
    { deep: true }
  );
  
  
  watch(
    () => store2.menu.data,
    async () => {
      // Limpia los productos actuales
      products.value = [];
      
      // Espera un segundo antes de asignar los nuevos productos
      setTimeout(() => {
        products.value = store2.menu.data;
      }, 1); // 1000ms = 1 segundo
    },
    { deep: true }
  );
  
  
  
  
  
  
  const getProductById = async (id) => {
  
          store.setLoading(true, 'cargando productos')
          try {
          let response = await fetch(`${URI}/product/${id}`);
          if (!response.ok) {
              store.setLoading(false, 'cargando')
  
              throw new Error(`HTTP error! status: ${response.status}`);
  
          }
          store.setLoading(false, 'cargando ')
  
          let data = await response.json();
         return data[0]
      } catch (error) {
          store.setLoading(false, 'cargando productos')
  
          console.error('Error fetching data: ', error);
      }
      
  }
     
  
  
  
  
  
  
  
  const getProducts = async (category_name) => {
      const site_id = siteStore.location.site.pe_site_id
      const category_id = route.params.category_id
      if(category_id && site_id){
          store.setLoading(true, 'cargando productos')
          try {
          let response = await fetch(`${URI}/get-product-integration/6149/${site_id}`);
          if (!response.ok) {
              store.setLoading(false, 'cargando productos')
  
              throw new Error(`HTTP error! status: ${response.status}`);
  
          }
          store.setLoading(false, 'cargando productos')
  
          let data = await response.json();
          products.value = data.data;
      } catch (error) {
          store.setLoading(false, 'cargando productos')
  
          console.error('Error fetching data: ', error);
      }
      }
  }
     
  
  
  
  const currentCity = ref(JSON.parse(localStorage.getItem('currentNeigborhood')));
  </script>
  
  <style scoped>
  
  
  
  
  </style>