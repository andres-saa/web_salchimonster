<template>

    

<p style="text-transform: capitalize; max-width: ;" class="text-2xl ml-2 py-2">
    {{ ruta.params.sesion }} 
</p> 
<span>
    <Button  @click="showAgregarProducto = !showAgregarProducto" class=" ml-2 mb-4"> Agregar  </Button>
</span>

    <div class="grid p-2 col-12 m-auto" style="max-width: 1280px;" >
        <div v-for="product in products" :key="product.id" class="xl:col-3 lg:col-4 md:p-3 col-12 m-0 ">
            <TarjetaMenu class="col-12 m-0 p-0"  :product="product"></TarjetaMenu>
        </div>
    </div>



 
<dialogoAgregarProducto></dialogoAgregarProducto>
<dialogoEditarProducto></dialogoEditarProducto>




<Dialog header="Confirmation" v-model:visible="showEliminarProducto" :style="{ width: '350px' }" :modal="true">
                    <div class="flex align-items-center justify-content-center">
                        <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
                        <span>Seguro que desea eliminar <b>{{ productoAEliminar.name }}</b></span>
                    </div>
                    <template #footer>
                        <Button label="No" icon="pi pi-times" @click="showEliminarProducto = !showEliminarProducto" class="p-button-text" />
                        <Button label="Si" icon="pi pi-check" @click="eliminarProducto" class="p-button-text" autofocus />
                    </template>
</Dialog>

</template>

<script setup>
import TarjetaMenu from '@/components/TarjetaMenu.vue';
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { URI } from '@/service/conection';
import router from '@/router/index.js';
import { productoAEliminar } from '../../../service/valoresReactivosCompartidos';
import { categoryValue,siteDropValue} from '@/service/valoresReactivosCompartidos';
import dialogoAgregarProducto from '../../../components/dialogos/dialogoAgregarProducto.vue';
import dialogoEditarProducto from '../../../components/dialogos/dialogoEditarProducto.vue';
import { showAgregarProducto, showEliminarProducto } from '../../../service/valoresReactivosCompartidos';
// import { siteDropValue } from '../../../service/valoresReactivosCompartidos';
// import { categoryValue } from '../../../service/valoresReactivosCompartidos';
import { productoEnviado } from '../../../service/valoresReactivosCompartidos';

const products = ref([]); // Definiendo la variable reactiva para almacenar los productos
const ruta = useRoute(); // Usando useRoute para acceder a los parámetros de la ruta

const getProducts = async (category_name) => {


    try {
        
        let response = await fetch(`${URI}/products/category/name/${category_name}/site/${siteDropValue.value.site_id}`);
        if (!response.ok) {
            products.value = [];
            throw new Error(`HTTP error! status: ${response.status}`);
           
        }
        let data = await response.json();
        products.value = data;
    } catch (error) {
        products.value = [];
        console.error('Error fetching data: ', error);
    }
}


watch(siteDropValue, (newValue, oldValue) => {
      if (newValue !== oldValue) {
        // console.log('siteValue changed from', oldValue, 'to', newValue);
        getProducts(ruta.params.sesion); // Assuming ruta.params.sesion is the correct parameter
      }
    });



watch(productoEnviado, (newValue, oldValue) => {
    if (newValue !== oldValue) {
    // console.log('siteValue changed from', oldValue, 'to', newValue);
    getProducts(ruta.params.sesion); // Assuming ruta.params.sesion is the correct parameter
    }
});



onMounted(async () => {
    getProducts(ruta.params.sesion);
});

// Opcional: Observar cambios en el parámetro de la ruta
watch(() => ruta.params.sesion, (newMenuName) => {
    getProducts(newMenuName);
});


const eliminarProducto = async () => {
    if (!productoAEliminar.value || !productoAEliminar.value.product_id) {
        console.error('No se ha seleccionado ningún producto para eliminar');
        return;
    }

    try {
        const response = await fetch(`${URI}/products/${productoAEliminar.value.product_id}`, {
            method: 'DELETE',
        });

        if (!response.ok) {
            throw new Error(`Error al eliminar el producto: ${response.status}`);
        }

        // Manejo post-eliminación, por ejemplo, actualizar la lista de productos
        await getProducts(ruta.params.sesion);
        showEliminarProducto.value = false; // Cerrar el diálogo de confirmación
        console.log(`Producto eliminado: ${productoAEliminar.value.name}`);
    } catch (error) {
        console.error('Error al eliminar el producto:', error);
    }
};


</script>

<style scoped>
.boton-menu {
    margin: 0;
    border: none;
    background-color: transparent;
    font-size: 20px;
    padding: 0 20px;
}

.menu-button {
    background-color: transparent;
    padding: 1rem;
    margin: 0 1rem;
    border: none;
    font-size: 20px;
    /* transition: all  0.3s; */
    /* font-weight: bold; */
}

.menu-button:hover {
    /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5); */
    /* transform: scale(1.1); */
    /* border-bottom:  2px red; */
    /* color: var(--primary-color); */
    /* padding:; */
    cursor: pointer;


}
*:focus{
    outline: none;
}

::-webkit-scrollbar {
  width: 12px;
  display: none;


   /* Ancho de la barra de desplazamiento */
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {

  background-color: white; /* Color del pulgar de la barra de desplazamiento */
  border-radius: 6px; /* Radio de esquinas del pulgar */
  transform: translateY(40px);
  /* padding: 50px; */
  /* display: none; */
}

.selected {
    /* color: var(--primary-color); */
    box-shadow: 0 0.5rem var(--primary-color);
    /* padding: 1rem; */
    /* font-weight: bold; */


}

.col-12 {

}</style>