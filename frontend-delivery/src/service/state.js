import { ref } from "vue";


function sumarAdiciones(adiciones) {
  let suma = 0;

  for (let i = 0; i < adiciones.length; i++) {
      suma += adiciones[i].price;
  }

  return suma;
}

function contarObjetosRepetidos(arr) {
  const objetoContador = {};

  // Contar la cantidad de veces que se repite cada objeto por su nombre "producto"
  arr.forEach((objeto) => {
      const id = objeto.id;
      if (objetoContador[id]) {
          objetoContador[id].quantity++;
      } else {
          objetoContador[id] = {
              product: objeto,
              quantity: 1
          };
      }
  });

  // Crear un nuevo array con los resultados
  const resultado = Object.values(objetoContador).map((item) => item);

  return resultado;
}

function calcularPrecioTotal(producto) {
  // Verificar si el producto tiene un precio base y adiciones
  if (producto.price ) {
      // Calcular la suma de los precios de las adiciones
      const sumaAdiciones = sumarAdiciones(producto.adiciones)

      // Calcular el precio total sumando el precio base y la suma de las adiciones
      const precioTotal = producto.price + sumaAdiciones;

      // Devolver el precio total
      return precioTotal;
      
  } else {
      // Devolver el precio base si el producto no tiene un precio base o adiciones
      return producto.price || 0;
  }
}


function calcularTotalCarrito(carrito) {
  let totalCarrito = 0;

  for (const producto of carrito.order_products) {
    totalCarrito += calcularPrecioTotal(producto);
  }

  return totalCarrito;
}



// const setShowDialog =()=>{
//   currentAditions.value=[]
//   currentSalsas.value=[]
  
//     showSiteDialog.value = !showSiteDialog.value
//     console.log('hola')
//     if (showProductDialog.value) {

       
//     }
//   }

  // const setProductDialog =(product)=>{
  //   checkedAdiciones.value = []
  //     checkedSalsas.value = []
  //     currentAditions.value = []
  //     currentAditions.value = []
  //   showProductDialog.value = !showProductDialog.value

  //   console.log('hola')
  //   if (product) {
  //     productDialog.value = product


  //   }
  // }



export {calcularTotalCarrito,calcularPrecioTotal,contarObjetosRepetidos}