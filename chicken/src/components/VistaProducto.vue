<template>
  <Dialog :close=" reset() "  v-model:visible="store.visibles.currentProduct" :style="{ width: '500px', }" header="Seleccion de sede"
    :modal="true" class="p-fluid pt-8 m-3"
    style="justify-content: center; background-color: white;position: relative ; border-radius: 1rem;padding-top: 2rem;">




    <div class="header col-12    "
      style=" display: flex;justify-content: space-between; ; background-color: rgb(255, 255, 255);z-index:99; position:absolute;top:0rem;left: 0;height: min-content;">
      <p class=" mayuscula md:pl-4 nombre col-9 text-l lg:text-xl p-0 text-left" style="color:black;font-weight: bold"> {{
        store.currentProduct.product_name }}</p>
      <p class="md:pr-4 precio col-3 text-l lg:text-xl p-0 text-right " style="color:black;font-weight: bold">
        {{ formatoPesosColombianos(store.currentProduct.price) }}</p>
    </div>


    <template #footer>
      <div class="col-12 pb-6 " style="display: flex; justify-content: center;">
        <Button class="" @click="addToCart(store.currentProduct)" label="Agregar al carrito" icon="pi pi-shopping-cart"
          style=" position: absolute;  pointer-events: all; background-color: black; color:white;width:auto;border:none;padding: 0.5rem 3rem; font-weight: bold;">
        </Button>
      </div>

    </template>



    <Button @click="store.setVisible('currentProduct', false)" severity="danger" icon="pi pi-times"
      style=" width: 2.5rem;height: 2.5rem; border: none; position: absolute; right: -1rem; top: -1rem; border-radius: 50%; display: flex; align-items: center;justify-content: center; z-index: 99;">

    </Button>








    <div class="grid col-12 p-0  md:p-2">





      <div class="col-12  p-0 mt-0 shadow-5"
        style="display: flex;align-items: center; max-height: 45rem; background-color:white;border-radius: 0.5rem; ">


        <img :class="see? 'cargado': 'sin-cargar'" :onload="seeImage" class="col-12 p-2 m-0" :src="`https://backend.salchimonster.com/read-product-image/600/${store.currentProduct.product_name}`"
          alt="" v-show="see" style="width: 100%;object-fit: contain; aspect-ratio: 1/1;">

      </div>




      <div v-show="!see" class="col-12  p-0 mt-0 shadow-5"
        style="display: flex;align-items: center; max-height: 45rem; background-color:white;border-radius: 0.5rem; ">


        <div style="width: 100%; aspect-ratio: 1 / 1; display: flex; align-items: center; justify-content: center">
          <ProgressSpinner   style="width: 100px; height: 100px" strokeWidth="5" 
        animationDuration=".2s" aria-label="Custom ProgressSpinner" />



        </div>
      
      </div>














      <!-- <p style="color: black;">{{ store.cart.additions }} {{ selectedAdditions }}</p> -->


      <div class="   col-12 p-0 my-5" style="  " :class="!isSmallScreen ? 'scroll' : 'static'">
        <p class="col-12 p-0 " style="font-weight: bold;color: black; ">
          DESCRIPCION

        </p>


        <p class="col-12 text-l p-0" style="color: black;text-transform:capitalize">
          {{ store.currentProduct.product_description.toLowerCase() }}

        </p>


        <div style="color: black;">
          <!-- {{ adicionales }}
          
          -->

          <div v-for="grupo in adicionales" :key="grupo.category">
            <div class="mb-2">
              <span class="mb-2 text-center">
                <b>{{ grupo.category }}</b>
              </span>
              <div class="mt-2">
                <div v-for="item in grupo.items" :key="item.aditional_item_instance_id" style="display: flex; gap: 1rem;">

                  <Checkbox class="my-1" :binary="true" v-model="item.checked"
                    @change="() => handleAdditionChange(item, grupo.category)" />
                  <div style="display: flex; width: 100%; gap: 1rem; justify-content: space-between;">
                    <span class="text-sm adicion" style="text-transform: lowercase;">{{ item.aditional_item_name }}</span>
                    <span v-if="item.checked" style="display: flex; align-items: center;">







                      <span v-if="item.aditional_item_price > 0" class="pl-2 py-1 text-sm">
                        <b>{{ formatoPesosColombianos(item.aditional_item_price *
                          selectedAdditions[item.aditional_item_instance_id]?.quantity) }}</b>
                      </span>

                      <Button @click="decrement(item)" class="ml-2" severity="danger"
                        style="width: 2rem; height: 1.5rem;border: none;" icon="pi pi-minus"></Button>
                      <InputText :modelValue="selectedAdditions[item.aditional_item_instance_id]?.quantity" readonly
                        style="width: 2rem;border: none; height: 1.5rem;" class="p-0 text-center" />
                      <Button @click="increment(item)" severity="danger" style="width: 2rem;height: 1.5rem; border: none;"
                        icon="pi pi-plus"></Button>
                    </span>



                    <span v-else-if="item.aditional_item_price > 0" class="pl-2 py-1 text-sm">
                        <b>{{ formatoPesosColombianos(item.aditional_item_price)}}
                          </b>
                      </span>

                  </div>

                </div>
                <hr>
              </div>
            </div>
          </div>
        </div>







      </div>

      <div v-if="!isSmallScreen" class="col-12 md:col-6 add-car pt-5 " style="pointer-events: none;display: flex; align-items: end; justify-content: center;     background: linear-gradient(to bottom, rgba(255, 255, 255, 0) 0%, rgb(255, 255, 255) 80%);
  height: 5rem; bottom: 0rem;right: 0;">



      </div>


    </div>


