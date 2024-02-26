<template>
  <div style="max-width: 600px" class="grid col-12  m-auto m-0 p-0" >
    <div  class="col-12 p-0" style="" > 
 
      <div  class="col-12 mb-6 m-0 pb-0" 
        style=";border-radius: 1rem; box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.3);overflow:hidden">

        
 

       


          <div class=" col-12  p-0 " v-for="order in pedidos   " style="border-radius: 40rem"  @click="open_order(order)" :class="order.order_status.status.split(' ')[0]">

        

            <div class="col-12 mb-3 p-0" >

              <div class=" grid  pedido  " style=";color:white;cursor: pointer;">

      

               
              <span class="col"  style="color: black; font-weight: bold; min-width: max-content;"> ORDEN # {{ order.order_id}}</span>
              <div class="col py-0 m-0" style="display: flex; justify-content:end;align-items: center; ">
                <i v-if="order.order_status.status == 'en preparacion'"  class="pi pi-spin pi-spinner p-0 mr-3" style="font-size: 2rem;color: var(--primary-color);font-weight: bold;"></i>
                <i v-if="order.order_status.status == 'enviada'" class="pi  pi-check tex-l mr-3" style="font-size: 2rem;color: var(--primary-color);font-weight: bold;"></i>
                <i v-if="order.order_status.status == 'generada'" class="pi pi-star-fill p-0 mr-3" style="font-size: 2rem;color: var(--primary-color);font-weight: bold;"></i>
                <i v-if="order.order_status.status == 'cancelada'" class="pi pi-times p-0 mr-3" style="font-size: 2rem;color: var(--primary-color);font-weight: bold;"></i>

                
                <div class="py-1 px-2 text-center " style="border-radius: 50rem;min-width: 80px; color: black; width: max-content;" :class="order.order_status.status.split(' ')[0]" > {{order.order_status.status}} </div>
                
              </div>
              
              



                <!-- <div class="col-" style="background-color: rgb(172, 172, 255);"></div> -->


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
  border-radius:20rem;overflow: hidden;background-color: rgba(255, 255, 255, 0.742);
  transition: .3s all ease;
  padding:0; margin: 0;
  outline: 2px solid rgb(255, 255, 255);

}

.pedido:hover{
    background-color: rgb(255, 255, 255);
    outline: 2px solid red;
    /* transform:  translateX(10px); */
}

.RECIBIDOS{

  background-color: rgba(252, 255, 179, 0.73)
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
  background-color: rgba(255, 160, 160, 0.73);
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