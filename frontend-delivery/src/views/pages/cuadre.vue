<template>
<div style="height: 80vh;overflow-y: auto; display:flex; align-items: center;">
  <div class="  col-12 m-auto" style="width: 30rem; box-shadow: 0 0 10px rgba(0, 0, 0, 0.196); border-radius: 2rem; ">

<p class="text-center text-xl " style="font-weight: bold;"> VENTAS {{ formatearFechaHora(fecha_del_server).toUpperCase() }} </p>

<p class=" text-center mb-1" style="font-weight: bold; background-color: rgb(191, 255, 96); border-radius: 1rem;"> PEDIDOS ENVIADOS  {{  filtrarPorEstado(ordenes_de_hoy,'enviada').length }}</p>

<div >
  <div class=" pedido" v-for="order in filtrarPorEstado(filtrarPedidosPorFecha(pedidos,fecha_del_server),'enviada')" style="display: flex;">

   <div class="col p-0 text-left"  >
    Pedido #{{ order.order_id }}  
   </div>
   <div class="col p-0 text-right" style="font-weight: bold;">
    {{ formatoPesosColombianos(sumarProductos(contarObjetosRepetidos(order.order_products))) }}

   </div>
  </div>

</div>

<div class="p-1 mb-2 " style="border-bottom: 1px solid;"></div>

<div class=" grid p-3 pb-0  text-xl mb-2 p-0" style="">
  <p class="  col p-0 text-left m-0" style="font-weight: bold; ">  TOTAL CAJA</p>
  <p class="  col p-0 text-right m-0 pr-3" style="font-weight: bold;border-radius: 1rem;  background: linear-gradient(to right,transparent, rgb(191, 255, 96) );
">  {{formatoPesosColombianos( calcularTotalConjuntoOrdenes(filtrarPorEstado(filtrarPedidosPorFecha(pedidos,fecha_del_server),'enviada')) )}}</p>
</div>




<p class=" text-center mb-1 pt-0" style="font-weight: bold; background-color: rgb(255, 165, 180);border-radius: 1rem;"> PEDIDOS CANCELADOS {{  filtrarPorEstado(ordenes_de_hoy,'cancelada').length }}</p>

<div >
  <div class="grid" v-for="order in filtrarPorEstado(ordenes_de_hoy,'cancelada')">

   <div class="col pb-0 text-left">
    Pedido #{{ order.order_id }} 
    

   </div>
   <div class="col pb-0 text-right" ref="hola" style="font-weight: bold;">
    {{ formatoPesosColombianos(sumarProductos(contarObjetosRepetidos(order.order_products))) }}

   </div>

    

  </div>

</div>
</div>


</div>



</template>
 








<script setup>

import { fecha_del_server,open_order, filtrarPedidosPorFecha, fechaHoyFormateada,set_dialog_order, pedidos, ordenes_de_hoy,filtrarPorEstado,dialog_pedido_visible } from '../../service/un_pedido';
import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { calcularPrecioTotal, calcularTotalCarrito, contarObjetosRepetidos, sumarProductos } from '../../service/state';
import { URI } from "@/service/conection";
import dialogoPedido from './dialogo-pedido.vue';


 
const clickarPedido = (pedido_id) => {
  const pedido = ref("hola")
  console.log(hola)
  // pedido.click()
}
function calcularTotalConjuntoOrdenes(orders) {
  // Inicializar la variable para almacenar la suma total
  let totalGlobal = 0;

  // Iterar sobre cada orden en el conjunto de órdenes
  for (let i = 0; i < orders.length; i++) {
    // Calcular el total de la orden actual utilizando la función calcularTotalCarrito
    const totalOrden = calcularTotalCarrito(orders[i]);

    // Sumar el total de la orden actual al total global
    totalGlobal += totalOrden;
  }

  // Devolver el total global
  return totalGlobal;
}

const formatearFechaHora = (fechaHoraString) => {
  const fechaHora = new Date(fechaHoraString);
  const diaSemanaNumero = fechaHora.getDay();
  const diasSemana = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
  const diaSemana = diasSemana[diaSemanaNumero];
  const diaMes = fechaHora.getDate();
  const mes = fechaHora.toLocaleString("es-ES", { month: "long" });
  const anio = fechaHora.getFullYear();
  const horas = fechaHora.getHours();
  const minutos = fechaHora.getMinutes();
  const periodo = horas >= 12 ? "PM" : "AM";
  const horasFormato12 = horas % 12 || 12;

  return `${diaSemana} ${diaMes} de ${mes} de ${anio} hasta las ${horasFormato12}:${minutos} ${periodo}`;
};


const fechaActualServidor = ref()
const fechapedido = ref()

const nombresMeses = [
  "enero", "febrero", "marzo", "abril", "mayo", "junio",
  "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
];

// const filtrarOrdenesPorFecha = async (ordenes) => {
//   // Obtener la fecha actual del servidor
//   const serverTimeResponse = await fetch(`${URI}/server_time`);
//   const serverTimeData = await serverTimeResponse.json();
//   fechaActualServidor.value = serverTimeData.fecha;

//   // Filtrar las órdenes por la fecha actual
//   const ordenesFiltradas = ordenes.filter(orden => {
//     const fechaOrden = orden.order_status.timestamp.fecha;
//     fechapedido.value = fechaOrden
//     return (
//       fechaOrden.d === fechaActualServidor.value.d &&
//       fechaOrden.m === fechaActualServidor.value.m &&
//       fechaOrden.a === fechaActualServidor.value.a
//     );
//   });

//   fechapedido.value = ordenesFiltradas
//   return ordenesFiltradas
// }






</script>


<style>

/* .pedido:hover{


  background-color: rgb(204, 204, 204);
  cursor: pointer;
} */

</style>