<!-- 
    <img :onLoad="seeImageLeftHand" v-show="see" :class="see? 'cargado-left-hand': 'sin-cargar'" style="     pointer-events: none;
   ; position: absolute;right: 95%; top: 20%;" :src="'/images/garra-sm-hor.png'" alt="">
    <img :onLoad="seeImageRightHand" v-show="see"  :class="see? 'cargado-right-hand': 'sin-cargar'"  style="     pointer-events: none;
   ; position: absolute;left: 95%; top: 20%;" :src="'/images/garra-sm-izq.png'" alt=""> -->

  </Dialog>
</template>




<script setup>
import { menuOptions } from '@/service/menuOptions';
import { onMounted, onBeforeUnmount, watch } from 'vue'
// import { getProductsByCategory, getCategory, getMenu } from '@/service/productServices.js'
import { ref, computed } from 'vue';
import { PrimeIcons } from 'primevue/api';
// import { changeProduct } from '@/service/productServices';
import { currentCambios, currentToppings, currentAcompanantes, checkedAcomp, sumarAdiciones, showSiteDialog, setShowDialog, showProductDialog, productDialog, checkedSalsas, checkedAdiciones, currentSalsas, currentAditions } from '@/service/state';
import { carro_para_la_barra_de_abajo } from '@/service/cart';
// import { useRouter } from 'vue-router';
import { adiciones } from '@/service/menu/adiciones/adiciones.js'
import { URI } from '@/service/conection'
import { useToast } from 'primevue/usetoast';
import { domicilio, quantity } from '@/service/cart';
// import { cart } from '@/service/cart';
// import {vue} from 'vue';imp
import { cities } from '@/service/citiesService';
import { menuGlobal, version_menu } from '@/service/menu/menu';
// import { PrimeIcons } from 'primevue/api';
import { formatoPesosColombianos } from '@/service/formatoPesos';
// import TarjetaMenu from '@/components/TarjetaMenu.vue';
// import { RouterLink } from 'vue-router';
import router from '@/router/index.js'
import { useCart, deleteAllCookies } from '@/service/cart';
// import barra from '@/components/barra.vue';
import { useRoute } from 'vue-router';
import barra from '@/components/barra.vue';
import siteDialog from '@/components/siteDialog.vue';
// import ProductDial from '@/views/pages/productDial.vue';
import { verCerrado } from '../service/state';
import { usecartStore } from '../store/shoping_cart';
import { curentProduct } from '../service/productServices';
import { carService } from '../service/car/carService'
import { adicionalesService } from '../service/restaurant/aditionalService';
import { useSitesStore } from '../store/site';

