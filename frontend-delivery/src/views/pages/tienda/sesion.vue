<template>
    

    <div class="grid p-1 pb-8" style="max-width: 1024px;margin: auto;" >
    
    
    
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



onMounted( async () => {
    getProducts()
})


const getProducts = async()=> {
    const category_id = route.params.category_id
    const site_id = siteStore.site.site_id
    products.value = await productService.getProductsByCategorySite(category_id,site_id)
}

watch(() => route.params.category_id, async () => {
    if(route.params.category_id){
        getProducts();
    await nextTick(); 
    }
},{deep:true});

</script>