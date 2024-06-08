<template>
    <Loading v-if="guardando" tittle="guardando"></Loading>
    <Loading v-if="cargando" tittle="cargando horario"></Loading>

    <p class="text-center my-6 text-4xl" style="font-weight: bold;"> Horario</p>
    <!-- {{ horario }} -->

    <!-- {{ horario }} -->
    <Dialog v-model:visible="isEditing" style="width: 30rem;" modal>
        <div class="m-auto p-0" style="max-width: 600px; ">
            <DataTable ref="dt" class="p-0" :value="horario" dataKey="id" style="border: 1rem;overflow: hidden;" :rows="7"
                paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                :rowsPerPageOptions="[5, 10, 25, 100]"
                currentPageReportTemplate="Mostrando {first} a {last} de {totalRecords} scheldules"
                responsiveLayout="scroll" scrollable scroll-height="62vh">


                <!-- <Column class="p-2" selectionMode="multiple" headerStyle="width: 3rem; " frozen></Column> -->

                <Column class="p-2" field="day_of_week" header="Dia" headerStyle="width:5rem; min-width:5rem; ">
                    <template #body="scheldule">
                        <span class="p-column-title">Code</span>
                        {{ dias[scheldule.data.day_of_week - 1] }}

                    </template>
                </Column>





                <Column class="p-2" field="opening_time" header="Apertura" headerStyle="width:5rem; min-width:5rem;">
                    <template #body="scheldule">
                        <span class="p-column-title">Code</span>
                        <Calendar :disabled="!isEditing" hourFormat="12" timeOnly v-model="scheldule.data.opening_time">
                        </Calendar>
                    </template>
                </Column>

                <Column class="p-2" field="closing_time" header="Cierre" headerStyle="width:5rem; min-width:3rem;">
                    <template #body="scheldule">
                        <span class="p-column-title">Code</span>
                        <Calendar :disabled="!isEditing" hourFormat="12" timeOnly v-model="scheldule.data.closing_time">
                        </Calendar>
                    </template>
                </Column>






            </DataTable>







        </div>

        <template #footer>

            <div class="col-12 p-2 m-0" style="display: flex;gap: 1rem; justify-content: end;">
                <Button outlined severity="danger" @click="isEditing = false" style="font-weight: bold;border-radius: 0.3rem; " class="m-0"
                    label="Cancelar" ></Button>
                    <Button severity="success" @click="saveChanges" style="font-weight: bold;border-radius: 0.3rem; " class="m-0"
                    label="Guardar"></Button>
            </div>

        </template>
    </Dialog>

    <div class="m-auto p-0" style="max-width: 600px; ">

        <DataTable showGridlines ref="dt" class="p-0" :value="horario" dataKey="id" style="border: 1rem;overflow: hidden;" :rows="7"
            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[5, 10, 25, 100]"
            currentPageReportTemplate="Mostrando {first} a {last} de {totalRecords} scheldules" responsiveLayout="scroll"
            scrollable scroll-height="62vh">



            <Column class="p-2" field="day_of_week" header="Dia" headerStyle="width:2rem;">
                <template #body="scheldule">
                    <span class="p-column-title">Code</span>
                    {{ dias[scheldule.data.day_of_week - 1] }}

                </template>
            </Column>

            <Column class="p-2" field="opening_time" header="Apertura" headerStyle="width:2rem">
                <template #body="scheldule">
                    <span class="p-column-title">Code</span>
                    <span :disabled="!isEditing" hourFormat="12" timeOnly> {{ formatearHora(scheldule.data.opening_time)
                    }}</span>
                </template>
            </Column>

            <Column class="p-2" field="closing_time" header="Cierre" headerStyle="width:2rem;">
                <template #body="scheldule">
                    <span class="p-column-title">Code</span>
                    <span :disabled="!isEditing" hourFormat="12" timeOnly> {{ formatearHora(scheldule.data.closing_time)
                    }}</span>
                </template>
            </Column>

        </DataTable>


        <div class="col-12 p-0 mt-5" style="display: flex; justify-content: end;">
            <Button severity="danger" @click="enableEditing" size="small" label="Modificar El horario" class="m-0 mb-3"
            style="font-weight: bold;border-radius: 0.3rem;"></Button>

        </div>
        


    </div>
</template>
        
<script setup>
import { URI } from '../../service/conection';
import { onMounted, ref } from 'vue'
import Loading from '@/components/Loading.vue'
const isEditing = ref(false);

function formatearHora(fecha) {
    // Extraer la hora y los minutos
    var hora = fecha.getHours();
    var minutos = fecha.getMinutes();

    // Convertir a formato de 12 horas y determinar AM o PM
    var ampm = hora >= 12 ? 'PM' : 'AM';
    hora = hora % 12;
    hora = hora ? hora : 12; // El '0' se convierte a '12'

    // Formatear la hora para mostrarla en formato hh:mm AM/PM
    var horaFormateada = hora + ':' + minutos.toString().padStart(2, '0') + ' ' + ampm;

    return horaFormateada;
}


const enableEditing = () => {
    isEditing.value = true;
};

const guardando = ref(false)
const horario = ref([])
const cargando = ref(false)

onMounted(() => {
    const site_id = localStorage.getItem('siteId')

    getHorarios(site_id).then(data => horario.value = data)
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
        // Formatear los datos para enviar solo la hora en formato 24 horas
        const horarioToSend = horario.value.map(item => {
            const options = { hour12: false, hour: '2-digit', minute: '2-digit' };
            
            const openingTime  = item.opening_time instanceof Date ? item.opening_time.toLocaleTimeString([], options) : item.opening_time;
            const closingTime  = item.closing_time instanceof Date ? item.closing_time.toLocaleTimeString([], options) : item.closing_time;

            return {
                ...item,
                opening_time: openingTime,
                closing_time: closingTime
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
            throw new Error('Error al enviar los datos');

        // Después de enviar los datos, deshabilitar la edición
        isEditing.value = false;
        guardando.value = false
    } catch (error) {
        console.log(error);
        guardando.value = false
    }
};



const dias = ref(["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"])

</script>

