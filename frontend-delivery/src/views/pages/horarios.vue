<template>

    <Loading v-if="guardando" tittle="guardando"></Loading>
    <Loading v-if="cargando" tittle="cargando horario"></Loading>

    <p class="text-center my-6 text-4xl" style="font-weight: bold;"> Horario</p>
    <!-- {{ horario }} -->

    <!-- {{ horario }} -->
    <div class="m-auto p-2" style="max-width: 600px; box-shadow: 0 0 20px rgba(0, 0, 0, 0.31);border-radius: 1rem;">
        <Button @click="enableEditing" size="small" class="m-3" outlined style="font-weight: bold;border-radius: 0.5rem;">Modificar</Button>
        <DataTable ref="dt" class="p-5" :value="horario" dataKey="id" style="border: 1rem;overflow: hidden;" :rows="7"
            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[5, 10, 25, 100]"
            currentPageReportTemplate="Mostrando {first} a {last} de {totalRecords} scheldules" responsiveLayout="scroll"
            scrollable scroll-height="62vh">


            <!-- <Column class="p-2" selectionMode="multiple" headerStyle="width: 3rem; " frozen></Column> -->

            <Column  class="p-2" field="day_of_week" header="Dia" 
                headerStyle="width:5rem; min-width:5rem; ">
                <template #body="scheldule">
                    <span class="p-column-title">Code</span>
                    {{ dias[scheldule.data.day_of_week - 1] }}

                </template>
            </Column>

            



            <Column class="p-2" field="opening_time" header="Apertura" 
    headerStyle="width:5rem; min-width:5rem;">
    <template #body="scheldule">
        <span class="p-column-title">Code</span>
        <Calendar :disabled="!isEditing" timeOnly v-model="scheldule.data.opening_time" ></Calendar>
    </template>
</Column>

<Column class="p-2" field="closing_time" header="Cierre" 
    headerStyle="width:5rem; min-width:5rem;">
    <template #body="scheldule">
        <span class="p-column-title">Code</span>
        <Calendar :disabled="!isEditing" timeOnly v-model="scheldule.data.closing_time" ></Calendar>
    </template>
</Column>





        </DataTable>
        <div class="col-12" style="display: flex; justify-content: end;">
            <Button @click="saveChanges" style="font-weight: bold;border-radius: 0.5rem;d " class="">Guardar</Button>

        </div>


    </div>
</template>
        
<script setup>
import { URI } from '../../service/conection';
import { onMounted, ref } from 'vue'
import Loading from '@/components/Loading.vue'
const isEditing = ref(false);

const enableEditing = () => {
    isEditing.value = true;
};

const guardando = ref(false)
const horario = ref([])
const cargando = ref(false)

onMounted(() => {
    getHorarios(1).then(data => horario.value = data)
})


const getHorarios = async () => {

    cargando.value = true
    const site_id = localStorage.getItem('siteId')
    try {
        const response = await fetch(`${URI}/site-schedule/${site_id}/`)
        if (!response.ok)
            throw ('paila')

        const data = await response.json()
        // Convertir opening_time de cadena de texto a objeto de fecha
        data.forEach(item => {
            item.opening_time = new Date(`1970-01-01T${item.opening_time}`);
            item.closing_time = new Date(`1970-01-01T${item.closing_time}`);
        });
        cargando.value = false

        return data
    } catch (error) {
        cargando.value = false

        console.log(error)
    }
}



const saveChanges = async () => {
    guardando.value = true
    try {
        // Formatear los datos para enviar solo la hora
        const horarioToSend = horario.value.map(item => {
            const openingTime  = item.opening_time instanceof Date ? item.opening_time.toLocaleTimeString() : item.opening_time;
            const closing_time = item.closing_time instanceof Date ? item.closing_time.toLocaleTimeString() : item.closing_time;

            return {
                ...item,
                opening_time: openingTime.split(' ')[0],
                closing_time: closing_time.split(' ')[0] // Obtener solo la hora de la cadena de fecha y hora
            };
        });

        // Enviar los horarios modificados al servidor
        const response = await fetch(`${URI}/site-schedule/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(horarioToSend)
        });

        if (!response.ok)
            throw ('Error al enviar los datos');

        // Después de enviar los datos, deshabilitar la edición
        isEditing.value = false;
        guardando.value = false
    } catch (error) {
        console.log(error);
        guardando.value = false

    }
};


const dias = ref(["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"])

</script>

