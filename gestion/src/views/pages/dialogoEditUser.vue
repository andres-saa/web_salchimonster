<template>

    <div class="col-12" style="height:80vh; display:flex; align-items: center; justify-content: center;">
        
        <Button @click="productDialog = true" class="p-button-danger" style="z-index: 99; position: absolute;border: none; ; font-weight: bold"> ACTUALIZAR MIS DATOS</Button>
        <img class=""  style="width: 900px;opacity: 0.5; max-width: 900px;height: 100%;object-fit: cover;" src="/images/actualizar-datos.jpg" alt="">
    </div>


   <Toast/>
    <Dialog v-model:visible="productDialog" :style="{ width: '450px' }" header="Registrar un Usuario" :modal="true"
        class="p-fluid">

        <!-- <img src="http://localhost:8000/read-site-cover/IMPERIO%20CANEY" :alt="currentUser.id"
                        v-if="currentUser.id" width="150" class="mt-0 mx-auto mb-5 block shadow-2" /> -->
        <!-- <FileUpload /> -->

        <!-- <img :src="imageUrlUserAdd.value" :alt="currentUser.id"
                         width="150" class="mt-0 mx-auto mb-5 block shadow-2"  id="imagePreview"/> -->



        <!-- <FileUpload /> -->

        <img class="img-profile-add" style="width: 100%; height: 30vh; object-fit: cover;"
            :src="urlPhotoProfile ? urlPhotoProfile : `${URI}/read-product-image/600/employer-${currentUser.dni}`"
            alt="">
        <div class="field col-12">
            <input ref="fileInput" type="file" accept="image/*" @change="handleFileChange" style="display: none;">
            <Button label="Seleccionar foto de perfil" class="col-12 m0"
                style="width: 100%; background-color: var(--primary-color);" @click="$refs.fileInput.click();" />

        </div>


        <!-- {{ currentUser }} -->
        <div class="field">
            <label for="name">Nombre</label>
            <InputText id="name" v-model.trim="currentUser.name" required="true" autofocus
                :class="{ 'p-invalid': submitted && !currentUser.name }" />
            <small class="p-invalid" v-if="submitted && !currentUser.name">name is required.</small>
        </div>

        <div class="field">
            <label for="dni" :disabled="!verificarRol(getUserRole(),roles.adminTienda)">Identificación</label>
            <InputText  :disabled="!verificarRol(getUserRole(),roles.adminTienda)" id="dni" v-model.trim="currentUser.dni" required="true" autofocus
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
            <label for="position" >Cargo</label>
            <Dropdown :disabled="!verificarRol(getUserRole(),roles.adminTienda)" filter v-model.trim="currentUser.position" :options="PositionDropValues" placeholder=""
                required="true" :class="{ 'p-invalid': submitted && !currentUser.position }" />

            <small class="p-invalid" v-if="submitted && !currentUser.position">el cargo es obligatorio</small>

        </div>


        <div class="field">
            <label for="site_id" :disabled="!verificarRol(getUserRole(),roles.adminTienda)">Sede</label>
            <Dropdown :disabled="!verificarRol(getUserRole(),roles.adminTienda)" filter v-model="SiteDropValue" :options="sitesDropValues" placeholder="" optionLabel="site_name"
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
            <label for="birth_country" >Pais de Nacimiento</label>
            <InputText id="birth_country" v-model="currentUser.birth_country" required="true" autofocus
                :class="{ 'p-invalid': submitted && !currentUser.birth_country }" />
            <small class="p-invalid" v-if="submitted && !currentUser.birth_country">País de nacimiento es
                obligatorio.</small>
        </div>

        <!-- Sample Dropdown field with validation -->


        <!-- Sample input field with validation -->
        <div class="field">
            <label for="birth_department">Departamento de Nacimiento</label>
            <Dropdown filter v-model="departamentDropValue" :options="departamentos" optionLabel="departamento"
                placeholder="" required="true" :class="{ 'p-invalid': submitted && !currentUser.gender }" />
            <small class="p-invalid" v-if="submitted && !currentUser.gender">el genero es obligatorio
            </small>
        </div>

        <!-- Sample input field with validation -->
        <div class="field">
            <label for="birth_city">Ciudad de Nacimiento</label>
            <Dropdown filter v-model="cityDropValue" :options="departamentDropValue.ciudades" placeholder="" required="true"
                :class="{ 'p-invalid': submitted && !currentUser.gender }" />
            <small class="p-invalid" v-if="submitted && !currentUser.gender">el genero es obligatorio
            </small>
        </div>

        <div class="field">
            <label for="blood_type">Tipo de sangre</label>
            <Dropdown v-model="currentUser.blood_type" :options="bloodTypesDropValues" placeholder="" required="true"
                :class="{ 'p-invalid': submitted && !currentUser.blood_type }" />
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
            <Dropdown v-model="currentUser.marital_status" :options="maritalStatusDropValues" placeholder="" required="true"
                :class="{ 'p-invalid': submitted && !currentUser.marital_status }" />
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
            <Dropdown v-model="currentUser.contract_type" :options="employmentContractTypeDropValues" placeholder=""
                required="true" :class="{ 'p-invalid': submitted && !currentUser.contract_type }" />
            <small class="p-invalid" v-if="submitted && !currentUser.contract_type">Tipo de Contrato es
                obligatorio.</small>
        </div>

        <div class="field">
            <label for="eps">EPS</label>
            <Dropdown filter v-model="currentUser.eps" :options="epsDropValues" placeholder="" required="true"
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
            <Dropdown v-model="currentUser.housing_type" :options="housingTypesDropValues" placeholder="" required="true"
                :class="{ 'p-invalid': submitted && !currentUser.housing_type }" />
            <small class="p-invalid" v-if="submitted && !currentUser.housing_type">Tipo de vivienda es
                obligatorio.</small>
        </div>


        <div class="field inputSwith">
            <label for="has_vehicle">Tiene Vehiculo</label>
            <InputSwitch id="has_vehicle" v-model="currentUser.has_vehicle" />
        </div>

        <div class="field" v-show="currentUser.has_vehicle">
            <label for="vehicle_type">Tipo de Vehiculo</label>
            <Dropdown v-model="currentUser.vehicle_type" :options="vehicleTypesDropValues" placeholder="" required="true"
                :class="{ 'p-invalid': submitted && !currentUser.vehicle_type }" />
            <small class="p-invalid" v-if="submitted && !currentUser.vehicle_type">Tipo de Vehiculo es
                obligatorio.</small>
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
            <Dropdown v-model="currentUser.shirt_size" :options="shirtSizesDropValues" placeholder="" required="true"
                :class="{ 'p-invalid': submitted && !currentUser.shirt_size }" />
            <small class="p-invalid" v-if="submitted && !currentUser.shirt_size">Talla de camisa es
                obligatoria.</small>
        </div>

        <div class="field">
            <label for="jeans_sweater_size">Talla de Pantalón</label>
            <Dropdown v-model="currentUser.jeans_sweater_size" :options="pantSizesDropValues" placeholder="" required="true"
                :class="{ 'p-invalid': submitted && !currentUser.jeans_sweater_size }" />
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
            <small class="p-invalid" v-if="submitted && !currentUser.food_handling_certificate_number">Número de
                certificado es obligatorio.</small>
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


        <div class="field">
            <label for="status">Estado</label>
            <Dropdown v-model="currentUser.status" :options="statusDropValues" placeholder="" required="true"
                :class="{ 'p-invalid': submitted && !currentUser.status }" />
            <small class="p-invalid" v-if="submitted && !currentUser.status">Estado es obligatorio.</small>
        </div>

        <div class="field" v-show="currentUser.entry_date && currentUser.status == 'inactivo'">
            <label for="exit_date">Fecha de Salida</label>
            <Calendar id="exit_date" v-model="currentUser.exit_date" required="false" />
        </div>

        <div class="field" v-show="currentUser.exit_date && currentUser.entry_date && currentUser.status == 'inactivo'">
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
                        </Dropdown>s
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
            <Button label="Salir" icon="pi pi-times" class="p-button-text" @click="hideDialog" />
            <Button label="Guardar" icon="pi pi-check" class="p-button-text" @click="saveProduct" />
        </template>
    </Dialog>
