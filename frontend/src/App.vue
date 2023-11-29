<script setup>
import { menuOptions } from './service/menuOptions';
import { onMounted, onBeforeUnmount, watch } from 'vue'
import { getProductsByCategory, getCategory, getMenu } from '@/service/productServices.js'
import { ref, computed } from 'vue';
import { PrimeIcons } from 'primevue/api';
import { changeProduct } from './service/productServices';
import {checkedAcomp, sumarAdiciones,calcularPrecioTotal, showSiteDialog, setShowDialog,showProductDialog,setProductDialog,productDialog,checkedSalsas,checkedAdiciones,currentAditions,currentSalsas, calcularTotalCarrito } from './service/state';
import { carro } from './service/cart';
import { useRouter } from 'vue-router';
import { adiciones } from '@/service/menu/adiciones/adiciones.js'
import {URI} from '@/service/conection'
import { useToast } from 'primevue/usetoast';
import { domicilio,quantity } from './service/cart';
// import { cart } from './service/cart';
// import {vue} from 'vue';imp
import { cities } from './service/citiesService';
import { menuGlobal,version_menu } from './service/menu/menu';
// import { PrimeIcons } from 'primevue/api';
import { formatoPesosColombianos } from './service/formatoPesos';
// import TarjetaMenu from './components/TarjetaMenu.vue';
import { RouterLink } from 'vue-router';
import router from '@/router/index.js'
import { useCart,deleteAllCookies } from './service/cart';
 

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
    carro.value = JSON.parse(localStorage.getItem('cart'))
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


  if (!c_neigbor.value) {
    showSiteDialog.value = true
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

const ruta = ref(router.currentRoute)
const vueMenu = ref(false)

const addcar =(product) => {

  showProductDialog.value = !showProductDialog.value

    const product_new = {... product}
    
    product_new.price = product_new.price + sumarAdiciones(currentAditions)
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
    currenSiteWsp:currenNeigborhood.value.site.wsp }))
  console.log(localStorage.getItem('currentNeigborhood'))
  // setShowDialog()
  location.reload();
  


}



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





const cargarAdiciones = (item) => {
  console.log('hola');

  // Asegúrate de que checkedAdiciones y currentAditions estén definidos en el ámbito adecuado

  if (checkedAdiciones.value[item.name]) {
    // Si el checkbox está marcado, agregar el elemento a la lista
    currentAditions.value.push(item);
  } else {
    // Si el checkbox está desmarcado, quitar el elemento de la lista
    const index = currentAditions.value.findIndex((el) => el.name === item.name);
    if (index !== -1) {
      currentAditions.value.splice(index, 1);
    }
  }
};


const cargarAcomp = (item) => {
  console.log('hola');

  // Asegúrate de que checkedAdiciones y currentAditions estén definidos en el ámbito adecuado

  if (checkedAcomp.value[item.name]) {
    // Si el checkbox está marcado, agregar el elemento a la lista
    currentAditions.value.push(item);
  } else {
    // Si el checkbox está desmarcado, quitar el elemento de la lista
    const index = currentAditions.value.findIndex((el) => el.name === item.name);
    if (index !== -1) {
      currentAditions.value.splice(index, 1);
    }
  }
};



const cargarSalsas = (item) => {
  console.log('hola');

  if (checkedSalsas.value['TODAS LAS SALSAS']) {
    // Si seleccionas 'TODAS LAS SALSAS', deselecciona las otras opciones
    checkedSalsas.value['SIN BURGER DE LA CASA'] = false;
    checkedSalsas.value['SIN VERDE DE LA CASA'] = false;
    checkedSalsas.value['SIN PIÑA'] = false;
    checkedSalsas.value['SIN BBQ'] = false;

    // Limpia la lista currentSalsas y agrega 'TODAS LAS SALSAS'
    currentSalsas.value = ['TODAS LAS SALSAS'];
  } else {
    // Asegúrate de que checkedSalsas y currentSalsas estén definidos en el ámbito adecuado

    // Si el checkbox está marcado, agregar el elemento a la lista
    if (checkedSalsas.value[item]) {
      // Agrega 'TODAS LAS SALSAS' solo si no está presente
      if (!currentSalsas.value.includes('TODAS LAS SALSAS')) {
        currentSalsas.value.push(item);
      }
    } else {
      // Si el checkbox está desmarcado, quitar el elemento de la lista
      const index = currentSalsas.value.findIndex((el) => el === item);
      if (index !== -1) {
        currentSalsas.value.splice(index, 1);
      }
    }
  }
};



