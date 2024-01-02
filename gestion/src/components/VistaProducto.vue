<template>
     <Dialog  v-model:visible="showProductDialog" :style="{ width: '1024px',height:'max-content' }"
    header="Seleccion de sede" :modal="true" class="p-fluid pt-8 m-3"
    style="    box-shadow: 0px 0px 30px rgb(0, 0, 0);; background-color: white; ; border-radius: 30px;padding-top: 2rem;">


 

    <div class="header col-12 grid m-0 text-justify" style="border-radius: 30px 30px 0 0; background-color: rgb(255, 255, 255);z-index:99; position:absolute;top:1rem;left: 0;height: max-content;">
        <p class="nombre col-9 text-xl lg:text-2xl p-0 text-left" style="color:black;font-weight: bold"> {{ productDialog.name }}</p>
        <p class="precio col-3 text-xl lg:text-2xl p-0 text-right " style="color:black;font-weight: bold"> {{formatoPesosColombianos( productDialog.price + sumarPrecios(currentAditions) ) }}</p>
      </div>




    <button  @click="showProductDialog = ! showProductDialog" style=" width: 3rem;height: 3rem; border: none; position: absolute; right: -1rem; top: -1rem;background-color: var(--primary-color); border-radius: 50%; display: flex; align-items: center;justify-content: center; z-index: 99;">
      <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>

    </button>
   
 
    <div class="grid col-12 p-0  md:p-4"  >



   <!-- <div class="bajador col-12 p-0 grid m-0" style="background-color: rgb(255, 255, 255); color: transparent; z-index:9;height: max-content;">
      <p class="nombre col-9 text-justify text-xl lg:text-2xl p-0 text-left" style="color:rgba(0, 0, 0, 0);font-weight: bold"> {{ productDialog.name }}</p>
      <p class="precio col-3 text-xl lg:text-2xl p-0 text-right " style="color:rgba(0, 0, 0, 0)09, 28, 28);font-weight: bold"> {{formatoPesosColombianos( productDialog.price )}}</p>
    </div> -->
      

      <div class="col-12 md:col-6 p-4 mt-5" style="display: flex;align-items: center; max-height: 45rem; background-color:white;box-shadow: 0 0 20px rgba(0, 0, 0, 0.239); border-radius: 2rem;; overflow: hidden; " >

      <!-- <div class="before"
                style="top: 0; left: 0; width: 100%; height: 100%; overflow: hidden; position: ;  position: absolute;">
                <img :src="`${URI}/read_product_image/600/${productDialog.id}`" alt=""
                    style="width: 110%; height: 110%; opacity: 0.3; object-fit:  cover; filter: blur(5px);">
        </div> -->
        <img class="col-12 p-0"  :src="`${URI}/read_product_image/600/${productDialog.id}`" alt="" style="width: 100%;object-fit: cover;">

      </div>
      
      <div class=" scroll  col-12 md:col-6 m-0 pl-3 pr-0 mr-0" style=" padding-bottom: 5rem;">
        <p class="col-12 text-xl " style="font-weight: bold;color: black; ">
          DESCRIPCION  
        </p>
        <p class="col-12 text-l p-0 md:pl-3" style="color: black;">
          {{ productDialog.description }}
        </p>

        <div v-if="productDialog.category_id != 4 && productDialog.category_id != 3 ">
                  <p class="col-12 text-xl p-0 md:pl-3" style="font-weight: bold;color: black;display: flex;align-items: center;">
          <span class="col-4 p-0 m-0">SALSAS</span> <div class="col p-0 m-0" style="height: auto; height: 01rem;background-color: var(--primary-color)"> </div>
        </p> 

        <div v-for="salsa in adiciones.salsas" class="col-12 pt-0 pb-0 mb-2 p-0 md:pl-3" :class="checkedSalsas[salsa] || checkedSalsas['TODAS LAS SALSAS'] ? 'selected' : ''" style="justify-content: start; padding-bottom: 0.5rem; padding-left: 1rem; border-radius: 1rem;">

<div class="salsa col-12 p-0" style="color: black; margin: 0; padding: 0; display: flex; justify-content: space-between; align-items: center;">
    <p class="texto p-0 m-0" style="margin: 0; padding: 0; min-width: max-content">{{ salsa }}</p>

    <Checkbox v-if="!(checkedSalsas['SIN SALSAS'] && !checkedSalsas[salsa] || (checkedSalsas['TODAS LAS SALSAS'] && !checkedSalsas[salsa]))" @change="cargarSalsas(salsa)" v-model="checkedSalsas[salsa]" :binary="true" style="margin-right: 1rem;" />
