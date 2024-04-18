<template>
  <div class="grid m-auto" style="max-width: 400px;">

    <DialogoPedido>

    </DialogoPedido>



    <div class=" my-2 p-2  m-0 " style="height: 80vh;overflow-y: auto;width: 100%; display: flex;align-items: center;">
     
        <div class="shadow-2 p-0 m-0" style="width: 100%;border-radius: 0.5rem;">


          <p class="col-12 text-center shadow-2" style="background-color: #ffffff61;">
                        <span class="text-center text-2xl" style="color: black;font-weight: bold;"><i class="pi pi-history
            text-2xl
            "></i> <b>
              CUADRE DE CAJA
            </b></span>
          </p>

          <p class="col-12 text-center p-0 my-0" style="background-color:#22c55e">
            <span class="text-center text-xl" style="color: black;font-weight: bold;"> Enviadas</span>
          </p>

          <div style="height: 100%; overflow-y: auto;">

            <div class="px-3 py-1" v-for="orden in store.TodayOrders.filter(order => order.current_status == 'enviada') ">
              <cuadreItem :order="orden" />
            </div>
          </div>


          <p class="col-12 text-center p-0 my-0" style="background-color:#ef4444">
            <span class="text-center text-xl" style="color: black;font-weight: bold;"> Canceladas</span>
          </p>

          <div style="height: 100%; overflow-y: auto;">

            <div class="px-3 py-1" v-for="orden in store.TodayOrders.filter(order => order.current_status == 'cancelada')">
              <cuadreItem :order="orden" />
            </div>
          </div>


          <p class="col-12 text-center text-white p-0 my-0" style="background-color:#000000;color: white;">
            <span class="text-center text-xl" style="color: rgb(255, 255, 255);font-weight: bold;"> Resumen</span>
          </p>




   <div class="px-3 py-2 text-2xl" style="display: flex;font-weight: bold; align-items: center;justify-content: space-between;">
            <div style=" display: flex;align-items: center;">
                <b style="min-width: max-content;color: black;">
        CUADRE
            </b>


            </div>

            
            
          
            
            
                <b style="color:black">
                    {{formatoPesosColombianos(totalEnviadas)  }}

                </b>
                
       
           

          

    
            
            
        </div>
        




        </div>
    
    </div>







  </div>


  <!-- <div :class="dialog_pedido_visible ? 'before' : ''"></div> -->
</template>

<script setup>


import DialogoPedido from './DialogoPedido.vue';

import { onMounted} from 'vue';
import { useOrderStore } from '../../store/order';
import cuadreItem from './cuadreItem.vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
const store = useOrderStore()


import { computed } from 'vue';

const totalEnviadas = computed(() => {
  return store.TodayOrders.filter(order => order.current_status === 'enviada')
                          .reduce((total, order) => total + order.total_order_price, 0);
});

onMounted(() => {
  store.getTodayOrders()
})

</script>
