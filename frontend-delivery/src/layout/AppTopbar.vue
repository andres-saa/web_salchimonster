<script setup>
import { ref, computed,onUnmounted, onMounted, onBeforeUnmount, watch } from 'vue';
import { useLayout } from '@/layout/composables/layout';
import { useRouter } from 'vue-router';
import { URI } from '../service/conection';
import { PrimeIcons } from 'primevue/api';

import { ableMenu } from '../service/menuOptions';
import router from '@/router/index.js'
import { buscarSedePorId } from '../service/sedes'
// import {curentSite} from '../service/un_pedido'
import { useSitesStore } from '../store/site';
const siteStore = useSitesStore()
const ruta = ref(router.currentRoute)

const { layoutConfig, onMenuToggle } = useLayout();
const screenWidth = ref(window.innerWidth);
const outsideClickListener = ref(null);
const topbarMenuActive = ref(false);
// const router = useRouter();
const onArea = ref(false)
const onMenu = ref(false)
const selectedMenu = ref({})
const products = ref([])

const categories = ref([{}])











const estado = ref(''); 
 


    const obtenerEstado = async () => {


    const siteId = siteStore.site.site_id
    // alert(siteId)
    
    if(!siteId){
        return
    }
    
      try {
        const response = await fetch(`${URI}/site/${siteId}/status`);
        const data = await response.json();
        
        if (data.status === 'closed') {
          estado.value = 'cerrado';
          localStorage.setItem('estado', 'cerrado');
        } else {
          estado.value = 'abierto';
          localStorage.setItem('estado', 'abierto');
        }
      } catch (error) {
        console.error('Error al obtener el estado:', error);
        estado.value = 'cerrado';
          localStorage.setItem('estado', 'cerrado');
      }
    };




    const intervalId = setInterval(obtenerEstado, 3000);

    onMounted(obtenerEstado);

    // Limpiar el intervalo cuando el componente se desmonta para evitar fugas de memoria
    onUnmounted(() => clearInterval(intervalId));



const isSmallScreen = computed(() => screenWidth.value < 992);

const updateScreenWidth = () => {
    screenWidth.value = window.innerWidth;
};

onMounted(() => {
    window.addEventListener('resize', updateScreenWidth);
});

onBeforeUnmount(() => {
    window.removeEventListener('resize', updateScreenWidth);
});



onMounted(async () => {

    bindOutsideClickListener();
    // getProducts().then( data => products.value = data)
    // getCategory().then(cat => categories.value=cat)
    // getMenu().then(products => menuOptions.value[0].menus = products)



});



const currentCity = ref(JSON.parse(localStorage.getItem('currentNeigborhood')));


window.addEventListener('storage', (e) => {
    if (e.key === 'currentNeigborhood') {
        // Actualizar la referencia reactiva cuando el valor en localStorage cambie
        currentCity.value = localStorage.getItem('currentNeigborhood');
    }
});

// // También puedes usar watch para realizar un seguimiento del cambio de currentCity
// watch(currentCity, () => {
//     // Realizar acciones adicionales cuando currentCity cambie
//     currentCity.value = localStorage.getItem('currentNeigborhood');
// });






onBeforeUnmount(() => {
    unbindOutsideClickListener();

});


const dropDownMenuVisible = ref(false)

const handleDropDownMenu = (value) => {
    dropDownMenuVisible.value = value
    value == false ? curentMenu.value = {} : ''
    ableMenu.value = true

}

const showMenu = (menu) => {
    curentMenu.value = menu
    dropDownMenuVisible.value = true

}

const currentgroupMenu = ref({
    category: {
        name: ''
    }
})
const changeCurrentGroupMenu = (grupoMenu) => {

    currentgroupMenu.value = grupoMenu


}
const menus = [
    { name: 'Atender', to: '/' },
    { name: ' Pedido manual', to: '/pedido-manual' },
    { name: 'Historial de pedidos', to: '/historial' },
    { name: ' Cuadre de caja', to: '/cuadre' },
    { name: ' Menu', to: '/tienda-menu/productos/SALCHIPAPAS/3' },
    { name: ' Horarios', to: '/horarios' },
    { name: ' Reportes', to: '/reporte-ventas/valor-ventas' }

]


