<template>




<Dialog class="mx-4" v-model:visible="visibleDialog" modal style="width:30rem ;background-color: white;">

<div style="height: auto;color: black;background-color: white; display: flex;flex-direction: column;justify-content: end;align-items: center;" >

    <h4>Hemos recibido su solicitud y ha quedado registrada con el id   </h4> <br><b> <p class="text-center" style="width: auto;font-size: 3rem;">{{ last_id[0]['id'] }} </p></b>
    
    <h4>Pronto te contactaremos </h4> 

    
    <router-link to="/">
        <Button class="m-auto" style="font-weight: bold;" severity="info" label="Listo"></Button>
    </router-link>
    
</div>
</Dialog>





    <div class="p-0 m-0 p-2" style="width: 100%; min-height: 100vh;height: 100%; display: flex;align-items: center;justify-content: center; left: 0;top:3rem"> 
        <div  style="max-width: 600px; background-color: white;border-radius: .5rem; margin: auto; margin-top: 4rem; padding: 1.5rem; box-shadow: 0 0 10px rgba(0,0,0,0.1);">


<h3 class="m-0 mb-3 text-black"> <b>  Formulario de Pre-Inscripción - Salchimonster Somos Todos</b></h3>
<div class="intro-text" style="text-align: justify;">
<p>Salchimonster es una Empresa que nace en el año 2017 a partir de una vitrina, siendo este el claro ejemplo que con Disciplina y perseverancia los sueños se cumplen. Actualmente contamos con 11 Imperios, Valle, Bogotá y Medellín, contamos con un Centro de distribución para garantizar la estandarización y calidad de los productos.</p>
<p>Estamos comprometidos con los buenos valores donde nuestros mounstruos (empleados) que cada día le meten a Fuego y salen a todo por el todo. Hemos logrado reconocimiento Nacional como los fundadores de las Salchipapas dejando el nombre de Cali en Alto.</p>
<p>Construimos una cadena de restaurantes atractiva, rentable y sostenible para inversionistas con el fin de proyectarnos como la mejor salchipaperia del país.</p>
<p> <b>¡¡¡AQUÍ EL MOUNSTRUO SOS VOS!!!</b> </p>
<p> <b>PAPIII NO ES POR VENDERTE PERO DONDE LLEGAMOS ROMPEMOS</b> </p>
</div>

<form @submit.prevent="enviarFormulario" style="display: grid;gap: .5rem;justify-content: end;align-items: center; ">


<h6 class="my-2">Nombre Completo:</h6>
<InputText v-model="formulario.nombre" placeholder="Ingrese su nombre completo" />

<h6 class="my-2">Teléfono:</h6>
<InputText v-model="formulario.telefono" placeholder="Ingrese su número de teléfono" />


<h6 class="my-2">Correo electronico:</h6>
<InputText v-model="formulario.email" placeholder="Correo electronico" />


<h6 class="my-2">Porque quieres una franquicia de salchimonster?:</h6>
<Textarea rows="5" rezise="none" style="resize: none;" v-model="formulario.razon" placeholder="Cuentanos" />


<h6 class="my-2">Capacidad de Inversión:</h6>
<Dropdown optionValue="value" :options="opcionesInversion" optionLabel="label" v-model="formulario.inversion" placeholder="Seleccione un rango" />

<h6 class="my-2">Zona de Interés:</h6>
<Dropdown optionValue="value" :options="zonas" optionLabel="label" v-model="formulario.zona" placeholder="Seleccione una zona" />

<h6 class="my-2">En que ciudad se ubicara' la franciquicia:</h6>
<InputText v-model="formulario.ciudad" placeholder="ciudad" />

<h6 class="my-2">¿Haces parte del sector gastronómico?</h6>
<Dropdown optionValue="value" optionLabel="label" :options="opcionesBooleanas" v-model="formulario.sectorGastronomico" placeholder="Seleccione una opción" />

<h6 class="my-2">¿Participarás en la operación de la franquicia?</h6>
<Dropdown optionValue="value" optionLabel="label" :options="opcionesBooleanas" v-model="formulario.operacionFranquicia" placeholder="Seleccione una opción" />

<h6 class="my-2">Confirma la fuente de tus ingresos:</h6>
<Dropdown optionValue="value" optionLabel="label" :options="opcionesFuenteIngresos" v-model="formulario.fuenteIngresos" placeholder="Seleccione una opción" />

<span></span>
<Button type="submit"  severity="help" label="Enviar" style="margin-top: 1rem;border: none;"></Button>
</form>
</div>
    </div>

  </template>



