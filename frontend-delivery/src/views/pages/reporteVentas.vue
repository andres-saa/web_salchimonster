<template>

    <!-- <Transition name="fade">
        <Loading :tittle=" `CARGANDO REPORTE DE ORDENES ${store.order_status}s` " v-if="store.loading"></Loading>

    </Transition> -->


    <div class="col-12 px-3 md:px-4 mx-auto" style="position: relative; max-width: 900px; margin-top: 6rem;" >
       
   
            <div class="  grid " style=" background-color:rgba(250, 250, 250, 0);">



     


                <div class="text-sm col-12 md:col-3 p-2 xl:col-2 ">
                    <Dropdown class="text-sm col-12 p-0 " style="height: 2.7rem;"  v-model="store.order_status" :options="estadosDropValues"  placeholder="Estado"></Dropdown>
                </div>

                   


       <!-- <div class="text-sm col-12 p-2  md:col-4  xl:col-6 ">
        <MultiSelect style="" display="chip" multiple v-model="store.selectedSites" optionLabel="site_name" :options="sites.filter(s => s.site_id != 12 & s.site_id !=13)" class="text-sm col-12 p-0" placeholder="Sedes"></MultiSelect>
       </div> -->
                    
<div class="text-center col-12 p-2  md:col-3  ">
    <InputText class="col-12 p-3"   @click="showDateDialog = true" style="height: 2.7rem;" :value="store.dateRangeDifference.rangeName || `${formatDate(store.dateRange.startDate) }  |  ${formatDate(store.dateRange.endDate)}`" placeholder="periodo"/>
</div>

                    


                    <div class="col-12 md:col-1 md:p-0" style="display: flex; align-items: center; justify-content: start;">
                        <Button icon="pi pi-search" severity="help" class="text-center p-0 col-12  md:p-0"   style="height: 2.5rem;width:min-content;aspect-ratio:  1 / 1;font-weight: bold; border-radius: 50%; display: flex;justify-content:center ; " @click="store.fetchSalesReport"></Button>
                    </div>
                    



</div>



<p class="text-3xl px-0 mx-0 my-6 pb-0" style="font-weight: bold;"> <i class="fa-solid fa-chart-simple"></i> Vision General</p>



    <div class="contenedor mt-5" style="position: sticky;top: 3rem;z-index: 99;">


<div class="col-12 px-0 py-0 my-0 p-0" style="overflow-x:auto; background-color: #fafafa;">
    <div class="px-0 mx-0" style="width: max-content; background-color:#fafafa; display:  flex;color: ; justify-content: start;gap: 2rem;min-width: max-content;">
   <div v-for="boton in menus" style="background-color: ">


    <RouterLink :to="`/reporte-ventas/${boton.to}`" >
        <Button  size="medium" :style="ruta.path.includes(boton.to)? 'box-shadow: 0 4px 0 #ff6200;color:#000;font-weight:bold;':''" class="text-md px-0 pt-2 pb-4 my-0 mx-0" text   severity="secondary" style=" border-radius: 0;transition: .3s all ease;">
            
            <i class="mr-2" :class="boton.icon"></i>
            {{ boton.name }}

            <!-- {{ ruta.fullPath }} -->
            
        
        </Button>
    </RouterLink>
   </div>
   <!-- <div class="p-0" style="display: flex;align-items: center;background-color: rgba(245, 222, 179, 0); ">
    
          <Button size="medium"   class="text-md px-0 py-0 mx-0 text-l btn-ocultar" text @click="store.toogleVisibleNotifications" :severity="store.visibleNotifications? 'danger': 'success'"  rounded style="font-weight: bold; ">
            <span>
               <span >{{ store.visibleNotifications? 'Ocultar notificaciones': 'Mostrar notificaciones' }} </span> <i  :class="PrimeIcons.ANGLE_DOUBLE_RIGHT"></i>
            </span>
        
        </Button>  

        
   </div>
        -->

    
</div>
</div>



