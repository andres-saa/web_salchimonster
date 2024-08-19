import { onMounted, ref } from "vue";
import { calcularPrecioTotal } from "./state";
import {URI} from '@/service/conection.js'

const carro_para_la_barra_de_abajo = ref({products:[],total:0})
import { calcularTotalCarrito } from "./state";

const products = ref([])
const quantity = ref(0);

const add = (product) => {
    try {
      // Check if 'cart' exists in localStorage
      if (!localStorage.getItem('cart')) {
        localStorage.setItem('cart', JSON.stringify({ products: [], total: 0 }));
      }
  
      // Parse the existing cart data from localStorage
      const cart = { ...JSON.parse(localStorage.getItem('cart')) };
  
      // Add the new product to the cart
      cart.products.push(product);
      carro_para_la_barra_de_abajo.value.products = cart.products
  
      // Update the total
    //   cart.total = Number(cart.total) + product.price;
  
      // Save the updated cart back to localStorage
      localStorage.setItem('cart', JSON.stringify(cart));
  
      // Update the value of 'carro'
    //   carro.value = cart;
  
      // Call the updateCart function (assuming it's defined elsewhere)
      updateCart();
  
    } catch (error) {
      console.error('Error updating cart:', error);
      // Handle the error as needed, for example, show an error message to the user.
    }
      updateCart();
  };


function deleteAllCookies() {
    const cookies = document.cookie.split(';');

    cookies.forEach(cookie => {
        const [name] = cookie.split('=');
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    });
}

function quitarElementos(array, elementosAEliminar) {
    console.log('array', array);
    console.log('elementosAEliminar', elementosAEliminar);
  
    return array.filter(product => !elementosAEliminar.some(el => el.id === product.id));
  }

  function quitarSalsas(array, elementosAEliminar) {
    console.log('array', array);
    console.log('elementosAEliminar', elementosAEliminar);
  
    return array.filter(product => !elementosAEliminar.some(el => el === product));
  }

  

const remove = (productToRemove) => {
    if (localStorage.getItem('cart')) {
        const cart = { ...JSON.parse(localStorage.getItem('cart')) };
        const indexToRemove = cart.products.findIndex((product) => {
            updateCart()
            return product.name === productToRemove.name && product.price === productToRemove.price;
        });

        if (indexToRemove !== -1) {
            const removedProduct = cart.products.splice(indexToRemove, 1)[0];
            cart.total = Number(cart.total) - removedProduct.price;
            localStorage.setItem('cart', JSON.stringify(cart));
            carro_para_la_barra_de_abajo.value = cart;
            console.log(localStorage.getItem('cart'));
            updateCart()
        }
    }
}



const useCart = {
    add,
    remove
}

const domicilio = ref()





onMounted( async() => {

    let barrio = {}

    if (localStorage.getItem('currentNeigborhood')){
        barrio = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood
        getNeighborhood(barrio.neighborhood_id).then(data => domicilio.value = data)

    }else{
        barrio = 'definir domicilio'
    } 

    
})


