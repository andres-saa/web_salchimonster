<template>
    <div class="cont p-4" style="background-color: white; height: 100%;position: relative"  >
        <!-- <router-link :to="`product/${props.product.id}` " @click="changeProduct(product)"> -->

            <button style="position: absolute;top: -1rem;right: -1rem;background-color:var(--primary-color); width: 2.5rem;height: 2.5rem;border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white;z-index: 99;" @click="prepararParaEditar" class="add-cart-btn text-xl"><i   class="icono text-2xl  p-0 m-0 " :class="PrimeIcons.PENCIL"> </i>  </button>

            

            <button  style="position: absolute;top: -1rem;right: 2rem;background-color:var(--red-500); width: 2.5rem;height: 2.5rem;border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white;z-index: 99;" @click="pregpararParaEliminar" class="add-cart-btn text-xl"><i  class="icono text-2xl  p-0 m-0 " :class="PrimeIcons.TRASH"> </i>  </button>


            <div class="imagen-cont " style="position: ;" @click="setProductDialog(product)">
                <!-- <img class="imagen" @error="imagenError" :src="`${URI}/read_product_image/300/${props.product.id}`" alt=""> -->
                <img class="imagen" @error="imagenError" style="height: 50;" :src="`${URI}/read-product-image/300/${props.product.name}`" alt="">
                
            
            </div>
           

        <!-- </router-link> -->
        <!-- <img class="imagen" src="src/images/iconos menu/salchipapa-icono.png" alt=""> -->

        
            <div style=" display: ; " >
                <p class="nombre-producto mt-4 " style="font-weight: bold;" > {{ props.product.name }}</p>
                <p class="descripcion-producto mt-2 text-sm mb-4" > {{ props.product.description }}</p>
                
            </div>

            
            <Toast style="box-shadow: none;"  />
       

        <div class="info " >
            <!-- {{ showEditarProducto }} -->
            
            <div class="text-l" style="font-weight: bold; "> {{ formatoPesosColombianos(props.product.price) }}</div>

            <InputSwitch class="p-0 m-0" v-model="isActive" @change="updateProductState" style=""/>

        </div> 


        
    </div>


    <!-- {{ productoAEditar }} -->







    <!-- <dialogoEditarProducto></dialogoEditarProducto> -->
</template>

<script setup>
import { PrimeIcons } from 'primevue/api';
import { changeProduct } from '../service/productServices';
import {URI} from '@/service/conection'
import {useCart} from '@/service/cart'
import { menuGlobal } from '../service/menu/menu';
import  {formatoPesosColombianos} from '../service/formatoPesos'
import { check_site, setProductDialog,showProductDialog } from '../service/state';
import { useToast } from 'primevue/usetoast';
import { comprobar_sede } from '../service/state';
import dialogoAgregarProducto from './dialogos/dialogoAgregarProducto.vue';
import { productoAEliminar, showEditarProducto, showEliminarProducto } from '../service/valoresReactivosCompartidos';
import dialogoEditarProducto from './dialogos/dialogoEditarProducto.vue';
import { onMounted, ref, watch } from 'vue';
import { productoAEditar } from '../service/valoresReactivosCompartidos';
const toast = useToast();
const isActive = ref(false);


const prepararParaEditar = () => {
    showEditarProducto.value = !showEditarProducto.value
    productoAEditar.value = props.product
}
const displayConfirmation = ref(false)


const isInitialWatchCall = ref(true)


// watch(isActive, (newValue) => {

//     if (isInitialWatchCall.value) {
//         isInitialWatchCall.value = false;
//         return;
//     }

//     // Tu lógica aquí, se ejecutará solo en cambios después del montaje
//     updateProductState();
// });

onMounted(async () => {
    isActive.value = props.product.state == 'active';
});


const pregpararParaEliminar = () => {
    
    showEliminarProducto.value = !showEliminarProducto.value
    productoAEliminar.value = props.product
}

