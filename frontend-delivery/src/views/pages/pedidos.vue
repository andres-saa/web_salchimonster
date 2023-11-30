<template>
  <div style="" class="grid  p-0">
    <div v-for=" estado in grupos" class="col-12 lg:col-6 xl:col-4 p-3" style="" > 
 
      <div  class="col-12 mb" :class="estado.name.split(' ')[0]" 
        style=";border-radius: 1rem; box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.3);">

        <div class="col-12 m-0 mb-3" style="background-color: rgba(255, 255, 255, 0.493); border-radius: 0.5rem;" ><span class="text-2xl m-auto col-12"
            style="font-weight: bold;"> {{ estado.name }}</span></div>
 

        <div class="col-12 p-0" style="height: 60vh;overflow-y: auto;">


          <div class="col-12 p-0 " v-for="order in filtrarPorEstado(pedidos,estado.order_status)   " style=""  @click="open_order(order)">

            <div class="col-12  " >

              <div class=" grid p-2 pedido " style=";color:white;cursor: pointer;">

                <div class="" v-for="product in order.order_products.slice(0,4)"  >
                
                <!-- {{ product.img_96x96 }} -->
                <img class="p-1" style=" width: 60px; height: 60px; object-fit: contain;" :src="`${URI}/read_product_image/96/${product.id}`" alt="">
               
                
                </div>

              <i v-if="estado.order_status == 'en preparacion'" class="pi pi-spin pi-spinner p-3" style="font-size: 3rem;color: var(--primary-color);font-weight: bold;"></i>
              <i v-if="estado.order_status == 'enviada'" class="pi pi-check p-3" style="font-size: 3rem;color: var(--primary-color);font-weight: bold;"></i>
              <i v-if="estado.order_status == 'generada'" class="pi pi-star-fill p-3" style="font-size: 3rem;color: var(--primary-color);font-weight: bold;"></i>

              
              <span class="col text-right" style="color: black; font-weight: bold; min-width: max-content;">{{order.order_id}}</span>
              <!-- {{ order.order_status.timestamp.split(' ')[1] }} -->
              



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
  transition: .3s all ease

}

.pedido:hover{
    background-color: rgb(255, 255, 255);
    /* transform:  translateX(10px); */
}

.RECIBIDOS{

  background-color: rgba(246, 255, 0, 0.73)
}


.EN{

background-color: rgba(66, 255, 255, 0.73)
}


.ENVIADOS{
  background-color: rgba(123, 255, 66, 0.73)

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