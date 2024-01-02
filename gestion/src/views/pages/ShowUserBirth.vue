<script setup>

import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount,computed } from 'vue';
import { useToast } from 'primevue/usetoast';
import {departamentos,findByDepartament} from '@/service/CountryService.js'
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
import { defineProps } from 'vue';

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
const props = defineProps({
      mes: String, // Define el tipo de la prop (en este caso, String)
    });


const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');



function filtrarUsuariosPorMes(users, mes) {
  // Filtrar los usuarios cuya fecha de cumpleaños está en el mes deseado
//   console.log(users)
  const usuariosCumplenEnMes = users.filter((usuario) => {
    const fechaNacimiento = new Date(usuario.birth_date);
    return fechaNacimiento.getMonth() + 1 === mes && usuario?.status.toLowerCase().split(' ')[0] === 'activo'; us // El mes se indexa desde 0 (enero) hasta 11 (diciembre)
  });

  return usuariosCumplenEnMes;
}





onBeforeMount(() => {
    // initFilters();
    // getSites()

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

console.log(filtrarUsuariosPorMes(users.value, 3),'hikaaaaaaaaaaaaaa')


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

};

const asignDropValueToEdit = (user) => {

    // statusDropValue.value = findByName(user.status, statusDropValues)
    // console.log(statusDropValue.value)
    // GenderDropValue.value = findByName(user.gender, GenderDropValues)
    // PositionDropValue.value = findByName(user.position, PositionDropValues)
    SiteDropValue.value = user.site_name
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

    // console.log(user)
}

const editProduct = (editUser) => {

    asignDropValueToEdit(editUser)

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

const verIMagen = (dni) => {
    visibleImage.value = true
    bigImage.value = `${URI}/read-product-image/600/employer-${dni}`
}


const onImageError = (gender, event)=> {


const genders = {
    masculino:'/images/male-avatar.png',
    femenino:'/images/female-avatar.png',
    default:'/images/who.png'
}

if (!gender || gender == ''){
    event.target.src = genders.default
}else
        event.target.src = genders[gender.toLowerCase()]
    }


    
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


</script>

<template>
    <div class="grid">
        <div class="col-12">
            <div class="">
            
                <DataTable ref="dt" :value="filtrarUsuariosPorMes(users, props.mes)" v-model:selection="selectedProducts" dataKey="id" :paginator="true"
                    :rows="10" :filters="filters"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
                    :rowsPerPageOptions="[5, 10, 25]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products"
                    responsiveLayout="scroll"
                    scrollable 
                    scroll-height="62vh"
                    :frozenValue="lockedCustomers">
                    <template #header>
                        
                    </template> 

                    <!-- <Column selectionMode="multiple" headerStyle="width: 3rem; " frozen></Column> -->

                    <!-- <Column field="id" header="Id" :sortable="true" headerStyle="width:min-content; min-width:min-content; " >
                        <template #body="user">
                            <span class="p-column-title">Code</span>
                            {{ user.data.id }}
                        </template>
                    </Column> -->

                    <Column header="Image" headerStyle="width:5%; min-width:5rem;">
                        <template #body="user">
                            <span class="p-column-title">Image</span>
                            <div>
                   
        <img @click="verIMagen(user.data.dni)" :src="`${URI}/read-product-image/96/employer-${user.data.dni}`"
             @error="onImageError(user.data.gender, $event)"
             class="shadow-2 img-profile"
             style="border:none; position:relative; height: 3rem; width:3rem; object-fit: cover; border-radius: 50%;" />
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

                    


                    <Column field="name" header="Nombre" :sortable="true" headerStyle="width:max-content; min-width:5rem; " >
                        <template #body="user">
                            <span class="p-column-title">name</span>
                            {{ user.data.name }}
                        </template>
                    </Column>
                    <Column field="birth_date" header="Fecha de Nacimiento" :sortable="true"
                        headerStyle="width:12%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Fecha de Nacimiento</span>
                            {{ user.data.birth_date }}
                        </template>
                    </Column>


                    <!-- <Column field="dni" header="Documento" :sortable="true" headerStyle="width:14%; min-width:10rem;">
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
                    </Column> -->

                    <Column field="position" header="Cargo" :sortable="true" headerStyle="width:auto; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Category</span>
                            {{ user.data.position }}
                        </template>
                    </Column>


                   
                    <!-- <Column field="site_name" header="Sede" :sortable="true" headerStyle="width:14%; min-width:10rem;">
                        <template #body="user">
                            <span class="p-column-title">Category</span>
                            {{ user.data.site_name }}
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

                    </Column> -->

                </DataTable>


        </div>
    </div>

</div>






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

</style>
