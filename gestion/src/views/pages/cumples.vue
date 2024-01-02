
<script setup>
import ShowUserBirth from './ShowUserBirth.vue';
import { ref, onMounted, onBeforeMount, computed, cloneVNode } from 'vue';
import { URI } from '../../service/conection';

const fechaFormateada = ref('');
const mesActual = ref()
// Array de nombres de meses en español
const nombresMeses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];

const obtenerFechaServidor = async () => {
    try {
        const serverTimeResponse = await fetch(`${URI}/server_time`);
        const serverTimeString = await serverTimeResponse.json();

        // Verificar si la respuesta es una cadena válida
        if (!serverTimeString || !serverTimeString.trim()) {
            throw new Error('Respuesta del servidor no válida o vacía');
        }

        // Asegurarse de que la cadena esté en el formato esperado
        const serverTime = new Date(serverTimeString.replace(' ', 'T') + 'Z');

        // Verificar si la fecha es válida
        if (isNaN(serverTime.getTime())) {
            throw new Error('La fecha del servidor no es válida');
        }

        // Obtener el día, mes y año
        const dia = serverTime.getDate();
        const mes = serverTime.getMonth();
        const anio = serverTime.getFullYear();
        mesActual.value = mes

        // Formatear la fecha
        fechaFormateada.value = `${dia} de ${nombresMeses[mes]} de ${anio}`;
    } catch (error) {
        console.error('Error al obtener la hora del servidor:', error);
        fechaFormateada.value = 'Fecha no disponible';
    }
};

onMounted(obtenerFechaServidor);


</script>

<template>
<div class="cont">
  <h5 class="m-auto col-12  text-center text-5xl" style="font-weight: bold; color: ;"> Cumples <i class="pi pi-spin pi-star-fill
" style="font-size: 3rem"></i> </h5>
  <h5 class="m-auto col-12  text-center text-2xl"> Hoy: {{ fechaFormateada }} 
       </h5>

  <div class="lg:col-6 md:col-9 m-auto" style="border-radius: 1REM; box-shadow: 0 0 20px rgba(0, 0, 0, 0.433); background-color: rgb(255, 206, 206);">



    <div style="display: flex; justify-content: space-between; align-items: center;">
      <h2 class="justify-center text-2xl" style="height: 100%; font-weight: bold;">
        Este mes
      </h2>


      <AvatarGroup class="mb-3 avatar"  @click="$refs.currentCumple.click()">
      <Avatar :image="'demo/images/avatar/amyelsner.png'" size="xlarge" shape="circle">
      </Avatar>
      <Avatar :image="'demo/images/avatar/asiyajavayant.png'" size="xlarge" shape="circle"></Avatar>
      <Avatar :image="'demo/images/avatar/onyamalimba.png'" size="xlarge" shape="circle"></Avatar>
      <Avatar :image="'demo/images/avatar/ionibowcher.png'" size="xlarge" shape="circle"></Avatar>
      <Avatar :image="'demo/images/avatar/xuxuefeng.png'" size="xlarge" shape="circle">
      </Avatar>
      <Avatar label="+2" shape="circle" size="xlarge" :style="{ 'background-color': '#9c27b0', color: '#ffffff' }">
      </Avatar>
    </AvatarGroup>

 
    </div>
   

  
    <Accordion :activeIndex="mesActual" >
      <AccordionTab header="Enero">
        <ShowUserBirth :mes="1" />
      </AccordionTab>
      <AccordionTab header="Febrero">
        <ShowUserBirth :mes="2" />
      </AccordionTab>
      <AccordionTab header="Marzo">
        <ShowUserBirth :mes="3" />
      </AccordionTab>
      <AccordionTab header="Abril">
        <ShowUserBirth :mes="4" />
      </AccordionTab>
      <AccordionTab header="Mayo">
        <ShowUserBirth :mes="5" />
      </AccordionTab>
      <AccordionTab header="Junio">
        <ShowUserBirth :mes="6" />
      </AccordionTab>
      <AccordionTab header="Julio" >
        <ShowUserBirth :mes="7" />
      </AccordionTab>
      <AccordionTab header="Agosto">
        <ShowUserBirth :mes="8" />
      </AccordionTab>
      <AccordionTab header="Septiembre">
        <ShowUserBirth :mes="9" />
      </AccordionTab>
      <AccordionTab header="Octubre">
        <ShowUserBirth :mes="10" />
      </AccordionTab>
      <AccordionTab header="Noviembre">
        <ShowUserBirth :mes="11" />
      </AccordionTab>
      <AccordionTab header="Diciembre">
        <ShowUserBirth :mes="12" />
      </AccordionTab>

    </Accordion>
  </div>
</div>
  
</template>


<style scoped>

.cont {
    position: relative;
    min-height: 100vh; /* Asegura que el div cubra toda la altura de la pantalla */
    width: 100%; /* Asegura que el div cubra todo el ancho de la pantalla */
    overflow: hidden; /* Evita cualquier desbordamiento del contenido */
}

.cont::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('https://www.enter.co/wp-content/uploads/2017/11/iStock-601920764-1024x768.jpg');
    background-size: cover; /* Asegura que la imagen cubra todo el espacio disponible */
    background-repeat: no-repeat; /* Evita que la imagen se repita */
    background-position: center; /* Centra la imagen de fondo */
    opacity: 0.5; /* Establece la opacidad del fondo */
    z-index: -1;
    
}

.cont > * {
    position: relative;
    z-index: 1;
}
</style>