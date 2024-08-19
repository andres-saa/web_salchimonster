<template>
    <div class="col-12">
      <div class="grid  pedido align-items-center" style="color: rgb(255, 200, 200); cursor: pointer;">
        <div v-for="product in order.order_products">
          <img class="" style="width: 60px; height: 60px; object-fit: contain;"
            :src="`${URI}/read-product-image/96/${product.name}`" alt="" />
        </div>
  
       
        <i v-if="estado.order_status == 'enviada'" class="pi pi-check "
          style="font-size: 2rem; color: var(--primary-color); font-weight: bold;"></i>
        <i v-if="estado.order_status == 'generada'" class="pi pi-star-fill p-3"
          style="font-size: 2rem; color: var(--primary-color); font-weight: bold;"></i>
  
        <span class="col text-right m-3 p-0" style="color: black; font-weight: bold; min-width: max-content;"> #{{
          order.order_id }}  <span class="col text-right m-3 p-0" style="color: black; font-weight: bold; min-width: max-content;"> {{
        obtenerHoraFormateadaAMPM(order.order_status.timestamp )  }}</span></span>

         
  
  
  
  
  <!-- <span class="col text-right m-3 p-0" style="color: black; font-weight: bold; min-width: max-content;"> #{{
          order.order_status.timestamp.hora.h }}</span> -->
  
        <!-- Agrega la cuenta regresiva aquí -->
  

  
  
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, ref, onMounted, onUnmounted } from "vue";
  import { URI } from "../service/conection";
//   import { convertirA12h } from "../service/un_pedido";
  

  const porcentajeCompletado = ref(0);
  const props = defineProps({
    order: {
      type: Object,
      default: {},
    },
    estado: {
      type: Object,
      default: {},
    },
  });

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
  


  </script>
  
  <style scoped>
  /* Estilos de la cuenta regresiva */
  
  </style>
  