const menusAdmin = [
    { name: 'RESUMEN SEDES', to: 'resumen-sedes' },
    { name: 'GESTIONAR PRODUCTOS', to: '/historial' },

]
// const menus = ref(
//     [
//         'Productos',
//         'Sedes',
//         'hola'
//     ])
const curentMenu = ref({})

// Ejemplo de cómo podrías utilizar getTokens

// const logoUrl = computed(() => {
//     // return `layout/images/${layoutConfig.darkTheme.value ? 'logo-white' : 'logo-dark'}.svg`;
//     return 'src/images/logo.png'
// });

const onTopBarMenuButton = () => {
    topbarMenuActive.value = !topbarMenuActive.value;
};

const onSettingsClick = () => {
    topbarMenuActive.value = false;
    router.push('/');
};
const topbarMenuClasses = computed(() => {
    return {
        'layout-topbar-menu-mobile-active': topbarMenuActive.value
    };
});

const bindOutsideClickListener = () => {
    if (!outsideClickListener.value) {
        outsideClickListener.value = (event) => {
            if (isOutsideClicked(event)) {
                topbarMenuActive.value = false;
            }
        };
        document.addEventListener('click', outsideClickListener.value);
    }
};
const unbindOutsideClickListener = () => {
    if (outsideClickListener.value) {
        document.removeEventListener('click', outsideClickListener);
        outsideClickListener.value = null;
    }
};
const isOutsideClicked = (event) => {
    if (!topbarMenuActive.value) return;

    const sidebarEl = document.querySelector('.layout-topbar-menu');
    const topbarEl = document.querySelector('.layout-topbar-menu-button');

    return !(sidebarEl.isSameNode(event.target) || sidebarEl.contains(event.target) || topbarEl.isSameNode(event.target) || topbarEl.contains(event.target));
};

const areaHandler = (value) => {
    areaHandler.value = value
}


const imagenNoCargada = (event) => {
    event.target.src = 'https://novatocode.online/assets/logo-f2daca0e.png'
}

const fondoVisible = ref(false)

const cerrar_sesion = () => {
    localStorage.removeItem('accessToken')
    router.push('/login')
}

</script>

<template>


    <div class="layout-topbar shadow-2 lg:pl-8 lg:pr-8 md:pr-8 " style=" background-color: rgb(255, 255, 255); ">


        <router-link to="/" class="layout-topbar-logo" style="z-index: 99999;">
            <img :src="'/images/logo.png'" alt="logo" />
        </router-link>

        


        <button class="p-link boton-menu layout-topbar-logo"
            style=" font-size: 24px; font-weight: bold;  color: black; z-index: 99999;display:flex; justify-content: center; align-items: center;">

            <i sty :class="PrimeIcons.MAP_MARKER" style="font-size: 100%; color: var(--primary-color)"> </i>


            <div style="display: flex;flex-direction: column; align-items: start; justify-content: center;">

                <span style="
                margin-left: 0.5rem; 
                text-transform:uppercase; 
                font-size: 1rem;
                color: var(--primary-color);">


                    {{ siteStore.site.site_name }}

                    
                </span>
                

                <span style="
            margin-left: 0.5rem; 
            text-transform:capitalize; 
            font-size: 1rem;
            font-weight: normal;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 200px;">
                    <span v-if="!isSmallScreen" class="sm:d-none"></span> <span v-else class="sm:d-none">
                        </span>  {{  }}                      <span class="px-2 py-0 text-sm" :class="estado == 'abierto'? 'abierto': 'cerrado'"  style="" >{{estado}}</span>

                </span>

            </div>


        </button>

        <button v-if="isSmallScreen" style="border: none" class="p-link layout-menu-button layout-topbar-button"
            @click="onMenuToggle()">
            <i style="border: ; color: var(--primary-color);" class="text-4xl pi pi-bars"></i>
        </button>


        <div v-else class="" style="left: 0; position: ; display: flex;gap: 1rem; width: 100%;justify-content: center;"> 
            
            <div v-for=" menu in menus" class="p-0 " style="width: max-content;">

                <RouterLink cla :to="menu.to" class="link-menu " style="text-decoration: none;color: black;">

                    <p class="col-12 text-md text-center p-1 p-" :class="ruta.fullPath == menu.to ? 'selected' : 'menu'"
                        style="font-weight: ;background-color: rgb(255, 255, 255);"> {{ menu.name }}</p>


                </RouterLink>

            </div>
            
        </div>
        <button @click="cerrar_sesion" class=" layout-menu-button" style="background-color: white;border-radius: 10rem; color:var(--primary-color); font-weight: bold; border: none;z-index: 999; cursor: pointer;" > Salir </button>



       




    </div>
    
