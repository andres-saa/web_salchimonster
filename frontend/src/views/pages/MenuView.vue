<template >


<div class="px-0 mx-0 mt-5" style="min-height: 100vh;">

    


  <CarouselBanner v-if="route.path == '/'" />
  <!-- <img src="/images/banners/banner-1.jpeg" class="pb-6" alt="" style="width: 100%; "> -->
  <!-- <Button  style="position: sticky;top:rem;z-index: 1000; left:-0.5rem;" severity="help" text icon="pi pi-angle-left text-4xl"></Button> -->

  <BarraCategorias/>

 
        <RouterView />
        
</div>

    









   
</template>

<script setup>
// import TarjetaCombo from '../../components/TarjetaCombo.vue';
import TarjetaMenu from '../../components/TarjetaMenu.vue'
import { menuOptions } from '../../service/menuOptions';
import {  onMounted, onBeforeUnmount, computed,watch } from 'vue';
import { PrimeIcons } from 'primevue/api';
import { curentProduct, changeProduct } from '../../service/productServices';
import { menuGlobal } from '../../service/menu/menu';
import { ableMenu } from '../../service/menuOptions';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import CarouselBanner from '../../components/CarouselBanner.vue'
import sesion from './sesion.vue';
import BarraCategorias from '../../components/BarraCategorias.vue';
import Loading from '../../components/Loading.vue';
import { useRoute } from 'vue-router';
import { URI } from '../../service/conection';

import { usecartStore } from '@/store/shoping_cart';
import { useReportesStore } from '@/store/ventas';
const store2 = usecartStore()
const store = useReportesStore()

const route = useRoute()

const siteStore = useSitesStore()


if(!siteStore.location.site.site_id){
    // alert(route.fullPath)
    siteStore.setVisible("currentSite", true)
  }

import {ref} from 'vue'
import { comprobar_sede } from '../../service/state';
import router from '@/router/index.js'
import { useSitesStore } from '../../store/site';
const ruta = ref(router.currentRoute)
const hola = ref( localStorage.getItem('currentNeigborhood') )

const screenWidth = ref(window.innerWidth);

const isSmallScreen = computed(() => screenWidth.value < 800);

const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(async() => {
  window.addEventListener('resize', updateScreenWidth);
  comprobar_sede()
//   await getProducts()
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreenWidth);
  
});


const currentSection = ref(menuOptions.value[0].menus[0])
const currentMenu = ref({})
const changesection = (section) => {
    currentSection.value = section
    console.log(section)
}


const setSection = () => {
    currentSection.value = { category: menuOptions.value[0].menus[1].category, products: menuOptions.value[0].menus[1].products }

    console.log('cambio')
}

watch(menuOptions, setSection);


const getProducts = async (category_name) => {
  
    const site_id = siteStore.location.site?.pe_site_id
    const category_id = route.params.category_id
    if(true){

        if(store2.menu?.data?.length < 1 || !store2.menu?.data ){
          store.setLoading(true, 'cargando productos')
        }
        try {
        let response = await fetch(`${URI}/get-product-integration/6149/${site_id}`);
    
        if (!response.ok) {
            store.setLoading(false, 'cargando productos')

            throw new Error(`HTTP error! status: ${response.status}`);

        }
        store.setLoading(false, 'cargando productos')

        let data = await response.json();
        store2.menu = data.data;

        const final_data = data.data.data.map(product => {
          const foundProduct = lista.find(p => p.id === product.productogeneral_id);
          return {
              ...product,
              last_price: foundProduct ? foundProduct.last_price : null // Verifica si se encontró el producto
          };
      });

      store2.menu.data = final_data;

      console.log(final_data,"hola");



    } catch (error) {
        store.setLoading(false, 'cargando productos')

        console.error('Error fetching data: ', error);
    }
    }
}
  





