<template>


    <Button size="small" class="py-2"  severity="success" @click="exportCSV"> <i class="pr-3 m-0 " :class="PrimeIcons.DOWNLOAD" ></i> Descargar reporte</Button>

    <div class="flex flex-wrap align-items-center justify-content-between gap-2 my-5 pl-0 ml-0">
                    <span class="text-l p-0  text-900 font-bold">Ordenes {{ store.order_status }}s entre {{ store.formatDate(store.dateRange.startDate)  }} y {{ store.formatDate(store.dateRange.endDate)  }} </span>
                    <div class="flex p-0  flex-column md:flex-row md:justify-content-between md:align-items-center" style="background-color: ;">
                           
                            <span class="block mt-2 md:mt-0 py-0">
                                <!-- <i class="pi pi-search pr-3" /> -->
                                <InputText class="p-2"  v-model="filters['global'].value" placeholder="Buscar..." />
                            </span>
                        </div>
                </div>



        <DataTable paginator  :value="store.salesReport.total_sales.orders_info" tableStyle="min-width: 50rem"
                
        
        :rows="10" :filters="filters"
                  paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                  :rowsPerPageOptions="[5, 10, 25,100]"
                    stripedRows=""
                  currentPageReportTemplate="Mostrando {first} a {last} de {totalRecords} ordenes"
                  responsiveLayout="scroll" scrollable >

                  
            <template>
                
            </template>
            <Column field="order_id" header="Id" class="py-0" headerStyle="width:12rem;min-width:6rem">
            
                <template #body="slotProps">
                 <P style="min-width: max-content;">
                    {{slotProps.data.order_id}}
                 </P>   
                </template>
            </Column>
            <Column field="total_price" header="Monto" class="py-0" headerStyle="min-width:max-content; width:5rem">
                <template #body="slotProps">
             
                    {{ formatToColombianPeso(slotProps.data.total_order_price)  }}
                </template>
            </Column>


                
      

            <Column field="site_name" header="Sede" class="py-0" headerStyle="min-width:max-content; width:6rem">
                <template #body="slotProps">
                   
                    {{ formatToColombianPeso(slotProps.data.site_name)  }}
                </template>
            </Column>


        
            <Column field="status.timestamp" class="px-1 py-0" header="Fecha" headerStyle="width:50rem; min-width:10rem ">
                <template #body="slotProps">
           
                    {{ slotProps.data.latest_status_timestamp?.split('T')[0]}} 
                    {{ slotProps.data.latest_status_timestamp?.split('T')[1]?.split(':')?.slice(0,2)?.join(':')}}
                </template>
            </Column>

            <Column field="status.timestamp" class="px-1 py-0" header="Hora" headerStyle="width:50rem; min-width:max-content ">
                <template #body="slotProps">
           
                    <!-- {{ slotProps.data.latest_status_timestamp?.split('T')[0]}}  -->
                    {{ slotProps.data.latest_status_timestamp?.split('T')[1]?.split(':')?.slice(0,2)?.join(':')}}
                </template>
            </Column>

            
            <Column field="status.timestamp" class="px-1 py-0" header="Domicilio" headerStyle="width:6rem; min-width:max-content">
                <template #body="slotProps">
           
                    ${{ slotProps.data.delivery_price}} 
                   
                </template>
            </Column>


            <Column field="status.timestamp" class="px-1 py-0" header="Metodo de pago" headerStyle="width:10rem; min-width:12rem">
                <template #body="slotProps">
           
                    ${{ slotProps.data.payment_method}} 
                   
                </template>
            </Column>

            <Column field="status.timestamp" class="px-1 py-0" header="Nombre del usuario" headerStyle="width:12rem; min-width:13rem ">
                <template #body="slotProps">
           
                    {{ slotProps.data.user_name .slice(0,40)}} 
                   
                </template>
            </Column>


            <Column field="status.timestamp" class="px-1 py-0" header="Telefono del usuario" headerStyle="width:12rem; min-width:11rem ">
                <template #body="slotProps">
           
                    {{ slotProps.data.user_phone}} 
                   
                </template>
            </Column>


            <Column field="status.timestamp" class="px-1 py-0" header="Direccion del usuario" headerStyle="width:12rem; min-width:30rem ">
                <template #body="slotProps">
           
                    {{ slotProps.data.user_address}} 
                   
                </template>
            </Column>

                 

            <Column class="px-1 py-0" v-if="store.order_status == 'cancelada'" headerStyle="width:20rem; min-width:8rem; " field="status.reazon" header="Responsable">
                <template #body="slotProps">
                
                   <span class="motivo">{{ slotProps.data.responsible?.toLowerCase()}}.</span> 
                </template>
            </Column>



            <Column class="px-1 py-0" v-if="store.order_status == 'cancelada'" headerStyle="width:30rem;min-width:40rem; " field="status.reazon" header="Motivo">
                <template #body="slotProps">
                
                   <span class="motivo">{{ slotProps.data.reason?.toLowerCase()}}.</span> 
                </template>
            </Column>


  

            

         
            <Column header="Status" class="px-1 py-0"> 
                <template #body="slotProps">
                    <Tag :value="slotProps.data.current_status" :severity="getSeverity(slotProps.data?.current_status)" />
                </template>
            </Column>
            

        
            <Column class="px-1 py-0" header="" frozen alignFrozen="right" headerStyle="width:0.5rem; max-width:0.5rem ">
                <template #body="slotProps">
                    <Button style="width: min-content;" @click="store.setVisibleOrder(true,slotProps.data)" text ><i class="text-2xl  p-0" :class="PrimeIcons.EYE"></i></Button>
                </template>
            </Column>



            











        </DataTable>




    <OrderDialog>

    </OrderDialog>

