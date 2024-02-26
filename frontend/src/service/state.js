import { ref } from "vue";
import { adiciones } from "./menu/adiciones/adiciones";
import { useRouter } from "vue-router";
import router from '@/router/index.js'
const showProductDialog = ref(false)
const showSiteDialog = ref(false)
const productDialog = ref({})
const checkedSalsas = ref({ })
const checkedAdiciones = ref({ })
const checkedAcomp = ref({ })
import {carro_para_la_barra_de_abajo } from "./cart";
const antojoVisible = ref(false)

const currentAditions=ref([]);
const currentCambios=ref([]);
const currentToppings=ref([]);
const currentSalsas=ref([]);
const currentAcompanantes=ref([]);
const verCerrado = ref(false)

const ruta = ref(router.currentRoute)

            



function sumarAdiciones(adiciones) {
  let suma = 0;

  if(!adiciones?.length) {
    return 0
  }
  for (let i = 0; i < adiciones.length; i++) {
      suma += adiciones[i].price;
  }

  return suma;
}



function calcularPrecioTotal(producto) {
  // Verificar si el producto tiene un precio base y adiciones
  if (producto.price ) {
      // Calcular la suma de los precios de las adiciones
      const sumaAdiciones = sumarAdiciones(producto.adiciones)
      const sumaCambios = sumarAdiciones(producto.cambios)
      const sumaAcompanantes = sumarAdiciones(producto.acompanantes)
      const sumaToppings = sumarAdiciones(producto.toppings)

      // Calcular el precio total sumando el precio base y la suma de las adiciones
      const precioTotal = producto.price + sumaAdiciones + sumaAcompanantes + sumaCambios + sumaToppings ;

      // Devolver el precio total
      return precioTotal;
      
  } else {
      // Devolver el precio base si el producto no tiene un precio base o adiciones
      return producto.price || 0;
  }
}


const subtotal  = ref()

function calcularTotalCarrito() {
  let totalCarrito = 0;

  for (const producto of carro_para_la_barra_de_abajo.value.products) {
    totalCarrito += calcularPrecioTotal(producto);
  }

  subtotal.value = totalCarrito
  return totalCarrito;
 
}

const c_neigbor = ref(localStorage.getItem('currentNeigborhood'))

const check_site = () => {
  if (!c_neigbor.value && ruta.fullPath == '/menu' ) {
    showSiteDialog.value = true
  }
}

const setShowDialog =()=>{
  currentAditions.value=[]
  currentSalsas.value=[]
  
    showSiteDialog.value = true
    console.log('hola')
    if (showProductDialog.value) {

      // location.reload()
    }
    
  }

  const setProductDialog =(product)=>{
    checkedAdiciones.value = []
      checkedSalsas.value = []
      currentAditions.value = []
      currentAditions.value = []
    showProductDialog.value = !showProductDialog.value

    console.log('hola')
    if (product) {
      productDialog.value = product


    }
  }


const comprobar_sede = () => {
  const c_neigbor = ref(localStorage.getItem('currentNeigborhood'))

  if (ruta.value.fullPath == '/menu' || ruta.value.fullPath == '/sedes'   ) {
    showSiteDialog.value = false
  }

  if (!c_neigbor.value && ruta.value.fullPath != '/menu' ) {
    showSiteDialog.value = true
  }
}

const comprobarEstado = () => {
  const estado = localStorage.getItem('estado')
    if(estado && estado=='cerrado'){
        // verCerrado.value = true
        // return null
    }
}

export {antojoVisible,currentCambios, currentToppings, currentAcompanantes, subtotal,verCerrado,comprobarEstado, comprobar_sede, check_site,checkedAcomp,calcularTotalCarrito,calcularPrecioTotal,sumarAdiciones, showSiteDialog,setShowDialog,showProductDialog,setProductDialog,productDialog,checkedSalsas,checkedAdiciones,currentAditions,currentSalsas}