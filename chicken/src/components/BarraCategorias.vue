<template>

    <div style="position: sticky; top: 3.5rem; z-index: 999; background-color: white;overflow-x: auto;" class="col-12 nav_bar shadow-3 d-flex  lg:justify-content-center align-items-center mb-5 p-0 md:p-0">
       
       
        <!-- <Button class="px-0" style="position: absolute;border: none;background-color: white;color: black; left: -0.5rem;z-index: 99;height: 100%;width: 1.7rem; border-radius: 0;" severity="help"  icon="pi pi-angle-left text-2xl"></Button>


        <Button class="px-0" style="position: absolute;border: none;background-color: white;color: black; right: -0.5rem;z-index: 99;height: 100%; width: 1.7rem; border-radius: none;" severity="help"  icon="pi pi-angle-right text-2xl"></Button> -->

        <div class=" d-flex p lg:justify-content-center align-items-center  p-0 m-0"
        style="gap: 0; background-color: rgba(255, 255, 255, 0.913)">

        <div v-for="section in categories" :key="section.id" class="p-0">
            <Button text severity="secondary" size="small" @click="navigateToCategory(section.category_name,section.category_id)" :label="section.category_name "
                :class="checkSelected(section.category_id) ? 'selected menu-button' : 'menu-button'"
                class="p-2 mx-2  text-lg titulo" style=" text-transform: capitalize;width:max-content; color:var(--text-color); border-radius: 0;outline: none;box-shadow: none;">
               
            </Button>
        </div>
    </div>
    </div>
    

</template>





<script setup>
import { ref, onMounted } from 'vue';
import router from '@/router/index.js';
import { useRoute } from 'vue-router';
import { categoriesService } from '../service/restaurant/categoriesService'



const categories = ref([]);


const navigateToCategory = (categoryName,category_id) => {
    router.push({ name: 'sesion', params: { menu_name: categoryName, category_id:category_id } });
};


onMounted(async () => {
    categories.value = await categoriesService.getCategories()});


const checkSelected = (section) => {
    const route = useRoute(); // Asegúrate de que tienes acceso a useRoute aquí
    return route.params.category_id == section; // Verifica si el path actual contiene la cadena section
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

* {
    text-transform: lowercase;
}

*::first-letter {
    text-transform: uppercase;
}

.menu-button {
    background-color: transparent;
    padding: 1rem;
    margin: 0 1rem;
    border: none;
    font-size: 20px;
    outline: none;
    box-shadow: none;

}

.menu-button:hover {

    cursor: pointer;


}

*:focus {
    outline: none;
}


.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s;
}

.titulo {
    text-transform: lowercase;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}


.selected {
    /* box-shadow: 0 0.4rem var(--primary-color) !important;
     */
     border-bottom: 3px none red !important;
     margin-bottom: 0%;
     margin-top: 0;
     padding: 0;
     /* font-weight: bold; */
     
     /* padding-bottom: 3px; */

}



.selected::after {
      content: '';
      position: absolute;
      left: 0;
      bottom: 0;
      width: 100%;
      font-weight: bold;
      height: 0;
      border-bottom: .3rem solid var(--primary-color); /* Borde inferior */
    }



.col-12 {
    width: 100vw;
    /* position: absolute; */
    left: 0;
    padding: 1.5rem;
}


.navbar {
  overflow-x: auto; /* Permite desplazamiento horizontal */
  white-space: nowrap; /* Evita el salto de línea en el texto */
}

.navbar-item {
  min-width: 100px; /* Ajusta el ancho mínimo de los elementos del navbar según sea necesario */
}
</style>