</div>
</div>

        </div>

        <div v-if="productDialog.category_id != 3">


          <p class="col-12 text-xl pl-0 md:pl-3" style="font-weight: bold;color: black;display: flex;align-items: center;">
          <span class="col-4 p-0 m-0">{{productDialog.category_id ==4 ? ' TOPINGS' : 'ADICIONES'}}</span> <div class="col p-0 m-0" style="height: auto; height: 01rem;background-color: var(--primary-color)"> </div>
        </p>
       

       

          <div class="md:p-0 p-0" v-for="adicion in 
            productDialog.category_id == 1 ? adiciones.salchipapas.products : 
            productDialog.category_id == 2 ? adiciones.hamburguesas.products :
            productDialog.category_id == 3 ? adiciones.salchipapas.products : 
            productDialog.category_id == 4 ? adiciones.topings.products :
            productDialog.category_id == 5 ? adiciones.almuerzos.products :
            productDialog.category_id == 6 ? productDialog.adiciones.products :[]" 
          style=" ;  ; color:black;border-radius:2rem" :class="checkedAdiciones[adicion.name]? 'selected':''" >



          <div class=" col-12 grid p-0  md:pl-5 mb-4" style=" align-items: center; justify-content: space-between;  ">
              

            <div class="col-9 p-0  " style="display: flex;">
              <Checkbox @change="cargarAdiciones(adicion)"   class="p-0" v-model="checkedAdiciones[adicion.name]" :binary="true" style="margin-right: 1rem;  " />

                  <p   class="   p-0" style=";"> {{ adicion.name }}
                  </p>

                
            </div>
                  

              <p class=" text col-3 text-right p-0 " style="font-weight: bold; margin-left: ;">${{ adicion.price }}
              </p>

        </div>


        </div>


        <p v-if="productDialog.category_id ==5" class="col-12 text-xl" style="font-weight: bold;color: black;display: flex;align-items: center;">
          <span  class="col-4 p-0 m-0 mr-4 ">{{ `ELIGE ${productDialog.acomp_cantidad} ${productDialog.acomp_cantidad<2? 'ACOMPANANTE':'ACOMPANANTES'}`}}</span> <div class="col p-0 m-0" style="height: auto; height: 01rem;background-color: var(--primary-color)"> </div>
        </p>
       

       

          <div v-if="productDialog.category_id ==5" class="p-0" v-for="i in adiciones.acomp_almuerzos.products" 
          style=" ; padding-bottom: 0.5rem; ; color:black;border-radius:2rem" :class="checkedAdiciones[i.name]? 'selected':''" >



          <div class=" col-12 grid pl-5 pb-0 pt-0 mb-4" style=" align-items: center; justify-content: space-between; ">
              

            <div class="col-9 p-0 " style="display: flex;">
              <Checkbox @change="cargarAdiciones(i,productDialog.acomp_cantidad)"   class="p-0" v-model="checkedAdiciones[i.name]" :binary="true" style="margin-right: 1rem;  " />

                  <p   class="   p-0" style=";"> {{ i.name }}
                  </p>

                
            </div>
                  

              <p class=" text col-3 text-right p-0 " style="font-weight: bold; margin-left: ;">${{ i.price }}
              </p>

        </div>


        </div>





        </div>
        

      
       

      </div>
      <div   class="col-12 md:col-6 add-car" style="position: absolute;display: flex; align-items: end; justify-content: center; background-color: rgba(255, 255, 255, 0);  height: rem; bottom: 1.5rem;right: 0;">

        <button @click="addcar(productDialog)" style="background-color: var(--primary-color); color:white; border:none;padding: 0.5rem 3rem; font-weight: bold; border-radius: 2rem;">  <span class="text-xl"  >AGREGAR AL CARRITO</span></button>

      </div>
    </div>

    
    

    <!-- <button  @click="setProductDialog" style="width: 3rem;height: 2rem; border: none; position: absolute; right: 1rem; top:1rem;background-color: var(--primary-color); border-radius: 5px; display: flex; align-items: center;justify-content: center;">
      <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>
 
    </button> -->

    <!-- <div
      style="width: 40%;max-width: 20rem; position: absolute; display: flex;align-items: center; justify-content: end;padding-right: 1rem; height: 1.5rem; background-color: black; top: 0; border-radius:  15px 15px ; top:0.5rem">
      <div class="led" style="width: 0.7rem;height: 0.7rem;border-radius: 50%; display: ;"></div>
      
    </div> -->

    <img style="    ; position: absolute;right: 95%; top: 20%;" :src="'images/garra-sm-hor.png'" alt="">
    <img style="    ; position: absolute;left: 95%; top: 20%;" :src="'images/garra-sm-izq.png'" alt="">

  </Dialog>
