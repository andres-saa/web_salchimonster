<template>
    <Dialog v-model:visible="showAgregarProducto" :style="{ width: '500px', height: 'max-content' }" header="Agregar producto"
        :modal="true" class="p-fluid p-2 m-3" style="   ; background-color: white;border-radius:1rem;overflow:hidden">


        <!-- {{ grupoSalsasdropValue }} -->

        <!-- <h5>Foto del Producto</h5> -->



<div v-if="urlFoto">
    <!-- <h5>Previsualización de la Foto</h5> -->
    <img :src="urlFoto" alt="Previsualización del Producto" style="max-width: 100%; height: auto;" />
</div>

<Input type="file" @change="cargarFoto" accept="image/*" />


        <h5>Nombre</h5>
        <span class="p-input-icon-left mb-4">
            <i class="pi pi-pencil" />
            <InputText v-model="nombre" type="text" />
        </span>

        <h5>Description</h5>
        <Textarea v-model="description" :autoResize="true" rows="3" cols="30" />

        <h5>Precio</h5>
        <span class="p-input-icon-left">
            <i class="pi pi-pencil" />
            <InputText v-model="precio" type="number" placeholder="Precio" />
        </span>

        <h5 style="display: flex; align-items: center;"> <InputSwitch class="p-0 m-0" v-model="checkedValuesSalsas" /> 
            <span class="ml-5">Conjunto de salsas</span></h5>
        <span v-if="checkedValuesSalsas" class="p-input-icon-left">

                <Dropdown style="outline: none; " class="p-0  " primary v-model="grupoSalsasdropValue" :options="grupoSalsasdropValues"
                    optionLabel='name' />
        </span>

        <h5 style="display: flex; align-items: center;"> <InputSwitch class="p-0 m-0" v-model="checkedValuesAdiciones" /> 
            <span class="ml-5">Conjunto de adiciones</span></h5>
        <span class="p-input-icon-left">
            <Dropdown v-if="checkedValuesAdiciones" style="outline: none; " class="p-0  " primary v-model="grupoAdicionesDropValue" :options="grupoAdicionesDropValues"
                    optionLabel='name' />
        </span>

        <h5 style="display: flex; align-items: center;"> <InputSwitch class="p-0 m-0" v-model="checkedValuesAcompanantes" /> 
            <span class="ml-5">Conjunto de acompanantes</span></h5>
        <span class="p-input-icon-left">
            <Dropdown v-if=" checkedValuesAcompanantes" style="outline: none; " class="p-0  " primary v-model="GrupoAcompananterDropvalue" :options="grupoAcompanantesDropValues"
                    optionLabel='name'  />
        </span>

        <h5 style="display: flex; align-items: center;"> <InputSwitch class="p-0 m-0" v-model="checkedValuesToppinns" /> 
            <span class="ml-5">Conjunto de toppings</span></h5>
        <span class="p-input-icon-left">
            <Dropdown v-if="checkedValuesToppinns" style="outline: none; " class="p-0  " primary v-model="GrupoToppingsDropValue" :options="grupoToppingsDropValues"
                    optionLabel='name'  />
        </span>


        <h5 style="display: flex; align-items: center;"> <InputSwitch class="p-0 m-0" v-model="checkedValuesCambios" /> 
            <span class="ml-5">Conjunto de cambios</span></h5>
        <span class="p-input-icon-left">
            <Dropdown v-if="checkedValuesCambios" style="outline: none; " class="p-0  " primary v-model="grupoCambiosDropValue" :options="grupoCambiosDropValues"
                    optionLabel='name'  />
        </span>


        <h5 style="display: flex; align-items: center;"> 
            <span class="">Estado</span></h5>
        <span class="p-input-icon-left">
            <Dropdown style="outline: none; " class="p-0  " primary v-model="estado" :options="estados"
                     />
        </span>



        <h5 style="display: flex; align-items: center;">  
            <span class="ml-0 mt-6" style="text-transform: capitalize; ">Sedes en las que estara disponible el producto  {{ nombre }}</span></h5>
        
        <div class="mt-6">            
            <h5 style="display: flex; align-items: center;"> <InputSwitch class="p-0 m-0" v-model="todasLasSedes" /> 
            <span class="ml-5">Todas</span></h5>

            <div  v-for="sede in siteDropValues" >
            <h5 style="display: flex; align-items: center;"> <InputSwitch class="p-0 m-0" v-model="sedesSeleccionadas[sede.site_id]" /> 
            <span class="ml-5">{{ sede.site_name }}</span></h5>
        </div>
        </div>
         



             
               
        <!-- <span class="p-input-icon-left">
                            <i class="pi pi-user" />
                            <InputText type="text" placeholder="Username" />
                        </span> -->


                        <Button @click="enviarProducto" class="m-auto my-4 text-center"> <span class="text-center col-12 p-0">Agregar</span></Button>







    </Dialog>

    <toast></toast>
</template>



<script setup>
import { onMounted, ref,computed } from 'vue';
import { useToast } from 'primevue/usetoast';
import { 
    showAgregarProducto, 
    categoryValue, 
    siteDropValues,
    grupoAdicionesDropValue, 
    grupoCambiosDropValue, 
    grupoSalsasdropValue, 
    GrupoAcompananterDropvalue, 
    GrupoToppingsDropValue } from '@/service/valoresReactivosCompartidos.js'
import { URI } from '../../service/conection';
import { checkedAdiciones } from '../../service/state';
import { useRoute } from 'vue-router';
import { getProductsByCategory } from '../../service/productServices';

