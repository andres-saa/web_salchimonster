<template style="" >
    <div class="  m-auto  grid lg:col-12     "
        style="; border-radius:20px; ; height: min-content; margin-bottom:30vh ; ">
   

        <div class=" xl:col  ml-4 "
            style=" display: flex; align-items: start; border-radius: 20px;background-color: ;   ">
            <div class=" info   " style=" ; ">

                <div class="info-header  text-4xl col">

                    <div class="title">
                        <p style="   font-weight: bold;">
                            {{ curentProduct.name }}
                        </p>
                    </div>

                    <p style="  font-weight: bold;">
                        {{ formatoPesosColombianos(curentProduct.price)  }}
                    </p>

                </div>

                <div class="title col-12 m-0 p-0" style="border-radius: 20px;">
                    <p style="   font-weight: bold; padding-top: 2rem;" class="text-4xl ">
                        Descripcion
                    </p>

                    <p class="text-xl pb-4">
                        {{ curentProduct.description }}

                    </p>


                    <div class=" col-12  pb-8 "
                        style="background-color: rgba(255, 98, 0, 0.184);border-radius: 20px;overflow: hidden;">



                        <div v-if="curentProduct.category_id == 1 || curentProduct.category_id == 2" class="  salsas grid col-12  "  
                            style=" display: flex; flex-direction: column; overflow: hidden;" >
                            <div class="title col-12">
                                <p style="font-weight: bold; width:100%; overflow: hidden; display: flex; align-items: center; gap: 5%;
                                " class="text-4xl nombre-salsa ">
                                    SALSAS
                                    <span
                                        style="; width: 100%; overflow: hidden; border-top: 5px solid var(--primary-color)  ;  border-bottom: 5px  ;height: 1px; border-top-style:solid ; color: ;">
                                        <p></p>
                                    </span>

                                </p>

                            </div>

                            <div v-for="i in adiciones.salsas" class=" col-6 p-1 "
                                style="display: ;  justify-content: start; ; padding-bottom: 0.5rem; padding-left: 1rem;">

                                <div class="salsa "
                                    style=" margin: 0; padding: 0; display: flex; justify-content: start; align-items: center;">
                                    <p class="texto  " style="margin: 0; min-width: max-content"> {{ i }}
                                    </p>

                                    <span
                                        style="; width:100% ; overflow: hidden; border-top: 2px  ;  border-bottom: 5px  ;height: 1px; border-top-style: dotted; color:; margin-right:1rem ;">
                                        <p></p>
                                    </span>

                                    <Checkbox v-model="checked[i]" :binary="true" style="margin-right: 1rem; " />


                                </div>
                            </div>
                        </div>




                        <div class="  adiciones grid col-12 " v-if="curentProduct.category_id != 3">
                            <div class="title col-12" style="overflow: hidden;">
                                <p style="   font-weight: bold; width:100%; overflow: hidden; display: flex; align-items: center; gap: 5%;"
                                    class="text-4xl p-o">

                                    <span style="padding: 0;">
                                        {{curentProduct.category_id == 4? 'TOPINGS': "ADICIONES"}}
                                    </span>
                                    <span
                                        style="; width: 100%; overflow: hidden; border-top: 5px solid var(--primary-color)  ;  border-bottom: 5px  ;height: 1px; border-top-style:solid ; color: ;">
                                        <p></p>
                                    </span>


                                </p>
                            </div>

                  
                            <div class="grid col">

                                <div v-for="i in adiciones[curentProduct.category_id ==1? 'salchipapas': curentProduct.category_id ==2? 'hamburguesas':'topings'].products" class=" col-11 p-1  m-0  "
                                style="min-width:max-content ; padding-bottom: 0.5rem; padding-left:">
                                <div class="salsa col m-0 p-0" style=" align-items: center; justify-content: start; ">
                                    <div style="display: flex;">
                                        <Checkbox v-model="checked[i.name]" :binary="true" style="margin-right: 1rem; m " />

                                        <p  v-if="checked[i.name]" class="texto text m-0" style="color: var(--primary-color);width:max-content"> {{ i.name }}
                                        </p>

                                        <p v-else class="texto text m-0" style="width:max-content;"> {{ i.name }}
                                        </p>
                                        
                                    </div>

                                    <span
                                        style="; width:100% ; overflow: hidden; border-top: 2px  ;  border-bottom: 5px  ;height: 1px; border-top-style: dotted; color:; margin-right:1rem ;">
                                       
                                    </span>

                                    <p class="texto text m-0 " style="font-weight: bold; margin-left: ;">${{ i.price }}
                                    </p>

                        </div>
                       

                        </div>

                            </div>
                                



                        </div>



                        <div style="width: 100%; display: flex; justify-content: end;">
                                                    
  <button class="    ver-mas mt-4 cl-12 mr-4 "
                        style="  display: flex;
                        padding: 1rem;
                         background-color:var(--primary-color)  ; 
                         color: white; 
                         align-items: center; 
                         justify-content: end;
                         gap: 20px; width: max-content ;
                         background-color:;padding: 1%;
                         height: auto;"
                         @click="useCart.add(curentProduct)"


                        >

                        <i style="font-size: 20px;color: white; " class="icono" :class="PrimeIcons.SHOPPING_CART "> </i>
                   
                        
                        <span style=" background-color: var();" >
                            Agregar al carrito
                        </span>
                    </button>
                        </div>


                    </div>



                </div>

               


            </div>
        </div>

    </div>
