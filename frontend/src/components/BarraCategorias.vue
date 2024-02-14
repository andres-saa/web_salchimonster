<template>
    <div :style="!showElement? 'transform: translateY(-5rem);opacity:0.5': ''" class="col-12 d-flex p lg:justify-content-center align-items-center mb-5 p-1 md:p-1" style="overflow-x: auto; position: sticky; z-index: 999; top: 4rem;backdrop-filter: blur(10px); background-color: rgba(255, 255, 255, 0.913); box-shadow: 0 0 1rem rgba(0, 0, 0, 0.337);">
        <div v-for="section in categories" :key="section.category_id" class="p-1" >
            <button @click="navigateToCategory(section.category_name)" :class="checkSelected(section.category_name) ? 'selected menu-button' : 'menu-button'" class="p-2 text-lg titulo"  style="font-weight: 400; text-transform: uppercase;">
               <span class="text-lg">{{ section.category_name }}</span> 
            </button>
        </div>
    </div>
    
</template>









<style scoped> 

*{transition: all .3s ease;}
</style>









<script setup>
import { ref, onMounted,onUnmounted } from 'vue';
import router from '@/router/index.js';
import { URI } from '@/service/conection';
import { useRoute } from 'vue-router';




const currentCity = ref(JSON.parse(localStorage.getItem('currentNeigborhood')));

const route = useRoute()
const categories = ref([]);
const ruta = ref(router.currentRoute);
// const route = useRoute();

const getCategories = async () => {
    try {
        let siteId = currentCity.value.currenSiteId; // Asegúrese de que esta es la forma correcta de obtener el site_id
        let response = await fetch(`${URI}/site/${siteId}/active-categories`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
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


let scrollTimer;

const handleScroll = () => {
      showElement.value = false;
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(() => {
        showElement.value = true;
      }, 500); // 2000ms (2 segundos) de inactividad antes de ocultar el elemento
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
    });

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll);
      clearTimeout(scrollTimer);
    });


const showElement = ref(true);
</script>




<style scoped>
.boton-menu {
    margin: 0;
    border: none;
    background-color: transparent;
    font-size: 20px;
    padding: 0 20px;    
}

*{
    text-transform: lowercase;
}

*::first-letter{
    text-transform: uppercase;
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

.titulo{
    text-transform: lowercase;
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