<script setup>
import { ref, onMounted } from 'vue';
import ProductService from '@/service/ProductService';
import { URI } from "@/service/conection.js"
import { useRouter } from 'vue-router';
import router from '@/router';
import {
    sitesDropValues,
    curentSite,

    getSites

} from '@/service/dropDownAux';

const navigateToSite = (siteData) => {
    localStorage.setItem('currentSiteFiles', JSON.stringify(siteData));
    router.push(`/site/${siteData.site_id}`);
};

const dataviewValue = ref(null);
const layout = ref('grid');
const sortKey = ref(null);
const sortOrder = ref(null);
const sortField = ref(null);

const productService = new ProductService();

onMounted(() => {
    productService.getProductsSmall().then((data) => (dataviewValue.value = data));
    getSites()
});

</script>

<template>
    <div class="grid">
        <div class="col-12 m-auto" style="max-width: 1280px;">
            <div class="">
                
                <div class="my-2 col-12">
                    <p style="font-weight: bold; color: black;" class="text-4xl pl-0 ml-0">Administrar recibos y documentacion</p>

                </div>
                
                <DataView :value="sitesDropValues" :layout="layout" :paginator="true" :rows="9" :sortOrder="sortOrder"
                    :sortField="sortField">
                    
                    <template #grid="slotProps">
                        
                        <div class="col-12 lg:col-4 md:col-6">
                            <div @click="navigateToSite(slotProps.data)">
                                <div class=" m-4      container-">
                                    <div class="text-center cont-img-sede">
                                        <div class="nombre-sede-cont">
                                            <AvatarGroup class="mb-3 avatar">
                                                <Avatar :image="'demo/images/avatar/amyelsner.png'" size="large"
                                                    shape="circle">
                                                </Avatar>
                                                <Avatar :image="'demo/images/avatar/asiyajavayant.png'" size="large"
                                                    shape="circle"></Avatar>
                                                <Avatar :image="'demo/images/avatar/onyamalimba.png'" size="large"
                                                    shape="circle"></Avatar>
                                                <Avatar :image="'demo/images/avatar/ionibowcher.png'" size="large"
                                                    shape="circle"></Avatar>
                                                <Avatar :image="'demo/images/avatar/xuxuefeng.png'" size="large"
                                                    shape="circle">
                                                </Avatar>
                                                <Avatar label="+2" shape="circle" size="large" :style="{ color: '#ffffff' }"
                                                    style="background-color: var(--primary-color);"></Avatar>
                                            </AvatarGroup>
                                            <div class="text-5xl font-bold text-white nombre-sede">
                                                <p style="width: 100%;">
                                                    {{ slotProps.data.site_name }}
                                                </p>
                                            </div>
                                        </div>
                                        <img :src="`${URI}/read-product-image/300/site-${slotProps.data.site_id}`"
                                            class="w-12   imagen" />
                                    </div>
                                    <div class="flex align-items-center justify-content-between">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </template>
                </DataView>

            </div>
        </div>
    </div>
</template>


<style scoped>
button {
    border: none;
}

.container-card {
    /* background-color: ;
 */
    padding: 0;
}

.nombre-sede {
    width: 100%;
    display: flex;
    align-items: center;

}

.nombre-sede-cont {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 1rem;
    justify-content: center;
}

.nombre-sede-cont:hover {
    opacity: 0;
    transition: all .3s ease;
}



.nombre-sede-cont:hover+.imagen {
    transition: all .3s ease;
    box-shadow: 1px 1px 50px var(--primary-color);
    z-index: -1;
    /* border-radius: 3rem; */
}

.cont-img-sede {
    position: relative;
    border: none;
    /* border-radius: 3rem; */


}



.imagen {
    width: 100%;
    height: 33vh;
    padding: 5px;
    border-radius: 1rem;
    object-fit: cover;
    transition: .3s ease;

}

p:hover {}

.imagen:hover {


    scale: 1.1;

}
</style>