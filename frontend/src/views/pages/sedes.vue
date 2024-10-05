

<template>
<div class="grid col-12 lg:col-10 m-auto p-3 my-5" style="max-width: 1024px">

    
    




    <div 
        v-for="sede in sedes.filter(sede => sede.city_id && sede.show_on_web && !sede.comming_soon)" 
        style="border-radius: 0.5rem; overflow: hidden;" 
        class="col-12 lg:col-6 p-0 mb-3 lg:px-2 m-0"
    >
        <div class="col-12 p-0 m-0 shadow-3" style="position: relative;overflow: hidden;height: min-content;box-shadow: 0 0 10px black; border-radius: 0.5rem;">
            <img
            :src="currentImage(sede.site_id)"
            @load="loadHighResImage(sede.site_id)"
            :style="{
                objectFit: 'cover',
                borderRadius: '0.5rem',
                width: '100%',
                height: '30rem',
                transition: 'opacity 0.5s ease-in-out',
           
            }"
            alt=""
        />
            <div 
                class="xl:pl-4 pl-2" 
                style="width: 100%;height: 40%;background: linear-gradient(to top, black, transparent);position: absolute; display: flex; flex-direction: column; justify-content: end;left: 0;bottom: 0;border-radius:0 0 0.5rem 0.5rem;"
            >
                <p class="xl:text-xl text-l m-0 " style="font-weight: bold; color:var(--primary-color)">
                    <span class="pr-4" style="text-transform: uppercase;">
                        <i :class="PrimeIcons.MAP_MARKER" style="color: var(--primary-color); font-weight: bold;"></i>
                    </span>
                    {{cities?.filter(s => sede.city_id == s.city_id )[0]?.city_name}} 
                    <span style="font-weight: normal; padding-left: 1rem; color: white;">{{ sede.site_address }}</span> 
                    <p style="color: white;">SALCHIMONSTER {{sede.site_name}}</p>
                </p>
                <p class="xl:text-xl text-l" style="font-weight:normal; color:white">
                    <span class="pr-4">
                        <i class="text-l p-0" :class="PrimeIcons.WHATSAPP" style="font-weight: bold; color: rgb(58, 255, 58);"></i>
                    </span>
                    {{ sede.site_phone }}
                </p>
                <div style="position: absolute; right: 0rem; width: 5rem;height: 5rem;bottom: 0; background-color:transparent;display: flex; padding: 1rem;">
                    <a :href="sede.maps" style="position:relative;">
                        <img style="width: 100%; height: 100%; background-color: rebeccapurple; border-radius: 0.5rem;" src="https://th.bing.com/th/id/R.68201495ac2d0c4d1cd3cbf6d25f6755?rik=l%2bilUrRDF30tdw&pid=ImgRaw&r=0"/>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

</template>

<script setup>


import { onMounted, ref } from 'vue';
import { PrimeIcons } from 'primevue/api';
import { URI } from "@/service/conection"


const highResLoaded = ref({});
    const currentImageSrc = ref({}); // Objeto para mantener la imagen actual de cada sede

    const lowResImage = (site_id) => `${URI}/read-product-image/96/site-${site_id}`;
    const highResImage = (site_id) => `${URI}/read-product-image/600/site-${site_id}`;

    const currentImage = (site_id) => {
      return currentImageSrc.value[site_id] || lowResImage(site_id);
    };

    const loadHighResImage = (site_id) => {
      const img = new Image();
      img.src = highResImage(site_id);
      img.onload = () => {
        currentImageSrc.value[site_id] = highResImage(site_id); // Reemplaza el src de la imagen cuando está completamente cargada
        highResLoaded.value[site_id] = true;
      };
    };


const sedes  = ref([])
const cities = ref([])

onMounted(() => getSites().then(data => sedes.value = data))
onMounted(() => getcies().then(data => cities.value = data))




const getSites = async(site_id) => {
    try {
        // spinnersView.value.barrio = true
     const response = await fetch(`${URI}/sites`)
     if(response.ok){
        const data = await response.json()
        // cities.value = data
        // spinnersView.value.barrio = false

        return data
     }
     
   } catch (error) {
    // spinnersView.value.barrio = false

    
   }
}




const getcies = async() => {
    try {
        // spinnersView.value.barrio = true
     const response = await fetch(`${URI}/cities`)
     if(response.ok){
        const data = await response.json()
        // cities.value = data
        // spinnersView.value.barrio = false

        return data
     }
     
   } catch (error) {
    // spinnersView.value.barrio = false

    
   }
}
</script>


<style scoped>

*{
    text-transform: uppercase
}


</style>