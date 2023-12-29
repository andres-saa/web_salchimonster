<!-- <script setup>

import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount,computed } from 'vue';
import { useToast } from 'primevue/usetoast';
import {departamentos,findByDepartament} from '@/service/CountryService.js'
import {uploadUserPhotoProfile} from '@/service/sendFileService'
import {
    sitesDropValues,
    GenderDropValues,
    PositionDropValues,
    maritalStatusDropValues,
    epsDropValues,
    educationLevelDropValues,
    employmentContractTypeDropValues,
    pantSizesDropValues,
    shirtSizesDropValues,
    bloodTypesDropValues,
    housingTypesDropValues,
    statusDropValues,
    vehicleTypesDropValues,
    findSiteById,
    getSites
} from '@/service/dropDownAux';
import { getUsers, } from '@/service/userServices'
import { URI } from "@/service/conection.js" 
import logo from '@/images/logo.png'
const toast = useToast();
const users = ref([]);
const adding = ref(false);
const productDialog = ref(false);
const currentUser = ref(null);
const selectedProducts = ref(null);
const dt = ref(null);
const filters = ref(null);
const submitted = ref(false);
const GenderDropValue = ref(null);
const PositionDropValue = ref(null);
const statusDropValue = ref({ name: 'activo', code: 'active' });
const SiteDropValue = ref(null);
const swithHasVehicle = ref(false)
const switchHasChildren = ref(false)
const switchFoodHandlingCertificate = ref(false)
const SwitchAuthorizationData = ref(false)
const maritalStatusDropValue = ref(null);
const educationLevelDropValue = ref(null);
const employmentContractTypeDropValue = ref(null);
const pantSizesDropValue = ref(null);
const shirtSizesDropValue = ref(null);
const bloodTypesDropValue = ref(null);
const epsDropValue = ref(null)
const housingTypesDropValue = ref(null)
const vehicleTypeDropValue = ref(null)
const serverResponse = ref('')
const departamentDropValue = ref([])
const cityDropValue         = ref([])
const imageUrlUserAdd = ref("file:///home/ludi/Downloads/9aa6397c673a5906ed994997df3a66bdc3e4f68dr1-194-259v2_00.jpg")
const op = ref(null);
const op2 = ref(null);
const file = ref(null)
const  urlPhotoProfile = ref("")





onBeforeMount(() => {
    initFilters();
    getSites()
});


const cambiar = (event) => {
    op.value.toggle(event);
};

const cambiar2 = (event) => {
    op2.value.toggle(event);
};

onMounted(async() => {
    getUsers().then(data => users.value = data)
    

});



// const formatCurrency = (value) => {
//     return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
// };

const resetValuesNewEntry = () => {
    statusDropValue.value = {}
    GenderDropValue.value = {}
    PositionDropValue.value = {}
    SiteDropValue.value = {}
    maritalStatusDropValue.value = {}
    educationLevelDropValue.value = {}
    employmentContractTypeDropValue.value = {}
    pantSizesDropValue.value = {}
    shirtSizesDropValue.value = {}
    bloodTypesDropValue.value = {}
    epsDropValue.value = {}
    housingTypesDropValue.value = {}
    vehicleTypeDropValue.value = {}
    swithHasVehicle.value = false
    switchHasChildren.value = false
    switchFoodHandlingCertificate.value = false
    SwitchAuthorizationData.value = false
    currentUser.value = {};
}

const openNew = () => {
    // al agregar un nuevo usuario
    resetValuesNewEntry()
    submitted.value = false;
    productDialog.value = true;
    adding.value = true
    file.value = null
    urlPhotoProfile.value = null

};

const asignDropValueToEdit = (user) => {

    // statusDropValue.value = findByName(user.status, statusDropValues)
    // console.log(statusDropValue.value)
    // GenderDropValue.value = findByName(user.gender, GenderDropValues)
    // PositionDropValue.value = findByName(user.position, PositionDropValues)
    SiteDropValue.value = findSiteById(user.site_id)
    departamentDropValue.value = findByDepartament(user.birth_department)
    cityDropValue.value = user.birth_city
    statusDropValue.value = user.status   

    // bloodTypesDropValue.value = findByType(user.blood_type, bloodTypesDropValues)
    // maritalStatusDropValue.value = findByName(user.marital_status, maritalStatusDropValues)
    // educationLevelDropValue.value = findByName(user.education_level, educationLevelDropValues)
    // employmentContractTypeDropValue.value = findByName(user.contract_type, employmentContractTypeDropValues)
    // epsDropValue.value = findByName(user.eps, epsDropValues)
    // housingTypesDropValue.value = findByName(user.housing_type, housingTypesDropValues)
    // vehicleTypeDropValue.value = findByName(user.vehicle_type, vehicleTypesDropValues)
    // shirtSizesDropValue.value = findByName(user.shirt_size, shirtSizesDropValues)
    // pantSizesDropValue.value = findByName(user.jeans_sweater_size, pantSizesDropValues)


    // switchHasChildren.value = user.has_children?? false
    // swithHasVehicle.value = user.has_vehicle?? false
    // switchFoodHandlingCertificate.value  = user.food_handling_certificate?? false
    // SwitchAuthorizationData.value = user.authorization_data?? false


    // currentUseruser.food_handling_certificate_number = !switchFoodHandlingCertificate.value ? null:data.food_handling_certificate_number ;
    // currentUseruser.vehicle_type = !swithHasVehicle.value ? null : data.vehicle_type;
    // currentUseruser.has_vehicle = !swithHasVehicle.value ? null : data.has_vehicle;
    // // checkDates(user)

    console.log(user)
}

