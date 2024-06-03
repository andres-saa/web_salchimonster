<template>
        <div v-if="store.visibleNotifications" class="card col-12 xl:col-3 mt-3 m-0 notificaciones"  :style="store.visibleNotifications? 'transform:scaleX(100%)':'transform:scaleX(100%);'" >
        <div class=""  >
            <div  class="flex align-items-center justify-content-between mb-4">
                <h5>Notificaciones</h5>
                <div>
                    <Button icon="pi pi-ellipsis-v" class="p-button-text p-button-plain p-button-rounded"
                        @click="$refs.menu1.toggle($event)"></Button>
                    <Menu ref="menu1" :popup="true" :model="items"></Menu>
                </div>
            </div>

            <span class="block text-600 font-medium mb-3">Sedes en linea</span>
            <ul style="height: 100%; overflow-y: auto;" class="p-0 mx-0 mt-0 mb-4 list-none">
                <li style="display: flex; align-items: center; justify-content: space-between;" v-for="sede in store.sitesStatus.filter(s => s.online_status)" class="flex align-items-center py-2 border-bottom-1 surface-border">
                    <div style="display: flex; align-items: center;" class=" p-0">
                        <div
                        class="w-2rem h-2rem flex align-items-center justify-content-center bg-blue-100 border-circle mr-3 flex-shrink-0">
                        <img style="width: 100%;border-radius: 0.5rem; object-fit: cover; aspect-ratio: 1 / 1;" :src="`${URI}/read-product-image/96/site-${sede.id}`" alt="">
                    </div>
                    <span class="text-900 line-height-3">{{ sede.site_name }}
                        
                    </span>
                    </div>

                    <Button style="width:0.5rem; aspect-ratio:  1 / 1;" rounded=""  class="p-0 mr-3 indicador" severity="success"></Button>
                    
                    
                </li>
                <!-- <li class="flex align-items-center py-2">
                    <div
                        class="w-3rem h-3rem flex align-items-center justify-content-center bg-orange-100 border-circle mr-3 flex-shrink-0">
                        <i class="pi pi-download text-xl text-orange-500"></i>
                    </div>
                    <span class="text-700 line-height-3">Your request for withdrawal of <span
                            class="text-blue-500 font-medium">2500$</span> has been initiated.</span>
                </li> -->
            </ul>

            <span class="block text-600 font-medium mb-3">Sedes desconectadas</span>
            <ul style="height: 100% overflow-y: auto;" class="p-0 mx-0 mt-0 mb-4 list-none">
                <li style=" display: flex; align-items: center; justify-content: space-between;" v-for="sede in store.sitesStatus.filter(s => !s.online_status)" class="flex align-items-center py-2 border-bottom-1 surface-border">
                    <div style="display: flex; align-items: center;" class=" p-0">
                        <div
                        class="w-2rem h-2rem flex align-items-center justify-content-center bg-blue-100 border-circle mr-3 flex-shrink-0">
                        <img style="width: 100%;border-radius: 0.5rem; object-fit: cover; aspect-ratio: 1 / 1;" :src="`${URI}/read-product-image/96/site-${sede.id}`" alt="">



                        <!-- {{ sede.id }} -->
                        
                    </div>
                    <span class="text-900 line-height-3">{{sede.site_name}}
                        
                    </span>
                    </div>

                    <Button style="width:0.5rem; aspect-ratio:  1 / 1;" rounded=""  class="p-0 mr-3 indicador" severity="danger"></Button>
                    
                    
                </li>
                <!-- <li class="flex align-items-center py-2">
                    <div
                        class="w-3rem h-3rem flex align-items-center justify-content-center bg-orange-100 border-circle mr-3 flex-shrink-0">
                        <i class="pi pi-download text-xl text-orange-500"></i>
                    </div>
                    <span class="text-700 line-height-3">Your request for withdrawal of <span
                            class="text-blue-500 font-medium">2500$</span> has been initiated.</span>
                </li> -->
            </ul>

           
        </div>
    </div>
</template>



<script setup>












import { onMounted, reactive, ref, watch } from 'vue';
// import ProductService from '@/service/ProductService';
import { useLayout } from '@/layout/composables/layout';
import { useRoute } from 'vue-router';
import { URI } from '../../service/conection';
import {salesReport} from '../../service/valoresReactivosCompartidos'
import {useReportesStore} from '@/store/reportes.js'

const store = useReportesStore()


onMounted(() =>{
    store.startSitesStatusUpdate()

})



</script>

<style scoped>


@keyframes flash {
from { opacity: 1;transform: scale(1.5) }	
to { opacity: 0; ; }
}


.indicador {
  animation: flash .2s ease infinite alternate;
}
</style>