</template>

<script setup>
import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount, computed } from 'vue';
import { useToast } from 'primevue/usetoast';
import { departamentos, findByDepartament } from '@/service/CountryService.js'
import { uploadUserPhotoProfile } from '@/service/sendFileService'
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
    findSiteByName,
    getSites

} from '@/service/dropDownAux';
import { getUsers, } from '@/service/userServices'
import { URI } from "@/service/conection.js"
// import logo from '@/images/logo.png'
import { getUserRole } from '@/service/valoresReactivosCompartidos.js'
import * as XLSX from 'xlsx';
import { defineProps } from 'vue';
import { getUserDni } from '../../service/valoresReactivosCompartidos';
import router from '../../router';
import { roles,verificarRol } from '../../service/roles';
// import { getUserRole } from '../../service/valoresReactivosCompartidos';
const toast = useToast();
const users = ref([]);
const adding = ref(false);
const productDialog = ref(true);
const currentUser = ref({});
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
const cityDropValue = ref([])
const excelData = ref(null);
const imageUrlUserAdd = ref("file:///home/ludi/Downloads/9aa6397c673a5906ed994997df3a66bdc3e4f68dr1-194-259v2_00.jpg")
const op = ref(null);
const op2 = ref(null);
const file = ref(null)
const urlPhotoProfile = ref("")


