<template>

    

<p style="text-transform: capitalize; max-width: ;" class="text-2xl ml-2 py-2">
    {{ ruta.params.sesion }} 
</p> 

<!-- {{ products }} -->
<Toast style="box-shadow: none;"  />
<div class="grid">

</div>

    <div class="grid p-2 col-12 m-auto" style="max-width: 1024px;" >
        <div v-for="product in products" :key="product.id" class="xl:col-3 lg:col-4 md:p-3 col-12 m-0 ">

    <div class="cont p-2" style="background-color: white; height: 100%;position: relative"  >
        <!-- <router-link :to="`product/${product.id}` " @click="changeProduct(product)"> -->

            <button style="position: absolute;top: -1rem;right: -1rem;background-color:var(--primary-color); width: 2.5rem;height: 2.5rem;border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white;z-index: 99;" @click="prepararParaEditar" class="add-cart-btn text-xl"><i   class="icono text-2xl  p-0 m-0 " :class="PrimeIcons.PENCIL"> </i>  </button>

            

            <button  style="position: absolute;top: -1rem;right: 2rem;background-color:var(--red-500); width: 2.5rem;height: 2.5rem;border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white;z-index: 99;" @click="pregpararParaEliminar" class="add-cart-btn text-xl"><i  class="icono text-2xl  p-0 m-0 " :class="PrimeIcons.TRASH"> </i>  </button>


            <div class="imagen-cont " style="position: ;">
                <!-- <img class="imagen" @error="imagenError" :src="`${URI}/read_product_image/300/${product.id}`" alt=""> -->
                <img class="imagen" @error="imagenError" style="height: 50;" :src="`${URI}/read-product-image/300/${product.name}`" alt="">
                
            
            </div>
           

        <!-- </router-link> -->
        <!-- <img class="imagen" src="src/images/iconos menu/salchipapa-icono.png" alt=""> -->

        
            <div style=" display: ; " >
                <p class="nombre-producto mt-4 " style="font-weight: bold;" > {{ product.name }}</p>
                <p class="descripcion-producto mt-2 text-sm mb-4" > {{ product.description }}</p>
                
            </div>

            
            <Toast style="box-shadow: none;"  />
       

        <div class="info " >
            <!-- {{ showEditarProducto }} -->
            
            <div class="text-l" style="font-weight: bold;border-radius: 100px; "> {{ formatoPesosColombianos(product.price) }}</div>

            <InputSwitch v-model="product.isActive" @change="() => updateProductState(product)" />


        </div> 


        
    </div>


    <!-- {{ productoAEditar }} -->







    <!-- <dialogoEditarProducto></dialogoEditarProducto> -->

        </div>
    </div>



 
<!-- <dialogoAgregarProducto></dialogoAgregarProducto> -->
<!-- <dialogoEditarProducto></dialogoEditarProducto> -->




<Dialog header="Confirmation" v-model:visible="showEliminarProducto" :style="{ width: '350px' }" style="background-color: white; color: black;" :modal="true">
                    <div class="flex align-items-center justify-content-center">
                        <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
                        <span style="color:black;">No esta autorizado para eliminar  <b>{{ productoAEliminar.name }}</b></span>
                    </div>
                    <template #footer>
                        <Button label="Salir" icon="pi pi-times" @click="showEliminarProducto = !showEliminarProducto" class="p-button-text" />
                        <!-- <Button label="Si" icon="pi pi-check" @click="eliminarProducto" class="p-button-text" autofocus /> -->
                    </template>
</Dialog>

</template>

<script setup>
import TarjetaMenu from '@/components/TarjetaMenu.vue';
import { formatoPesosColombianos } from '../../../service/formatoPesos';
import { PrimeIcons } from 'primevue/api';
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { URI } from '@/service/conection';
import router from '@/router/index.js';
import { productoAEliminar } from '../../../service/valoresReactivosCompartidos';
import { categoryValue,siteDropValue} from '@/service/valoresReactivosCompartidos';
// import dialogoAgregarProducto from '../../../components/dialogos/dialogoAgregarProducto.vue';
// import dialogoEditarProducto from '../../../components/dialogos/dialogoEditarProducto.vue';
import { showAgregarProducto, showEliminarProducto } from '../../../service/valoresReactivosCompartidos';
// import { siteDropValue } from '../../../service/valoresReactivosCompartidos';
// import { categoryValue } from '../../../service/valoresReactivosCompartidos';
import { productoEnviado } from '../../../service/valoresReactivosCompartidos';









// import { changeProduct } from '../service/productServices';

import {useCart} from '@/service/cart'
// import { menuGlobal } from '../service/menu/menu';
// import { check_site, setProductDialog,showProductDialog } from '../service/state';
import { useToast } from 'primevue/usetoast';
// import { comprobar_sede } from '../service/state';
// import dialogoAgregarProducto from './dialogos/dialogoAgregarProducto.vue';
// import { productoAEliminar, showEditarProducto, showEliminarProducto } from '../service/valoresReactivosCompartidos';
// import dialogoEditarProducto from './dialogos/dialogoEditarProducto.vue';
// import { onMounted, ref, watch } from 'vue';
// import { productoAEditar } from '../service/valoresReactivosCompartidos';
const toast = useToast();
const isActive = ref([]);


// const prepararParaEditar = () => {
//     showEditarProducto.value = !showEditarProducto.value
//     productoAEditar.value = product
// }
const displayConfirmation = ref(false)


const isInitialWatchCall = ref(true)


// watch(isActive, (newValue) => {