import { watch } from 'vue';
import { productoEnviado } from '../../service/valoresReactivosCompartidos';
import { fotos } from '../../service/menu/fotos';






const urlFoto = ref(null);
const file = ref(null);

// Función para cargar y previsualizar la foto
const cargarFoto = (event) => {
    const archivo = event.target.files[0];
    if (archivo) {
        urlFoto.value = URL.createObjectURL(archivo);
        file.value = archivo
    }
};



// const handleFileChange = (event) => {
//     const file = event.target.files[0];
//     if (file) {
//         selectedFile.value = file;
//         imageUrl.value = URL.createObjectURL(file);
//     }
// };







const toast = useToast();
const route = useRoute();
const category_id = computed(() => route.query.category);
const sedesSeleccionadas = ref([]);
const todasLasSedes = ref(false);


watch(todasLasSedes, (nuevoValor) => {
  siteDropValues.value.forEach(sede => {
    sedesSeleccionadas.value[sede.site_id] = nuevoValor;
  });
});





function actualizarSeleccionSede(site_id) {
  if (sedesSeleccionadas.value.includes(site_id)) {
    sedesSeleccionadas.value = sedesSeleccionadas.value.filter(id => id !== site_id);
  } else {
    sedesSeleccionadas.value.push(site_id);
  }
}



console.log(category_id.value)



const nombre = ref("producto sin nombre")
const description = ref("producto sin descripcion")
const precio = ref(0)
const estado = ref('inactive')
const estados = ref(['active', 'inactive'])



const grupoSalsasdropValues = ref([])
const grupoAdicionesDropValues = ref([])
const grupoCambiosDropValues = ref([])
const grupoAcompanantesDropValues = ref([])
const grupoToppingsDropValues = ref([])


const checkedValuesSalsas = ref()
const checkedValuesAdiciones = ref()
const checkedValuesToppinns = ref()
const checkedValuesCambios = ref()
const checkedValuesAcompanantes = ref()







const enviarProducto = async () => {
    const url = `${URI}/products`;
    uploadImage(nombre.value);


    for (const [site_id, isSelected] of Object.entries(sedesSeleccionadas.value)) {
        if (isSelected) {
            const nuevoProducto = {
                "name": nombre.value,
                "price": precio.value,
                "description": description.value,
                "category_id": category_id.value,
                "porcion": "1",
                "state": estado.value,
                "grupo_salsa_id": grupoSalsasdropValue.value ? grupoSalsasdropValue.value.grupo_salsa_id : null,
                "grupo_topping_id": GrupoToppingsDropValue.value ? GrupoToppingsDropValue.value.grupo_topping_id : null,
                "grupo_acompanante_id": GrupoAcompananterDropvalue.value ? GrupoAcompananterDropvalue.value.grupo_acompanante_id : null,
                "grupo_cambio_id": grupoCambiosDropValue.value ? grupoCambiosDropValue.value.grupo_cambio_id : null,
                "grupo_adicional_id": grupoAdicionesDropValue.value ? grupoAdicionesDropValue.value.grupo_adicional_id : null,
                "site_id": site_id
            };

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(nuevoProducto)
                });

                if (!response.ok) {
                    throw new Error(`Error: ${response.status}`);
                }
                toast.add({ severity:'success' , summary:`agregado a la sede ${site_id}` , detail: 'espaerando las otras sedes', life: 3000 });
                productoEnviado.value = productoEnviado.value + 1
               
                
            } catch (error) {
                console.error('Error al enviar producto:', error);
            }
        }
    }

    showAgregarProducto.value = false;
    // location.reload();
};



const uploadImage = async (productId) => {
    const formData = new FormData();
    formData.append('file', file.value);
    
    try {
        const response = await fetch(`${URI}/upload-product-image/${productId}`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Error al subir la imagen');
        }

        // Manejar respuesta de éxito
    } catch (error) {
        console.error('Error al subir la imagen:', error);
        // Manejar error
    }
};

































const getGrupoSalsas = async () => {
    try {
        let response = await fetch(`${URI}/grupo-salsas`);
        let data = await response.json();
        // categories.value = data
        return data
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}

const getGrupoCambios = async () => {
    try {
        let response = await fetch(`${URI}/grupo-cambios`);
        let data = await response.json();
        // categories.value = data
        return data
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}

const getGrupoAdiciones = async () => {
    try {
        let response = await fetch(`${URI}/grupo-adicionales`);
        let data = await response.json();
        // categories.value = data
        return data
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}

const getGrupoGrupoToppings = async () => {
    try {
        let response = await fetch(`${URI}/grupo-toppings`);
        let data = await response.json();
        // categories.value = data
        return data
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}

const getGrupoGrupoAcompanantes = async () => {
    try {
        let response = await fetch(`${URI}/grupo-acompanantes`);
        let data = await response.json();
        // categories.value = data
        return data
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}


onMounted(async () => {
    
    getGrupoSalsas().then(data => { grupoSalsasdropValues.value = data })
    getGrupoAdiciones().then(data => { grupoAdicionesDropValues.value = data })
    getGrupoCambios().then(data => { grupoCambiosDropValues.value = data })
    getGrupoGrupoAcompanantes().then(data => { grupoAcompanantesDropValues.value = data })
    getGrupoGrupoToppings().then(data => { grupoToppingsDropValues.value = data })


    siteDropValues.value.forEach(sede => {
        sedesSeleccionadas.value[sede.site_id] = false;
    });

})


</script>


<style scoped>

*{
    text-transform: lowercase;
}


*::first-letter{text-transform: uppercase;}
</style>