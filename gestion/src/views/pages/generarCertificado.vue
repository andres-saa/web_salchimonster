<template>

<p class="text-4xl text-center py-4" style="font-weight: bold;">Generar Certificado Laboral</p>
<span class="a4-size mb-6" style="display: flex; height: auto;">
  
  
  <InputNumber v-model="usrDni" :disabled="getUserRole()?.toLowerCase() != 'gerente'"  class="mr-5" style="width: 100%;" placeholder="Cedula del empleado"></InputNumber>
    <Button @click="getUser(usrDni)">Buscar</Button>
    


</span>
<p v-if=" usrDni==null " class="text-1xl m-auto  col-6 p-0" style="color: var(--primary-color);"> Por favor digite el numero de decumento del usuario  y presione Buscar</p>


<p v-if="!user.dni && usrDni" class="text-5xl m-auto col-6">
  {{queja}}
</p>



<div class="grid mt-1"  style="min-height: ;">


    <div  v-if="user.dni && usrDni" class=" col-12 a4-size p-0 m-auto" style=" height: max-content; background-color: transparent;" >

        

        
        <h6 class="text-center p-2 m-0 mb-5" style="border-radius: 2rem; font-weight: bold; background-color: var(--gray-200);">INFORMACIÓN DEL EMPLEADO</h6>

<div class=" px-0 grid" style="display: ;">
    <h6 class="col-6 m-0  text-left">NOMBRE</h6>
    <h6 class="col-6 m-0 text-right" style="font-weight: 300;min-width: max-content;">{{ user.name }}</h6>
</div>


<div class=" px-0 grid p-0 " style="display: ; border-radius: 2rem; " :style="user?.status?.toLowerCase().split(' ')[0] == 'activo'? 'background-color:rgb(193, 255, 100);':'background-color: rgb(255, 132, 132);'">
    <h6 class="col-6 m-0  py-2 text-left">ESTADO</h6>
    <h6 class="col-6 m-0  py-2 text-right" style="font-weight: 300;min-width: max-content;">{{ user.status }}</h6>
</div>


<div class="px-0 grid" style="">
    <h6 class="col-6 m-0  text-left">DOCUMENTO</h6>
    <h6 class="col-6 m-0  text-right" style="font-weight: 300;min-width:max-content;">{{ user.dni }}</h6>
</div>

<div class="px-0 grid" style="">
    <h6 class="col-6 m-0  text-left">FECHA DE INICIO</h6>
    <h6 class="col-6 m-0  text-right" style="font-weight: 300; ">{{ user.entry_date }}</h6>
</div>

<div class="px-0 grid" style="background-color: ">
    <h6 class="col-6 m-0  text-left">CARGO</h6>
    <h6 class="col-6 m-0  text-right" style="font-weight: 300;">{{ user.position }}</h6>
</div>

<h6 class="text-center p-2 mb-5" style=" border-radius: 2rem;font-weight: bold; background-color: var(--gray-200)">DETALLES ADICIONALES</h6>




<div class="px-0 grid" style="">
    <h6 class="col-6 m-0  text-left">TIPO DE CONTRATO</h6>
    <h6 class="col-6 m-0  text-right" style="font-weight: 300;">{{ user.contract_type }}</h6>
</div>

<div class="px-0 grid" style="">
    <h6 class="col-6 m-0  text-left">SALARIO</h6>
    <h6 class="col-6 m-0  text-right" style="font-weight: 300;">{{ formatoPesosColombianos(user.salary) }}</h6>
</div>



        
        
        
    </div>
    
    <div class=" col-12 certificado" v-if="user?.status?.toLowerCase().split(' ')[0] == 'activo'" ref="contenidoParaPDF" >

      <div  class=" a4-size p-8" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.508);">


        <img class="m-auto" src="https://salchimonster.com/images/logo.png" style="width: 10%;" alt="">

        <h6 style="font-size: 14pt; font-weight: normal;color: black; font-family: Arial, Helvetica, sans-serif;">