</template>

<style lang="scss" scoped>
.dropDownMenu {
    // background-color: rgba(255, 255, 255, 1);
    width: 100%;
    height: min-content;
    // height: auto;
    position: absolute;
    top: 4rem;
    left: 0;
    border: 20px 20px;
    // border: 2px solid red;
    // padding: 1% 1%;
    // height: 50vh;
    // padding-bottom:200px ;
    // padding: 0 10%;
    z-index: 999;
    padding-bottom: 5%;
    // box-shadow: 1px 4px 2px rgba(0, 0, 0, 1);

    // background-color: red;


}

.gost {
    width: 10%;
    height: 100px;
    background-color: teal;
    position: absolute;
    top: 0;
    left: 10%;
    z-index: -1;
}

.menu {
    color: #000;
    // background-color: none;
    border: none;
    text-decoration: none;
    list-style: none;
    text-align: center;
    // width: 100%;
    margin: 0;
    // padding: 50px;
    // width: auto;

}

@keyframes parpadeo {
  0% { opacity: 1; background-color: greenyellow; }
  50% { opacity: 1;background-color: rgb(255, 245, 47); }
  100% { opacity: 1; }
}

@keyframes parpadeo2 {
  0% { opacity: 1; background-color: rgb(136, 0, 0); }
  50% { opacity: 1;background-color: rgb(255, 5, 5);; }
  100% { opacity: 1; }
}

.abierto {
  animation: parpadeo 1s infinite; /* 1s es la duración de la animación */
   border-radius: 1rem; color: rgb(0, 0, 0); font-weight: 500; 
  
}


.cerrado {
  animation: parpadeo2 1s infinite; /* 1s es la duración de la animación */
 border-radius: 1rem; color: rgb(255, 255, 255); font-weight: 500; 
}

.menus {

    display: flex;
    width: 40%;
    gap: 10px;
    height: 100%;
    // margin: auto;
    align-items: flex-end;

    // justify-content: center;

}

.boton-menu {
    // margin: 0;
    border: none;
    background-color: transparent;
    font-size: 20px;
    padding: 0 5px;
    font-weight: bold;
}

.ver-mas {
    transition: all 0.2s ease;
    border: 1px solid var(--primary-color);
    // font-weight: bold;
    font-size: 15px;
    // margin-bottom: 200px;
    background-color: transparent;
    border-radius: 5px;
}

.ver-mas:hover {
    background-color: var(--primary-color);
    transform: scale(1.1);
    animation: rot 1s ease infinite;


    color: #fff;
    cursor: pointer;
}



// .icono{
//     color: var(--primary-color);
// }
.ver-mas:hover>.icono {
    // background-color: var(--primary-color);

    // display: none;
    color: #fff;
    transform: translateX(5px);
}

.icono {
    transition: all 0.2s ease;
    color: var(--primary-color);
    transform: translateX(-15px);
    font-weight: bold;
}

.img-product {
    // transform: scale(1.1);
    transition: all 0.2s ease;
    width: 10vh;
    height: 10vh;
    object-fit: contain;
    margin: 0.5rem;
    border-radius: 10px;

}

.name-product {
    transition: all 0.2s ease;
}

.img-product-sede {
    // transform: scale(1.1);
    transition: all 0.1s ease;
    width: 100%;
    height: 10vh;
    object-fit: contain;
    margin: 0.5rem;
    border-radius: 10px;

}

.img-product-cont:hover>.img-product {

    transform: scale(1.1);
    filter: brightness(1.2);


}

.img-product-cont:hover>.name-product {

    transform: translateX(10px);
    color: var(--primary-color);
    font-weight: bold;



}

.img-product-cont:hover {
    cursor: pointer;
}

.selected {
    // border: 1px solid red;
    box-shadow: 0px 3px 0px var(--primary-color);
    border-radius: 0;
}
</style>