</div>

    

  


    <div class="grid p-0 m-0"> 
    
    <div class="p-0" :class="store.visibleNotifications? 'col-9':'col-12'">
    
    <transition name="fade">
        <RouterView>

        </RouterView>
    </transition>
    </div>
    

 

    </div>





    <Dialog v-model:visible="showDateDialog" modal header="Periodo" :style="{ width: '25rem' }">
        <div class="grid">

            <div class="col-12 px-0 mx-0">
            <!-- Botones para selección rápida de fechas -->
            <Button text label="Hoy" @click="setDateRange(0)" class="p-button-text col-12 p-1 m-0" />
            <Button text label="Ayer" @click="setDateRange(1)" class="p-button-text col-12 p-1 m-0" />
            <Button text label="Últimos 7 días" @click="setDateRange(7)" class="p-button-text col-12 p-1 m-0" />
            <Button text label="Últimos 14 días" @click="setDateRange(14)" class="p-button-text col-12 p-1" />
            <Button text label="Últimos 28 días" @click="setDateRange(28)" class="p-button-text col-12 p-0" />
        </div>

        <!-- <Divider></Divider> -->
            <div class="col-12 " style="display: flex; flex-direction: column;">


                <span class="text-l" style="font-weight: bold;">Desde -  {{ formatDate(startDate) }} </span>
                <Calendar style="min-width: max-content;" v-model="TempStartDate"  />

            </div>

            <!-- <Divider></Divider> -->

            <div class="col-12 " style=" display: flex;flex-direction: column;">
                <span style="font-weight: bold; " class="text-l">Hasta - {{ formatDate(endDate) }} </span>
                <Calendar style="min-width: max-content;" v-model="TempEndDate"  showWeek />

            </div>


            <div class="col-12 p-0" style="display: flex; justify-content: center;">
                <div class="col-12" style="display: flex; justify-content: center;">
            <Button @click=" () => {
                    store.setDateRange(TempStartDate,TempEndDate);
                    showDateDialog = false;
                    store.fetchSalesReport();


            }">Aplicar</Button>
        </div>
            </div>


        </div>

    </Dialog>


    
    </div>

<!-- {{ store }} -->
<!-- {{ salesReport }} -->




</template>


<script setup>












import { onMounted, reactive, ref, watch,onUnmounted } from 'vue';
// import ProductService from '@/service/ProductService';
import { useLayout } from '@/layout/composables/layout';
import { useRoute } from 'vue-router';
import { URI } from '../../service/conection';
import {salesReport} from '../../service/valoresReactivosCompartidos'
import { formatToColombianPeso } from '../../service/valoresReactivosCompartidos';
import Loading from '../../components/Loading.vue';
import { PrimeIcons } from 'primevue/api';
import {useReportesStore} from '@/store/reportes.js'
import RepValorVentas from './RepValorVentas.vue';
import RepNotificaciones from './RepNotificaciones.vue';
const store = useReportesStore()
const { isDarkTheme } = useLayout();
import { useSitesStore } from '@/store/site';

const storeSite = useSitesStore()

const estadosDropValues = ref(['enviada', 'cancelada', 'en preparacion'])
const estadosDropValue = ref('enviada')
const ruta = useRoute()
const sites = ref([])
const selectedSites = ref([storeSite.site])
const showDateDialog = ref(false)
const startDate = ref(new Date(new Date().setDate(new Date().getDate() - 7))); // Fecha de inicio hace 7 días
const endDate = ref(new Date());















// function checkCustomDateRange() {
//     // Determina la diferencia en días entre las fechas seleccionadas
//     const diffTime = Math.abs(store.dateRange - TempStartDate.value);
//     const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)) + 1; // +1 para incluir ambos días en el rango

//     switch(diffDays) {
//         case 7:
//             selectedRangeName.value = 'Últimos 7 días';
//             break;
//         case 14:
//             selectedRangeName.value = 'Últimos 14 días';
//             break;
//         case 28:
//             selectedRangeName.value = 'Últimos 28 días';
//             break;
//         default:
//             selectedRangeName.value = ''; // No coincide con ningún rango predefinido
//     }
// }




const TempStartDate = ref(new Date()) // Fecha de inicio del período
const TempEndDate = ref(new Date())

const selectedRangeName = ref('');


// watch(estadosDropValue, (viejo,nuevo)=> {
//     if(viejo != nuevo){
//         fetchSalesReport()

//     }
// })

function setDateRange(days) {
    const today = new Date();
    const tomorrow = new Date(today);
    tomorrow.setDate(tomorrow.getDate() + 1); // Incrementa en uno para incluir el día de mañana

    const pastDate = new Date(today);
    pastDate.setDate(today.getDate() - days); // Ajustado para incluir el día de hoy en el rango si es necesario

    TempStartDate.value = pastDate;


    if (days == 1){
        TempEndDate.value = today;
        store.setDateRange(TempStartDate.value,TempEndDate.value)
        showDateDialog.value = false


    }else{
        TempEndDate.value = tomorrow;
        store.setDateRange(TempStartDate.value,TempEndDate.value)
        showDateDialog.value = false

    }

    


    store.fetchSalesReport()
    
    // Usando 'tomorrow' en lugar de 'today'
}