const getNeighborhood = async(neighborhood_id) => {
    try {
        const response = await fetch(`${URI}/neighborhood/${neighborhood_id}`)
        if (!response.ok){
            console.log('paila')
        } else{
            data = await response.json()
            return data
        }



    } catch (error) {
        
    }
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



const updateCart = () =>{
    products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
    // domicilio.value = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood.deliveryPrice
    
    // carro_para_la_barra_de_abajo.value.products = products.value

    const cartDataString = localStorage.getItem('cart');

    // Check if 'cart' exists and is not null or undefined
    if (cartDataString) {
        // Attempt to parse the 'cart' data
        const cartData = JSON.parse(cartDataString);
    
        // Check if 'cart' has 'products' attribute
        const productsLength = cartData.products ? cartData.products.length : 0;
    
        // Assign the calculated quantity to the 'quantity' variable
       quantity.value = productsLength;
    
        // Now 'quantity' contains the calculated value, either the length of 'products' or 0 if 'products' is missing
    } else {
        // 'cart' is not present in localStorage, set quantity to 0 or handle it as needed
       quantity.value = 0;
    }
}

function eliminarAdicionDelCarrito(adicionAEliminar, producto) {

    // Obtener el carrito actual desde el localStorage
    const carritoEnLocalStorage = JSON.parse(localStorage.getItem('cart')) || { products: [], total: 0 };

    // Verificar si el carrito tiene productos y la propiedad "adiciones"
    if (carritoEnLocalStorage.products) {
        // Encontrar el producto en el carrito
        const productoEnCarrito = carritoEnLocalStorage.products.find(p => p.id === producto.id);

        // Verificar si se encontró el producto y tiene la propiedad "adiciones"
        if (productoEnCarrito && productoEnCarrito.adiciones) {
            // Filtrar las adiciones del producto para excluir la adición especificada
            productoEnCarrito.adiciones = productoEnCarrito.adiciones.filter(adicion => adicion.id !== adicionAEliminar.id);

            // Actualizar el localStorage con el carrito modificado
            localStorage.setItem('cart', JSON.stringify(carritoEnLocalStorage));

            // Devolver el carrito modificado
            carro_para_la_barra_de_abajo.value = carritoEnLocalStorage
            updateCart()

            return carritoEnLocalStorage;
        }
    }

    // Devolver el carrito original si no se encuentra el producto o la propiedad "adiciones"
    updateCart()
    return carritoEnLocalStorage;
}

function eliminarSalsaDelCarrito(salsaAEliminar, producto) {

    // Obtener el carrito actual desde el localStorage
    const carritoEnLocalStorage = JSON.parse(localStorage.getItem('cart')) || { products: [], total: 0 };

    // Verificar si el carrito tiene productos y la propiedad "adiciones"
    if (carritoEnLocalStorage.products) {
        // Encontrar el producto en el carrito
        const productoEnCarrito = carritoEnLocalStorage.products.find(p => p.id === producto.id);

        // Verificar si se encontró el producto y tiene la propiedad "adiciones"
        if (productoEnCarrito && productoEnCarrito.salsas) {
            // Filtrar las adiciones del producto para excluir la adición especificada
            productoEnCarrito.salsas = productoEnCarrito.salsas.filter(salsa => salsa !== salsaAEliminar);

            // Actualizar el localStorage con el carrito modificado
            localStorage.setItem('cart', JSON.stringify(carritoEnLocalStorage));

            // Devolver el carrito modificado
            carro_para_la_barra_de_abajo.value = carritoEnLocalStorage
            updateCart()

            return carritoEnLocalStorage;
        }
    }

    // Devolver el carrito original si no se encuentra el producto o la propiedad "adiciones"
    updateCart()
    return carritoEnLocalStorage;
}

function agregarAdicionAlCarrito(adicionAAgregar, producto) {
    // Obtener el carrito actual desde el localStorage
    const carritoEnLocalStorage = JSON.parse(localStorage.getItem('cart')) || { products: [], total: 0 };
  
    // Verificar si el carrito tiene productos y la propiedad "adiciones"
    if (carritoEnLocalStorage.products) {
      // Encontrar el producto en el carrito
      const productoEnCarrito = carritoEnLocalStorage.products.find(p => p.id === producto.id);
  
      // Verificar si se encontró el producto y tiene la propiedad "adiciones"
      if (productoEnCarrito && productoEnCarrito.adiciones) {
        // Verificar la cantidad de adiciones gratis permitidas
        const gratis = 2; // Ajusta este valor según tus necesidades
        const negativePriceCount = productoEnCarrito.adiciones.filter(adicion => adicion.price <= 0).length;
  
        if (negativePriceCount >= gratis && adicionAAgregar.price <= 0) {
          console.log('ya');
          toast.add({ severity: 'error', summary: 'Recuerda', detail: `solo puede elegir ${gratis} acompañantes gratis`, life: 3000 });
          // Devolver el carrito sin cambios si se excede la cantidad de adiciones gratis
          updateCart();
          return carritoEnLocalStorage;
        }
  
        // Verificar si la adición ya existe en el producto
        const adicionExistente = productoEnCarrito.adiciones.find(adicion => adicion.id === adicionAAgregar.id);
  
        if (!adicionExistente) {
          // Agregar la nueva adición al producto
          productoEnCarrito.adiciones.push(adicionAAgregar);
  
          // Actualizar el localStorage con el carrito modificado
          localStorage.setItem('cart', JSON.stringify(carritoEnLocalStorage));
  
          // Devolver el carrito modificado
          carro_para_la_barra_de_abajo.value = carritoEnLocalStorage;
          updateCart();
  
          return carritoEnLocalStorage;
        } else {
          // Devolver el carrito sin cambios si la adición ya existe
          updateCart();
          return carritoEnLocalStorage;
        }
      }
    }
  
    // Devolver el carrito original si no se encuentra el producto o la propiedad "adiciones"
    updateCart();
    return carritoEnLocalStorage;
  }
  


function agregarSalsasAlCarrito(salsaAAgregar, producto) {
    // Obtener el carrito actual desde el localStorage

    if(producto.salsas[0] == 'TODAS LAS SALSAS'){
        return
    }
    const carritoEnLocalStorage = JSON.parse(localStorage.getItem('cart')) || { products: [], total: 0 };

    // Verificar si el carrito tiene productos y la propiedad "adiciones"
    if (carritoEnLocalStorage.products) {
        // Encontrar el producto en el carrito
        const productoEnCarrito = carritoEnLocalStorage.products.find(p => p.id === producto.id);

        // Verificar si se encontró el producto y tiene la propiedad "adiciones"
        if (productoEnCarrito && productoEnCarrito.salsas) {
            // Verificar si la adición ya existe en el producto
            const salsasExistentes = productoEnCarrito.salsas.find(salsa => salsa === salsaAAgregar);

            if (!salsasExistentes) {
                // Agregar la nueva adición al producto
                
                if (salsaAAgregar == 'TODAS LAS SALSAS'){
                    productoEnCarrito.salsas =[]
                    productoEnCarrito.salsas.push(salsaAAgregar);
                }else{
                    productoEnCarrito.salsas.push(salsaAAgregar);
                }

                // Actualizar el localStorage con el carrito modificado
                localStorage.setItem('cart', JSON.stringify(carritoEnLocalStorage));

                // Devolver el carrito modificado
                carro_para_la_barra_de_abajo.value = carritoEnLocalStorage;
                updateCart();

                return carritoEnLocalStorage;
            } else {
                // Devolver el carrito sin cambios si la adición ya existe
                updateCart();
                return carritoEnLocalStorage;
            }
        }
    }

    // Devolver el carrito original si no se encuentra el producto o la propiedad "adiciones"
    updateCart();
    return carritoEnLocalStorage;
}







export {deleteAllCookies, quitarSalsas, eliminarSalsaDelCarrito,agregarSalsasAlCarrito,domicilio, quantity,useCart,carro_para_la_barra_de_abajo,eliminarAdicionDelCarrito,products,updateCart,contarObjetosRepetidos,quitarElementos,agregarAdicionAlCarrito}