const lista = [
    {
        "id": "59",
        "name": "1/4 CHICKEN MONSTER",
        "last_price": null
    },
    {
        "id": "147",
        "name": "2X1 BURGER MONSTER + 2 PAPAS",
        "last_price": 61800
    },
    {
        "id": "96",
        "name": "2X1 BURGERMONSTER + PAPAS",
        "last_price": null
    },
    {
        "id": "219",
        "name": "2X1 GRANIZADO CITRICOS",
        "last_price": null
    },
    {
        "id": "146",
        "name": "2X1 MONSTER BACON + 2 PAPAS",
        "last_price": null
    },
    {
        "id": "145",
        "name": "2X1 MONSTER CHEESE + 2 PAPAS",
        "last_price": null
    },
    {
        "id": "143",
        "name": "2X1 MONSTER CHICKEN + 2 PAPAS",
        "last_price": null
    },
    {
        "id": "148",
        "name": "2X1 MONSTER DOBLE CARNE + 2 PAPAS",
        "last_price": null
    },
    {
        "id": "144",
        "name": "2X1 MONSTER GHETTO + 2 PAPAS",
        "last_price": null
    },
    {
        "id": "150",
        "name": "2X1 MONSTER REALEZA + 2 PAPAS",
        "last_price": null
    },
    {
        "id": "142",
        "name": "2X1 MONSTER SENCILLA + 2 PAPAS",
        "last_price": null
    },
    {
        "id": "149",
        "name": "2X1 OIGA, MIRE, VEA + 2 PAPAS",
        "last_price": null
    },
    {
        "id": "61",
        "name": "ADICION BACON PREMIUM",
        "last_price": null
    },
    {
        "id": "78",
        "name": "ADICION CARNE DE RES",
        "last_price": null
    },
    {
        "id": "62",
        "name": "ADICION CARNE PREMIUM (DESMECHADA)",
        "last_price": null
    },
    {
        "id": "63",
        "name": "ADICION CHICHARRON",
        "last_price": null
    },
    {
        "id": "64",
        "name": "ADICION CHORIZO",
        "last_price": null
    },
    {
        "id": "65",
        "name": "ADICION COSTILLA AHUMADA",
        "last_price": null
    },
    {
        "id": "66",
        "name": "ADICION GUACAMOLE",
        "last_price": null
    },
    {
        "id": "67",
        "name": "ADICION MADURO GUAYABO",
        "last_price": null
    },
    {
        "id": "68",
        "name": "ADICION MAIZ",
        "last_price": null
    },
    {
        "id": "69",
        "name": "ADICION PAPA AMARILLA",
        "last_price": null
    },
    {
        "id": "70",
        "name": "ADICION PAPA FRANCESA",
        "last_price": null
    },
    {
        "id": "71",
        "name": "ADICION PICO E GALLO",
        "last_price": null
    },
    {
        "id": "72",
        "name": "ADICION POLLO APANADO",
        "last_price": null
    },
    {
        "id": "73",
        "name": "ADICION POLLO DESMECHADO",
        "last_price": null
    },
    {
        "id": "74",
        "name": "ADICION QUESO MOZARELLA",
        "last_price": null
    },
    {
        "id": "79",
        "name": "ADICION QUESO MOZARELLA 2 LONCHAS",
        "last_price": null
    },
    {
        "id": "75",
        "name": "ADICION RIPIO",
        "last_price": null
    },
    {
        "id": "76",
        "name": "ADICION SALCHICHA PREMIUM",
        "last_price": null
    },
    {
        "id": "77",
        "name": "ADICION SALCHICHA RANCHERA",
        "last_price": null
    },
    {
        "id": "9",
        "name": "AGUA BRISA 600 ML",
        "last_price": null
    },
    {
        "id": "27",
        "name": "BACONMONSTER 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "41",
        "name": "BACONMONSTER PERSONAL",
        "last_price": null
    },
    {
        "id": "80",
        "name": "BAÑO DE QUESO BURGER 6 LONCHAS",
        "last_price": null
    },
    {
        "id": "107",
        "name": "BURGER MONSTER",
        "last_price": null
    },
    {
        "id": "26",
        "name": "BURGERMONSTER",
        "last_price": null
    },
    {
        "id": "23",
        "name": "CERVEZA BUDWEISER LATA",
        "last_price": null
    },
    {
        "id": "24",
        "name": "CERVEZA CORONA BOT. 355ML",
        "last_price": null
    },
    {
        "id": "33",
        "name": "CHICHAMONSTER",
        "last_price": null
    },
    {
        "id": "28",
        "name": "CLASICMONSTER 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "42",
        "name": "CLASICMONSTER PERSONAL",
        "last_price": null
    },
    {
        "id": "10",
        "name": "COCA COLA SABOR ORIGINAL 1.5 LT",
        "last_price": null
    },
    {
        "id": "11",
        "name": "COCA COLA SABOR ORIGINAL 400 ML",
        "last_price": null
    },
    {
        "id": "12",
        "name": "COCA COLA ZERO 400 ML",
        "last_price": null
    },
    {
        "id": "157",
        "name": "COCACOLA ZERO 1.5L",
        "last_price": null
    },
    {
        "id": "152",
        "name": "COMBO BACONMONSTER 2P + 2 BEBIDAS",
        "last_price": 53700
    },
    {
        "id": "98",
        "name": "COMBO BACONMONSTER PERSONAL + BEBIDA",
        "last_price": 35400
    },
    {
        "id": "132",
        "name": "COMBO BURGER MONSTER  +PAPAS+BEBIDA",
        "last_price": 36800
    },
    {
        "id": "101",
        "name": "COMBO BURGERMONSTER + PAPAS + BEBIDA",
        "last_price": 36800
    },
    {
        "id": "153",
        "name": "COMBO CLASICMONSTER 2P +  2 BEBIDAS",
        "last_price": 42700
    },
    {
        "id": "100",
        "name": "COMBO CLASICMONSTER PERSONAL + BEBIDA",
        "last_price": 28800
    },
    {
        "id": "154",
        "name": "COMBO COSTIMONSTER 2P  +  2 BEBIDAS",
        "last_price": 64300
    },
    {
        "id": "99",
        "name": "COMBO COSTIMONSTER PERSONAL + BEBIDA",
        "last_price": 41800
    },
    {
        "id": "155",
        "name": "COMBO LA DE SIEMPRE 2P + 2 BEBIDAS",
        "last_price": 72700
    },
    {
        "id": "92",
        "name": "COMBO LA MATAHAMBRE 2P + 2 BEBIDAS",
        "last_price": 67100
    },
    {
        "id": "53",
        "name": "COMBO LA MIXTICA 2P + 2 BEBIDAS",
        "last_price": 81700
    },
    {
        "id": "131",
        "name": "COMBO MONSTER BACON +PAPAS+BEBIDA",
        "last_price": null
    },
    {
        "id": "130",
        "name": "COMBO MONSTER CHEESE +PAPAS+BEBIDA",
        "last_price": null
    },
    {
        "id": "126",
        "name": "COMBO MONSTER CHICKEN +PAPAS+BEBIDA",
        "last_price": null
    },
    {
        "id": "133",
        "name": "COMBO MONSTER DOBLE CARNE  +PAPAS+BEBIDA",
        "last_price": null
    },
    {
        "id": "129",
        "name": "COMBO MONSTER GHETTO +PAPAS+BEBIDA",
        "last_price": null
    },
    {
        "id": "135",
        "name": "COMBO MONSTER REALEZA +PAPAS+BEBIDA",
        "last_price": null
    },
    {
        "id": "125",
        "name": "COMBO MONSTER SENCILLA+PAPAS+BEBIDA",
        "last_price": null
    },
    {
        "id": "91",
        "name": "COMBO NACHIMONSTER 2P + 2 BEBIDAS",
        "last_price": 67100
    },
    {
        "id": "220",
        "name": "COMBO NAVIDEÑO",
        "last_price": null
    },
    {
        "id": "134",
        "name": "COMBO OIGA, MIRE, VEA +PAPAS+BEBIDA",
        "last_price": null
    },
    {
        "id": "29",
        "name": "COSTIMONSTER 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "43",
        "name": "COSTIMONSTER PERSONAL",
        "last_price": null
    },
    {
        "id": "141",
        "name": "DETODITO",
        "last_price": null
    },
    {
        "id": "14",
        "name": "JUGO DE LULO",
        "last_price": null
    },
    {
        "id": "16",
        "name": "JUGO DE MANGO",
        "last_price": null
    },
    {
        "id": "17",
        "name": "JUGO DE MARACUYA",
        "last_price": null
    },
    {
        "id": "222",
        "name": "JUGO FRESH CITRUS 188 ML",
        "last_price": null
    },
    {
        "id": "221",
        "name": "JUGO FRUTAL MANGO 188 ML",
        "last_price": null
    },
    {
        "id": "224",
        "name": "JUGO FRUTAL MORA 188 ML",
        "last_price": null
    },
    {
        "id": "223",
        "name": "JUGO FRUTAL SALPICON 188 ML",
        "last_price": null
    },
    {
        "id": "138",
        "name": "KIT #1 CUMPLEAÑOS",
        "last_price": null
    },
    {
        "id": "34",
        "name": "LA DE SIEMPRE 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "44",
        "name": "LA DE SIEMPRE PERSONAL",
        "last_price": null
    },
    {
        "id": "35",
        "name": "LA MIXTICA 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "45",
        "name": "LA MIXTICA PERSONAL",
        "last_price": null
    },
    {
        "id": "36",
        "name": "LA NEA 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "30",
        "name": "MADURIMONSTER 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "46",
        "name": "MADURIMONSTER PERSONAL",
        "last_price": null
    },
    {
        "id": "37",
        "name": "MATA HAMBRE 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "47",
        "name": "MATA HAMBRE PERSONAL",
        "last_price": null
    },
    {
        "id": "106",
        "name": "MONSTER BACON",
        "last_price": null
    },
    {
        "id": "105",
        "name": "MONSTER CHEESE",
        "last_price": null
    },
    {
        "id": "103",
        "name": "MONSTER CHICKEN",
        "last_price": null
    },
    {
        "id": "108",
        "name": "MONSTER DOBLE CARNE",
        "last_price": null
    },
    {
        "id": "104",
        "name": "MONSTER GHETTO",
        "last_price": null
    },
    {
        "id": "110",
        "name": "MONSTER REALEZA",
        "last_price": null
    },
    {
        "id": "102",
        "name": "MONSTER SENCILLA",
        "last_price": null
    },
    {
        "id": "31",
        "name": "NACHIMONSTER 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "48",
        "name": "NACHIMONSTER PERSONAL",
        "last_price": null
    },
    {
        "id": "109",
        "name": "OIGA, MIRE, VEA",
        "last_price": null
    },
    {
        "id": "137",
        "name": "PAPA CRIOLLA PARA BURGER (150G)",
        "last_price": null
    },
    {
        "id": "136",
        "name": "PAPA FRANCESA PARA BURGER (150GR)",
        "last_price": null
    },
    {
        "id": "139",
        "name": "PAPAS BACON",
        "last_price": null
    },
    {
        "id": "113",
        "name": "PAPAS CARNE",
        "last_price": null
    },
    {
        "id": "120",
        "name": "PAPAS CARNE + GASEOSA 400 ML",
        "last_price": null
    },
    {
        "id": "116",
        "name": "PAPAS CERDO",
        "last_price": null
    },
    {
        "id": "123",
        "name": "PAPAS CERDO + GASEOSA 400 ML",
        "last_price": null
    },
    {
        "id": "115",
        "name": "PAPAS CHICHA",
        "last_price": null
    },
    {
        "id": "122",
        "name": "PAPAS CHICHA + GASEOSA 400 ML",
        "last_price": null
    },
    {
        "id": "112",
        "name": "PAPAS HAWAINA",
        "last_price": null
    },
    {
        "id": "119",
        "name": "PAPAS HAWAINA + GASEOSA 400 ML",
        "last_price": null
    },
    {
        "id": "114",
        "name": "PAPAS MIXTA",
        "last_price": null
    },
    {
        "id": "121",
        "name": "PAPAS MIXTAS + GASEOSA 400 ML",
        "last_price": null
    },
    {
        "id": "117",
        "name": "PAPAS MONSTER",
        "last_price": null
    },
    {
        "id": "124",
        "name": "PAPAS MONSTER + GASEOSA 400 ML",
        "last_price": null
    },
    {
        "id": "111",
        "name": "PAPAS SAMBA",
        "last_price": null
    },
    {
        "id": "118",
        "name": "PAPAS SAMBA + GASEOSA 400 ML",
        "last_price": null
    },
    {
        "id": "204",
        "name": "PECERA 14 PERSONAS",
        "last_price": null
    },
    {
        "id": "212",
        "name": "PECERA 14 PERSONAS UP",
        "last_price": null
    },
    {
        "id": "140",
        "name": "PICADA PA 3 PERSONAS",
        "last_price": null
    },
    {
        "id": "32",
        "name": "POLLIMONSTER 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "49",
        "name": "POLLIMONSTER PERSONAL",
        "last_price": null
    },
    {
        "id": "38",
        "name": "PORKYMONSTER 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "50",
        "name": "PORKYMONSTER PERSONAL",
        "last_price": null
    },
    {
        "id": "94",
        "name": "POSTRE CHOCOMONSTER",
        "last_price": null
    },
    {
        "id": "159",
        "name": "PREMIO 1.5 L",
        "last_price": null
    },
    {
        "id": "20",
        "name": "PREMIO 400 ML",
        "last_price": null
    },
    {
        "id": "158",
        "name": "QUATRO 1.5 L",
        "last_price": null
    },
    {
        "id": "21",
        "name": "QUATRO 400 ML",
        "last_price": null
    },
    {
        "id": "39",
        "name": "RANCHIMONSTER 2 PERSONAS",
        "last_price": null
    },
    {
        "id": "51",
        "name": "RANCHIMONSTER PERSONAL",
        "last_price": null
    },
    {
        "id": "40",
        "name": "SALCHIMONSTER PARA 6 PERSONAS",
        "last_price": null
    },
    {
        "id": "57",
        "name": "SHOW CHICHARRON",
        "last_price": null
    },
    {
        "id": "56",
        "name": "SHOW QUESO",
        "last_price": null
    },
    {
        "id": "156",
        "name": "SPRITE 1.5 L",
        "last_price": null
    },
    {
        "id": "22",
        "name": "SPRITE 400 ML",
        "last_price": null
    },
    {
        "id": "60",
        "name": "STRIPS MONSTER",
        "last_price": null
    }
]



onMounted(async () => {
    // changesection({category:localStorage.getItem('menu').category,products:localStorage.getItem('menu').products})
    // getMenu().then(products => currentSection.value = products[0])
    ableMenu.value = true
});

</script>
