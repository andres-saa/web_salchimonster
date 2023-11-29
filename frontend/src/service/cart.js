import { ref } from "vue";
import { calcularPrecioTotal } from "./state";


const carro = ref({products:[],total:0})
import { calcularTotalCarrito } from "./state";

const products = ref([])
const quantity = ref(0);
const add = (product) => {

    if (!localStorage.getItem('cart')){
        localStorage.setItem('cart',{products:[],total:0})
        // localStorage.setItem('totalCart',0)
    }
    const cart = {...JSON.parse(localStorage.getItem('cart'))}
    // const cart = {products:[],total:0}
    // localStorage.setItem('cart',JSON.stringify(cart.value))
    // console.log(JSON.parse(localStorage.getItem('cart')))
    cart.products.push(product)
    cart.total = Number(cart.total)+product.price
    localStorage.setItem('cart',JSON.stringify(cart))
    carro.value = cart
    updateCart()
    // console.log(localStorage.getItem('cart'))
}


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
            carro.value = cart;
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

if (localStorage.getItem('currentNeigborhood')){
    domicilio.value = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood
}else{
    domicilio.value = 'definir domicilio'
}


function contarObjetosRepetidos(arr) {
    const objetoContador = {};

    // Contar la cantidad de veces que se repite cada objeto por su nombre "producto"
    arr.forEach((objeto) => {
        const nombre = objeto.name;
        if (objetoContador[nombre]) {
            objetoContador[nombre].quantity++;
        } else {
            objetoContador[nombre] = {
                product: objeto,
                quantity: 1
            };
        }
    });

    // Crear un nuevo array con los resultados
    const resultado = Object.values(objetoContador).map((item) => item);

    return resultado;
}

const updateCart = () =>{
    products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
    // domicilio.value = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood.deliveryPrice
    
    

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
            carro.value = carritoEnLocalStorage
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
            carro.value = carritoEnLocalStorage
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
            // Verificar si la adición ya existe en el producto
            const adicionExistente = productoEnCarrito.adiciones.find(adicion => adicion.id === adicionAAgregar.id);

            if (!adicionExistente) {
                // Agregar la nueva adición al producto
                productoEnCarrito.adiciones.push(adicionAAgregar);

                // Actualizar el localStorage con el carrito modificado
                localStorage.setItem('cart', JSON.stringify(carritoEnLocalStorage));

                // Devolver el carrito modificado
                carro.value = carritoEnLocalStorage;
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
                carro.value = carritoEnLocalStorage;
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







export {deleteAllCookies, quitarSalsas, eliminarSalsaDelCarrito,agregarSalsasAlCarrito,domicilio, quantity,useCart,carro,eliminarAdicionDelCarrito,products,updateCart,contarObjetosRepetidos,quitarElementos,agregarAdicionAlCarrito}