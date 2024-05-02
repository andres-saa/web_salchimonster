<template>







  <div class="grid mx-auto mb-8" style="max-width: 400px;">

    <DialogoPedido>

    </DialogoPedido>

    <div id="cuadre" class=" cuadre my-2 p-2  m-0 " style="width: 100%;top: 5rem; display: flex;align-items: center;position: relative;">
     
        <div class="shadow-2 p-0 m-0" style="width: 100%;border-radius: 0.5rem;">


          <p class="" style="background-color: #ffffff61; width: max-content; margin: auto; padding: 1rem;">
                        <p class="text-center text-2xl" style="color: black;font-weight: bold;"><i class="pi pi-history
            text-2xl
            "></i> <b>
              CUADRE DE CAJA <br> {{ siteStore.site.site_name }}  <br> {{ colombiaDateTime }}
            </b></p>
          </p>

          <p class="" style="background-color:#00c510;text-align: center;margin: 0;">
            <span class="text-center text-xl" style="color: black;font-weight: bold;"> Enviadas</span>
          </p>

          <div style="overflow-y: auto;">

            <div class="px-3 py-1" v-for="orden in store.TodayOrders.filter(order => order.current_status == 'enviada') ">
              <cuadreItem :order="orden" />
            </div>

          </div>


          <p class="" style="background-color:#ff4444; text-align: center;margin: 0;">
            <span class="text-center text-xl" style="color: black;font-weight: bold;"> Canceladas</span>
          </p>

          <div style="overflow-y: auto;">

            <div class="px-3 py-1" v-for="orden in store.TodayOrders.filter(order => order.current_status == 'cancelada')">
              <cuadreItem :order="orden" />
            </div>
          </div>


          <p class="" style="background-color:yellow;text-align: center;">
            <span class="text-center text-xl" style="color: rgb(0, 0, 0);font-weight: bold;"> Resumen</span>
          </p>


          <Button style="border-radius: 50%;left: 100%; position: absolute;" rounded severity="help" icon="pi pi-print text-2xl" @click="IMPRIMIR"> </Button>

   <div class="px-3 py-2 text-2xl" style="display: flex;font-weight: bold;margin: 0; align-items: center;justify-content: space-between;">
            <div style=" display: flex;align-items: center;">
                <b style="min-width: max-content;color: black;">
        CUADRE 

            </b>


            </div>

            
            
          
            
            
                <b style="color:black">
                    {{formatoPesosColombianos(totalEnviadas)  }}

                </b>
                
       
           

          

    
            
            
        </div>
        




        </div>
    
    </div>



  


  </div>


  <!-- <div :class="dialog_pedido_visible ? 'before' : ''"></div> -->
</template>

<script setup>


import DialogoPedido from './DialogoPedido.vue';

import { onMounted} from 'vue';
import { useOrderStore } from '../../store/order';
import cuadreItem from './cuadreItem.vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
const store = useOrderStore()
const siteStore = useSitesStore()

const now = new Date();

// Convertir la fecha y hora actual a la zona horaria de Colombia
const options = {
  timeZone: 'America/Bogota',
  year: 'numeric',
  month: 'numeric',
  day: 'numeric',
  hour: 'numeric',
  minute: 'numeric',
  second: 'numeric'
};

// Formatear la fecha y la hora según las opciones establecidas
const colombiaDateTime = now.toLocaleString('es-CO', options);

console.log(colombiaDateTime);

import { computed } from 'vue';
import { useSitesStore } from '../../store/site';

const totalEnviadas = computed(() => {
  return store.TodayOrders.filter(order => order.current_status === 'enviada')
                          .reduce((total, order) => total + order.total_order_price, 0);
});

onMounted(() => {
  store.getTodayOrders()
})



const IMPRIMIR = () => {
  const contenidoFactura = document.getElementById('cuadre').innerHTML;

  // Abrir una nueva ventana para imprimir
  const ventanaImpresion = window.open('', '_blank');

  ventanaImpresion.document.write('<html><head><title>Cuadre</title>');

  // Copiar estilos CSS de la página principal a la ventana de impresión
  const estilosPagina = document.getElementsByTagName('style');

  for (let i = 0; i < estilosPagina.length; i++) {
    ventanaImpresion.document.write(estilosPagina[i].outerHTML);
  }

  ventanaImpresion.document.write('<style>  @media print {  html{height: min-content; box-shadow:none}  *{text-transform:uppercase;align-items:center; font-family: sans-serif;padding:0;margin:0; font-size:12pt !IMPORTANT} body { padding:0rem; -webkit-print-color-adjust: exact; /* Chrome, Safari */ color-adjust: exact; /* Firefox */ } }  </style>');
  ventanaImpresion.document.write('</head><body>');
  ventanaImpresion.document.write(contenidoFactura);

  ventanaImpresion.document.write('</body></html>');

  ventanaImpresion.document.close();

  // Imprimir la ventana
  ventanaImpresion.print();

  // Cerrar la ventana después de 1 segundo (puedes ajustar este tiempo)
  setTimeout(() => {
    ventanaImpresion.close();
  }, 0.01);
};

</script>