const hay_barrio = ref(JSON.parse(localStorage.getItem('currentNeigborhood'))) 









</script>

<template>
  <router-view  style="background-color: ;" class="col-12 p-0 m-0" :class="screenWidth<800 && ruta.fullPath == '/cart' || ruta.fullPath == '/pay' || screenWidth<800 && ruta.fullPath == '/menu' || screenWidth<800 && ruta.fullPath == '/Sedes'? 'fondo-movil':'fondo-pc'"  />
  <!-- <Dialog v-if="menuOptions[0].menus.length < 2" v-model:visible="menuOptions" modal header="Header"
        :style="{ width: '100%', border: 'none', overflow: 'hidden' }" :breakpoints="{ '960px': '75vw', '641px': '100vw' }">
        <img class="imagen" style="" src="http://localhost:5173/src/images/logo.png" alt="">
 
      </Dialog> -->

  <!-- <Dialog  v-model:visible="menuOptions" modal header="Header"
        :style="{ width: '100%', border: 'none', overflow: 'hidden' }" :breakpoints="{ '960px': '75vw', '641px': '100vw' }">
        <img class="imagen" style="" src="http://localhost:5173/src/images/logo.png" alt="">
      </Dialog> -->

  <Dialog :closeOnEscape="!c_neigbor? false: true" v-if="!c_neigbor || showSiteDialog" v-model:visible="showSiteDialog" :style="{ width: '500px' }"
    header="Seleccion de sede" :modal="true" class="p-fluid "
    style="    box-shadow: 0px 0px 50px rgb(255, 0, 0);; background-color: white;border: .5rem solid ;position: relative; border-radius: 30px;padding-top: 2rem;">

    <div class="notch"
                style="display: flex; align-items: center; width: 30%; background-color: black; border-radius: 0 0 1rem 1rem; height: 2rem; position: absolute; top: 0rem; left: 35%;">
                <div class="led"
                    style="position:absolute ;right: 1rem; width: 0.7rem; height: 0.7rem; background-color: var(--primary-color); border-radius: 50%;: 1rem">
                </div>

            </div>

 
    <div
      style="width: 100%;display: flex; flex-direction: column; align-items: center; border-radius: ;background-color: ">

      <img style="width: 50px;" src="http://localhost:5173/src/images/logo.png" alt="">

      <div class="field col-12 " style="width: 100%;">
        <label for="site_id" style="color: black;">Ciudad</label>
        <Dropdown @click="() => currenNeigborhood = {
          site: {
            name: 'default'
          }
        }" v-model="currenCity" :options="cities" placeholder="" optionLabel="name" required="true" />

      </div>
      <div class="field col-12" style="width: 100%; display: block;">
        <label for="site_id" style="color: black;">Barrio</label>

        <Dropdown filter v-model="currenNeigborhood" :disabled="!possibleNeigborhoods" :options="possibleNeigborhoods"
          optionLabel="name" required="true" />

        <!-- <Dropdown v-model="seleFcarrctedCity" editable :options="possibleNeigborhoods"  placeholder="Select a City" class="w-full md:w-14rem" /> -->

      </div>

      <div class="field col-12" style="width: 100%; height:300px ; position: relative;">


        <div class="img-cont">

          <div class="img-before" v-if="currenNeigborhood.site?.name == 'default'">
            <p class="text-2xl lg:text-4xl text-center " style="font-weight: bold;color: black;">Vamos a buscar tu sede mas cercana</p>
          </div>
          <img :src="sitesImages[currenNeigborhood.site?.name]"
            :class="currenNeigborhood.site?.name == 'default' ? 'default-image' : ''"
            style="border: 1px solid gray; width: 100%; height: 100%; object-fit: cover; border-radius: 5px;" alt="">
        </div>



        <div
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display:flex; padding: 1rem; align-items: end; ">
          <p v-if="currenNeigborhood.site.name != 'default'" class=""
            style="text-align: center; height: min-content;  width: 100%; font-size: 35px; font-weight: bold; background-color: rgba(0, 0, 0, 0.577);">
            <span class="text-2xl lg:text-2xl" style=""> SALCHIMONSTER</span> <span style="text-transform: uppercase;" class="text-2xl lg:text-2xl">{{ currenNeigborhood.site.name }}</span>
          </p>
        </div>


      </div>

      <div class="field col-12" style="width: 100%;  ;">
        <Button @click="setNeigborhood" :disabled="currenNeigborhood.site.name == 'default'"
          style="width: max-content; padding: 10px 20px;width: 100%; text-align: center;" class="menu-button-new">
          <p style="width: 100%; padding: 0; margin: 0">
            <i :class="PrimeIcons.SAVE"></i> GUARDAR
          </p>
        </Button>

      </div>


    </div>

    <button v-if="hay_barrio"  @click="setShowDialog" style="width: 3rem;height: 3rem; border: none; position: absolute; right: 2rem; top:1rem;background-color: var(--primary-color); border-radius: 50%; display: flex; align-items: center;justify-content: center;">
      <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>

    </button>


  </Dialog>




  <Dialog  v-model:visible="showProductDialog" :style="{ width: '1024px',height:'max-content' }"
    header="Seleccion de sede" :modal="true" class="p-fluid "
    style="    box-shadow: 0px 0px 100px rgb(255, 0, 0);outline: 4px solid red; background-color: white;border: 1rem solid ; border-radius: 30px;padding-top: 2rem;">


    <button  @click="showProductDialog = ! showProductDialog" style="width: 3rem;height: 3rem; border: none; position: absolute; right: 1rem; top:0.5rem;background-color: var(--primary-color); border-radius: 50%; display: flex; align-items: center;justify-content: center; z-index: 9;">
      <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>

    </button>
   
 
    <div class="grid col-12 p-0 pt-6 md:p-4"  >
      <div class="header col-12 grid m-0 p-0" >
        <p class="nombre col-9 text-xl lg:text-2xl p-0 text-left" style="color:black;font-weight: bold"> {{ productDialog.name }}</p>
        <p class="precio col-3 text-xl lg:text-2xl p-0 text-right " style="color:black;font-weight: bold"> {{formatoPesosColombianos( productDialog.price + sumarAdiciones(currentAditions))}}</p>
      </div>

      <div class="col-12 md:col-6 p-0" style="display: flex;align-items: center; max-height: 45rem; background-color: var(--primary-color); border-radius: 2rem;; overflow: hidden; " >

      <div class="before"
                style="top: 0; left: 0; width: 100%; height: 100%; overflow: hidden; position: ;  position: absolute;">
                <img :src="`${URI}/read_product_image/600/${productDialog.id}`" alt=""
                    style="width: 110%; height: 110%; opacity: 0.3; object-fit:  cover; filter: blur(5px);">
        </div>
        <img class="col-12 p-0"  :src="`${URI}/read_product_image/600/${productDialog.id}`" alt="" style="width: 100%;object-fit: cover;">

      </div>
      
      <div class=" scroll  col-12 md:col-6 m-0 pl-3 pr-0 mr-0" style=" padding-bottom: 5rem;">
        <p class="col-12 text-xl " style="font-weight: bold;color: black; ">
          DESCRIPCION  
        </p>
        <p class="col-12 text-l " style="color: black;">
          {{ productDialog.description }}
        </p>

        <div v-if="productDialog.category_id != 4 && productDialog.category_id != 3 ">
                  <p class="col-12 text-xl" style="font-weight: bold;color: black;display: flex;align-items: center;">
          <span class="col-4 p-0 m-0">SALSAS</span> <div class="col p-0 m-0" style="height: auto; height: 01rem;background-color: var(--primary-color)"> </div>
        </p> 

        <div v-for="i in adiciones.salsas" class="col-12 pt-0 pb-0 mb-2" :class="checkedSalsas[i] || checkedSalsas['TODAS LAS SALSAS'] ? 'selected' : ''" style="justify-content: start; padding-bottom: 0.5rem; padding-left: 1rem; border-radius: 1rem;">

