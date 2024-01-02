<script setup>


import { ref, onMounted, onBeforeMount, computed, cloneVNode } from 'vue';
import { useToast } from 'primevue/usetoast';
import {
    curentSite, getSiteDocument, curentSiteDocuments,
    getSiteDocumentInfo
} from '@/service/dropDownAux';
import { URI } from '../../service/conection';
// import { getUsers, } from '@/service/userServices'
// import { URI } from "@/service/conection.js" 
// import { getSiteDocument } from '../../service/dropDownAux';
import ProductService from '@/service/ProductService';
// import { ref, onMounted } from 'vue';
// import { useToast } from 'primevue/usetoast';
import { useConfirm } from 'primevue/useconfirm';
import { uploadPDF } from '@/service/sendFileService.js'
import { useRoute } from 'vue-router';
const documents = ref([])
const file = ref()
const currentdocument = ref()
const documentsDropValues = ref([
    "CÁMARA DE COMERCIO",
    "USO DE SUELOS",
    "RUT",
    "BOMBEROS",
    "CONCEPTO SANITARIO",
    "SAYCO Y ACIMPRO"
])

const currentSite = ref({})

onMounted(() => {
      const storedSiteData = localStorage.getItem('currentSiteFiles');
      if (storedSiteData) {
        currentSite.value = JSON.parse(storedSiteData);
      }
    });

const documentType = ref('')
const documentRenovationDate = ref('')
const route = useRoute()

const toast = useToast()

documents.value = curentSiteDocuments.value

const handleFileChange = (event) => {
    // Accede al archivo seleccionado a través del objeto de evento
    const selectedFile = event.target.files[0];

    if (selectedFile) {
        // Aquí puedes realizar acciones con el archivo seleccionado, como cargarlo al servidor
        console.log('Archivo seleccionado:', selectedFile);
        file.value = selectedFile
    }

}

const uploadPDFInfo = async (data) => {
    let Method = "post"
    const queryUrl = `${URI}/site-document/`
    const requestOptions = {
        method: Method,
        headers: {
            'Content-Type': 'application/json' // Asegúrate de establecer el tipo de contenido adecuado
        },
        body: JSON.stringify(data)
    };
    await fetch(queryUrl, requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
        })
        .catch(error => {
        });
}

const updatePDFInfo = async (data,document_id) => {
    let Method = "put"
    const queryUrl = `${URI}/site-document/${document_id}`
    const requestOptions = {
        method: Method,
        headers: {
            'Content-Type': 'application/json' // Asegúrate de establecer el tipo de contenido adecuado
        },
        body: JSON.stringify(data)
    };
    await fetch(queryUrl, requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
        })
        .catch(error => {
        });
}


onMounted(() => {
    getSiteDocumentInfo(route.params.site_id)
    console.log(curentSite)
});

const display = ref(false);
const display2 = ref(false);

const upload = (file, document_type, site_name) => {
    const existe = curentSiteDocuments.value.some(objeto => objeto.document_type == documentType.value);
    console.log(documents,documentType.value)
    console.log(existe)
    if (!existe ) {
        const data = {
            "document_name": `${currentSite.value.site_name} ${documentType.value}`,
            "document_type": documentType.value,
            "renovation_date": documentRenovationDate.value,
            "site_id": route.params.site_id
        }

        uploadPDFInfo(data)
        uploadPDF(file, document_type, site_name)
        toast.add({ severity: 'success', summary: `hecho`, detail: '', life: 3000 })
        close()
    }else{
        // console.log(existe)
        toast.add({ severity: 'error', summary: `Ya hay cargado un ${documentType.value} para ${currentSite.value.site_name} pero puede renovarlo si gusta  `, detail: '', life: 3000 })
    }


};

const update = (file, document_type, site_name) => {
    // const existe = documents.value.some(objeto => objeto.document_type == documentType.value);
    console.log(documents,documentType.value)

    if (4 ) {
        const data = {
            "document_name": `${currentdocument.value.document_name}`,
            "document_type": currentdocument.value.document_type,
            "renovation_date": documentRenovationDate.value,
            "site_id": route.params.site_id
        }
        console.log(data)

        updatePDFInfo(data,currentdocument.value.document_id)
        uploadPDF(file, document_type, site_name)
        toast.add({ severity: 'success', summary: `hecho`, detail: '', life: 3000 })
        close()
    }else{
        // console.log(existe)
        toast.add({ severity: 'error', summary: `Ya hay cargado un ${documentType.value} para ${currentSite.value.site_name} pero puede renovarlo si gusta  `, detail: '', life: 3000 })
    }


};

const open = (currentdoc) => {
        display.value = true;
        currentdocument.value = currentdoc
    };

    const open2 = (currentdoc) => {
        display2.value = true;
        currentdocument.value = currentdoc
    };
    const close = () => {
        display.value = false;
        display2.value = false;
        // file.value = null
    }

</script>