</template>

<script setup>

import { PrimeIcons } from "primevue/api";
import { ref, onMounted } from "vue"
import { curentProduct } from "../../service/productServices";
import { URI } from "@/service/conection"
import { adiciones } from '@/service/menu/adiciones/adiciones.js'
import { menuGlobal } from "../../service/menu/menu";
import { useRouter } from 'vue-router';
import { formatoPesosColombianos } from "../../service/formatoPesos";
import { useCart } from "../../service/cart";
import router from  '../../router';

// import Crud from '@/views/pages/Crud.vue'
// import router from '../../router/index.js'
const ruta_id = ref(Number(router.currentRoute._value.params.product_id))

// const router = useRouter();
const checked = ref({ })
// const checked = false

const errorImage = (event) => {
    event.target.src = 'https://novatocode.online/assets/logo-f2daca0e.png'
}

onMounted(() => {

    // console.log($route)


    if ( localStorage.getItem('product') && JSON.parse(localStorage.getItem('product')).product_id == ruta_id.value) {
        curentProduct.value = JSON.parse(localStorage.getItem('product'))
    } else {
        curentProduct.value = buscarProductoPorId(menuGlobal,ruta_id.value)
        localStorage.setItem('product', JSON.stringify(buscarProductoPorId(menuGlobal,ruta_id.value)))
        // location.reload()

    }
    // location.reload()


    // curentProduct.value = buscarProductoPorId(menuGlobal,6)
    // curentProduct.value = buscarProductoPorId(menuGlobal,router.params.product_id)
    // console.log(router.currentRoute._value.params.product_id)



})

function buscarProductoPorId(jsonData, productId) {
    for (const category of jsonData) {
        for (const product of category.products) {
            if (product.id === productId) {
                return product;
            }
        }
    }
    return null; // Devuelve null si el producto no se encuentra
}


console.log(curentProduct.value)
const props = defineProps({
    product: {
        type: Object,
        default: {}
    },


});

</script>

<style scoped>
.cart {

    box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.4);



}

.img-cont {
    background-color: var(--primary-color);
    /* display: flex; */
    /* justify-content: flex-start; */
    align-items: start;

    /* box-shadow: 10px 0px 10px rgba(0, 0, 0, 0.5); */
    height: auto;
    position: relative
    /* flex-direction: column; */
}



.imagen {
    /* position: sticky; */
    width: 100%;
    /* height: ; */
    /* top: 10%; */
    /* transform: translateY(-50%); */
    /* top:10vh; */
    /* left: 50vh; */
    object-fit: contain;
    transition: all ease 0.5s;
    /* margin-left: 1vw; */
    border-radius: 50px;
    filter: brightness(1.2) drop-shadow(-2px 2px 15px rgba(0, 0, 0, 1));

    /* filter: drop-shadow(-2px 2px 15px rgba(0, 0, 0, 0.7)); */

}

.imagen:hover {
    transform: scale(1.1);
    ;

    /* box-shadow: 0px 0px 30px rgba(0, 0, 0, 1); */
    filter: brightness(1.2) drop-shadow(-2px 2px 15px rgba(0, 0, 0, 1));
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

.ver-mas {
    transition: all 0.2s ease;
    border: 2px solid var(--primary-color);
    /* // font-weight: bold; */
    font-size: 20px;
    /* // margin-bottom: 200px; */
    background-color: transparent;
    border-radius: 10px;
}

.whatsapp:hover{
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

.adiciones {
    display: flex;
    padding: 0;
    margin: 0;

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
</style>