{{convertirFecha(serverDate)}}
</h6>
<h6 class="text-center mi-clase" style="font-size: 14pt; font-weight: bold;color: black; font-family: Arial, Helvetica, sans-serif;">
  INVERSIONES SALCHIMONSTER SAS
</h6>  

<!-- [Logo de la Empresa] -->

<h6 style="font-size: 14pt; font-weight: normal;color: black; font-family: Arial, Helvetica, sans-serif;" class="text-center">NIT: 901.420.874-0</h6>

<h6 class="text-center py-4" style="font-weight: bold;"> CERTIFICA A:   <span style="text-transform: capitalize;">{{ user.name }}</span></h6>

<h5 class="text-l text-justify" style="font-size: 14pt; font-weight: normal;color: black; font-family: Arial, Helvetica, sans-serif;">
  El(la) señor(a) <b style="text-transform: uppercase;">{{ user.name }}</b> identificado con CC No. <b>{{ user.dni }}</b> labora en nuestra empresa con un contrato <b style="text-transform: uppercase;">{{ user.contract_type }}</b> desde el dia {{ convertirFecha(user.entry_date) }} activa a la fecha desempenando el cargo de <b style="text-transform: uppercase;"> {{ user.position }}. </b> 
  
  
  <!-- Sus ingresos laborales mensuales se componen de la siguiente manera:

  <div class=" grid mt-2 col-10 mb-0 pb-0 ">
    <div class=" col-8 p-0">SALARIO BASICO</div>
    <div class="col text-right p-0">{{ formatoPesosColombianos(user.salary)  }} </div>
  </div>
  <div class=" grid pt-0 mt-0 col-10 ">
    <div class="col-8 p-0">BONIFICACION NO PRESTACIONAL</div>
    <div class="col text-right p-0">{{ formatoPesosColombianos(100000)  }} </div>
  </div>
  <div class=" grid pt-0  col-10 ">
    <div class="col-8 p-0">AUXILIO DE TRANSPORTE</div>
    <div class="col text-right p-0">{{ formatoPesosColombianos(140606)  }} </div>
  </div> -->

  <h5 style="font-size: 14pt; font-weight: normal;color: black; font-family: Arial, Helvetica, sans-serif;" class="py-1 mt-0">
    Para constancia de lo anterior se firma en Bogota D.C a {{convertirFechaserver(serverDate)}}

    <p class="py-6">
      Cordialmente,
    </p>
   


<img style="width: 20rem; border-bottom: 2px solid ; padding-right: 3rem; padding-bottom: 1rem;" src="/images/sello gestion humana.png" alt="">
<!-- <p class="py-0  my-0"> <b> YARY CESPEDES MEJIA</b></p> -->
<p class="py-0  my-0"> Oficina de  Gestión Humana</p>
<p class="py-0  my-0">INVERSIONES SALCHIMONSTER SAS</p>
<p class="py-0  my-0">
  NIT. 901420874-0
</p>

  </h5>

</h5>



</div>
    </div>




</div>







</template>


<script setup>



import { onMounted, ref, watch } from 'vue';
import { URI } from '../../service/conection';
import {formatoPesosColombianos} from '../../service/formatoPesos.js';
import { useRoute } from 'vue-router';
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';
import { getUserDni, getUserRole } from '../../service/valoresReactivosCompartidos';




const user = ref({})
const usrDni= ref(getUserDni()  )
const mensaje = ref()
const serverDate = ref("2029-12-21 16:19")
const queja = ref()

var elementos = document.getElementsByClassName("mi-clase");




const convertirFechaserver = (fecha) => {
    // Crear objeto de fecha
    let date = new Date(fecha);

    // Obtener día, mes y año
    let day = date.getDate();
    let month = date.getMonth(); // Los meses en JavaScript comienzan en 0
    let year = date.getFullYear();

    // Nombres de los meses en español
    let monthNames = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
                      "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
    let monthName = monthNames[month];

    // Formatear la fecha
    return `los ${day} días del mes de ${monthName} de ${year}`;
};

watch(usrDni, (newValue, oldValue) => {
      console.log(`El valor de usrDni ha cambiado de ${oldValue} a ${newValue}`);
      // Aquí puedes agregar cualquier lógica adicional que necesites
    });