const editProduct = (editUser) => {

    asignDropValueToEdit(editUser)
    urlPhotoProfile.value=null

    //valores booleanos que vienen de mysql son uno y cero

    // despues de alterar el edit user lo enviamos al valor del usuario actual
    currentUser.value = { ...editUser };
    productDialog.value = true;
    adding.value = false
};


const hideDialog = () => {
    productDialog.value = false;
    submitted.value = false;
    adding.value = false
    resetValuesNewEntry()
    currentUser.value = {};
};



const asingDataToSave = () => {
    const { ...data } = currentUser.value;

    // primero asignamos los epsDropValue
    //     data.gender = GenderDropValue.value.name
    //     // data.position = PositionDropValue.value.name

    //     data.marital_status = maritalStatusDropValue.value.name
    //     data.eps = epsDropValue.value.name
    //     data.blood_type = bloodTypesDropValue.value.type
    //     data.education_level = educationLevelDropValue.value.name
    //     data.contract_type = employmentContractTypeDropValue.value.name
    //     data.shirt_size = shirtSizesDropValue.value.name
    //     data.jeans_sweater_size = pantSizesDropValue.value.name
    //     data.housing_type = housingTypesDropValue.value.name
    //     data.status = statusDropValue.value.name
    // // Luego los swithees
    // data.food_handling_certificate = switchFoodHandlingCertificate.value
    // data.has_children = switchHasChildren.value
    // data.has_vehicle = switchHasChildren.value
    // data.authorization_data = SwitchAuthorizationData.value
    // y por ultimo las dependencias de las swithes

    // enviar el id de la sede en lugar del nombre de esta
    data.site_id = SiteDropValue.value.site_id
    data.food_handling_certificate_number = switchFoodHandlingCertificate.value ? data.food_handling_certificate_number : null;
    // swithHasVehicle.value? data.vehicle_type = null:data.vehicle_type = vehicleTypeDropValue.value
    data.birth_department = departamentDropValue.value.departamento
    data.birth_city = cityDropValue.value

    // data.status = currentUser.status
    data.exit_date = (data.status === "activo") ? null : data.exit_date;
    data.exit_reason = (data.exit_date === null) ? null : data.exit_reason;   

    if (adding.value) {
        
        data.vehicle_type = data.vehicle_type ?? null;
        data.gender = data.gender ?? null;
        data.position = data.position ?? null;
        data.site_id = data.site_id ?? null;
        data.has_children = data.has_children ?? null;
        data.has_vehicle = data.has_vehicle ?? null;
        data.food_handling_certificate = data.food_handling_certificate ?? null;
        data.authorization_data = data.authorization_data ?? null;
        data.marital_status = data.marital_status ?? null;
        data.eps = data.eps ?? null;
        data.blood_type = data.blood_type ?? null;
        data.education_level = data.education_level ?? null;
        data.contract_type = data.contract_type ?? null;
        data.shirt_size = data.shirt_size ?? null;
        data.jeans_sweater_size = data.jeans_sweater_size ?? null;
        data.housing_type = data.housing_type ?? null;
        data.status = data.status ?? null;
        data.exit_date = null
        data.exit_reason = null
        data.comments_notes = data.comments_notes ?? ''
    }

    currentUser.value = { ...data }
    return data

}

