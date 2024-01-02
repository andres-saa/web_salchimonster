<template>
    <div class="" style="display: flex; overflow-x: auto; position: sticky; z-index: 999; top: 4rem; background-color: rgb(255, 255, 255); box-shadow: 0 0 1rem rgba(0, 0, 0, 0.337);">
        <div v-for="section in categories" :key="section.category_id" class="p-1" >
            <button @click="navigateToCategory(section.category_name)" :class="checkSelected(section.category_name) ? 'selected menu-button' : 'menu-button'" class="p-2 text-lg"  style="font-weight: 500; text-transform: uppercase;">
                {{ section.category_name }}
            </button>
        </div>
    </div>
    
</template>





<script setup>
import { ref, onMounted } from 'vue';
import router from '@/router/index.js';
import { URI } from '@/service/conection';
import { useRoute } from 'vue-router';

const route = useRoute()
const categories = ref([]);
const ruta = ref(router.currentRoute);
// const route = useRoute();

const getCategories = async () => {
    try {
        let response = await fetch(`${URI}/categories`);
        let data = await response.json();
        categories.value = data;
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}

const navigateToCategory = (categoryName) => {
    router.push({ name: 'sesion', params: { menu_name: categoryName }});
};

onMounted(getCategories);


const checkSelected = (section) => {
    const route = useRoute(); // Asegúrate de que tienes acceso a useRoute aquí
    return route.path.includes(section); // Verifica si el path actual contiene la cadena section
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
    outline: none;
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
    width: 100vw;
    /* position: absolute; */
    left: 0;
    padding: 1.5rem;
}</style>