<template>
    <div style="display: flex; align-items: center;" class="col p-2 col-12">
        <Dropdown class="col-12 md:col-6 p-0   " v-model="siteDropValue" :options="siteDropValues" optionLabel="site_name"
            placeholder="sede" />
    </div>
    <div class="grid col-12 m-0 p-0 ">

        <div class="col p-2">
            <Dropdown style="outline: none; " class="p-1 col-12  " primary v-model="categoryValue" :options="categories"
                 placeholder="Productos" >


            <template #value="data">
                <div> <i :class="PrimeIcons.STAR_FILL" class="mr-2"></i>{{ data.value?.category_name? data.value.category_name:{} }}</div> 
               

            </template>

            <template #option="data">
                    <div>
                        <span> <i :class="data.option.category_name == 'Nueva categoria'? PrimeIcons.PLUS_CIRCLE:  PrimeIcons.TRASH" class="mr-3"></i></span>{{ data.option.category_name }}
                    </div>
                </template>



        </Dropdown>

        </div>


        <div v-for="menu in MenuOptions" class="col p-2 ">
            <RouterLink :to="`/tienda-menu/${menu.to}`">
                <Button :style="`background-color:${pastelColors[menu.to]}`" class="outlined col-12 p-3 text-center"
                    outlined Secondary> <span style="width: 100%;" sclass="text-center"> {{ menu.name }}</span> </Button>
            </RouterLink>

        </div>
    </div>

    <RouterView />



    <Dialog header="Confirmation" v-model:visible="showAgregarCategoria" :style="{ width: '350px' }" :modal="true">
        <h5>Nombre de la nueva categoria</h5>
        <span class="p-input-icon-left " style="width: 100%;">
            <i class="pi pi-pencil" />
            <InputText v-model="nameNewCategorie" class="w-100" style="width: 100%;"  type="text"  />
        </span>

        <Button @click="createCategory()" style="margin:auto ;" class="m-auto my-4 text-center"> <span class="text-center col-12 p-0">Agregar Categoria</span></Button>

    </Dialog>

   

</template>

<script setup>
import crud from '@/views/pages/Crud.vue'
import ListaProductos from './ListaProductos.vue';
import { onMounted, ref } from 'vue';
import { URI } from '../../../service/conection';
import { watch } from 'vue';
import router from '@/router/index.js';
import { pastelColors,siteDropValues } from '../../../service/valoresReactivosCompartidos';
// import { RouterView } from 'vue-router';
import dialogoEditarProducto from '../../../components/dialogos/dialogoEditarProducto.vue';

// import router from '@/router/index.js';

import { useRoute } from 'vue-router';

const route = useRoute()
import { categoryValue, siteDropValue } from '@/service/valoresReactivosCompartidos.js'
import { PrimeIcons } from 'primevue/api';

const showAgregarCategoria = ref(false)
const categories = ref([]);
const nameNewCategorie = ref()
const ruta = ref();
// const route = useRoute();



const getCategories = async () => {
    try {
        let response = await fetch(`${URI}/categories`);
        let data = await response.json();
        // categories.value = data
        return data
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}














watch(categoryValue, (newValue, oldValue) => {
    if (newValue !== oldValue) {
        console.log(oldValue, newValue);
        // Save the new value to localStorage
        localStorage.setItem('categoryValue', JSON.stringify(newValue));

        // Perform the router push based on the new value
        if (newValue.category_name != 'Nueva categoria') {
            router.push({
                path: `/tienda-menu/productos/${newValue.category_name}`,
                query: { category: newValue.category_id }
            });
        } else {
           showAgregarCategoria.value = true
        }
    }
});

watch(siteDropValue, (newValue, oldValue) => {
    if (newValue !== oldValue) {
        console.log(oldValue, newValue);
        // Save the new value to localStorage
        localStorage.setItem('siteDropValue', JSON.stringify(newValue));

        // Additional actions based on the new siteDropValue
        // Perform actions similar to what you did with categoryValue, if necessary
    }
});

const createCategory = async () => {
    const url = `${URI}/categories`; // Replace with your actual API endpoint

    const categoryData = {
        category_name:nameNewCategorie.value

    }
    try {
        const response = await fetch(url, {
            method: 'POST', // HTTP method
            headers: {
                'Content-Type': 'application/json' // Content type
            },
            body: JSON.stringify(categoryData) // Convert the category data to a JSON string
        });

        if (!response.ok) {
            showAgregarCategoria.value = false
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const responseData = await response.json(); // Convert response to JSON
        console.log('Success:', responseData);
        
        showAgregarCategoria.value = false
        prepararCategorias()
        router.push({
                path: `/tienda-menu/`,
            });
        
        // Perform actions after successful creation, like updating UI or redirecting
    } catch (error) {
        console.error('Error:', error);
        // Handle errors, like showing error messages to the user
    }
};


const MenuOptions = [


    {
        name: 'Adiciones',
        to: 'adicionales'
    },
    {
        name: 'Salsas',
        to: 'salsas'
    },
    {
        name: 'Topping',
        to: 'toppings'
    },
    {
        name: 'Cambios',
        to: 'cambios'
    },
    {
        name: 'Acompanantes',
        to: 'acompanantes'
    }
]

const getSites = async () => {
    try {
        const response = await fetch(`${URI}/sites`)
        const data = response.json()
        return data
    } catch (error) {
        console.log(error)
    }
}


const prepararCategorias = () => {

    getCategories().then(data => {
        categories.value = data
        categories.value.push(
            {
                category_name: 'Nueva categoria'
            }

        )
    })
    
}


onMounted(async () => {

    const initialCategoryValue = localStorage.getItem('categoryValue');
    if (initialCategoryValue) {
        categoryValue.value = JSON.parse(initialCategoryValue);
    }

    const initialSiteValue = localStorage.getItem('siteDropValue');
    if (initialSiteValue) {
        siteDropValue.value = JSON.parse(initialSiteValue);
    }

    getSites().then(data => siteDropValues.value = data)
    prepararCategorias()
    
})


</script>                                                                                                                                                                                                                                                                