<div class="salsa col-12 p-0" style="color: black; margin: 0; padding: 0; display: flex; justify-content: space-between; align-items: center;">
    <p class="texto p-0 m-0" style="margin: 0; padding: 0; min-width: max-content">{{ i }}</p>

    <Checkbox v-if="!(checkedSalsas['TODAS LAS SALSAS'] && !checkedSalsas[i])" @change="cargarSalsas(i)" v-model="checkedSalsas[i]" :binary="true" style="margin-right: 1rem;" />
</div>
</div>

        </div>




        <div v-if="productDialog.category_id != 3">


          <p class="col-12 text-xl" style="font-weight: bold;color: black;display: flex;align-items: center;">
          <span class="col-4 p-0 m-0">{{productDialog.category_id ==4 ? ' TOPINGS' : 'ADICIONES'}}</span> <div class="col p-0 m-0" style="height: auto; height: 01rem;background-color: var(--primary-color)"> </div>
        </p>
       

       

          <div class="p-0" v-for="i in 
            productDialog.category_id == 1 ? adiciones.salchipapas.products : 
            productDialog.category_id == 2 ? adiciones.hamburguesas.products :
            productDialog.category_id == 3 ? adiciones.salchipapas.products : 
            productDialog.category_id == 4 ? adiciones.topings.products :
            productDialog.category_id == 5 ? adiciones.almuerzos.products :
            productDialog.category_id == 6 ? productDialog.adiciones.products :[]" 
          style=" ; padding-bottom: 0.5rem; ; color:black;border-radius:2rem" :class="checkedAdiciones[i.name]? 'selected':''" >



          <div class=" col-12 grid pl-5 pb-0 pt-0 mb-4" style=" align-items: center; justify-content: space-between; ">
              

            <div class="col-9 p-0 " style="display: flex;">
              <Checkbox @change="cargarAdiciones(i)"   class="p-0" v-model="checkedAdiciones[i.name]" :binary="true" style="margin-right: 1rem;  " />

                  <p   class="   p-0" style=";"> {{ i.name }}
                  </p>

                
            </div>
                  

              <p class=" text col-3 text-right p-0 " style="font-weight: bold; margin-left: ;">${{ i.price }}
              </p>

        </div>


        </div>


        <p v-if="productDialog.category_id ==5" class="col-12 text-xl" style="font-weight: bold;color: black;display: flex;align-items: center;">
          <span  class="col-4 p-0 m-0 mr-4 ">{{ `ELIGE ${productDialog.acomp_cantidad} ${productDialog.acomp_cantidad<2? 'ACOMPANANTE':'ACOMPANANTES'}`}}</span> <div class="col p-0 m-0" style="height: auto; height: 01rem;background-color: var(--primary-color)"> </div>
        </p>
       

       

          <div v-if="productDialog.category_id ==5" class="p-0" v-for="i in adiciones.acomp_almuerzos.products" 
          style=" ; padding-bottom: 0.5rem; ; color:black;border-radius:2rem" :class="checkedAcomp[i.name]? 'selected':''" >



          <div class=" col-12 grid pl-5 pb-0 pt-0 mb-4" style=" align-items: center; justify-content: space-between; ">
              

            <div class="col-9 p-0 " style="display: flex;">
              <Checkbox @change="cargarAdiciones(i)"   class="p-0" v-model="checkedAcomp[i.name]" :binary="true" style="margin-right: 1rem;  " />

                  <p   class="   p-0" style=";"> {{ i.name }}
                  </p>

                
            </div>
                  

              <p class=" text col-3 text-right p-0 " style="font-weight: bold; margin-left: ;">${{ i.price }}
              </p>

        </div>


        </div>





        </div>
        

      
       

      </div>
      <div @click="addcar(productDialog)"  class="col-12 md:col-6 add-car" style="position: absolute;display: flex; align-items: end; justify-content: center; background-color: white;  height: rem; bottom: 1.5rem;right: 0;">

        <button style="background-color: var(--primary-color); color:white; border:none;padding: 0.5rem 3rem; font-weight: bold; border-radius: 2rem;">  <span class="text-xl"  >AGREGAR AL CARRITO</span></button>

      </div>
    </div>

    
    

    <!-- <button  @click="setProductDialog" style="width: 3rem;height: 2rem; border: none; position: absolute; right: 1rem; top:1rem;background-color: var(--primary-color); border-radius: 5px; display: flex; align-items: center;justify-content: center;">
      <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>
 
    </button> -->

    <!-- <div
      style="width: 40%;max-width: 20rem; position: absolute; display: flex;align-items: center; justify-content: end;padding-right: 1rem; height: 1.5rem; background-color: black; top: 0; border-radius:  15px 15px ; top:0.5rem">
      <div class="led" style="width: 0.7rem;height: 0.7rem;border-radius: 50%; display: ;"></div>
      
    </div> -->

    <img style="    filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 123, 0)); position: absolute;right: 95%; top: 20%;" :src="'images/garra-sm-hor.png'" alt="">
    <img style="    filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 123, 0)); position: absolute;left: 95%; top: 20%;" :src="'images/garra-sm-izq.png'" alt="">

  </Dialog>


 
  <div v-if="ruta.fullPath != '/cart'" class="barra-carrito col-12 " style=" 
                          /* width: auto; */
                            display: flex;
                            gap:2rem;
                            align-items: center;  
                            position: relative;
                            z-index: 1000;
                            /* z-index: 999;  */
                            justify-content:center ;
                            /* touch-action: none;  */
                            /* width: %;  */
                            height: 5rem;
                            /* padding: 1rem; */
                        /* padding: 1rem;  */
                            background-color: rgb(255, 255, 255); 
                            position: fixed; bottom: 0; left: 0; 
                            box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.5);">
 
     


      <RouterLink to="/cart" style="">
        <button class="    carro  " style="  
                            display: flex; 
                            background-color: ; 
                            align-items: center; 
                            justify-content: center;
                            gap: 1rem; 
                            background-color:;
                        

                            border-bottom: 4px solid rgb(0, 0, 0);
                        
                            ">
 
 

          <i style="font-size: 2rem; " class="icono" :class="PrimeIcons.SHOPPING_CART"> </i>


          <div v-for="product in carro.products.slice(0, 5)">
            <img class="img-cart" @mouseover="() => vueMenu = true" style="height: 2rem; object-fit: contain;"
              :src="`${URI}/read_product_image/300/${product.id}`" alt="">

            <!-- <TarjetaMenu v-if="vueMenu" style="width: 200px;height: 200px;" :product="product"></TarjetaMenu> -->

          </div>

          <div v-if="carro.products.length > 5 "
            style="width: auto; border-radius: 50%; ; height: 100%; object-fit: contain;" alt="">

            <p style="font-weight: bold; font-size: 2rem; ">
              +{{ carro.products.length - 5 }}
            </p>
          </div>



        </button>
      </RouterLink>

      <p class="h2" style="position: absolute;top: 0;">
       

      </p>
      

      <!-- <RouterLink style="background-color: green;" to="/pay" v-if="carro.products.length > 0 && screenWidth>555">
        <button  class=" ordenar  " style="text-decoration: none;  display: flex;
                             background-color:var(--primary-color)  ; 
                             color: white; 
                             align-items: center;  
                         
                             gap: 20px; width: auto ;
                             background-color:;padding: 0.1rem 1rem;
                             height: 0%;">

          <i style="font-size: 2rem;color: white; " class="icono" :class="PrimeIcons.MONEY_BILL"> </i>


          <span style="font-size: 2rem; background-color: var();">
            Ordenar
          </span>
        </button>
      </RouterLink> -->


      <a v-if="carro.products.length > 0 && screenWidth>720" >



        <button class=" " style="
                            border: none; background-color:transparent; 
                            /* border-radius: 50%;  */
                            display: flex;align-items: center; justify-content: center;
                            


    /* box-shadow: 0px 0px 10px rgb(255, 255, 255); */

    ">
          <span :class="topbarMenuClasses"  style="font-size:2rem ; font-weight: bold;">
            {{ formatoPesosColombianos(Number(calcularTotalCarrito())) }}</span>
        </button>
      </a>


   



    
    <a class="whatsapp" style="
                            
                        
                            ">
 
 
 
         <button class="whatsapp-btn" style="
                             border: none; background-color:transparent; 
                             transition: all ease .3s;
                             /* border-radius: 50%;  */
                             display: flex;align-items: center; justify-content: center;
 
 
     /* box-shadow: 0px 0px 10px rgb(255, 255, 255); */
 
     ">
           <i class="" :class="PrimeIcons.WHATSAPP"
             style=";position: relative;  font-weight:  bold; font-size: 2rem; color: rgb(255, 255, 255);width:auto">
           </i>
         </button>
       </a>





  </div>


  <div v-if="showProductDialog" class="full-before col-12 p-0 m-0" style="top: 0;left: 0; position: fixed; background-color: black;height: 100vh;opacity: 0.8;"> </div>
