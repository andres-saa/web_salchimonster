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

  // Contar la cantidad de veces que se repite cada objeto por su nombre "producto", adiciones, salsas, toppings y acompanantes
  arr.forEach((objeto) => {
      const nombre = objeto.name;
      const adiciones = JSON.stringify(objeto.adiciones); // Convertir adiciones a cadena para comparar
      const salsas = JSON.stringify(objeto.salsas); // Convertir salsas a cadena para comparar
      const toppings = JSON.stringify(objeto.toppings); // Convertir toppings a cadena para comparar
      const acompanantes = JSON.stringify(objeto.acompanantes); // Convertir acompanantes a cadena para comparar

      // Crear una clave única incluyendo salsas, adiciones, toppings y acompanantes
      const clave = `${nombre}-${adiciones}-${salsas}-${toppings}-${acompanantes}`;

      if (objetoContador[clave]) {
          objetoContador[clave].quantity++;
      } else {
          objetoContador[clave] = {
              product: objeto,
              quantity: 1
          };
      }
  });
  
  // Retornar el array de resultados
  return Object.values(objetoContador);
}


function calcularPrecioTotal(producto) {
  // Verificar si el producto tiene un precio base
  if (!producto.price) {
    return 0;
  }

  // Función para sumar los precios de las adiciones si existen
  function sumarAdiciones(adiciones) {
    if (!adiciones || !Array.isArray(adiciones)) {
      return 0;
    }
    return adiciones.reduce((suma, adicion) => suma + (adicion.price || 0), 0);
  }

  // Calcular la suma de los precios de las adiciones, cambios, toppings y acompañantes
  const sumaAdiciones = sumarAdiciones(producto.adiciones);
  const sumaCambios = sumarAdiciones(producto.cambios);
  const sumaToppins = sumarAdiciones(producto.toppings);
  const sumaAcompanantes = sumarAdiciones(producto.acompanantes);  // Corregido: de sumaAcompanantes a acompanantes

  // Calcular el precio total sumando el precio base y la suma de las adiciones
  const precioTotal = producto.price + sumaAdiciones + sumaCambios + sumaToppins + sumaAcompanantes;

  // Devolver el precio total
  return precioTotal;
}


function totalOrden(listaProductos) {
  // Verificar si la lista de productos está definida y es un arreglo
  if (!Array.isArray(listaProductos)) {
    return 0;
  }

  // Calcular el precio total para cada producto y sumarlos
  return listaProductos.reduce((total, producto) => {
    return total + calcularPrecioTotal(producto);
  }, 0);
}


function calcularTotalCarrito(carrito) {
  let totalCarrito = 0;

  for (const producto of carrito.order_products) {
    totalCarrito += calcularPrecioTotal(producto);
    console.log( "precio producto",totalCarrito)
  }

  return totalCarrito;
}



const sumarAdicionesAlProducto = (product) => {

  let sumaAdicionesValue = 0


  for (const adicion of product.product.adiciones) {
    sumaAdicionesValue += adicion.price*product.quantity
  }

  return product.quantity * product.product.price + sumaAdicionesValue 

}

const sumarProductos = (productos) => {
  
  let sumaProductos = 0

  for (const product of productos) {
    sumaProductos += calcularPrecioTotal(product.product)
  }

  return sumaProductos
}


export {totalOrden, sumarProductos, sumarAdicionesAlProducto, calcularTotalCarrito,calcularPrecioTotal,contarObjetosRepetidos}