<template>
  <div class="col-12">
    <div class="grid  pedido align-items-center" style="color: white; cursor: pointer;">
      <div v-for="product in order.order_products">
        <img class="" style="width: 60px; height: 60px; object-fit: contain;"
          :src="`${URI}/read_product_image/96/${product.id}`" alt="" />
      </div>

     
      <i v-if="estado.order_status == 'enviada'" class="pi pi-check "
        style="font-size: 3rem; color: var(--primary-color); font-weight: bold;"></i>
      <i v-if="estado.order_status == 'generada'" class="pi pi-star-fill p-3"
        style="font-size: 3rem; color: var(--primary-color); font-weight: bold;"></i>

      <span class="col text-right m-3 p-0" style="color: black; font-weight: bold; min-width: max-content;"> #{{
        order.order_id }}  <span class="col text-right m-3 p-0" style="color: black; font-weight: bold; min-width: max-content;"> {{
      obtenerHoraFormateadaAMPM(order.order_status.timestamp )  }}</span></span>




<!-- <span class="col text-right m-3 p-0" style="color: black; font-weight: bold; min-width: max-content;"> #{{
        order.order_status.timestamp.hora.h }}</span> -->

      <!-- Agrega la cuenta regresiva aquí -->


      <div v-if="order.order_status.status == 'en preparacion'" :class="minutos == 0 && segundos == 0 ? 'finalizado' : ''"
        class="countdown-timer m-3" style="display: flex; align-items: center;justify-content: center;"
        :style="{ borderRadius: '50%', position: 'relative', width: '3rem', height: '3rem' }">

        <div style="position: absolute; top: 50%; left: 50%; z-index: 99; transform: translate(-50%, -50%);">
          {{ minutos }}:{{ segundos }}
        </div>

       

        <div
          :style="{ position: 'absolute', width: '100%', height: '100%', borderRadius: '50%', clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0% 100%)' }">
        </div>

      </div>


    </div>
  </div>
</template>

<script setup>
import { defineProps, ref, onMounted, onUnmounted } from "vue";
import { URI } from "../service/conection";
import { convertirA12h,obtenerHoraFormateadaAMPM } from "../service/un_pedido";

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


// Obtenemos el tiempo restante de localStorage o establecemos 15 minutos si no existe
const tiempoRestante = ref(parseInt(localStorage.getItem(props.order.order_id)) || 15 * 60);
const minutos = ref(Math.floor(tiempoRestante.value / 60));
const segundos = ref(tiempoRestante.value % 60);

function actualizarTiempo() {
  if (props.order.order_status.status === 'en preparacion') {
    tiempoRestante.value--;
    minutos.value = Math.floor(tiempoRestante.value / 60);
    segundos.value = tiempoRestante.value % 60;
    localStorage.setItem(props.order.order_id, tiempoRestante.value);

    porcentajeCompletado.value = ((15 * 60 - tiempoRestante.value) / (15 * 60)) * 100;
    if (tiempoRestante.value <= 0) {
      clearInterval(intervalId);
      alert(`Se terminó el tiempo de preparación de la orden #${props.order.order_id}`);
    }
  }
}

const intervalId = setInterval(actualizarTiempo, 1000);

onUnmounted(() => {
  clearInterval(intervalId);
});
</script>

<style scoped>
/* Estilos de la cuenta regresiva */
.countdown-timer {
  color: black;
  font-weight: bold;
  /* background-color: white; */
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 3rem;
  width: 3rem;
  outline: 0.3rem solid var(--primary-color);
  animation:  parpadeoColor 1s infinite;
  /* margin-top: 10px; */
}

@keyframes parpadeoColor {
  0% {
    background-color: rgb(159, 221, 255); /* Color inicial */
  }
  50% {
    background-color: rgb(255, 255, 179); /* Color intermedio */
  }
  100% {
    background-color: rgb(151, 255, 167)(255, 195, 195); /* Color final */
  }
}

.texto-negro {
  color: black;
}

.finalizado {
  background-color: rgb(255, 0, 0);
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