</template>

<style scoped>
@keyframes rot {
  0% {
    transform: translatey(-50%) scale(1.25, 0.75);
  }

  50% {
    transform: translatey(-150%) scale(1, 1);
  }

  100% {
    transform: translatey(-50%) scale(1.25, 0.75);
  }
}

* *:focus{
  outline: none;
  border: none;
}

.imagen {
  margin: 200px;
  width: 100px;
  /* overflow: hidden;  */
  animation: rot 0.7s infinite;
  transform-origin: center bottom;
}

.img-cart:hover {
  transform: scale(1.3);
}

.img-cart {
  transition: all .3s ease;
}







@media (min-width: 767px) {
  .scroll{
  max-height:45rem ;overflow-y: auto;

}

.add-car{
  width: 50%;
}
}

.led{
    animation: cambiaColor 1s infinite; /* 3s de duración, animación infinita */
}
    @keyframes cambiaColor {
      0% { background-color: rgb(0, 0, 0); }
      50% { background-color: rgb(30, 255, 0); }
      100% { background-color: var(--primary-color); }
    }
.img-before {
  /* background-color: rgba(0, 0, 0, 0.235); */
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0%;
  left: 0;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;

}

.carro:hover {
  /* transform: scalex(1.2); */
  background-color: #ff62004a;
  cursor: pointer
}