//     if (isInitialWatchCall.value) {
//         isInitialWatchCall.value = false;
//         return;
//     }

//     // Tu lógica aquí, se ejecutará solo en cambios después del montaje
//     updateProductState();
// });

// onMounted(async () => {
//     isActive.value = product.state == 'active';
// });


// watch(product.state, () => {
//     isActive.value = product.state == 'active';
// })

// const pregpararParaEliminar = () => {
    
//     showEliminarProducto.value = !showEliminarProducto.value
//     productoAEliminar.value = product
// }

const updateProductState = (product) => {

    const data = {...product}    
    data.state = product.isActive? 'active': 'inactive'
    // console.log(data)

    fetch(`${URI}/products/${product.product_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        toast.add({ severity: `${!isActive.value? 'error':'success'}`, summary: `${!isActive.value? 'Desactivado':'Activado'}`, detail: product.name, life: 3000 });
        isActive.value = product.state == 'active';
        // location.reload()
        return response.json(); 
    })
    .then(data => {
        // Manejar la respuesta (puedes mostrar un mensaje de éxito, por ejemplo)
    })
    .catch(error => {
        console.error('Error al actualizar el producto:', error);
    });
};








































const products = ref([]); // Definiendo la variable reactiva para almacenar los productos
const ruta = useRoute(); // Usando useRoute para acceder a los parámetros de la ruta
// const categories = ref([]);
const getProducts = async (category_name) => {

    console.log(localStorage)

    const site_id = localStorage.getItem('siteId')
    try {
        
        let response = await fetch(`${URI}/products/category/name/${category_name}/site/${site_id}`);
        if (!response.ok) {
            products.value = [];
            throw new Error(`HTTP error! status: ${response.status}`);
           
        }
        let data = await response.json();
        products.value = data.map(product => ({
        ...product,
        isActive: product.state == 'active' // Inicializar el campo isActive basado en los datos del servidor

    }));
    } catch (error) {
        products.value = [];
        console.error('Error fetching data: ', error);
    }
}



const toggleProductState = async (product) => {
    try {
        // Actualizar el estado en el frontend
        product.isActive = !product.isActive;

        // Enviar actualización al backend
        const response = await fetch(`${URI}/products/${product.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(...product)
        });

        if (!response.ok) {
            throw new Error('Error al actualizar el estado del producto');
        }

        // Opcional: Mostrar mensaje de éxito
        toast.add({ severity: 'success', summary: 'Producto actualizado', detail: product.name, life: 3000 });
    } catch (error) {
        console.error('Error al actualizar el producto:', error);
        // Revertir cambio en el frontend en caso de error
        product.isActive = !product.isActive;
    }
};


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

.info {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    /* background-attachment: fixed; */
    /* position: absolute; */

    
    /* gap: 20px; */
 
    /* padding: 20px; */
}




.nombre-producto,.descripcion-producto{
    text-transform: lowercase;
}

.nombre-producto,.descripcion-producto::first-letter{
    text-transform: uppercase;
}

.descripcion-producto{
overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* Number of lines you want to display */
  -webkit-box-orient: vertical;
  max-height: 4.5em; /* Adjust based on line-height and number of lines */
  line-height: 1.5em;
}

.add-cart-btn{
    /* transition: all  0.2s ease; */
    border-radius: 50%;
    border: none;
    /* height: 3rem; */
    /* width: 3rem; */
    /* display: flex; */
    /* align-items: center; */
    /* justify-content: center; */

    /* padding: 1rem 1rem; */
    font-size: 20px;
    background-color: rgba(251, 0, 0, 0);
    /* border-radius: 10px; */
    color: #ff0000;
}

.add-cart-btn .icono{

    color: #fff;
}




*:focus{
    outline: none;
}

.icono{
    /* transition: all  0.2s ease; */
    color: var(--primary-color);
    /* transform: translateX(-15px); */
    font-weight: bold;
}
.cont {
    /* border: 1px solid gray; */
    border-radius: 1rem;
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.3);
    /* margin: 20px; */
    /* height: max-content; */
    /* width: 100%; */
    /* padding: 5%; */
    /* min-height: 100%; */
    /* max-height: 100%; */
    /* padding-bottom: 6rem;     */
    position: relative;
    margin: 0;


    /* margin: 0px; */
    /* width: 90%; */
    /* width: 100%; display: flex; */
    /* margin: auto; */

    /* height: 100%; */
    /* max-height: ; */
    /* background-color: red; */
    /* margin:1rem; */
}
/* .cont:hover .imagen{
    filter: brightness(1);
    transform: scale(1.1) rotate(3deg); */
    /* filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 123, 0)); */
    /* filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(0, 0, 0)); */


.cont:hover .add-cart-btn{
    
    /* transform: translateY(-10px); */
}
.imagen:hover {
    filter: brightness(1.1);
    /* box-shadow: 0px 0px 30px var(--primary-color); */
    background-color: #ff620035;
}
.imagen{
    width: 100%;
    object-fit: contain;
    height: 200px;
    transition: transform ease .3s ;;
 
    /* background-image: url('https://i.ytimg.com/vi/yvIhfmAfsck/maxresdefault.jpg'); */
    /* height: 100%; */
    /* background-color: red; */
    /* filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 123, 0)); */
}

.imagen-cont{
    /* width: 100%; */
    overflow: hidden;
    border-radius:0.5rem;
    /* height: max-content; */
    /* background-color: green; */

}

button{
    cursor: pointer;
}

.col-12 {

}</style>