onMounted( () => {

    getSites().then(data => {
        sites.value = data

        store.setSelectedSites(selectedSites.value);
        // selectedSites.value = sites.value.filter(s => s.site_id != 12 && s.site_id != 13);
        // fetchSalesReport()


    } )
    // fetchSales()
    store.fetchSalesReport()    
})

// function setDateRange(days) {
//     const today = new Date();
//     const pastDate = new Date();
//     pastDate.setDate(today.getDate() - days + 1); // +1 para incluir el día de hoy en el rango

//     TempStartDate.value = pastDate;
//     TempEndDate.value = today;

//     applyDateSelection()
    
// }
function applyDateSelection() {
    checkCustomDateRange()
    showDateDialog.value = false
    startDate.value = TempStartDate.value;
    endDate.value = TempEndDate.value;
    showDateDialog = false;
     // Asegúrate de volver a buscar el informe de ventas con las nuevas fechas
}


const fetchSalesReport = async () => {
  const formattedStartDate = formatDate(startDate.value);
  const formattedEndDate = formatDate(endDate.value);
//   const siteIds = selectedSites.value.map(site => site.site_id).join(',');

  // Construir la URL con parámetros de consulta
  const queryParams = new URLSearchParams({
    site_ids: [],
    status: estadosDropValue.value,
    start_date: formattedStartDate,
    end_date: formattedEndDate
  });

  const url = `${URI}/sales_report?${queryParams.toString()}`;

  try {
    const response = await fetch(url, {
      method: 'GET', // Método GET especificado aquí
      headers: {
        'Content-Type': 'application/json',
        // Agrega aquí otros encabezados si son necesarios
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    salesReport.value = data


    // Maneja la respuesta
    console.log(data);
  } catch (error) {
    console.error('Fetch error:', error);
  }
};

watch([startDate, endDate], () => {
    // Esta función se ejecutará cada vez que cambien startDate o endDate
    fetchSalesReport(); // Llama a tu función que obtiene el reporte de ventas
}, { deep: true });


watch(() => store.order_status, (newValue, oldValue) => {
  // Esta función se ejecutará cada vez que order_status cambie.
  // Aquí puedes llamar a fetchSalesReport o cualquier otra lógica necesaria
  console.log(`El estado de orden ha cambiado de ${oldValue} a ${newValue}`);
  store.fetchSalesReport(); // Llamada al método de la tienda
});


watch(store.selectedSites, (nuevasSedes) => {
  store.setSelectedSites(nuevasSedes);
}, { deep: true });


const getSites = async() => {
    try {
        const response = await fetch(`${URI}/sites`)

        if(!response.ok){
            throw 'paila'
        }

        const data = await response.json()
        return data
        
    } catch (error) {
        console.log(error)
    }
}

const menus = ref([
    {
        name: 'Valor ventas',
        to: 'valor-ventas',
        icon:'fa-solid fa-dollar-sign'
    },
    // {
    //     name: 'No. Ordenes',
    //     to: 'no-ordenes',
    //     icon:'fa-solid fa-sort'
    // },
    // {
    //     name: 'Ticket promedio',
    //     to: 'ticket',
    //     icon: 'fa-solid fa-money-bill'
    // },
    {
        name: 'Ordenes',
        to: 'ordenes',
        icon:'fa-solid fa-table'
    }
])






const products = ref(null);
const lineData = reactive({
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
        {
            label: 'First Dataset',
            data: [65, 59, 80, 81, 56, 55, 40],
            fill: false,
            backgroundColor: '#2f4860',
            borderColor: '#2f4860',
            tension: 0.4
        },
        {
            label: 'Second Dataset',
            data: [28, 48, 40, 19, 86, 27, 90],
            fill: false,
            backgroundColor: '#00bb7e',
            borderColor: '#00bb7e',
            tension: 0.4
        }
    ]
});
const items = ref([
    { label: 'Add New', icon: 'pi pi-fw pi-plus' },
    { label: 'Remove', icon: 'pi pi-fw pi-minus' }
]);
const lineOptions = ref(null);
// const productService = new ProductService();

// onMounted(() => {
//     productService.getProductsSmall().then((data) => (products.value = data));
// });

const formatCurrency = (value) => {
    return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
};
const applyLightTheme = () => {
    lineOptions.value = {
        plugins: {
            legend: {
                labels: {
                    color: '#495057'
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: '#495057'
                },
                grid: {
                    color: '#ebedef'
                }
            },
            y: {
                ticks: {
                    color: '#495057'
                },
                grid: {
                    color: '#ebedef'
                }
            }
        }
    };
};

const applyDarkTheme = () => {
    lineOptions.value = {
        plugins: {
            legend: {
                labels: {
                    color: '#ebedef'
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: '#ebedef'
                },
                grid: {
                    color: 'rgba(160, 167, 181, .3)'
                }
            },
            y: {
                ticks: {
                    color: '#ebedef'
                },
                grid: {
                    color: 'rgba(160, 167, 181, .3)'
                }
            }
        }
    };
};

watch(
    isDarkTheme,
    (val) => {
        if (val) {
            applyDarkTheme();
        } else {
            applyLightTheme();
        }
    },
    { immediate: true }
);




































 // Fecha de finalización del período

// Formatear el período de fechas
const formattedPeriod = ref(`${startDate.value} - ${endDate.value}`)

function formatDate(dated) {
const date = new Date(dated)
  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, '0');
  const day = date.getDate().toString().padStart(2, '0');
  return `${year}-${month}-${day}`;
}


const selectedCountry = ref({})

const countries = ref()

watch([TempStartDate, TempEndDate], ([newStartDate, newEndDate]) => {
    if (newStartDate > newEndDate) {
        alert('La fecha de inicio debe ser anterior o igual a la fecha final.');
        // Ajusta las fechas según sea necesario, por ejemplo:
        TempEndDate.value = newStartDate;
    }
});



function saveState() {
    const state = {
        startDate: formatDate(startDate.value),
        endDate: formatDate(endDate.value),
        estadosDropValue: estadosDropValue.value,
        selectedSites: selectedSites.value.map(site => site.site_id),
        salesReport: salesReport.value,
    };
    localStorage.setItem('reportState', JSON.stringify(state));
}

// Cargar estado desde Local Storage
// function loadState() {
//     const state = JSON.parse(localStorage.getItem('reportState'));
//     if (state) {
//         startDate.value = new Date(state.startDate);
//         endDate.value = new Date(state.endDate);
//         estadosDropValue.value = state.estadosDropValue;
//         // Aquí necesitas asegurarte de reconstruir los objetos de las sedes si solo guardaste los IDs
//         selectedSites.value = state.selectedSites; // Asumiendo que tienes una manera de reconstruir los objetos de las sedes a partir de los IDs
//         salesReport.value = state.salesReport;
//     }
// }

// // Hook para cargar el estado al montar el componente
// watch([startDate, endDate, estadosDropValue, selectedSites, salesReport], () => {
//     saveState();
// }, { deep: true }); // La opción 'deep' es importante si estás observando objetos o arrays para detectar cambios dentro de ellos

// // Hook para cargar el estado al montar el componente
// onMounted(() => {
//     loadState();
// });






</script>


<style scoped>

*:focus{
    /* box-shadow: none; */
    border: none;
    outline: none;
    transition: all ease .3s;
}



*{
    box-shadow: none;
    /* border: none; */
    outline: none;
    transition: all ease .3s;
}

.btn-ocultar{
    /* outline: none !important; */
    box-shadow: none    ;
    border: none !important;
    /* background-color: ; */
}
.fade-enter-active,.fade-leave-active {
  transition: all ease  .3s;
  
}


.noti-enter-active,.noti-leave-active {
  transition: all ease  1s;
  
}

 .fade-leave-to{
  opacity: 0;
  transform: translateY(20rem);

}

/* .fade-enter-to  {
  opacity: 0;
  transform: translateX(20rem);
 
} */


.fade-leave-from  {
  opacity: 1;
  transform: translateY(20rem);

}
 /*
*/

 .fade-enter-from {
  opacity: 0;
  transform: translateY(20rem);
  filter: blur(10px);
  /* filter: blur(0); */
  
}


.noti-enter-from {
  opacity: 0;
  transform: translateY(20rem);
  filter: blur(10px);
  /* filter: blur(0); */
  
}

.noti-enter-to {
    opacity: 1;
  filter: blur(0);
  
}



.fade-enter-to {
  opacity: 1;
  filter: blur(0);

  
} 



/* 
.fade-leave-from {
  opacity: 0;
  transform: translateX(0);
  
} 


.fade-leave-to {
  opacity: 1;
  transform: translateX(20rem);
  
}   */

*{
    transition: .3s ease all;
}

</style>