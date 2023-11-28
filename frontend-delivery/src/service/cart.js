import { ref } from "vue";
import { calcularPrecioTotal } from "./state";


const carro = ref({products:[],total:0})
import { calcularTotalCarrito } from "./state";

const products = ref([])

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


function quitarElementos(array, elementosAEliminar) {
    console.log('array', array);
    console.log('elementosAEliminar', elementosAEliminar);
  
    return array.filter(product => !elementosAEliminar.some(el => el.id === product.id));
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









const updateCart = () =>{
    products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
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
// Ejemplo de uso






export {useCart,carro,eliminarAdicionDelCarrito,products,updateCart,quitarElementos,agregarAdicionAlCarrito}