<template>
  <div class="grid xl:mx-2 my-0 py-0 ">

    <DialogoPedido>

  </DialogoPedido>

    <div class="md:px-2 xl:pt-5 p-0 col-12 xl:col-4 top">

      <div class=" shadow-4 contenedor pb-2" style="overflow: hidden; background-color:#ffad53
">

        <div style="height: 85%;width: 100%;">
          <p class="col-12 text-center shadow-4 " style="background-color: #ffffff61;">
            <span class="text-center text-2xl" style="color: black;font-weight: bold;"> <i class="pi pi-envelope
 text-2xl"></i> RECIBIDOS</span>
          </p>


          <div style="height: 100%; overflow-y: auto;">

            <div class="px-3 py-2"
              v-for="orden in store.TodayOrders.filter(orden => orden.current_status == 'generada')">
              <OrderItem :order="orden"/>
            </div>
          </div>
        </div>





      </div>



    </div>



   <div class="md:px-2 xl:pt-5  p-0 col-12 xl:col-4 top">
      <div class=" shadow-4 contenedor pb-2" style="overflow: hidden; background-color:#8e3693
">
        <div style="height: 86%;width: 100%;">

          <p class="col-12 text-center shadow-4" style="background-color: #ffffff61;">
            <span class="text-center text-2xl" style="color: black;font-weight: bold;"> <i
                class="pi pi-clock text-2xl"></i>
              EN PREPARACION</span>
          </p>
          <div style="height: 100%; overflow-y: auto;">

            <div class="px-3 py-2"
            v-for="orden in store.TodayOrders.filter(orden => orden.current_status == 'en preparacion')">
              <OrderItem :order="orden"/>
            </div>
          </div>



        </div>
      </div>
    </div>


    <div class="md:px-2 xl:pt-5 p-0 col-12 xl:col-4 top">
      <div class=" shadow-4 contenedor pb-2" style="overflow: hidden; background-color:#00bf7a
">
        <div style="height: 100%;width: 100%;">


          <p class="col-12 text-center shadow-4" style="background-color: #ffffff61;">
            <span class="text-center text-2xl" style="color: black;font-weight: bold;"><i class="pi pi-send text-2xl
"></i> ENVIADOS</span>
          </p>
          <div style="height: 100%; overflow-y: auto;">

            <div class="px-3 py-2"
            v-for="orden in store.TodayOrders.filter(orden => orden.current_status == 'enviada')">
              <OrderItem :order="orden"/>
            </div>
          </div>



        </div>
      </div>
    </div>







  </div>


  <div :class="dialog_pedido_visible ? 'before' : ''"></div>
</template>

<script setup>

// import { gruposPedidos, obtenerHoraFormateadaAMPM, filtrarPedidosPorFecha, fecha_del_server, grupos, pedido, pedidos, ordenes_de_hoy, dialog_pedido_visible, set_dialog_order, filtrarPorEstado, open_order } from '@/service/un_pedido'
// import { URI } from '../../service/conection';
import DialogoPedido from './DialogoPedido.vue';
// import pedidoItem from '@/components/pedidoItem.vue';
import { onMounted, ref } from 'vue';
import OrderItem from './OrderItem.vue';
// import { orderService } from '../../service/orderService';
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


.contenedor{
  height: calc(100vh - 8rem);
  border-radius: 0.5rem;
}

.top{
  margin-top:0rem;
}

@media  ( max-width: 1200px)  {

  .contenedor{
    height: 1000%;
    min-height: 20vh;
    margin: 0;
    border-radius: 0;

  }
  .top{
  margin-top:1rem;
}
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