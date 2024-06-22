<script setup>
import { ref, computed, onMounted, onBeforeUnmount, watch,onUnmounted } from 'vue';
import { useLayout } from '@/layout/composables/layout';

import { PrimeIcons } from 'primevue/api';
import { quantity } from '@/service/cart'
import { menuOptions } from '@/service/menuOptions';
import { ableMenu } from '../service/menuOptions';
import { URI } from "@/service/conection";
import { showSiteDialog, setShowDialog } from '../service/state';
import { productDialog, setProductDialog } from '../service/state';
import router from '../router';
import { useRoute } from 'vue-router';
import { domicilio } from '../service/cart';
import { useSitesStore } from '../store/site';
import { usecartStore } from '../store/shoping_cart';
  import {loginStore} from '@/store/userCall.js'

  const store = loginStore()
const car = usecartStore()

const siteStore = useSitesStore()
const status = ref(''); 


const obtenerstatus = async () => {


const siteId = siteStore.location.site.site_id  
// alert(siteId)

if(!siteId){
    return
}

  try {
    const response = await fetch(`${URI}/site/${siteId}/status`);
    const data = await response.json();
    
    if (data.status === 'closed') {
      siteStore.status = 'cerrado';
    } else {
      siteStore.status = 'abierto';
   
    }
  } catch (error) {
    console.error('Error al obtener el status:', error);
    siteStore.status = 'cerrado';
     
  }
};

    const intervalId = setInterval(obtenerstatus, 60000);

    // Llamar a obtenerstatus cuando el componente se monta
    onMounted(obtenerstatus);

    // Limpiar el intervalo cuando el componente se desmonta para evitar fugas de memoria
    onUnmounted(() => clearInterval(intervalId));















const { layoutConfig, onMenuToggle } = useLayout();

const outsideClickListener = ref(null);
const topbarMenuActive = ref(false);

const onArea = ref(false)
const onMenu = ref(false)
const selectedMenu = ref({})
const products = ref([])

const categories = ref([{}])
const screenWidth = ref(window.innerWidth);
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

const ruta = ref(router)

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

// También puedes usar watch para realizar un seguimiento del cambio de currentCity
watch(currentCity, () => {
    // Realizar acciones adicionales cuando currentCity cambie
    currentCity.value = localStorage.getItem('currentNeigborhood');
});



// Verificar si la ruta actual o alguna de sus rutas secundarias es /admin-products
const route = useRoute();

// Verificar si la ruta actual o alguna de sus rutas secundarias es /admin-products
const isInAdminProductsRoute =
    route.matched.some(record => record.path === '/admin-products') ||
    route.matched.some(record => record.path.startsWith('/admin-products/'));


const isEntregasRoute =
    route.matched.some(record => record.path === '/entregas') ||
    route.matched.some(record => record.path.startsWith('/entregas/'));




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
    event.target.src = '/images/logo.png'
}

const fondoVisible = ref(false)



</script>

<template>
    <div v-if="!isInAdminProductsRoute && !isEntregasRoute" st class="layout-topbar shadow-3 px-3 md:pl-4 md:pr-4 lg:pl-8 lg:pr-8 "
        style=" z-index:999;background-color: white; ">


        <router-link to="/" class="layout-topbar-logo" style="z-index: 99999;">
            <img :src="'/images/logo.png'" alt="logo" />


        </router-link>


        <button @click="(siteStore.setVisible('currentSite',true))" class="p-link boton-menu layout-topbar-logo"
            style=" font-size: 24px; font-weight: bold;  color: black; z-index: 99999;display:flex; justify-content: center; align-items: center;">

            <i sty :class="PrimeIcons.MAP_MARKER" style="font-size: 100%; color: var(--primary-color)"> </i>


            <div style="display: flex;flex-direction: column; align-items: start; justify-content: center;">

                <span style="
                margin-left: 0.5rem; 
               
                font-size: 1rem;
                color: var(--primary-color);">


                    {{ siteStore.location.city?.city_name || 'Definir ubicacion' }}  <span ST class="px-3 py-0 text-sm " :class="siteStore.status == 'abierto'? 'abierto': 'cerrado'"  style="text-transform: uppercase;" > {{siteStore.status}}</span>
                     <!-- <Tag>{{store.rawUserData.name}}</Tag> -->
                </span>
                

                <span style="
            margin-left: 0.5rem; 
            /* text-transform:uppercase;  */
            font-size: 1rem;
            font-weight: normal;
            white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 200px;">
                      <span style="" >sede </span>  <span class="site-name">{{ siteStore.location.site.site_name?.toLowerCase() || 'Definir ubicacion' }}   </span>
                </span>

            </div>


        </button>

        <button v-if="isSmallScreen" style="border: none" class="p-link layout-menu-button layout-topbar-button"
            @click="onMenuToggle()">
            <i style="border: ; color: var(--primary-color);" class="text-4xl pi pi-bars"></i>
        </button>









        <div class="layout-topbar-menu " :class="topbarMenuClasses" v-if="!isInAdminProductsRoute">
           

            <!--  -->

            <div class=" botones-menu" :class="topbarMenuClasses" v-for=" menuTopbar in menuOptions"
                style="display: flex; ">


                <router-link :to="`/${menuTopbar.to}`" @click="handleDropDownMenu(false)" class="col-12">
                    <button class="p-link boton-menu text-xl" style=""
                        :class="curentMenu.name == menuTopbar.name || router.currentRoute.value.path == `/${menuTopbar.to}` ? 'selected' : 'boton-menu'">
                        <!-- <i class="pi pi-calendar"></i> -->
                        <!-- <h3> {{i}}</h3> -->
                        {{ menuTopbar.name }}
                    </button>

                </router-link>
            </div>


        </div>

        <div class="layout-topbar-menu" :class="topbarMenuClasses" style="z-index: 999 ;">

            <button @click="onTopBarMenuButton()" class="p-link layout-topbar-button">
                <i class="pi pi-user"></i>
                <span>Profile</span>
            </button>
            <button @click="onSettingsClick()" class="p-link layout-topbar-button">
                <i class="pi pi-cog"></i>
                <span>Settings</span>
            </button>

            <router-link to="/cart">
                <button class="p-link layout-topbar-button p-0" style="position: relative;">
                    <i badge="5+" :class="PrimeIcons.SHOPPING_CART"></i>
                    <div class="p-0"
                        style="display: flex;align-items: center;justify-content: center; position: absolute;bottom: 50%;right:0; background-color:var(--primary-color); width: 1.5rem;height: 1.5rem;border-radius: 50%">
                        <div class="text-xl" style="color: white;font-size">
                            {{ car.cart.products.length }}
                        </div>

                    </div>


                    <span>Calendar</span>
                </button>
            </router-link>



        </div>


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
    // font-size: 20px; 
    padding: 0 5px;
    // font-weight: bold;
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

*:focus {
    border: none;
    outline: none;
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

.site-name{
    text-transform: capitalize;
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
    box-shadow: 0px 5px 0px var(--primary-color);
    border-radius: 0;
}

*{ text-transform: lowercase;}

*::first-letter{
    text-transform: uppercase;
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

</style>