const hideDialog = () => {
    productDialog.value = false;
    submitted.value = false;
    adding.value = false
    // resetValuesNewEntry()
    currentUser.value = {};
    router.push('/')
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

const getUser = async (dni) => {
    fetch(`${URI}/employer/dni/${dni}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            return response.json();
        })
        .then(data => {
            console.log('Employer data:', data);
            currentUser.value = data
            SiteDropValue.value = findSiteById(data.site_id)
            departamentDropValue.value = findByDepartament(data.birth_department) || []
            cityDropValue.value = data.birth_city
            statusDropValue.value = data.status 
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            currentUser.value = {}

        });
}



const asingDataToSave = () => {
    const { ...data } = currentUser.value;

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

const saveProduct = async () => {
    let Method = "PUT"
    let queryUrl = ""

    const data = asingDataToSave()


    queryUrl = `${URI}/employer/${currentUser.value.id}`


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
            file.value ? uploadUserPhotoProfile(file.value, data.dni) : ''

            adding.value ? toast.add({ severity: 'success', summary: 'Usuario registrado', detail: 'Hecho', life: 3000 }) :
                toast.add({ severity: 'success', summary: 'Usuario actualizado', detail: 'Hecho', life: 3000 })

            hideDialog()

            return response.json();
        })
        .then(data => {
            // Aquí puedes trabajar con los datos actualizados
            console.log('Datos actualizados:', data);

            // Cambiar el valor de serverResponse de manera reactiva
            serverResponse.value = data;

            // Verificar si la respuesta del servidor es 'ok' y actualizar productDialog

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
urlPhotoProfile.value = null

//valores booleanos que vienen de mysql son uno y cero

// despues de alterar el edit user lo enviamos al valor del usuario actual
currentUser.value = { ...editUser };
productDialog.value = true;
adding.value = false
};
const props = defineProps({
    user: Object, // Define el tipo de la prop (en este caso, String)
});


onMounted(() => {
    // currentUser.value = props.user
    getUser(getUserDni())
    getSites()
})






</script>