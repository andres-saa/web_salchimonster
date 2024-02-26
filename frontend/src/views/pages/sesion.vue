<template>
           
<div class="grid xl:col-10 xl:m-auto p-2 m-auto" style="border-radius:2rem; margin-bottom: 5rem;max-width: 1024px;">
    <transition-group name="fade">
    <div v-for="(product, index) in products.filter(product => product.state === 'active')" :key="product.id" class="xl:col-3 lg:col-4 md:p-3 col-6 p-3 aparecer">
        


            <TarjetaMenu  :id="`tarjeta-${index}`" style="width: 100%;" :product="product"></TarjetaMenu>

 
    </div>
    </transition-group>


</div>




</template>

<script setup>
import TarjetaMenu from '@/components/TarjetaMenu.vue';
import { onMounted, ref, watch,nextTick  } from 'vue';
import { useRoute } from 'vue-router';
import { URI } from '../../service/conection';
import router from '@/router/index.js';



import { useReportesStore } from '../../store/ventas';
const store = useReportesStore()
const products = ref([]); // Definiendo la variable reactiva para almacenar los productos
const ruta = useRoute(); // Usando useRoute para acceder a los parámetros de la ruta




onMounted(async () => {
    getProducts(ruta.params.menu_name);
    await nextTick();
});

watch(() => ruta.params.menu_name, async (newMenuName) => {
    getProducts(newMenuName);
    await nextTick(); // Espera a que el DOM se actualice
});



const getProducts = async (category_name) => {
    store.setLoading(true, 'cargando productos')
    try {
        let response = await fetch(`${URI}/products/category/name/${category_name}/site/${currentCity.value.currenSiteId}`);
        if (!response.ok) {
            store.setLoading(false, 'cargando productos')

            throw new Error(`HTTP error! status: ${response.status}`);

        }
        store.setLoading(false, 'cargando productos')

        let data = await response.json();
        products.value = data;
    } catch (error) {
        store.setLoading(false, 'cargando productos')

        console.error('Error fetching data: ', error);
    }
}

onMounted(async () => {
    getProducts(ruta.params.menu_name);
});

// Opcional: Observar cambios en el parámetro de la ruta
watch(() => ruta.params.menu_name, (newMenuName) => {
    getProducts(newMenuName);
});


const currentCity = ref(JSON.parse(localStorage.getItem('currentNeigborhood')));
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
  transition: opacity 0.3s ease, transform 0.3s ease;
}

/* Estado Final de Salida: desvanecido y desplazado hacia la derecha */
.fade-leave-to {
  opacity: 0;
  transform: translateX(20rem);
}

/* Estado Inicial de Entrada: ligeramente desplazado hacia arriba y desenfocado */
.fade-enter-from {
  opacity: 0;
  transform: translateY(-10vh);
  filter: blur(10px);
}

/* Estado Final de Entrada: totalmente opaco, sin desplazamiento y enfocado */
.fade-enter-to {
  opacity: 1;
  transform: translateY(0);
  filter: blur(0);
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
    width: 100vw;
    /* position: absolute; */
    left: 0;
    padding: 1.5rem;
}</style>