</template>




<script setup>
import { menuOptions } from '@/service/menuOptions';
import { onMounted, onBeforeUnmount, watch } from 'vue'
// import { getProductsByCategory, getCategory, getMenu } from '@/service/productServices.js'
import { ref, computed } from 'vue';
import { PrimeIcons } from 'primevue/api';
// import { changeProduct } from '@/service/productServices';
import {checkedAcomp, sumarAdiciones, showSiteDialog, setShowDialog,showProductDialog,productDialog,checkedSalsas,checkedAdiciones,currentSalsas,currentAditions } from '@/service/state';
import { carro_para_la_barra_de_abajo } from '@/service/cart';
// import { useRouter } from 'vue-router';
import { adiciones } from '@/service/menu/adiciones/adiciones.js'
import {URI} from '@/service/conection'
import { useToast } from 'primevue/usetoast';
import { domicilio,quantity } from '@/service/cart';
// import { cart } from '@/service/cart';
// import {vue} from 'vue';imp
import { cities } from '@/service/citiesService';
import { menuGlobal,version_menu } from '@/service/menu/menu';
// import { PrimeIcons } from 'primevue/api';
import { formatoPesosColombianos } from '@/service/formatoPesos';
// import TarjetaMenu from '@/components/TarjetaMenu.vue';
// import { RouterLink } from 'vue-router';
import router from '@/router/index.js'
import { useCart,deleteAllCookies } from '@/service/cart';
// import barra from '@/components/barra.vue';
import { useRoute } from 'vue-router';
import barra from '@/components/barra.vue';
import siteDialog from '@/components/siteDialog.vue';
// import ProductDial from '@/views/pages/productDial.vue';


const route = useRoute();

// Verificar si la ruta actual o alguna de sus rutas secundarias es /admin-products
const isInAdminProductsRoute =
route.matched.some(record => record.path === '/admin-products') ||
route.matched.some(record => record.path.startsWith('/admin-products/')) || 
route.matched.some(record => record.path === '/entregas') ||
route.matched.some(record => record.path.startsWith('/entregas/'));;



const ruta = ref(router.currentRoute)
const version_tienda = ref(1)
const screenWidth = ref(window.innerWidth);
console.log(screenWidth.value)
// Función para actualizar el valor del ancho de la pantalla
const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

const toast = useToast();
// Escuchar el evento de cambio de tamaño de la ventana
window.addEventListener('resize', updateScreenWidth);

// Limpieza al desmontar el componente
onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreenWidth);
});





const storedVersion = localStorage.getItem('version_tienda');

// Check if it doesn't exist in local storage
if (!storedVersion) {
  // If it doesn't exist, save the current version to local storage
  localStorage.setItem('version_tienda', version_tienda.value);
} else {
  // If it exists, compare with the current version
  if (parseInt(storedVersion) !== version_tienda.value) {
    // If it's not equal, update the local storage with the current version
    localStorage.setItem('version_tienda', version_tienda.value);
    localStorage.removeItem('menu')
    localStorage.removeItem('cart')
    localStorage.removeItem('currentNeigborhood')
    deleteAllCookies()

    // Perform any additional actions needed when the version changes
    // For example, you might want to update the UI or perform other logic.
    console.log('Version updated. Do additional actions here.');
  }
}































const c_neigbor = ref(localStorage.getItem('currentNeigborhood'))