<script setup>
import { ref } from 'vue';
import { fetchService } from '../../service/utils/fetchService';
import { URI } from '../../service/conection';
const visibleDialog = ref(false)
const last_id = ref('')
const formulario = ref({
  nombre: '',
  telefono: '',
  email: '',
  razon: '',
  inversion: null,
  zona: null,
  ciudad: '',
  sectorGastronomico: null,
  operacionFranquicia: null,
  fuenteIngresos: '',
  status:'Pendiente'
});


const opcionesInversion = [
    { label: '$250.000.000 - $350.000.000', value: '$250.000.000 - $350.000.000' },
    { label: '$350.000.000 - $450.000.000', value: '$350.000.000 - $450.000.000' },
    { label: '$450.000.000 - $550.000.000', value: '$450.000.000 - $550.000.000' }
  ];
  
  const zonas = [
    { label: 'Eje Cafetero', value: 'Eje Cafetero' },
    { label: 'Cundinamarca', value: 'Cundinamarca' },
    { label: 'Caribe', value: 'Caribe' },
    { label: 'Otros', value: 'Otros' }
  ];
  
  const opcionesBooleanas = [
    { label: 'Sí', value: true },
    { label: 'No', value: false }
  ];

  const cupos = [
  { label: 'Cupo por $180 millones por el 1% de renta Mensual', value: '180-1' },
  { label: 'Cupo por $360 millones por el 1% de renta mensual', value: '360-1' },
  { label: 'Cupo por $540 millones por el 1.2% de renta mensual', value: '540-1.2' }
];

const opcionesFuenteIngresos = [
  { label: 'Recurso propio', value: 'Propio' },
  { label: 'Recurso prestado', value: 'Prestado' },
  { label: 'Recurso Mixto', value: 'Mixto' }
];

const validarFormulario = () => {
  if (!formulario.value.nombre.trim()) {
    alert('Por favor, ingrese su nombre completo.');
    return false;
  }
  if (!formulario.value.telefono.trim()) {
    alert('Por favor, ingrese su número de teléfono.');
    return false;
  }
  if (!formulario.value.email.trim() || !formulario.value.email.includes('@')) {
    alert('Por favor, ingrese un correo electrónico válido.');
    return false;
  }
  if (!formulario.value.razon.trim()) {
    alert('Por favor, explique su motivo de inversión.');
    return false;
  }
  if (!formulario.value.inversion) {
    alert('Por favor, seleccione un rango de inversión.');
    return false;
  }
  if (!formulario.value.zona) {
    alert('Por favor, seleccione una zona.');
    return false;
  }
  if (!formulario.value.ciudad.trim()) {
    alert('Por favor, describa su ciudad.');
    return false;
  }
  if (formulario.value.sectorGastronomico === null) {
    alert('Por favor, indique si forma parte del sector gastronómico.');
    return false;
  }
  if (formulario.value.operacionFranquicia === null) {
    alert('Por favor, indique si participará en la operación de la franquicia.');
    return false;
  }
  if (!formulario.value.fuenteIngresos) {
    alert('Por favor, seleccione una fuente de ingresos.');
    return false;
  }
  return true;

}


const fieldMapping = {
  nombre: 'name',
  telefono: 'phone',
  email: 'email',
  razon: 'reason',
  inversion: 'investment_capacity',
  zona: 'zone_of_interest',
  ciudad: 'city',
  sectorGastronomico: 'is_in_gastronomic_sector',
  operacionFranquicia: 'will_participate_in_operation',
  fuenteIngresos: 'source_of_income',
  status: 'status'
};





const enviarFormulario = async() => {
  if (validarFormulario()) {
    // Map the Spanish field names to English
    const jsonData = {
      [fieldMapping.nombre]: formulario.value.nombre,
      [fieldMapping.telefono]: formulario.value.telefono,
      [fieldMapping.email]: formulario.value.email,
      [fieldMapping.razon]: formulario.value.razon,
      [fieldMapping.inversion]: formulario.value.inversion,
      [fieldMapping.zona]: formulario.value.zona,
      [fieldMapping.ciudad]: formulario.value.ciudad,
      [fieldMapping.sectorGastronomico]: formulario.value.sectorGastronomico,
      [fieldMapping.operacionFranquicia]: formulario.value.operacionFranquicia,
      [fieldMapping.fuenteIngresos]: formulario.value.fuenteIngresos,
      [fieldMapping.status]: 'Pendiente'
    };
   last_id.value =  await fetchService.post(`${URI}/create_franquicia_request`,jsonData)
   visibleDialog.value = true
  }
};
</script>


 <style scoped>
  .intro-text p {
    margin-bottom: 0.5rem;
  }



  form{
    grid-template-columns: repeat(2,1fr);
  }


 

  @media (width < 580px) {
    
  form{
    grid-template-columns: repeat(1,1fr);
  }

  }
  </style>
  