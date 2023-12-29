<template>



<div class="mb-6" style="background-color: rgb(255, 255, 255);position: sticky; top:4rem;z-index: 9999;z-index: 9999;">
    <div class="col-12 m-auto" style="max-width: 1024px;  background-color: white;">

<p class="text-4xl text-center py-4" style="font-weight: bold;">Consultar estado de mi pedidio</p>
<span class="a4-size mb-6" style="display: flex; height: auto;">


<InputNumber v-model="order_id"  class="mr-5 px-2" style="width: 100%; " placeholder="Numero de pedido"></InputNumber>
<Button class="px-4" style="background-color: var(--primary-color); font-weight: bold; border: none;" @click="getOrder()">Buscar</Button>




</span>




<p class="text-2xl estado" v-if="order.order_status?.status == 'enviada'" style="text-transform: lowercase;"> 
    
    El pedido fue enviado a su domicilio  a las {{ obtenerHoraFormateadaAMPM(order.order_status.timestamp) }}

</p>


<p class="text-2xl estado" v-if="order.order_status?.status == 'en preparacion'" style="text-transform: lowercase;"> 
    
    El pedido esta en preparacion desde las  {{ obtenerHoraFormateadaAMPM(order.order_status.timestamp) }} y ser'a enviada en breve

</p>


<p class="text-2xl estado" v-if="order.order_status?.status == 'generada'" style="text-transform: lowercase;"> 
    
    Hemos recibido su pedido a las  {{ obtenerHoraFormateadaAMPM(order.order_status.timestamp) }} y empezaremos a prepararlo en breve, gracias por su esperar

</p>

<div class="col-12 m-auto p-0">
 <!-- hola {{ order.order_status.status }}  -->
 
 
 <pedidoItem class="p-6" style="max-width: 1024px;  border-radius: 1rem;" v-if="order.order_status" :order="order" :estado="order.order_status?.status" :class="order.order_status.status.split('-')[0]"></pedidoItem>


 
 </div>
</div>


</div>






<!-- <BarraCategorias></BarraCategorias> -->
<Sesion_main ></Sesion_main>





</template>

<script setup> 

import { ref } from 'vue';
import Sesion_admin from './sesion_admin.vue';
import Sesion_main from './sesion_main.vue';
import pedidoItem from '../../components/pedidoItem.vue';
import { URI } from '../../service/conection';


const order = ref({status:''})
const order_id= ref()
const mensaje = ref()
const serverDate = ref("2029-12-21 16:19")
const queja = ref()




const getOrder = async() => {
    fetch(`${URI}/order/${order_id.value}`)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    
    return response.json();
  })
  .then(data => {
    console.log('Employer data:', data);
    order.value = data
    queja.value = ''
    determinarMensaje()
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
    order.value = {}
    queja.value = '  No hay un usuario para el número de documento '+ order_id.value
    // mensaje.value = 'error'
  });
}


const obtenerHoraFormateadaAMPM = (fecha) => {
  const fechaParseada = new Date(fecha);
  const horas = fechaParseada.getHours();
  const minutos = fechaParseada.getMinutes();
  const ampm = horas >= 12 ? 'pm' : 'am';
  const hora12 = horas % 12 || 12;
  const horaFormateada = hora12 < 10 ? '0' + hora12 : hora12;
  const minutosFormateados = minutos < 10 ? '0' + minutos : minutos;

  return `${horaFormateada}:${minutosFormateados} ${ampm}`;
};

const determinarMensaje =   () => {

    if( !order.order_status) {
    return
    }


    order.value.order_status?.status == 'enviada'? mensaje.value = 'env':''
}

</script>


<style scoped>

.generada{
    background-color: rgba(255, 255, 0, 0.804);
}
.enviada{
    background-color: rgb(153, 255, 0);
}

.en{
    background-color: rgb(84, 212, 255);
}


.cancelada{
    background-color: rgb(255, 84, 84);
}


.estado::first-letter{
    text-transform: capitalize;
}

</style>