</template>


<script setup>
import {useReportesStore} from '@/store/reportes.js'
import { formatToColombianPeso, salesReport } from '../../service/valoresReactivosCompartidos';
import { PrimeIcons } from 'primevue/api';
import {onBeforeMount} from 'vue'
import { FilterMatchMode } from 'primevue/api';
import {ref} from 'vue'
import OrderDialog from '../../components/orderDialog.vue';
import * as XLSX from 'xlsx';

const filters = ref(null);




const store = useReportesStore()
onBeforeMount(() => {
    initFilters();
    // getSites()
});



const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};


const getSeverity = (state) => {
    switch (state) {
        case 'enviada':
            return 'success';

        // case 'LOWSTOCK':
        //     return 'warning';

        case 'cancelada':
            return 'danger';

        default:
            return null;
    }
};


const obtenerDatosFiltrados = async () => {
    

    let Orders1 = [...store.salesReport.total_sales.orders_info];

    store.order_status = store.order_status == 'enviada' ? 'cancelada' : 'enviada';
    // Esperamos a que se complete la operación asincrónica
    await store.fetchSalesReport();

    // Ahora podemos trabajar con los datos actualizados
    Orders1 = Orders1.concat([...store.salesReport.total_sales.orders_info]);
    // store.order_status = store.order_status == 'enviada' ? 'cancelada' : 'enviada';

    if (!filters?.value?.global.value) {
        return Orders1
    }

    const filtroGlobal = filters.value.global.value.trim().toLowerCase();


    // store.fetchSalesReport()

    return Orders1.filter(order => {
        // Asumiendo que `order` es un objeto y comprobamos cada propiedad
        return Object.values(order).some(value =>
            value && value.toString().trim().toLowerCase().includes(filtroGlobal)
        );
    });
}; 



const exportCSV = async() => {
    const datosFiltrados = await obtenerDatosFiltrados();
    const data = datosFiltrados.map(order => ({
        "Orden No": order.order_id,
        "Monto": order.total_order_price,
        "Sede": order.site_name,
        "Fecha": order.latest_status_timestamp?.split('T')[0],
        "Hora": order.latest_status_timestamp?.split('T')[1]?.split(':')?.slice(0,2)?.join(':'),
        "Estado": order.current_status,
        "Responsable": order.responsible ? `cancelada por ${order.responsible}` : 'no aplica',
        "razon de la cancelacion": order.reason || 'no aplica',
        "Domicilio": order.delivery_price,
        "Metodo de pago": order.payment_method,
        "Nombre del usuario": order.user_name,
        "telefono del usuario": order.user_phone,
        "direccion del usuario": order.user_address
    }));

    const worksheet = XLSX.utils.json_to_sheet(data);

    // Calcular el ancho máximo de cada columna
    const colWidths = data.reduce((widths, row) => {
        Object.keys(row).forEach((key, i) => {
            const contentLength = row[key]?.toString().length || 0;
            widths[i] = Math.max(widths[i] || 10, contentLength);
        });
        return widths;
    }, []);

    worksheet["!cols"] = colWidths.map(maxWidth => ({
        wch: maxWidth
    }));

    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "ventas");
    XLSX.writeFile(workbook, "reporte de ventas salchimonster.xlsx");
};





// exportCSV()
</script>

<style scoped>




*{
    transition: all ease .3s;
}

.motivo{
    text-transform: capitalize;
}


</style>