onMounted(() => {

  const cartData = JSON.parse(localStorage.getItem('cart'));

  // Check if 'cart' exists in localStorage and has 'products' attribute
  const productsLength = cartData && cartData.products ? cartData.products.length : 0;

  // Create a ref with the calculated quantity
  quantity.value = productsLength;






  if (localStorage.getItem('cart')) {
    // localStorage.setItem('cart',{products:[],total:0})
    carro_para_la_barra_de_abajo.value = JSON.parse(localStorage.getItem('cart'))
  }

  if (!localStorage.getItem('cart')) {
    localStorage.setItem('cart', JSON.stringify({ products: [], total: 0 }))
    // localStorage.setItem('totalCart',0)
  }

  console.log(JSON.parse((localStorage.getItem('menu'))))
  // cart.value = JSON.parse(localStorage.getItem('cart'))

  if (localStorage.getItem('menu') && localStorage.getItem('versionMenu') && parseFloat(localStorage.getItem('versionMenu')) ==  version_menu.value) {
    const version_local = parseFloat(localStorage.getItem('versionMenu')) 
    console.log(version_local, version_menu.value)

  
      console.log('habia')
      menuOptions.value[0].menus = JSON.parse(localStorage.getItem('menu'))
    // menuOptions.value[0].version = JSON.parse(localStorage.getItem('versionMenu'))

    
  } else {

    //   getMenu().then(products => {
    //   menuOptions.value[0].menus = products
    //   localStorage.setItem("menu", JSON.stringify(products))

    //   if(!showSiteDialog.value){
    //     location.reload()
    //   }

    // })

    menuOptions.value[0].menus = menuGlobal
    localStorage.setItem('menu', JSON.stringify(menuGlobal))
    localStorage.setItem('versionMenu', version_menu.value)
    console.log('nuevo menu')
    localStorage.removeItem('cart')
    localStorage.removeItem('currentNeigborhood')

  }






})
const sitesImages = ref({
  Caney: 'https://drive.google.com/file/d/1LpmzmgBDOR-YAT4_SstyAldl1Nid-CF2/view?usp=sharing',
  'La Flora': 'https://backend.novatocode.online/read-site-cover/IMPERIO%20CANEY',
  Palmira: '	https://backend.novatocode.online/read-site-cover/IMPERIO%20PALMIRA',
  Bretaña: 'https://backend.novatocode.online/read-site-cover/IMPERIO%20BRETA%C3%91A',
  Jamundi: 'https://backend.novatocode.online/read-site-cover/IMPERIO%20JAMUNDI',
  Tulua: 'https://backend.novatocode.online/read-site-cover/IMPERIO%20TULUA',
  default: ''
})
const currenNeigborhood = ref({
  site: {
    name: 'default'
  }
})
const possibleNeigborhoods = ref()

const vueMenu = ref(false)

const addcar =(product) => {

  showProductDialog.value = !showProductDialog.value

    const product_new = {... product}
    
    product_new.price = product_new.price 
    product_new.salsas = currentSalsas.value
    product_new.adiciones = currentAditions.value
    useCart.add(product_new)  
    toast.add({ severity: 'success', summary: 'Agregado al carrito', detail: productDialog.value.name, life: 3000 });
}
const currenCity = ref({})

const changePossiblesNeigborhoods = () => {
  const neigborhoods = []

  currenCity.value.sites.map(site => {
    site.neigborhoods.map(neigborhood => {
      neigborhoods.push({ name: neigborhood.name, neigborhood: neigborhood, site: site })
      console.log(site)
    })
  })

  possibleNeigborhoods.value = neigborhoods
}
watch(currenCity, () => { changePossiblesNeigborhoods() })

const setNeigborhood = () => {
  localStorage.setItem('currentNeigborhood', JSON.stringify({ 
    currenCity: currenCity.value.name, 
    currenNeigborhood: currenNeigborhood.value.neigborhood, 
    currenSite: currenNeigborhood.value.site.name, 
    currenSiteId:currenNeigborhood.value.site.site_id,
     }))
  // console.log(localStorage.getItem('currentNeigborhood'))
  localStorage.setItem('currenSiteWsp', currenNeigborhood.value.site.wsp)
  
  setShowDialog()
  location.reload()
  
  


}

const wsp = ref(localStorage.getItem('currenSiteWsp'))

const searchCountry = (event) => {
  setTimeout(() => {
    if (!event.query.trim().length) {
      autoFilteredValue.value = [...autoValue.value];
    } else {
      autoFilteredValue.value = autoValue.value.filter((country) => {
        return country.name.toLowerCase().startsWith(event.query.toLowerCase());
      });
    }
  }, 250);
};

console.log(router.currentRoute)

const topbarMenuClasses = computed(() => {
  return {
    'layout-topbar-menu-mobile-active': topbarMenuActive.value
  };
});

const topbarMenuActive = ref(false);