<template>
     <Toast />
    <div class="grid">
        <div class="col-12">
            <div class="">

                <DataTable ref="dt" :value="[]" dataKey="id" :paginator="true" :rows="10"
                    :filters="filters"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                    :rowsPerPageOptions="[5, 10, 25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products"
                    responsiveLayout="scroll" scrollable scroll-height="62vh" :frozenValue="lockedCustomers">
                    <template #header>

                        <Button label="SUBIR UN RECIBO" style="width: 100%;"
                            class="p-button-rounded p-button-danger mr-0"  />
                            <!-- @click="open2('camarita')" -->
                    </template>

                    <Column header="" headerStyle="width:0%; min-width:5rem;">
                        <template #body="slotProps">
                            <span class="p-column-title">Image</span>
                            <img src="/images/document_image.jpg" class="shadow-2" width="100" @click="cambiar" />

                            <div>

                            </div>
                        </template>
                    </Column>




                    <Column field="name" header="Nombre Documento" :sortable="true"
                        headerStyle="width:30%; min-width:5rem; ">
                        <template #body="user">
                            <span class="p-column-title">name</span>
                            {{ user.data.document_type }} </template>
                    </Column>


                    <Column field="position" header="Responsable" :sortable="true"
                        headerStyle="width:30%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Category</span>
                            {{ user.data.document_name }}
                        </template>
                    </Column>

                    <Column field="birth_date" header="Fecha de renovacion" :sortable="true"
                        headerStyle="width:12%; min-width:10rem;">
                        <template #body="user">
                            <!-- <span class="p-column-title">Fecha de Nacimiento</span> -->
                            {{ user.data.renovation_date }}
                        </template>
                    </Column>

                    <Column fieldheaderStyle="width:30%; min-width:10rem;" frozen alignFrozen="right">
                        <template #body="user">
                            <Button label="DESCARGAR" style="width: 100% "
                                class="p-button-rounded p-button-success mr-2 mb-2 "
                                @click="getSiteDocument(currentSite.site_name, user.data.document_type)" />
                            <Button label="RENOVAR" style="width: 100%;" class="p-button-rounded p-button-danger mr-0"
                                @click="open(user.data)" />

                        </template>

                    </Column>


                    <Dialog
                        :header="` CARGAR ${currentdocument ? currentdocument.document_type : ''} PARA ${currentSite.site_name}`"
                        v-model:visible="display" :breakpoints="{ '960px': '75vw' }"
                        :style="{ width: '50vw', padding: '50p0x' }" :modal="true">

                        <input ref="fileInput" type="file" accept=".pdf" @change="handleFileChange" style="display: none;">

                        <div class="col-12">
                                <label for="position">FECHA DE RENOVACION</label>

                                <Calendar id="entry_date" style="width: 100%;margin: 20px 0 ;"
                                    v-model="documentRenovationDate" required="true" autofocus />
                            </div>


                        <p class="p-3" v-show="file" style="background-color:rgba(115, 255, 76, 0.306);">
                            <i class="pi pi-check" style="color: slateblue"></i> {{ file ? file.name : '' }}
                        </p>
                        <!-- <img src="@/images/document_image.jpg" class="shadow-2" style="width: 20%;" @click="cambiar" /> -->
                        <div style="display: flex; justify-content: space-between;">
                            <Button label="Seleccionar documento"
                                style="width: 40%; background-color: var(--primary-color);"
                                @click="$refs.fileInput.click();" />
                            <Button label="Enviar" style="width: 40%;background-color: var(--primary-color);"
                                @click="update(file, currentdocument.document_type, currentSite.site_name)" />

                        </div>


                        <!-- <Button label="enviar" severity="warning" @click="$refs.fileInput.click();" /> -->
                    </Dialog>
                    <!-- <Button label="Show" icon="pi pi-external-link" style="width: auto" @click="open" /> -->


                    <Dialog
                        :header="` CARGAR ${currentdocument ? currentdocument.document_type : ''} PARA ${currentSite.site_name}`"
                        v-model:visible="display2" :breakpoints="{ '960px': '75vw' }"
                        :style="{ width: '50vw', padding: '50p0x' }" :modal="true">


                        <div class="" style="display: flex; padding: 0; margin: 0;">
                            <div class="col-6">
                                <label for="position">TIPO DE DOCUMENTO</label>
                                <Dropdown v-model.trim="documentType" :options="documentsDropValues" placeholder=""
                                    required="true" :class="{ 'p-invalid': submitted && !currentUser.position }"
                                    style="width: 100%;margin: 20px 0 ;" />
                            </div>


                            <div class="col-6">
                                <label for="position">FECHA DE RENOVACION</label>

                                <Calendar id="entry_date" style="width: 100%;margin: 20px 0 ;"
                                    v-model="documentRenovationDate" required="true" autofocus />
                            </div>

                        </div>

                        <input ref="fileInput" type="file" accept=".pdf" @change="handleFileChange" style="display: none;">

                        <p class="p-3" v-show="file" style="background-color:rgba(19, 164, 0, 0.306);">
                            <i class="pi pi-check" style="color: slateblue"></i> {{ file ? file.name : '' }}
                        </p>
                        <!-- <img src="@/images/document_image.jpg" class="shadow-2" style="width: 20%;" @click="cambiar" /> -->
                        <div style="display: flex; justify-content: space-between;">
                            <Button label="Seleccionar documento"
                                style="width: 40%; background-color: var(--primary-color);"
                                @click="$refs.fileInput.click();" />
                            <Button label="Enviar" style="width: 40%;background-color: var(--primary-color);"
                                @click="upload(file, documentType, currentSite.site_name)" />
                        </div>
                        <!-- <Button label="enviar" severity="warning" @click="$refs.fileInput.click();" /> -->
                    </Dialog>
                </DataTable>




            </div>
        </div>

    </div>


    <!-- 

    <Dock :model="[1, 2, 4]">
        <template #item="{ item }">
            <a v-tooltip.top="item" href="#" class="p-dock-link" @click="onDockItemClick($event, item)">
                <img :alt="item"
                    src="https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
                    style="width: 100%" />
            </a>
        </template>
    </Dock> -->
</template>

<style scoped lang="scss">
.inputSwith {
    display: flex;
    justify-content: space-between;
    margin: 2em 0;
}


button {
    border: none;
}</style>
