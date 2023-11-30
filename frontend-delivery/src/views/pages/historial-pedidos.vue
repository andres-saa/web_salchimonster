<template>
  <div style="" class="grid col-12 m-0 p-0" >
    <div  class="col p-0" style="" > 
 
      <div  class="col-12 mb-6 m-0 pb-0" 
        style=";border-radius: 1rem; box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.3);overflow:hidden">

        
 

        <div class=" p-0 grid ">


          <div class=" col-12 xl:col-6 p-0 " v-for="order in pedidos   " style=""  @click="open_order(order)" :class="order.order_status.status.split(' ')[0]">

        

            <div class="col-12  " >

              <div class=" grid p-2 pedido " style=";color:white;cursor: pointer;">

                <div class="" v-for="product in order.order_products"  >
                
                <!-- {{ product.img_96x96 }} -->
                <img class="p-1" style=" width: 60px; height: 60px; object-fit: contain;" :src="`${URI}/read_product_image/96/${product.id}`" alt="">
               
                
                </div>

              <!-- <i v-if="estado.order_status == 'en preparacion'" class="pi pi-spin pi-spinner p-3" style="font-size: 3rem;color: var(--primary-color);font-weight: bold;"></i> -->

              

               
     
              <div class="col " style="display: flex; justify-content:end;align-items: center;gap: 1rem; ">
                <i v-if="order.order_status.status == 'en preparacion'"  class="pi pi-spin pi-spinner p-3" style="font-size: 3rem;color: var(--primary-color);font-weight: bold;"></i>
                <i v-if="order.order_status.status == 'enviada'" class="pi pi-check p-3" style="font-size: 3rem;color: var(--primary-color);font-weight: bold;"></i>
                <i v-if="order.order_status.status == 'generada'" class="pi pi-star-fill p-3" style="font-size: 3rem;color: var(--primary-color);font-weight: bold;"></i>
                <i v-if="order.order_status.status == 'cancelada'" class="pi pi-times p-3" style="font-size: 3rem;color: var(--primary-color);font-weight: bold;"></i>

                
                <div class="p-2" style="border-radius: 2rem; color: black; width: max-content;" :class="order.order_status.status.split(' ')[0]" > {{order.order_status.status}} </div>
                <span  style="color: black; font-weight: bold; min-width: max-content;">{{ order.order_id}}</span>
              </div>
              
              



                <!-- <div class="col-" style="background-color: rgb(172, 172, 255);"></div> -->


              </div>

            </div>

          </div>
        </div>


      </div>

    </div>
  </div>

  <DialogoPedido>

  </DialogoPedido>


  <div :class="dialog_pedido_visible ? 'before' : ''"></div>
</template>

<script setup>

import {gruposPedidos, grupos, pedido, pedidos, dialog_pedido_visible,set_dialog_order,filtrarPorEstado } from '@/service/un_pedido'
import { URI } from '../../service/conection';
import DialogoPedido from './dialogo-pedido.vue';

const open_order = (order) => {
  set_dialog_order(order)
  dialog_pedido_visible.value = !dialog_pedido_visible.value
}




</script>

<style scoped>
.texto-negro {
  color: black;
}

.before {
  background-color: rgba(0, 0, 0, 0.8);
  width: 100vw;
  height: 100vh;
  z-index: 999;
  position: absolute;
  top: 0;
  left: 0;
  transform: scale(2);
}


.pedido{
  /* background-color: white; */
  border-radius: 0.5rem;overflow: hidden;background-color: rgba(255, 255, 255, 0.742);
  transition: .3s all ease;
  padding:0; margin: 0;

}

.pedido:hover{
    background-color: rgb(255, 255, 255);
    /* transform:  translateX(10px); */
}

.RECIBIDOS{

  background-color: rgba(246, 255, 0, 0.73)
}


.en{

background-color: rgba(66, 255, 255, 0.73)
}


.ENVIADOS{
  background-color: rgba(123, 255, 66, 0.73)

}

.enviada{
  background-color: rgba(123, 255, 66, 0.73);
  /* border: 2px solid red; */
  

}

.cancelada{
  background-color: rgba(255, 66, 66, 0.73);
  /* border: 2px solid red; */
  

}

.generada{
  background-color: rgba(246, 255, 0, 0.73)

}

::-webkit-scrollbar {
    width: 0.5rem;
    /* Ancho de la barra de desplazamiento */
    padding-top: 1rem;
    position: absolute;
    /* display: none; */
}

.clase {}

/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {
    background-color:var(--primary-color);
    /* Color del pulgar de la barra de desplazamiento */
    border-radius: 9px;
    /* border: 5px solid var(--primary-color); */
    height: 10rem;
    width: 10rem;
    /* display: none;  */
}
</style>