const updateProductState = () => {

    const data = {...props.product}    
    data.state = isActive.value? 'active': 'inactive'
    // console.log(data)

    fetch(`${URI}/products/${props.product.product_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        toast.add({ severity: `${!isActive.value? 'error':'success'}`, summary: `${!isActive.value? 'Desactivado':'Activado'}`, detail: props.product.name, life: 3000 });

        return response.json();
    })
    .then(data => {
        // Manejar la respuesta (puedes mostrar un mensaje de éxito, por ejemplo)
    })
    .catch(error => {
        console.error('Error al actualizar el producto:', error);
    });
};
















const prepare_product = (product) => {
    product.adiciones = []
    product.salsas =[]

    return product

}
const props = defineProps({
    product: {
        type: Object,
        default: {}
    },


});

const addcar =(product) => {

    comprobar_sede()
    useCart.add(product)  
    // check_site()
}


const imagenError = (Event) => {
    Event.target.src = 'https://salchimonster.com/images/logo.png'
}

</script>

<style scoped>
.info {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    /* background-attachment: fixed; */
    /* position: absolute; */

    
    /* gap: 20px; */
 
    /* padding: 20px; */
}




.nombre-producto,.descripcion-producto{
    text-transform: lowercase;
}

.nombre-producto,.descripcion-producto::first-letter{
    text-transform: uppercase;
}

.descripcion-producto{
overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* Number of lines you want to display */
  -webkit-box-orient: vertical;
  max-height: 4.5em; /* Adjust based on line-height and number of lines */
  line-height: 1.5em;
}

.add-cart-btn{
    /* transition: all  0.2s ease; */
    border-radius: 50%;
    border: none;
    /* height: 3rem; */
    /* width: 3rem; */
    /* display: flex; */
    /* align-items: center; */
    /* justify-content: center; */

    /* padding: 1rem 1rem; */
    font-size: 20px;
    background-color: rgba(251, 0, 0, 0);
    /* border-radius: 10px; */
    color: #ff0000;
}

.add-cart-btn .icono{

    color: #fff;
}




*:focus{
    outline: none;
}

.icono{
    /* transition: all  0.2s ease; */
    color: var(--primary-color);
    /* transform: translateX(-15px); */
    font-weight: bold;
}
.cont {
    /* border: 1px solid gray; */
    border-radius: 1rem;
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.3);
    /* margin: 20px; */
    /* height: max-content; */
    /* width: 100%; */
    /* padding: 5%; */
    /* min-height: 100%; */
    /* max-height: 100%; */
    /* padding-bottom: 6rem;     */
    position: relative;
    margin: 0;


    /* margin: 0px; */
    /* width: 90%; */
    /* width: 100%; display: flex; */
    /* margin: auto; */

    /* height: 100%; */
    /* max-height: ; */
    /* background-color: red; */
    /* margin:1rem; */
}
/* .cont:hover .imagen{
    filter: brightness(1);
    transform: scale(1.1) rotate(3deg); */
    /* filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 123, 0)); */
    /* filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(0, 0, 0)); */


.cont:hover .add-cart-btn{
    
    /* transform: translateY(-10px); */
}
.imagen:hover {
    filter: brightness(1.1);
    /* box-shadow: 0px 0px 30px var(--primary-color); */
    /* background-color: #ff620035; */
}
.imagen{
    width: 100%;
    object-fit: contain;
    height: 200px;
    transition: transform ease .3s ;;
 
    /* background-image: url('https://i.ytimg.com/vi/yvIhfmAfsck/maxresdefault.jpg'); */
    /* height: 100%; */
    /* background-color: red; */
    /* filter: brightness(1.1) drop-shadow(2px 2px 10px rgb(255, 123, 0)); */
}

.imagen-cont{
    /* width: 100%; */
    overflow: hidden;
    border-radius:0.5rem;
    /* height: max-content; */
    /* background-color: green; */

}

button{
    cursor: pointer;
}
</style>