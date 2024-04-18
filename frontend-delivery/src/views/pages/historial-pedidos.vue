<template>
  <div class="grid m-auto" style="max-width: 700px;">

    <DialogoPedido>

  </DialogoPedido>

   

    <div class="md:p-3 my-2 p-0 col-12 m-0 ">
      <div class=" shadow-4" style="border-radius: 0.5rem;height: 80vh;overflow: hidden; background-color:#00bf7a
">
        <div style="height: 86%;width: 100%;">


          <p class="col-12 text-center shadow-4" style="background-color: #ffffff61;">
            <span class="text-center text-2xl" style="color: black;font-weight: bold;"><i class="pi pi-history
 text-2xl
"></i> PEDIDOS DE HOY</span>
          </p>
          <div style="height: 100%; overflow-y: auto;">

            <div class="px-3 py-2"
            v-for="orden in store.TodayOrders">
              <OrderItem :order="orden"/>
            </div>
          </div>



        </div>
      </div>
    </div>







  </div>


  <!-- <div :class="dialog_pedido_visible ? 'before' : ''"></div> -->
</template>

<script setup>

import DialogoPedido from './DialogoPedido.vue';
import { onMounted, ref } from 'vue';
import OrderItem from './OrderItem.vue';
import { useOrderStore } from '../../store/order';


const store = useOrderStore()


onMounted(() => {
  store.getTodayOrders()
})

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


.pedido {
  /* background-color: white; */
  border-radius: 0.5rem;
  overflow: hidden;
  background-color: rgba(255, 255, 255, 0.742);
  transition: .3s all ease
}

.pedido:hover {
  background-color: rgb(255, 255, 255);
  /* transform:  translateX(10px); */
}

.RECIBIDOS {

  background-color: rgba(246, 255, 0, 0.73)
}


.EN {

  background-color: rgba(66, 255, 255, 0.73)
}


.ENVIADOS {
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
  background-color: var(--primary-color);
  /* Color del pulgar de la barra de desplazamiento */
  border-radius: 9px;
  /* border: 5px solid var(--primary-color); */
  height: 10rem;
  width: 10rem;
  /* display: none;  */
}
</style>