const getUser = async(dni) => {



    fetch(`${URI}/employer/dni/${dni}`)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    
    return response.json();
  })
  .then(data => {
    console.log('Employer data:', data);
    user.value = data
    queja.value = ''
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
    user.value = {}
    queja.value = '  No hay un usuario para el número de documento '+ usrDni.value
    mensaje.value = 'error'
  });
}


const getDate = async() => {
    fetch(`${URI}/server_time`)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    
    return response.json();
  })
  .then(data => {
    console.log('Employer data:', data);
    serverDate.value = data
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
    mensaje.value = 'error'
  });
}

onMounted( async() => {
getDate()

})

function convertirFecha(fecha) {

  if(!fecha){
    fecha = "2029-12-21 16:19"
  }
    const meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];

    // Dividimos la fecha y la hora
    let [fechaParte, horaParte] = fecha.split(' ');

    // Dividimos los componentes de la fecha
    let [año, mes, día] = fechaParte.split('-').map(Number);

    // Convertimos el mes a formato legible
    let mesLegible = meses[mes - 1];

    // Formateamos la fecha
    return `${día} de ${mesLegible} de ${año}`;
}




function numeroATexto(numero) {
    const unidades = ['cero', 'un', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'];
    const especiales = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve'];
    const decenas = ['', '', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'];

    // Función auxiliar para convertir los dígitos en palabras
    function convertir(trio) {
        let resultado = '';
        let cien = 'cien';

        if (trio[0] > 1) {
            resultado += unidades[trio[0]] + 'cientos ';
            cien = '';
        } else if (trio[0] === 1) {
            resultado += cien + ' ';
        }

        if (trio[1] > 1) {
            resultado += decenas[trio[1]] + ' y ';
        } else if (trio[1] === 1) {
            return resultado + especiales[trio[2]];
        }

        if (trio[2] !== 0 || (trio[0] === 0 && trio[1] === 0)) {
            resultado += unidades[trio[2]];
        }

        return resultado;
    }

    if (numero === 0) {
        return unidades[0];
    }

    if (numero < 0) {
        return 'menos ' + numeroATexto(-numero);
    }

    let grupos = [];
    while (numero > 0) {
        grupos.push(numero % 1000);
        numero = Math.floor(numero / 1000);
    }

    let partes = grupos.map((grupo, i) => {
        if (grupo === 0) return '';
        let parte = convertir([Math.floor(grupo / 100), Math.floor((grupo % 100) / 10), grupo % 10]);
        if (i === 1) return grupo === 1 ? 'mil' : parte + ' mil';
        if (i === 2) return grupo === 1 ? 'un millón' : parte + ' millones';
        return parte;
    });

    return partes.reverse().join(' ').trim();
}

// Ejemplo de uso
console.log(numeroATexto(1600000)); // "un millón seiscientos mil"

// Ejemplo de uso
console.log(numeroATexto(1600000)); // "un millón seiscientos mil"



console.log(numeroATexto(1111111)); // "un millón seiscientos mil"










const contenidoParaPDF = ref(null);
const exportarComoPDF = async () => {
  console.log(contenidoParaPDF)
  try {
    const canvas = await html2canvas(elementos, { scale: 2 });
    const imgData = canvas.toDataURL('image/png');
    const pdf = new jsPDF({
      orientation: 'portrait',
      unit: 'px',
      format: 'a4'
    });

    pdf.addImage(imgData, 'PNG', 0, 0, pdf.internal.pageSize.getWidth(), pdf.internal.pageSize.getHeight());
    pdf.save('documento.pdf');
  } catch (error) {
    console.error("Error al exportar PDF: ", error);
    // Manejar el error adecuadamente
  }
};






</script>

<style scoped>


.a4-size {
    width: 210mm;
    height: 297mm;
    margin: auto; /* Centrar en la pantalla */
    background-color: white; /* Opcional: para simular el color de una hoja de papel */
}



*{
  font-family: Arial, Helvetica, sans-serif;
  font-size: 14pt;
  color: black;
}

</style>