.menu-button-new {
  background-color: var(--primary-color);
  /* padding: 1rem; */
  /* margin: 0 1rem; */
  border: none;
  font-size: 20px;
  /* transition: all  0.3s; */
  /* font-weight: bold; */
  border-radius: 10px;
  color: #fff;
  width: 300px;
  transition: all 0.3s ease;
  text-align: center;

}

.fondo-movil{
  background-color: var(--primary-color);
}

.fondo-pc{
  background-color: #ffffff;
  overflow-x: hidden;
}
.img-cont {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;


}

.default-image {
  filter: blur(10px);
  position: relative;
}
*:focus{
 border: none;
 outline: none;
}
.default-image::before {
  content: 'hola';
  width: 100%;
  background-color: rgba(177, 99, 9, 0.1);
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.selected{
  background-color:#ff620050 
}

.menu-button-new:hover {
  /* filter: brightness(1.5);  
   */
  background-color: black;
  cursor: pointer;

}




.cart {

  box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.4);



}

.img-cont {
  background-color:rgb(255, 226, 192);
  /* display: flex; */
  /* justify-content: flex-start; */
  align-items: start;

  /* box-shadow: 30px 0px 30px rgba(0, 0, 0, 0.5); */
  height: 100%;
  /* flex-direction: column; */
}



