<template>
    <div class="grid">

        <div class="grid col-12 ">
            <div class="col-12 lg:col-6 m-0">
                <div class="card mb-0 ">
                    <div class="flex justify-content-between mb-3">
                        <div>
                            <span class="block text-500 font-medium mb-3">Venta bruta</span>
                            <div class="text-900 font-medium text-xl">
                                {{ formatToColombianPeso(store.salesReport?.total_sales?.total_sales) || '$0' }}</div>
                        </div>
                        <div class="flex align-items-center justify-content-center bg-blue-100 border-round"
                            style="width: 2.5rem; height: 2.5rem">
                            <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
                        </div>
                    </div>

                    <div style="display:flex; align-items: center;">
                        <span class="text-500">Total de ordenes</span>
                    
                    
                    <RouterLink to="/reporte-ventas/ordenes">
                        <Button outlined class="p-2 font-medium ml-3  " :style="store.order_status == 'enviada'? 'color:var(--blue-500);background-color:var(--blue-100)': 'color:rgba(255, 99, 132, 1);background-color:var(--pink-100)'" style="border: none ;"> ordenes</Button>

                    </RouterLink>    <span class=" font-medium ml-3" :style="store.order_status == 'enviada'? 'color:var(--blue-500)': 'color:rgba(255, 99, 132, 1)'">{{ store.salesReport?.total_sales?.total_orders || 0 }} </span>
                    </div>
                    
                </div>
            </div>
            <div class="col-12 lg:col-6 " style="height: ;">
                <div class="card mb-0" style="height: 100%;">
                    <div class="flex justify-content-between mb-3">
                        <div>
                            <span class="block text-500 font-medium mb-3">Ticket promedio</span>
                            <div class="text-900 font-medium text-xl">
                                {{ formatToColombianPeso(store.salesReport?.total_sales?.average_ticket) || '$0' }}</div>
                        </div>
                        <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
                            style="width: 2.5rem; height: 2.5rem">
                            <i class="pi pi-map-marker text-orange-500 text-xl"></i>
                        </div>
                    </div>
                    <!-- <span class="text-green-500 font-medium">%52+ </span> -->
                    <span class="text-500">Valor de la venta promedio</span>
                </div>
            </div>


            <!-- <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Customers</span>
                        <div class="text-900 font-medium text-xl">28441</div>
                    </div>
                    <div class="flex align-items-center justify-content-center bg-cyan-100 border-round" style="width: 2.5rem; height: 2.5rem">
                        <i class="pi pi-inbox text-cyan-500 text-xl"></i>
                    </div>
                </div>
                <span class="text-green-500 font-medium">520 </span>
                <span class="text-500">newly registered</span>
            </div>
        </div> -->
            <!-- <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Comments</span>
                        <div class="text-900 font-medium text-xl">152 Unread</div>
                    </div>
                    <div class="flex align-items-center justify-content-center bg-purple-100 border-round" style="width: 2.5rem; height: 2.5rem">
                        <i class="pi pi-comment text-purple-500 text-xl"></i>
                    </div>
                </div>
                <span class="text-green-500 font-medium">85 </span>
                <span class="text-500">responded</span>
            </div>
        </div> -->

            <!-- <div class="col-12 xl:col-6">
            <div class="card">
                <h5>Recent Sales</h5>
                <DataTable :value="products" :rows="5" :paginator="true" responsiveLayout="scroll">
                    <Column style="width: 15%">
                        <template #header> Image </template>
                        <template #body="slotProps">
                            <img :src="'demo/images/product/' + slotProps.data.image" :alt="slotProps.data.image" width="50" class="shadow-2" />
                        </template>
                    </Column>
                    <Column field="name" header="Name" :sortable="true" style="width: 35%"></Column>
                    <Column field="price" header="Price" :sortable="true" style="width: 35%">
                        <template #body="slotProps">
                            {{ formatCurrency(slotProps.data.price) }}
                        </template>
                    </Column>
                    <Column style="width: 15%">
                        <template #header> View </template>
                        <template #body>
                            <Button icon="pi pi-search" type="button" class="p-button-text"></Button>
                        </template>
                    </Column>
                </DataTable>
            </div>
            <div class="card">
                <div class="flex justify-content-between align-items-center mb-5">
                    <h5>Best Selling Products</h5>
                    <div>
                        <Button icon="pi pi-ellipsis-v" class="p-button-text p-button-plain p-button-rounded" @click="$refs.menu2.toggle($event)"></Button>
                        <Menu ref="menu2" :popup="true" :model="items"></Menu>
                    </div>
                </div>
                <ul class="list-none p-0 m-0">
                    <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                        <div>
                            <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Space T-Shirt</span>
                            <div class="mt-1 text-600">Clothing</div>
                        </div>
                        <div class="mt-2 md:mt-0 flex align-items-center">
                            <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                                <div class="bg-orange-500 h-full" style="width: 50%"></div>
                            </div>
                            <span class="text-orange-500 ml-3 font-medium">%50</span>
                        </div>
                    </li>
                    <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                        <div>
                            <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Portal Sticker</span>
                            <div class="mt-1 text-600">Accessories</div>
                        </div>
                        <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                            <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                                <div class="bg-cyan-500 h-full" style="width: 16%"></div>
                            </div>
                            <span class="text-cyan-500 ml-3 font-medium">%16</span>
                        </div>
                    </li>
                    <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                        <div>
                            <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Supernova Sticker</span>
                            <div class="mt-1 text-600">Accessories</div>
                        </div>
                        <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                            <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                                <div class="bg-pink-500 h-full" style="width: 67%"></div>
                            </div>
                            <span class="text-pink-500 ml-3 font-medium">%67</span>
                        </div>
                    </li>
                    <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                        <div>
                            <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Wonders Notebook</span>
                            <div class="mt-1 text-600">Office</div>
                        </div>
                        <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                            <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                                <div class="bg-green-500 h-full" style="width: 35%"></div>
                            </div>
                            <span class="text-green-500 ml-3 font-medium">%35</span>
                        </div>
                    </li>
                    <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                        <div>
                            <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Mat Black Case</span>
                            <div class="mt-1 text-600">Accessories</div>
                        </div>
                        <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                            <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                                <div class="bg-purple-500 h-full" style="width: 75%"></div>
                            </div>
                            <span class="text-purple-500 ml-3 font-medium">%75</span>
                        </div>
                    </li>
                    <li class="flex flex-column md:flex-row md:align-items-center md:justify-content-between mb-4">
                        <div>
                            <span class="text-900 font-medium mr-2 mb-1 md:mb-0">Robots T-Shirt</span>
                            <div class="mt-1 text-600">Clothing</div>
                        </div>
                        <div class="mt-2 md:mt-0 ml-0 md:ml-8 flex align-items-center">
                            <div class="surface-300 border-round overflow-hidden w-10rem lg:w-6rem" style="height: 8px">
                                <div class="bg-teal-500 h-full" style="width: 40%"></div>
                            </div>
                            <span class="text-teal-500 ml-3 font-medium">%40</span>
                        </div>
                    </li>
                </ul>
            </div>
        </div> -->
            <div class="col-12 ">
                <div class="card">
                    <h5 style="background-color: ;"   >Historico de cantidad de ordenes <span :style="store.order_status == 'enviada'? 'color:var(--blue-500)': 'color:rgba(255, 99, 132, 1)'">{{ store.order_status }}s</span>  </h5>
                    <!-- <Chart type="bar" :data="lineData" :options="lineOptions" /> -->
                    <div class="card" >
                        <Button class="p-0" text @click="visible_graph = true" size="small" style="border: none;" :style="store.order_status == 'enviada'? 'color:var(--blue-500)': 'color:rgba(255, 99, 132, 1)'"><i class="text-4xl" style="transform: rotate(45deg);;" :class="PrimeIcons.ARROW_A"></i></Button>
                        <Chart type="line" :data="store.ordersCharData" :options="chartOptions" class="h-30rem" />
                    </div>
                </div>


            </div>
        </div>


        <Dialog v-model:visible="visible_graph" modal header="Periodo" :style="{ width: '90vw',height:'max-content' }">
