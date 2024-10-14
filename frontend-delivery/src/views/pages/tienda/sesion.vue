



<template>


<div style="position:sticky; left: 3rem; top: 8rem;display: flex; width:max-content; gap:1rem;padding-left: 2rem;padding-top: 1rem; z-index: 900;background-color: white;">
             <div @click="set_restaurant(i.id)" v-for=" i in restaurants" style="cursor: pointer;">
                    <img style="width: 3rem;" :src="i.logo" alt="">
             </div>
        </div>  
    

    <div class="grid p-1 pb-8" style="max-width: 1024px;margin: auto; position: relative;" >
    


    <p class="text-center text-3xl col-12" style="font-weight: bold;display: flex;gap: 1rem;align-items: center;">
      <div style="width: 100%;height: 5px; background-color: #ff6200">
    
      </div>
      {{ route.params.menu_name }}
    
        <div style="width: 100%;height: 5px; background-color:#ff6200">
    
    </div>
        
    </p>
    
    
        <div v-for="(product, index) in products" :key="product.id" class=" col-12 md:col-4 lg:col-3 sm:col-6">
    
                <TarjetaMenu style="width: 100%;" :id="`tarjeta-${index}`"  :product="product"></TarjetaMenu>
        </div>
    
    


  
    
    
    </div>
    
    

    
</template>

<script setup>
import { onMounted,ref,watch } from 'vue'
import {productService} from '../../../service/ProductService'
import TarjetaMenu from '@/components/TarjetaMenu.vue'
import { useRoute } from 'vue-router'
import { useSitesStore } from '../../../store/site'

const siteStore = useSitesStore()
const route = useRoute()
const products = ref([])

const restaurants = ref([
    {
        name:'SALCHIMONSTER',
        id:1,
        logo:'/images/logo.png'
    },
    {
        name:'BURGUERMONSTER',
        id:4,
        logo:'https://papasmonster.com/images/LOGO.png'
    },
    {
        name:'PAPASMONSTER',
        id:2,
        logo:'https://burgermonsterr.com/images/LOGO.png'
    }
])



const set_restaurant = (restaurant_id) => {

    siteStore.restaurant_id = restaurant_id
    // getProducts()
}




onMounted( async () => {
    getProducts()
})



watch(() => siteStore.restaurant_id, async() => {
    products.value = []
} )


const getProducts = async()=> {
    const category_id = route.params.category_id
    const site_id = siteStore.site.site_id
    products.value = await productService.getProductsByCategorySite(category_id,site_id)
}

watch(() => route.params.category_id, async () => {
    if(route.params.category_id){
        getProducts();
    }
},{deep:true});

</script>