.imagen {
  /* position: fixed; */
  width: 100%;
  height: auto;
  object-fit: contain;
  transition: all ease 0.5s;
  /* margin-left: 1vw; */
  border-radius: 50px;

  /* filter: drop-shadow(-2px 2px 15px rgba(0, 0, 0, 0.7)); */

}

.imagen:hover {
  transform: scale(1.1);
  ;

  /* box-shadow: 0px 0px 30px rgba(0, 0, 0, 1); */
  filter: brightness(1.2) drop-shadow(-2px 2px 15px rgba(0, 0, 0, ));
  /* filter: drop-shadow(-2px 2px 15px rgba(0, 0, 0, 0.7)); */

}

.producto {
  /* filter: brightness(1.2); */
}

.info {
  /* padding-left: 10%; */

  /* padding-top: 5%; */
  display: flex;
  flex-direction: column;
  align-items: fle;
  /* gap: 10px; */
  /* box-shadow: 0px 0px 30px rgba(0, 0, 0, 1); */
}

.ordenar {
  transition: all 0.2s ease;
  border: 2px solid var(--primary-color);
  /* // font-weight: bold; */
  font-size: 20px;
  /* // margin-bottom: 200px; */
  background-color: transparent;
  border-radius: 5px;
}

.carro {

  border: none;
  /* // font-weight: bold; */
  /* font-size: 20px; */
  /* // margin-bottom: 200px; */
  background-color: transparent;
  border-radius: 5px;
  margin: auto;
  /* border-radius:; */
}