<!-- <RepValorVentas></RepValorVentas> -->     
                        <Chart type="line" :data="store.ordersCharData" :options="chartOptions" style="height: 60vh;" />

</Dialog>

    </div>
</template>

<!-- 
<script setup>












import { onMounted, reactive, ref, watch } from 'vue';
// import ProductService from '@/service/ProductService';
import { useLayout } from '@/layout/composables/layout';
import { useRoute } from 'vue-router';

const { isDarkTheme } = useLayout();


const ruta = useRoute()







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




































const date = ref(false)
const startDate = ref(new Date()) // Fecha de inicio del período
const endDate = ref(new Date())   // Fecha de finalización del período

// Formatear el período de fechas
const formattedPeriod = ref(`${startDate.value} - ${endDate.value}`)

function formatDate(date) {
    if (!date) {
        return 'periodo'
    }
    const mes = date.getMonth() + 1; // Extraer el mes (agregar 1 porque los meses comienzan desde 0)
    const dia = date.getDate(); // Extraer el día
    const año = date.getFullYear(); // Extraer el año

    // Formatear la fecha con ceros a la izquierda si es necesario
    const fechaFormateada = `${mes.toString().padStart(2, '0')}/${dia.toString().padStart(2, '0')}/${año.toString().slice(-2)}`;

    return fechaFormateada;
}


const selectedCountry = ref({})

const countries = ref()


</script> -->


<script setup>
import { ref, onMounted } from "vue";
import { salesReport, formatToColombianPeso } from "../../service/valoresReactivosCompartidos";
import { URI } from "../../service/conection";
import {useReportesStore} from '@/store/reportes.js'
import { PrimeIcons } from "primevue/api";
const store = useReportesStore()
const visible_graph = ref(false)
onMounted(() => {
    // store.fetchDilyReport()
    chartOptions.value = setChartOptions();
});


const chartData = ref();
const chartOptions = ref();





const fetchSalesReport = async () => {
    //   const formattedStartDate = formatDate(startDate.value);
    //   const formattedEndDate = formatDate(endDate.value);
    //   const siteIds = selectedSites.value.map(site => site.site_id).join(',');

    // Construir la URL con parámetros de consulta
    const queryParams = new URLSearchParams({
        site_ids: '7',
        status: 'enviada',
        start_date: '2024-01-01',
        end_date: '2024-02-08'
    });

    const url = `${URI}/daily_sales?${queryParams.toString()}`;

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
        // salesReport.value = data
        return (data)


        // Maneja la respuesta
        console.log(data);
    } catch (error) {
        console.error('Fetch error:', error);
    }
};



// fetchSalesReport()



// onMounted(() => {
//     store.fetchSalesReport()    

// })






const setChartOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--text-color');
    const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
    const surfaceBorder = documentStyle.getPropertyValue('--surface-border');

    return {
        maintainAspectRatio: true,
        aspectRatio: 3,
        plugins: {
            legend: {
                labels: {
                    color: textColor
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder,
                    display:false
                }
            },
            y: {
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder,
                    
                }
            }
        }
    };
}





</script>