const cargarAdiciones = (item,gratis=0) => {


  // Asegúrate de que checkedAdiciones y currentAditions estén definidos en el ámbito adecuado

  const negativePriceCount = currentAditions.value.filter((el) => el.price <= 0).length;
  
 

  if (checkedAdiciones.value[item.name]) {

    if (negativePriceCount >= gratis && item.price ==0) {
    checkedAdiciones.value[item.name] = false
    console.log('ya')

    toast.add({ severity: 'error', summary: 'Recuerda', detail: `solo puede elegir ${gratis} acompanantes gratis`, life: 3000 });

    // Si ya hay dos o más objetos con price < 0, no hacer nada y retornar
    return;
   
  }
    // Si el checkbox está marcado, agregar el elemento a la lista
    currentAditions.value.push(item);
  } else {
    // Si el checkbox está desmarcado, quitar el elemento de la lista
    const index = currentAditions.value.findIndex((el) => el.name === item.name);
    if (index !== -1) {
      currentAditions.value.splice(index, 1);
    }
  }

  console.log(currentAditions.value)
};

function sumarPrecios(arrayDeObjetos) {
  // Verificar si el array está vacío
  if (arrayDeObjetos.length === 0) {
    return 0;
  }

  // Utilizar reduce para sumar los valores de .price
  const suma = arrayDeObjetos.reduce((acumulador, objeto) => {
    // Asegurarse de que .price sea un número antes de sumarlo
    const precio = parseFloat(objeto.price);
    // Sumar al acumulador solo si se obtuvo un número válido desde .price
    return isNaN(precio) ? acumulador : acumulador + precio;
  }, 0);

  return suma;
}
// const cargarAcomp = (item) => {
//   console.log('hola');

//   // Asegúrate de que checkedAdiciones y currentAditions estén definidos en el ámbito adecuado

//   if (checkedAcomp.value[item.name]) {
//     // Si el checkbox está marcado, agregar el elemento a la lista
//     currentAditions.value.push(item);
//   } else {
//     // Si el checkbox está desmarcado, quitar el elemento de la lista
//     const index = currentAditions.value.findIndex((el) => el.name === item.name);
//     if (index !== -1) {
//       currentAditions.value.splice(index, 1);
//     }
//   }
// };



const cargarSalsas = (item) => {
  console.log('hola');

  if (item === 'TODAS LAS SALSAS') {
    // Si seleccionas 'TODAS LAS SALSAS', establece todas las demás opciones como false
    for (const key in checkedSalsas.value) {
      if (key !== 'TODAS LAS SALSAS') {
        checkedSalsas.value[key] = false;
      }
    }

    // Limpia la lista currentSalsas y agrega 'TODAS LAS SALSAS'
    currentSalsas.value = ['TODAS LAS SALSAS'];
  } else if (item === 'SIN SALSAS') {
    // Si seleccionas 'SIN SALSAS', establece todas las demás opciones como false
    for (const key in checkedSalsas.value) {
      if (key !== 'SIN SALSAS') {
        checkedSalsas.value[key] = false;
      }
    }

    // Limpia la lista currentSalsas y agrega 'SIN SALSAS'
    currentSalsas.value = ['SIN SALSAS'];
  } else {
    // Asegúrate de que checkedSalsas y currentSalsas estén definidos en el ámbito adecuado

    // Si 'TODAS LAS SALSAS' está presente, quitarlo de la lista
    const indexTodasLasSalsas = currentSalsas.value.indexOf('TODAS LAS SALSAS');
    if (indexTodasLasSalsas !== -1) {
      currentSalsas.value.splice(indexTodasLasSalsas, 1);
    }

    // Si 'SIN SALSAS' está presente, quitarlo de la lista
    const indexSinSalsas = currentSalsas.value.indexOf('SIN SALSAS');
    if (indexSinSalsas !== -1) {
      currentSalsas.value.splice(indexSinSalsas, 1);
    }

    // Si el checkbox está marcado, agregar el elemento a la lista
    if (checkedSalsas.value[item]) {
      currentSalsas.value.push(item);
    } else {
      // Si el checkbox está desmarcado, quitar el elemento de la lista
      const index = currentSalsas.value.indexOf(item);
      if (index !== -1) {
        currentSalsas.value.splice(index, 1);
      }
    }
  }

  console.log(currentSalsas.value);
};




const hay_barrio = ref(JSON.parse(localStorage.getItem('currentNeigborhood'))) 









</script>