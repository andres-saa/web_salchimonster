<template>


         
<div class="grid px-3 pb-8" style="max-width: 1024px;margin: auto; position:relative;" >



  <!-- <Dialog class="p-0 m-0"  v-model:visible="store.visible.show_new_product" modal style="width: 30rem;padding: 0;"> 
    <div style="max-width: 30rem;background-color: white;color: black;border-radius: .5rem;" class="">
      <TarjetaMenuDialog :product="{ id: 241,product_id: 118,    site_id: 11,    status: true,    price: 10000,    product_name: 'CHOCOMONSTER',    product_description:' CHOCORRAMO APANADO',    category_id: 14,    category_name: 'NUEVOS'}"> </TarjetaMenuDialog>
    </div>
  </Dialog> -->




  <div  style="position:absolute;display:flex;right:100%;gap:10rem; height:100vh;max-width:100%; justify-content:space-around; flex-direction:column;z-index: 9;">

<!-- <img style="width:15vw;" v-for="character in [1,2,3,4,5]" :src="`/images/characters/line/${character}.png`" alt=""> -->

</div>


<!-- <div  style="position:absolute;display:flex;left:100%;gap:10rem; height:100vh;max-width:100%; justify-content:space-around; flex-direction:column;z-index: 9;">

<img style="width:15vw;" v-for="character in [1,2,3,4,5].reverse()" :src="`/images/characters/line/${character}.png`" alt="">

</div> -->




<p class="text-center text-3xl col-12 my-7" style="font-weight: bold;display: flex;border-radius:  1rem  1rem; gap: 1rem;align-items: center;background-color: red; justify-content: center;">
  <!-- <div style="width: 100%;height: 5px; background-color: #ff6200">

  </div > -->


    <h2 class="m-0 text-white">
      <i class="fa-solid fa-drumstick-bite text-white"></i>
      <b>
        POLLO
      </b>
          
    </h2>

    <!-- <div style="width: 100%;height: 5px; background-color:#ff6200"> -->

<!-- </div> -->
    
</p>

<div v-for="(product, index) in products" :key="product.id" class=" col-12   md:col-6 lg:col-4 ">

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
import TarjetaMenuDialog from '../../components/TarjetaMenuDialog.vue';
const store2 = usecartStore()
const siteStore = useSitesStore()

import { useReportesStore } from '../../store/ventas';
const store = useReportesStore()
const products = ref([]); // Definiendo la variable reactiva para almacenar los productos
const route = useRoute(); // Usando useRoute para acceder a los parámetros de la route



onMounted(async () => {
  getProducts();
  await nextTick();
});

watch(() => route.params.category_id, async () => {
  if(route.params.category_id){
      getProducts();
  await nextTick(); 
  }
},{deep:true});



const getProducts = async (category_name) => {
  const site_id = siteStore.location.site.site_id
  const category_id = 12
  if(category_id && site_id){
      store.setLoading(true, 'cargando productos')
      try {
      let response = await fetch(`${URI}/products-active/category-id/${category_id}/site/${site_id}`);
      if (!response.ok) {
          store.setLoading(false, 'cargando productos')

          throw new Error(`HTTP error! status: ${response.status}`);

      }
      store.setLoading(false, 'cargando productos')

      let data = await response.json();
      products.value = data;
  } catch (error) {
      store.setLoading(false, 'cargando productos')

      console.error('Error fetching data: ', error);
  }
}
  }
 







  
const getProductBy_id = async (category_name) => {
  const site_id = siteStore.location.site.site_id
  const category_id = 3
      try {
      let response = await fetch(`${URI}/products-active/category-id/${category_id}/site/${site_id}`);
      if (!response.ok) {
          store.setLoading(false, 'cargando productos')

          throw new Error(`HTTP error! status: ${response.status}`);

      }
      store.setLoading(false, 'cargando productos')

      let data = await response.json();
      products.value = data;
  } catch (error) {
      store.setLoading(false, 'cargando productos')

      console.error('Error fetching data: ', error);
  }
}
  













// Opcional: Observar cambios en el parámetro de la rou


const currentCity = ref(JSON.parse(localStorage.getItem('currentNeigborhood')));
</script>

