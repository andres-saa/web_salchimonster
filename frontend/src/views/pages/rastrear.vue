<template>



<div class="mb-6" style="background-color: rgb(255, 255, 255);position: sticky; top:4rem;z-index: 9999;z-index: 9999;">
    <div class="col-12 m-auto" style="max-width: 1024px;  background-color: white;">

<p class="text-4xl text-center py-4" style="font-weight: bold;">Consultar estado de mi pedido</p>
<span class="a4-size mb-6" style="display: flex; height: auto;">


  <div style="display:  flex; justify-content: space-between;width: 100%;gap: 1rem;">
    <InputText v-model="order_id"  class=" px-2" style="width: 100%; " placeholder="Numero de pedido"></InputText>
    <Button  label="Buscar" class="px-4" style="background-color: var(--primary-color); font-weight: bold;min-width: max-content; border: none;" @click="getOrder()"></Button>
  </div>

</span>




<p class="text-2xl estado" :class="order?.status" v-if="order?.status == 'enviada'" style="text-transform: lowercase;"> 
    
    El pedido fue enviado a su domicilio  a las {{ obtenerHoraFormateadaAMPM(order?.timestamp) }}

</p>


<p class="text-2xl estado" :class="order?.status" v-if="order?.status == 'cancelada'" style="text-transform: lowercase;"> 
    
    El pedido fue cancelado a las {{ obtenerHoraFormateadaAMPM(order?.timestamp) }}
    <br><b>responsable</b>: {{ order.responsible }}
    <br><b>Razon</b>: {{ order.reason }}

</p>

<p class="text-2xl estado" :class="order?.status" v-if="order?.status == 'en preparacion'" style="text-transform: lowercase;"> 
    
    El pedido esta en preparacion desde las  {{ obtenerHoraFormateadaAMPM(order?.timestamp) }} y ser'a enviada en breve

</p>


<p class="text-2xl estado" :class="order?.status" v-if="order?.status == 'generada'" style="text-transform: lowercase;"> 
    
    Hemos recibido su pedido a las  {{ obtenerHoraFormateadaAMPM(order?.timestamp) }} y empezaremos a prepararlo en breve, gracias por su esperar

</p>


<p class="text-2xl estado" :class="order?.status" v-if="!order.status" style="text-transform: lowercase;"> 
    
    Este pedido no existe en nuestra base de datos

</p>

<div class="col-12 m-auto p-0">
 <!-- hola {{ order.order_status.status }}  -->
 
 

 
 </div>
</div>


</div>




</template>

<script setup> 

import { ref,onMounted } from 'vue';
import Sesion_main from './sesion_main.vue';
import pedidoItem from '../../components/pedidoItem.vue';
import { URI } from '../../service/conection';
import { usecartStore } from '@/store/shoping_cart';


const order = ref({status:'false'})
const order_id= ref()
const mensaje = ref()
const serverDate = ref("2029-12-21 16:19")
const queja = ref()

import { useReportesStore } from '../../store/ventas';
const store = useReportesStore()
const order_store = usecartStore()

const getOrder = async() => {
  store.setLoading(true, 'buscando orden')
    fetch(`${URI}/order/${order_id.value}`)
  .then(response => {
    if (!response.ok) {
      store.setLoading(false, 'buscando orden')

      throw new Error('Network response was not ok');
    }
    
    return response.json();
  })
  .then(data => {
    store.setLoading(false, 'buscando orden')

    console.log('Employer data:', data);
    order.value = data
    queja.value = ''
    determinarMensaje()
  })
  .catch(error => {
    store.setLoading(false, 'buscando orden')

    console.error('There has been a problem with your fetch operation:', error);
    order.value = {}
    queja.value = '  No hay un usuario para el número de documento '+ order_id.value
    // mensaje.value = 'error'
  });
}



onMounted( () => {
  order_id.value = order_store.last_order
})


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


    order.value.status == 'enviada'? mensaje.value = 'env':''
}

</script>


<style scoped>

.generada{
    background-color: rgba(255, 255, 0, 0.804);
    padding: 2rem;
    border-radius: 0.5rem;
}
.enviada{
    background-color: rgb(153, 255, 0);
    padding: 2rem;
    border-radius: 0.5rem;


}

.en{
    background-color: rgb(84, 212, 255);
    padding: 2rem;
    border-radius: 0.5rem;


}


.cancelada{
    background-color: rgba(255, 84, 84, 0.692);
    padding: 2rem;
    border-radius: 0.5rem;


}


.estado::first-letter{
    text-transform: capitalize;
}

</style>