const sonido = new Audio('/sounds/sarpazo.mp3')

const selectedAdditions = ref({});


const see = ref(false)

const seeImage = () => {
  
  see.value = true
}


const reset = () => {
  see.value = seeLeftHand.value = seeRightHand.value = false
}

const seeLeftHand = ref(false)

const seeImageLeftHand = () => {
  seeLeftHand.value = true
}

const seeRightHand = ref(false)

const seeImageRightHand = () => {
  seeRightHand.value = true
}




const handleAdditionChange = (item, group) => {
  if (item.checked) {

    const new_item = {
      id: item.aditional_item_instance_id,
      name: item.aditional_item_name,
      price: item.aditional_item_price,
      group: group
    }

    selectedAdditions.value[new_item.id] = {
      ...new_item,
      quantity: item.quantity || 1
    };
  } else {
    delete selectedAdditions.value[item.aditional_item_instance_id];
  }
};

const increment = (item) => {
  if (item.checked) {

    const new_item = {
      id: item.aditional_item_instance_id,
      name: item.aditional_item_name,
      price: item.aditional_item_price,
      // quantity:item.quantity
    }


    selectedAdditions.value[new_item.id].quantity++;
  }
};

const decrement = (item) => {

  if (selectedAdditions.value[item.aditional_item_instance_id].quantity > 1 && selectedAdditions.value[item.aditional_item_instance_id]) {
    selectedAdditions.value[item.aditional_item_instance_id].quantity--
  }

};


const addToCart = (product) => {
  // Convertir las adiciones seleccionadas de un objeto a un array


  const additionsArray = Object.values(selectedAdditions.value);
  store.addProductToCart(product);

  additionsArray.forEach(adition => {
    store.addAdditionToCart(adition)
    console.log(adition)
  })

  selectedAdditions.value = {}; // Resetear las adiciones seleccionadas


  store.setVisible('currentProduct', false)
};

const adicionales = ref([])
const store = usecartStore()

const checkedAdition = ref({})



const salsas = ref()
const cambios = ref()
const route = useRoute();
// const adicionales = ref()
const toppings = ref()
const acompanantes = ref()


onMounted(async () => {
  const product_id = await store.currentProduct.id


  if (product_id) {
    adicionales.value = await adicionalesService.getAditional(product_id)
  }
})


watch(() => store.currentProduct, async () => {
  const product_id = await store.currentProduct.id


  if (product_id) {
    adicionales.value = await adicionalesService.getAditional(product_id)
  }
})


watch(() => store.visibles.addAdditionToCart, async (new_val) => {
  if (!new_val) {
    selectedAdditions.value = {}
    adicionales.value = []
  } else {
    const product_id = await store.currentProduct.id
    if (product_id) {
      adicionales.value = await adicionalesService.getAditional(product_id)
    }
  }
}, { deep: true })




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

const isSmallScreen = computed(() => screenWidth.value < 768);





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