.whatsapp:hover {
  transform: scale(1.1);
}

.ver-mas:hover {
  background-color: var(--primary-color);
  transform: scale(1.1);



  color: #fff;
  cursor: pointer;
}


/* // .icono{
//     color: var(--primary-color);
// } */
.ver-mas:hover>.icono {
  /* // background-color: var(--primary-color);

// display: none; */
  color: #fff;
  transform: translateX(5px);
}

.info-header {
  display: flex;
  justify-content: space-between;
  /* align-items: center; */
  /* gap: 20px; */
}

.salsa {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: start;
  padding: 0;

  margin: 0;


}

.salsa:hover {
  color: var(--primary-color);
}

.salsas {
  display: flex;
  padding: 0;
  margin: 0;


}

.whatsapp {
    /* background-color: red; */
    /* min-width: 1024px; */
    width: 3rem;
    height: 3rem;
    display: flex;
    transition: all ease .3s;
    right: 5rem;
    bottom: 9rem;

    /* align-items: center; */
    justify-content: center;
    background-color: #25D366;
    border-radius: 50%;
    position: absolute;
 
  }
@media (max-width:500px)  {
  .whatsapp {
    /* background-color: red; */
    /* min-width: 1024px; */
    width: 4rem;
    height: 4rem;
    right: 5%;
    bottom: 130%;

  }
}


.led {
    animation: cambiaColor 1s infinite;
    /* 3s de duración, animación infinita */
}

@keyframes cambiaColor {
    0% {
        background-color: rgb(0, 0, 0);
    }

    50% {
        background-color: rgb(30, 255, 0);
    }

    100% {
        background-color: var(--primary-color);
    }
}
.adiciones {
  display: flex;
  padding: 0;
  margin: 0;

}

a{
  text-decoration: none;
}

.texto {
  /* width: 40%; */
  /* min-width: 200px; */
  padding-right: 20px;
  /* min-width: 200px; */
  /* margin-right: 20px; */
}

.icono {
  transition: all 0.2s ease;
  color: var(--primary-color);
  transform: translateX(-5px);
  font-weight: bold;
}

.title {}

.nombre-salsa::after {}


.animador {
  animation: para-aca 1s infinite ease;

}


@keyframes para-aca {
  0% {
    transform: translateX(0%);
  }

  50% {
    transform: translateX(100%)
  }

}

::-webkit-scrollbar {
  width: 1rem; /* Ancho de la barra de desplazamiento */
  padding-top: 1rem;
  position: absolute;
  display: none;
}
.clase{
    
}
/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {
  background-color: rgb(255, 0, 0); /* Color del pulgar de la barra de desplazamiento */
  border-radius: 9px;
  border: 5px solid var(--primary-color);
  height: 10rem;
  width: 10rem;
  /* display: none;  */
}
</style>