const saveProduct = async() => {
    let Method = ""
    let queryUrl = ""

    const data = asingDataToSave()

    adding.value ? Method = "POST" : Method = "PUT"

    adding.value ? queryUrl = `${URI}/insert/user` : queryUrl = `${URI}/update/user/${currentUser.value.id}`


    // Configuración de la solicitud
    const requestOptions = {
        method: Method,
        headers: {
            'Content-Type': 'application/json' // Asegúrate de establecer el tipo de contenido adecuado
        },
        body: JSON.stringify(data)
    };

    // Realizar la solicitud Fetch
   await fetch(queryUrl, requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.status}`);
            }
            file.value? uploadUserPhotoProfile(file.value,data.dni): '' 

            return response.json();
        })
        .then(data => {
            // Aquí puedes trabajar con los datos actualizados
            console.log('Datos actualizados:', data);

            // Cambiar el valor de serverResponse de manera reactiva
            serverResponse.value = data;

            // Verificar si la respuesta del servidor es 'ok' y actualizar productDialog
            if (data === 'ok') {
                adding.value? toast.add({ severity: 'success', summary: 'Usuario registrado', detail: 'Hecho', life: 3000 }):
                toast.add({ severity: 'success', summary: 'Usuario actualizado', detail: 'Hecho', life: 3000 })

                hideDialog()
            } else {
                productDialog.value = true;
            }
        })
        .catch(error => {
            console.error('Error en la solicitud:', error);
            toast.add({ severity: 'error', summary: 'llene todos los campos', detail: '', life: 3000 })
            
        });


    console.log(currentUser.value)
    console.log(data);
    console.log(serverResponse.value)
    submitted.value = true

}
const toggle = (event) => {
    op.value.toggle(event);
};


const exportCSV = () => {
    dt.value.exportCSV();
};

// const confirmDeleteSelected = () => {
//     deleteProductsDialog.value = true;
// };
// const deleteSelectedProducts = () => {
//     products.value = products.value.filter((val) => !selectedProducts.value.includes(val));
//     deleteProductsDialog.value = false;
//     selectedProducts.value = null;
//     toast.add({ severity: 'success', summary: 'Successful', detail: 'Products Deleted', life: 3000 });
// };

const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS }
    };
};


    // const onUpload = (event) => {
    //   if (event.files.length > 0) {
    //     const file = event.files[0];
    //     // Crear una URL temporal para mostrar la imagen
    //     imageUrlUserAdd.value = URL.createObjectURL(file);
    //     console.log(URL.createObjectURL(file))
    //   } else {
    //     // Borrar la vista previa si no se selecciona ningún archivo
    //     imageUrlUserAdd.value = null;
    //   }
      
      
    // };


    const onUpload = (event) => {
      if (event.files.length > 0) {
        const file = event.files[0];
        const reader = new FileReader();

        reader.onload = () => {
          // Cuando el archivo se ha leído, asigna la URL al imagePreview
          imageUrlUserAdd.value = reader.result;
        };

        reader.readAsDataURL(file);
      } else {
        // Borrar la vista previa si no se selecciona ningún archivo
        imageUrlUserAdd.value = null;
      }
    };



    const handleFileChange = (event) => {
    // Accede al archivo seleccionado a través del objeto de evento
    const selectedFile = event.target.files[0];


    if (selectedFile) {
        // Aquí puedes realizar acciones con el archivo seleccionado, como cargarlo al servidor
        console.log('Archivo seleccionado:', selectedFile);
        file.value = selectedFile
        urlPhotoProfile.value = URL.createObjectURL(selectedFile);
    }

}





</script>

<template>
    <div class="grid">
        <div class="col-12">
            <div class="">
                <Toast />
                <Toolbar class="mb-4">
                    <template v-slot:start>
                        <div class="my-2">
                            <Button label="REGISTRAR USUARIO" icon="pi pi-plus" class="p-button-success mr-2"
                                @click="openNew" />
                        </div>
                    </template>

                    <template v-slot:end>
                        <!-- <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" label="Import" chooseLabel="Import"
                            class="mr-2 inline-block" /> -->
                        <Button label="EXPORTAR EXCEL" icon="pi pi-upload" class="p-button-success" @click="exportCSV($event)" />
                    </template>
                </Toolbar>

                <DataTable ref="dt" :value="users" v-model:selection="selectedProducts" dataKey="id" :paginator="true"
                    :rows="10" :filters="filters"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                    :rowsPerPageOptions="[5, 10, 25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products"
                    responsiveLayout="scroll"
                    scrollable 
                    scroll-height="62vh"
                    :frozenValue="lockedCustomers">
                    <template #header>
                        <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
                            <h5 class="m-0 text-white text-2xl">Administrar usuarios</h5>
                            <span class="block mt-2 md:mt-0 p-input-icon-left">
                                <i class="pi pi-search" />
                                <InputText v-model="filters['global'].value" placeholder="Search..." />
                            </span>
                        </div>
                    </template>

                    <Column selectionMode="multiple" headerStyle="width: 3rem; " frozen></Column>

                    <Column field="id" header="Id" :sortable="true" headerStyle="width:min-content; min-width:min-content; " >
                        <template #body="user">
                            <span class="p-column-title">Code</span>
                            {{ user.data.id }}
                        </template>
                    </Column>

                    <Column header="Image" headerStyle="width:14%; min-width:10rem;" >
                        <template #body="user"   >
                            <span class="p-column-title">Image</span> 
                            <div>
                            <img  :src=" `${URI}/read_user_photo_profile/${user.data.dni} ` || 'https://novatocode.online/assets/logo-f2daca0e.png'" @error="'https://novatocode.online/assets/logo-f2daca0e.png'"  class="shadow-2 img-profile"   style=" border:none; position:relative; height: 10vh; width: 10vh; object-fit: cover; border-radius: 50%; "/>

                            </div>
                            
                            <div>
                        
                                <!-- <Button type="button" label="Image"  class="p-button-success" /> -->
                            <!-- <OverlayPanel ref="op" appendTo="body" :showCloseIcon="true" style=" padding: 0; box-shadow: 4px 4px 8px var(--primary-color);">
                                <img   :src=" `${URI}/read_user_photo_profile/${user.data.id}`" alt="Nature 9" style="width: 40vw; height: ; "
    />
                            </OverlayPanel> -->


                        <!-- <OverlayPanel ref="op2" appendTo="body" :showCloseIcon="true" style=" padding: 0; box-shadow: 4px 4px 8px var(--primary-color);">
                            <img src="@/images/bg_black.jpg" alt="Nature 9" style="height:80vh ; "
 />
                        </OverlayPanel> -->
                    </div>
                        </template>
                    </Column>

                    


                    <Column field="name" header="Nombre" :sortable="true" headerStyle="width:20%; min-width:20rem; " >
                        <template #body="user">
                            <span class="p-column-title">name</span>
                            {{ user.data.name }}
                        </template>
                    </Column>


                    <Column field="dni" header="Documento" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Price</span>
                            {{ user.data.dni }}
                        </template>
                    </Column>

                    <Column field="address" header="Direccion" :sortable="true" headerStyle="width:14%; min-width:15rem;">
                        <template #body="user">
                            <span class="p-column-title">Category</span>
                            {{ user.data.address }}
                        </template>
                    </Column>

                    <Column field="position" header="Cargo" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Category</span>
                            {{ user.data.position }}
                        </template>
                    </Column>

                    <Column field="site_name" header="Sede" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Category</span>
                            {{ user.data.site_name }}
                        </template>
                    </Column>

                    <Column field="status" header="Estado" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Category</span>
                            {{ user.data.status }}
                        </template>
                    </Column>


                    <Column field="gender" header="Género" :sortable="true" headerStyle="width:10%; min-width:8rem;">
                        <template #body="user">
                            <span class="p-column-title">Género</span>
                            {{ user.data.gender }}
                        </template>
                    </Column>

                    <Column field="birth_date" header="Fecha de Nacimiento" :sortable="true"
                        headerStyle="width:12%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Fecha de Nacimiento</span>
                            {{ user.data.birth_date }}
                        </template>
                    </Column>

                    <Column field="phone" header="Teléfono" :sortable="true" headerStyle="width:12%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Teléfono</span>
                            {{ user.data.phone }}
                        </template>
                    </Column>

                    <Column field="email" header="Correo Electrónico" :sortable="true"
                        headerStyle="width:16%; min-width:12rem;">
                        <template #body="user">
                            <span class="p-column-title">Correo Electrónico</span>
                            {{ user.data.email }}
                        </template>
                    </Column>

                    <Column field="entry_date" header="Fecha de Ingreso" :sortable="true"
                        headerStyle="width:12%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Fecha de Ingreso</span>
                            {{ user.data.entry_date }}
                        </template>
                    </Column>

                    <Column field="exit_date" header="Fecha de Salida" :sortable="true"
                        headerStyle="width:12%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Fecha de Salida</span>
                            {{ user.data.exit_date }}
                        </template>
                    </Column>

                    <Column field="exit_reason" header="Motivo de Salida" :sortable="true"
                        headerStyle="width:14%; min-width:15rem;">
                        <template #body="user">
                            <span class="p-column-title">Motivo de Salida</span>
                            {{ user.data.exit_reason }}
                        </template>
                    </Column>

                    <Column field="authorization_data" header="Autorización de Datos" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Autorización de Datos</span>
                            {{ user.data.authorization_data == 1 ? 'si' : 'no' }}
                        </template>
                    </Column>

                    <Column field="birth_country" header="País de Nacimiento" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">País de Nacimiento</span>
                            {{ user.data.birth_country }}
                        </template>
                    </Column>

                    <Column field="birth_department" header="Departamento de Nacimiento" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Departamento de Nacimiento</span>
                            {{ user.data.birth_department }}
                        </template>
                    </Column>

                    <Column field="birth_city" header="Ciudad de Nacimiento" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Ciudad de Nacimiento</span>
                            {{ user.data.birth_city }}
                        </template>
                    </Column>

                    <Column field="blood_type" header="Tipo de Sangre" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Tipo de Sangre</span>
                            {{ user.data.blood_type }}
                        </template>
                    </Column>

                    <Column field="marital_status" header="Estado Civil" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Estado Civil</span>
                            {{ user.data.marital_status }}
                        </template>
                    </Column>

                    <Column field="education_level" header="Nivel de Educación" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Nivel de Educación</span>
                            {{ user.data.education_level }}
                        </template>
                    </Column>
                    <Column field="contract_type" header="Tipo de Contrato" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Tipo de Contrato</span>
                            {{ user.data.contract_type }}
                        </template>
                    </Column>

                    <Column field="eps" header="EPS" :sortable="true" headerStyle="width:18%; min-width:15rem;">
                        <template #body="user">
                            <span class="p-column-title">EPS</span>
                            {{ user.data.eps }}
                        </template>
                    </Column>

                    <Column field="pension_fund" header="Fondo de Pensión" :sortable="true"
                        headerStyle="width:18%; min-width:15rem;">
                        <template #body="user">
                            <span class="p-column-title">Fondo de Pensión</span>
                            {{ user.data.pension_fund }}
                        </template>
                    </Column>

                    <Column field="severance_fund" header="Fondo de Cesantías" :sortable="true"
                        headerStyle="width:18%; min-width:15rem;">
                        <template #body="user">
                            <span class="p-column-title">Fondo de Cesantías</span>
                            {{ user.data.severance_fund }}
                        </template>
                    </Column>

                    <Column field="has_children" header="Tiene Hijos" :sortable="true"
                        headerStyle="width:18%; min-width:15rem;">
                        <template #body="user">
                            <span class="p-column-title">Tiene Hijos</span>
                            {{ user.data.has_children == 1 ? 'si' : 'no' }}
                        </template>
                    </Column>

                    <Column field="housing_type" header="Tipo de Vivienda" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Tipo de Vivienda</span>
                            {{ user.data.housing_type }}
                        </template>
                    </Column>

                    <Column field="has_vehicle" header="Tiene Vehículo" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Tiene Vehículo</span>
                            {{ user.data.has_vehicle == 1 ? "si" : "no" }}
                        </template>
                    </Column>

                    <Column field="vehicle_type" header="Tipo de Vehículo" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Tipo de Vehículo</span>
                            {{ user.data.vehicle_type }}
                        </template>
                    </Column>

                    <Column field="household_size" header="Tamaño del Hogar" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Tamaño del Hogar</span>
                            {{ user.data.household_size }}
                        </template>
                    </Column>

                    <Column field="emergency_contact" header="Contacto de Emergencia" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Contacto de Emergencia</span>
                            {{ user.data.emergency_contact }}
                        </template>
                    </Column>

                    <Column field="shirt_size" header="Talla de Camisa" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Talla de Camisa</span>
                            {{ user.data.shirt_size }}
                        </template>
                    </Column>

                    <Column field="jeans_sweater_size" header="Talla de Pantalón" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Talla de Pantalón/Suéter</span>
                            {{ user.data.jeans_sweater_size }}
                        </template>
                    </Column>

                    <Column field="food_handling_certificate" header="Certificado de Manejo de Alimentos" :sortable="true"
                        headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Certificado de Manejo de Alimentos</span>
                            {{ user.data.food_handling_certificate == 1 ? 'si' : 'no' }}
                        </template>
                    </Column>

                    <Column field="food_handling_certificate_number" header="Número de Certificado de Manejo de Alimentos"
                        :sortable="true" headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Número de Certificado de Manejo de Alimentos</span>
                            {{ user.data.food_handling_certificate_number }}
                        </template>
                    </Column>

                    <Column field="salary" header="Salario" :sortable="true" headerStyle="width:18%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Salario</span>
                            {{ user.data.salary }}
                        </template>
                    </Column>

                    <Column field="comments_notes" header="Comentarios/Notas" :sortable="false"
                        headerStyle="width:500px; min-width:15rem;">
                        <template #body="user">
                            <span class="p-column-title">Comentarios/Notas</span>
                            {{ user.data.comments_notes }}
                        </template>
                    </Column>

                    <Column headerStyle="min-width:min-contents;" frozen alignFrozen="right">
                        <template #body="user">
                            <Button icon="pi pi-pencil" class="p-button-rounded p-button-success mr-2"
                                @click="editProduct(user.data)" />

                        </template>

                    </Column>

                </DataTable>


                <Dialog v-model:visible="productDialog" :style="{ width: '450px' }" header="Registrar un Usuario"
                    :modal="true" class="p-fluid">

                    <!-- <img src="http://localhost:8000/read-site-cover/IMPERIO%20CANEY" :alt="currentUser.id"
                        v-if="currentUser.id" width="150" class="mt-0 mx-auto mb-5 block shadow-2" /> -->
                        <!-- <FileUpload /> -->

                        <!-- <img :src="imageUrlUserAdd.value" :alt="currentUser.id"
                         width="150" class="mt-0 mx-auto mb-5 block shadow-2"  id="imagePreview"/> -->
                        
                       
                        
                        <!-- <FileUpload /> -->

                    <img  class="img-profile-add" style="width: 100%; height: 30vh; object-fit: cover;" :src=" adding? urlPhotoProfile || 'https://novatocode.online/assets/logo-f2daca0e.png':urlPhotoProfile || `${URI}/read_user_photo_profile/${currentUser.dni} ` || 'https://novatocode.online/assets/logo-f2daca0e.png' " alt="">
                    <div class="field col-12">
                        <input ref="fileInput" type="file" accept="image/*" @change="handleFileChange" style="display: none;">
                        <Button label="Seleccionar foto de perfil" 
                                class="col-12 m0"
                                style="width: 100%; background-color: var(--primary-color);"
                                @click="$refs.fileInput.click();" />
                        
                    </div>

                    <div class="field">
                        <label for="name">Nombre</label>
                        <InputText id="name" v-model.trim="currentUser.name" required="true" autofocus
                            :class="{ 'p-invalid': submitted && !currentUser.name }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.name">name is required.</small>
                    </div>

                    <div class="field">
                        <label for="dni">Identificación</label>
                        <InputText id="dni" v-model.trim="currentUser.dni" required="true" autofocus
                            :class="{ 'p-invalid': submitted && !currentUser.dni }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.dni">La identificación es
                            requerida.</small>
                    </div>


                    <div class="field">
                        <label for="address">Dirección</label>
                        <InputText id="address" v-model.trim="currentUser.address" required="true" autofocus
                            :class="{ 'p-invalid': submitted && !currentUser.address }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.address">La dirección es requerida.</small>
                    </div>


                    <div class="field">
                        <label for="position">Cargo</label>
                        <Dropdown v-model.trim="currentUser.position" :options="PositionDropValues" placeholder=""
                            required="true" :class="{ 'p-invalid': submitted && !currentUser.position }" />

                        <small class="p-invalid" v-if="submitted && !currentUser.position">el cargo es obligatorio</small>

                    </div>


                    <div class="field">
                        <label for="site_id">Sede</label>
                        <Dropdown v-model="SiteDropValue" :options="sitesDropValues" placeholder="" optionLabel="site_name"
                            required="true" :class="{ 'p-invalid': submitted && !currentUser.site_id }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.site_id">La sede es obligatoria
                        </small>
                    </div>





                    <div class="field">
                        <label for="gender">Género</label>
                        <Dropdown v-model="currentUser.gender" :options="GenderDropValues" placeholder="" required="true"
                            :class="{ 'p-invalid': submitted && !currentUser.gender }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.gender">el genero es obligatorio
                        </small>
                    </div>


                    <div class="field">
                        <label for="birth_date">Fecha de Nacimiento</label>
                        <Calendar id="birth_date" v-model="currentUser.birth_date" required="true" autofocus
                            :class="{ 'p-invalid': submitted && !currentUser.birth_date }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.birth_date">fecha de nacimiento es
                            obligatoria</small>
                    </div>

                    <!-- <div class="field">
                        <label for="birth_date">Pais de Nacimiento</label>
                        <InputText id="birth_date" v-model="currentUser.birth_country" required="true" autofocus />
                    </div>

                    <div class="field">
                        <label for="birth_date">Departamento de Nacimiento</label>
                        <InputText id="birth_date" v-model="currentUser.birth_department" required="true" autofocus />
                    </div>

                    <div class="field">
                        <label for="birth_date">Ciudad de Nacimiento</label>
                        <InputText id="birth_date" v-model="currentUser.birth_city" required="true" autofocus />
                    </div>

                    <div class="field">
                        <label for="birth_date">Tipo de sangre</label>
                        <Dropdown v-model="currentUser.blood_type" :options="bloodTypesDropValues" 
                            placeholder="" required="true" />
                    </div>

                    <div class="field">
                        <label for="phone">Teléfono</label>
                        <InputText id="phone" v-model.trim="currentUser.phone" required="true" autofocus
                            :class="{ 'p-invalid': submitted && !currentUser.phone }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.phone">El teléfono es requerido.</small>
                    </div> -->

                    <div class="field">
                        <label for="birth_country">Pais de Nacimiento</label>
                        <InputText id="birth_country" v-model="currentUser.birth_country" required="true" autofocus
                            :class="{ 'p-invalid': submitted && !currentUser.birth_country }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.birth_country">País de nacimiento es
                            obligatorio.</small>
                    </div>

                    <!-- Sample Dropdown field with validation -->
                    

                    <!-- Sample input field with validation -->
                    <div class="field">
                        <label for="birth_department">Departamento de Nacimiento</label>
                        <Dropdown v-model="departamentDropValue" :options="departamentos" optionLabel="departamento"  placeholder="" required="true"
                            :class="{ 'p-invalid': submitted && !currentUser.gender }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.gender">el genero es obligatorio
                        </small>
                    </div>

                    <!-- Sample input field with validation -->
                    <div class="field">
                        <label for="birth_city">Ciudad de Nacimiento</label>
                        <Dropdown v-model="cityDropValue" :options="departamentDropValue.ciudades"   placeholder="" required="true"
                            :class="{ 'p-invalid': submitted && !currentUser.gender }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.gender">el genero es obligatorio
                        </small>
                    </div>

                    <div class="field">
                        <label for="blood_type">Tipo de sangre</label>
                        <Dropdown v-model="currentUser.blood_type" :options="bloodTypesDropValues" placeholder=""
                            required="true" :class="{ 'p-invalid': submitted && !currentUser.blood_type }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.blood_type">Tipo de sangre es
                            obligatorio.</small>
                    </div>
                    <!-- Sample input field with validation -->
                    <div class="field">
                        <label for="phone">Teléfono</label>
                        <InputText id="phone" v-model.trim="currentUser.phone" required="true" autofocus
                            :class="{ 'p-invalid': submitted && !currentUser.phone }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.phone">El teléfono es requerido.</small>
                    </div>


                    <div class="field">
                        <label for="email">Correo Electrónico</label>
                        <InputText id="email" v-model.trim="currentUser.email" required="true" autofocus
                            :class="{ 'p-invalid': submitted && !currentUser.email }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.email">El correo electrónico es
                            requerido.</small>
                    </div>


                    <div class="field">
                        <label for="entry_date">Fecha de Ingreso</label>
                        <Calendar id="entry_date" v-model="currentUser.entry_date" required="true" autofocus
                            :class="{ 'p-invalid': submitted && !currentUser.entry_date }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.entry_date">Fecha de ingreso es
                            obligatoria.</small>
                    </div>

                    <div class="field">
                        <label for="marital_status">Estado civil</label>
                        <Dropdown v-model="currentUser.marital_status" :options="maritalStatusDropValues" placeholder=""
                            required="true" :class="{ 'p-invalid': submitted && !currentUser.marital_status }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.marital_status">Estado civil es
                            obligatorio.</small>
                    </div>

                    <div class="field">
                        <label for="education_level">Nivel de Educación</label>
                        <Dropdown v-model="currentUser.education_level" :options="educationLevelDropValues" placeholder=""
                            required="true" :class="{ 'p-invalid': submitted && !currentUser.education_level }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.education_level">Nivel de Educación es
                            obligatorio.</small>
                    </div>

                    <div class="field">
                        <label for="contract_type">Tipo de Contrato</label>
                        <Dropdown v-model="currentUser.contract_type" :options="employmentContractTypeDropValues"
                            placeholder="" required="true"
                            :class="{ 'p-invalid': submitted && !currentUser.contract_type }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.contract_type">Tipo de Contrato es
                            obligatorio.</small>
                    </div>

                    <div class="field">
                        <label for="eps">EPS</label>
                        <Dropdown v-model="currentUser.eps" :options="epsDropValues" placeholder="" required="true"
                            :class="{ 'p-invalid': submitted && !currentUser.eps }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.eps">EPS es obligatorio.</small>
                    </div>

                    <div class="field">
                        <label for="pension_fund">Fondo de Pensión</label>
                        <InputText id="pension_fund" v-model.trim="currentUser.pension_fund"
                            :class="{ 'p-invalid': submitted && !currentUser.pension_fund }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.pension_fund">Fondo de Pensión es
                            obligatorio.</small>
                    </div>

                    <div class="field">
                        <label for="severance_fund">Fondo de Cesantías</label>
                        <InputText id="severance_fund" v-model.trim="currentUser.severance_fund"
                            :class="{ 'p-invalid': submitted && !currentUser.severance_fund }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.severance_fund">Fondo de Cesantías es
                            obligatorio.</small>
                    </div>

                    <div class="field inputSwith">
                        <label for="has_children">Tiene Hijos</label>
                        <InputSwitch id="has_children" v-model="currentUser.has_children" />
                    </div>

                    <div class="field">
                        <label for="housing_type">Tipo de Vivienda</label>
                        <Dropdown v-model="currentUser.housing_type" :options="housingTypesDropValues" placeholder=""
                            required="true" :class="{ 'p-invalid': submitted && !currentUser.housing_type }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.housing_type">Tipo de vivienda es
                            obligatorio.</small>
                    </div>


                    <div class="field inputSwith">
                        <label for="has_vehicle">Tiene Vehículo</label>
                        <InputSwitch id="has_vehicle" v-model="currentUser.has_vehicle" />
                    </div>

                    <div class="field" v-show="currentUser.has_vehicle">
    <label for="vehicle_type">Tipo de Vehículo</label>
    <Dropdown v-model="currentUser.vehicle_type" :options="vehicleTypesDropValues" 
              placeholder="" required="true" :class="{ 'p-invalid': submitted && !currentUser.vehicle_type }" />
    <small class="p-invalid" v-if="submitted && !currentUser.vehicle_type">Tipo de vehículo es obligatorio.</small>
</div>

                    <div class="field">
                        <label for="household_size">Tamaño del Hogar</label>
                        <InputNumber id="household_size" v-model.number="currentUser.household_size"
                            :class="{ 'p-invalid': submitted && !currentUser.household_size }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.household_size">Tamaño del hogar es
                            obligatorio.</small>
                    </div>

                    <div class="field">
                        <label for="emergency_contact">Contacto de Emergencia</label>
                        <InputText id="emergency_contact" v-model.trim="currentUser.emergency_contact"
                            :class="{ 'p-invalid': submitted && !currentUser.emergency_contact }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.emergency_contact">Contacto de emergencia
                            es obligatorio.</small>
                    </div>

                    <div class="field">
                        <label for="shirt_size">Talla de Camisa</label>
                        <Dropdown v-model="currentUser.shirt_size" :options="shirtSizesDropValues" placeholder=""
                            required="true" :class="{ 'p-invalid': submitted && !currentUser.shirt_size }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.shirt_size">Talla de camisa es
                            obligatoria.</small>
                    </div>

                    <div class="field">
                        <label for="jeans_sweater_size">Talla de Pantalón</label>
                        <Dropdown v-model="currentUser.jeans_sweater_size" :options="pantSizesDropValues" placeholder=""
                            required="true" :class="{ 'p-invalid': submitted && !currentUser.jeans_sweater_size }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.jeans_sweater_size">Talla de pantalón es
                            obligatoria.</small>
                    </div>

                    <div class="field inputSwith">
                        <label for="food_handling_certificate">Certificado de Manejo de Alimentos</label>
                        <InputSwitch id="food_handling_certificate" v-model="currentUser.food_handling_certificate" />
                    </div>

                    <div class="field" v-show="currentUser.food_handling_certificate">
    <label for="food_handling_certificate_number">Número de Certificado de Manejo de Alimentos</label>
    <InputText id="food_handling_certificate_number" v-model.trim="currentUser.food_handling_certificate_number"
               :class="{ 'p-invalid': submitted && !currentUser.food_handling_certificate_number }" />
    <small class="p-invalid" v-if="submitted && !currentUser.food_handling_certificate_number">Número de certificado es obligatorio.</small>
</div>

                    <div class="field">
                        <label for="salary">Salario</label>
                        <InputNumber id="salary" v-model.number="currentUser.salary" />
                    </div>

                    <div class="field">
                        <label for="description">Comentarios</label>
                        <Textarea id="description" v-model="currentUser.comments_notes" required="true" rows="5" cols="20"
                            style="resize: none;" />
                    </div>


                    <div class="field" >
                        <label for="status">Estado</label>
                        <Dropdown v-model="currentUser.status" :options="statusDropValues" placeholder="" required="true"
                            :class="{ 'p-invalid': submitted && !currentUser.status }" />
                        <small class="p-invalid" v-if="submitted && !currentUser.status">Estado es obligatorio.</small>
                    </div>

                    <div class="field" v-show="currentUser.entry_date && currentUser.status == 'inactivo'">
                        <label for="exit_date">Fecha de Salida</label>
                        <Calendar id="exit_date" v-model="currentUser.exit_date" required="false" />
                    </div>

                    <div class="field"
                        v-show="currentUser.exit_date && currentUser.entry_date && currentUser.status == 'inactivo'">
                        <label for="exit_reason">Motivo de Salida</label>
                        <InputText id="exit_reason" v-model.trim="currentUser.exit_reason" required="true" autofocus />
                        <small class="p-invalid" v-if="submitted && !currentUser.exit_reason">El motivo de salida es
                            requerido.</small>
                    </div>

                    <div class="field inputSwith">
                        <label for="authorization_data">Autorización de Datos</label>
                        <div class="input-with-label">
                            <InputSwitch id="authorization_data" v-model="currentUser.authorization_data" />

                        </div>
                    </div>


                    <!-- <div class="field">
                        <label for="inventoryStatus" class="mb-3">Inventory Status</label>
                        <Dropdown id="inventoryStatus" v-model="user.id" :options="statuses" optionLabel="label" placeholder="Select a Status">
                            <template #value="slotProps">
                                <div v-if="slotProps.value && slotProps.value.value">
                                    <span :class="'product-badge status-' + slotProps.value.value">{{ slotProps.value.label }}</span>
                                </div>
                                <div v-else-if="slotProps.value && !slotProps.value.value">
                                    <span :class="'product-badge status-' + slotProps.value.toLowerCase()">{{ slotProps.value }}</span>
                                </div>
                                <span v-else>
                                    {{ slotProps.placeholder }}
                                </span>
                            </template>
                        </Dropdown>
                    </div> -->

                    <!-- <div class="field">
                        <label class="mb-3">Category</label>
                        <div class="formgrid grid">
                            <div class="field-radiobutton col-6">
                                <RadioButton id="category1" name="category" value="Accessories" v-model="user.id" />
                                <label for="category1">Accessories</label>
                            </div>
                            <div class="field-radiobutton col-6">
                                <RadioButton id="category2" name="category" value="Clothing" v-model="user.id" />
                                <label for="category2">Clothing</label>
                            </div>
                            <div class="field-radiobutton col-6">
                                <RadioButton id="category3" name="category" value="Electronics" v-model="user.id" />
                                <label for="category3">Electronics</label>
                            </div>
                            <div class="field-radiobutton col-6">
                                <RadioButton id="category4" name="category" value="Fitness" v-model="user.id" />
                                <label for="category4">Fitness</label>
                            </div>
                        </div>
                    </div> -->


                    <!-- <div class="formgrid grid">
                        <div class="field col">
                            <label for="price">Price</label>
                            <InputNumber id="price" v-model="user.id" mode="currency" currency="USD" locale="en-US"
                                :class="{ 'p-invalid': submitted && !user.id }" :required="true" />
                            <small class="p-invalid" v-if="submitted && !user.price">Price is required.</small>
                        </div>
                        <div class="field col">
                            <label for="quantity">Quantity</label>
                            <InputNumber id="quantity" v-model="user.id" integeronly />
                        </div>
                    </div> -->
                    <template #footer>
                        <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog" />
                        <Button label="Save" icon="pi pi-check" class="p-button-text" @click="saveProduct" />
                    </template>
                </Dialog>

        </div>
    </div>

</div>




<!-- <border :model="[1,2,4]">
    <template #item="{ item }">
        <a v-tooltip.top="item" href="#" class="p-border-link" @click="onborderItemClick($event, item)">
            <img :alt="item" src="https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510" style="width: 100%" />
        </a>
    </template>
</border> -->

</template>

<style scoped lang="scss">

.inputSwith {
    display: flex;
    justify-content: space-between;
    margin: 2em 0;
}


button{
    border: none;
}





.img-profile::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgb(255, 255, 255); /* Color de fondo desde la variable */
  opacity: 0.5; /* Opacidad deseada (0.5 = 50%) */
  z-index: -1; /* Asegura que el fondo esté detrás del contenido */
  background-image: url('https://novatocode.online/assets/logo-f2daca0e.png');
}

.img-profile-add{
    border: 1px solid var(--primary-color);
    // content: 'hola';
    // background-color: var(--primary-color)
}



</style> -->