const getSalsas = async () => {
  if (!productDialog.value.grupo_salsa_id) {
    salsas.value = []
    return
  }
  try {
    let response = await fetch(`${URI}/grupo-salsas/${productDialog.value.grupo_salsa_id}/salsas`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    let data = await response.json();
    salsas.value = data;
  } catch (error) {
    console.error('Error fetching data: ', error);
  }
}

const getCambios = async () => {
  if (!productDialog.value.grupo_cambio_id) {
    cambios.value = []
    return
  }
  try {
    let response = await fetch(`${URI}/grupo-cambios/${productDialog.value.grupo_cambio_id}/cambios`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    let data = await response.json();
    cambios.value = data;
  } catch (error) {
    console.error('Error fetching data: ', error);
  }
}




const getToppings = async () => {
  if (!productDialog.value.grupo_topping_id) {
    toppings.value = []
    return
  }
  try {
    let response = await fetch(`${URI}/grupo-toppings/${productDialog.value.grupo_topping_id}/toppings`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    let data = await response.json();
    toppings.value = data;
  } catch (error) {
    console.error('Error fetching data: ', error);
  }
}


const getAcompanantes = async () => {
  if (!productDialog.value.grupo_acompanante_id) {
    toppings.value = []
    return
  }
  try {
    let response = await fetch(`${URI}/grupo-acompanantes/${productDialog.value.grupo_acompanante_id}/acompanantes`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    let data = await response.json();
    acompanantes.value = data;
    // alert(response)
  } catch (error) {
    console.error('Error fetching data: ', error);
  }
}


const getAdiciones = async () => {
  if (!productDialog.value.grupo_adicional_id) {
    adicionales.value = []
    return
  }
  try {
    let response = await fetch(`${URI}/grupo-adicionales/${productDialog.value.grupo_adicional_id}/adicionales`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    let data = await response.json();
    adicionales.value = data;
  } catch (error) {
    console.error('Error fetching data: ', error);
  }
}






















const c_neigbor = ref(localStorage.getItem('currentNeigborhood'))

onMounted(() => {

  getToppings()
  getSalsas()
  getCambios()
  getAdiciones()
  getAcompanantes()
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

  if (localStorage.getItem('menu') && localStorage.getItem('versionMenu') && parseFloat(localStorage.getItem('versionMenu')) == version_menu.value) {
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

const addcar = (product) => {

  const estado = localStorage.getItem('estado')
  if (estado && estado == 'cerrado') {
    verCerrado.value = true
    return
  }

  showProductDialog.value = !showProductDialog.value

  const product_new = { ...product }

  product_new.price = product_new.price
  product_new.salsas = currentSalsas.value
  product_new.adiciones = currentAditions.value
  product_new.toppings = currentToppings.value
  product_new.cambios = currentCambios.value
  product_new.acompanantes = currentAcompanantes.value

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

watch(showProductDialog, (newval, oldval) => {

  currentAcompanantes.value = []
  currentToppings.value = []
  currentAditions.value = []
  currentSalsas.value = []
  currentCambios.value = []

  cambios.value = []
  salsas.value = []
  // acompanantes.value = []
  toppings.value = []
  adicionales.value = []
  acompanantes.value = []

  getToppings()
  getSalsas()
  getCambios()
  getAdiciones()
  getAcompanantes()


})
const setNeigborhood = () => {
  localStorage.setItem('currentNeigborhood', JSON.stringify({
    currenCity: currenCity.value.name,
    currenNeigborhood: currenNeigborhood.value.neigborhood,
    currenSite: currenNeigborhood.value.site.name,
    currenSiteId: currenNeigborhood.value.site.site_id,
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





const cargarAdiciones = (item, gratis = 0) => {


  // Asegúrate de que checkedAdiciones y currentAditions estén definidos en el ámbito adecuado

  const negativePriceCount = currentAcompanantes.value.filter((el) => el.price <= 0).length;



  if (checkedAdiciones.value[item.name]) {

    if (negativePriceCount >= gratis && item.price == 0) {
      checkedAdiciones.value[item.name] = false
      console.log('ya')

      toast.add({ severity: 'error', summary: 'Recuerda', detail: `solo puede elegir ${gratis} acompanantes gratis`, life: 3000 });

      // Si ya hay dos o más objetos con price < 0, no hacer nada y retornar
      return;

    }
    // Si el checkbox está marcado, agregar el elemento a la lista
    if (item.adicional_id) {
      currentAditions.value.push(item);
    } else if (item.cambio_id) {
      currentCambios.value.push(item);
    } else if (item.topping_id) {
      currentToppings.value.push(item);
    } else if (item.acompanante_id) {
      console.log('here')
      currentAcompanantes.value.push(item);
      console.log(item)
      console.log(currentAcompanantes)
    }

    // console.log(item.acompanante_id)


  } else if (item.adicional_id) {
    // Si el checkbox está desmarcado, quitar el elemento de la lista
    const index = currentAditions.value.findIndex((el) => el.name === item.name);
    if (index !== -1) {
      currentAditions.value.splice(index, 1);
    }
  } else if (item.cambio_id) {
    // Si el checkbox está desmarcado, quitar el elemento de la lista
    const index = currentCambios.value.findIndex((el) => el.name === item.name);
    if (index !== -1) {
      currentCambios.value.splice(index, 1);
    }
  } else if (item.topping_id) {
    // Si el checkbox está desmarcado, quitar el elemento de la lista
    const index = currentToppings.value.findIndex((el) => el.name === item.name);
    if (index !== -1) {
      currentToppings.value.splice(index, 1);
    }
  } else if (item.acompanante_id) {
    // Si el checkbox está desmarcado, quitar el elemento de la lista
    const index = currentAcompanantes.value.findIndex((el) => el.name === item.name);
    if (index !== -1) {
      currentAcompanantes.value.splice(index, 1);
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








<style scoped>

@keyframes fadeIn {
    from {
       opacity: 0;
        transform: translateX(-100px);
        /* transform: scale(.5); */
        /* background-color: rgb(255, 255, 0); */
        /* filter: blur(1px); */
    }
    to {
        opacity: 1;
        /* filter: blur(1px); */

    }
}

.cargado {
    opacity: 0; /* Inicialmente invisible */
    animation: fadeIn .1s ease-out forwards; /* Duración de 1 segundo, 'ease-out' para desacelerar hacia el final, y 'forwards' para mantener el estado final visible */
}





@keyframes fadeIn {
    from {
       opacity: 0;
        transform: translateY(-100px);
        /* transform: scale(.5); */
        /* background-color: rgb(255, 255, 0); */
        /* filter: blur(1px); */
    }
    to {
        opacity: 1;
        /* filter: blur(1px); */

    }
}



@keyframes fadeInLeftHand {
    from {
       opacity: 0;
        transform: translateX(-1000px);
        /* transform: scale(.5); */
        /* background-color: rgb(255, 255, 0); */
        /* filter: blur(1px); */
    }
    to {
        opacity: 1;
        /* filter: blur(1px); */

    }
}

.cargado-left-hand {
    opacity: 0; /* Inicialmente invisible */
    animation: fadeInLeftHand .1s ease-out forwards; /* Duración de 1 segundo, 'ease-out' para desacelerar hacia el final, y 'forwards' para mantener el estado final visible */
}




@keyframes fadeInRightHand {
    from {
       opacity: 0;
        transform: translateX(1000px);
        /* transform: scale(.5); */
        /* background-color: rgb(255, 255, 0); */
        /* filter: blur(1px); */
    }
    to {
        opacity: 1;
        /* filter: blur(1px); */

    }
}

.cargado-right-hand {
    opacity: 0; /* Inicialmente invisible */
    animation: fadeInRightHand .1s ease-out forwards; /* Duración de 1 segundo, 'ease-out' para desacelerar hacia el final, y 'forwards' para mantener el estado final visible */
}









*::-webkit-scrollbar {
  overflow-y: auto;
  display: none;
  /* oculta la barra de desplazamiento en navegadores basados en WebKit/Blink */
}

/* .scroll{
  overflow-y: auto;
} */

.adicion::first-letter {
  text-transform: uppercase;
}

.mayuscula {
  text-transform: uppercase;
}</style>