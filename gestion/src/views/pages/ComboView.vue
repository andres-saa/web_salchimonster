<template style="" >
    <div class="cart   m-auto grid col-12 p-8 m "
        style="; border-radius:20px; position: relative; height: min-content; margin-bottom:30vh ; width: 100%; ">
        <div class="img-cont   col-5 grid  mb-6 p-3"
            style="  display: flex; align-items: start; overflow: hidden; position: relative; height: auto;border-radius: 20px;background-color: ;   ">
           

            <div class="cont"  style="background-color: var(--primary-color); overflow: hidden; width: 100%;  border-radius: 10px; ">


                <img @error="errorImage" style="border-radius: 10px;; z-index: 100 ; width: 100%;

            " class="imagen  "
                src="http://localhost:5173/src/images/imagenes%20combos/combo%204.jpeg"
                alt="">



                <img @error="errorImage" style="; z-index: 100 ; width: 100%;
                 position: absolute;left: 0; overflow: hidden; top:0rem ; 
                 transform:scaley(1.03)
                
            " class="llamas p-3"
                :src="`src/images/assets/llamas.png`">
            </div>
                       
        </div>

        <div class=" col grid ml-6 mb-6 "
            style=" display: flex; align-items: start; overflow: hidden; position: relative; height: auto;border-radius: 20px;background-color: ;   ">
            <div class=" info grid  " style=" ; ">

                <div class="info-header  text-5xl">

                    <div class="title">
                        <p style="   font-weight: bold;">
                            {{ curentProduct.name }}
                        </p>
                    </div>

                    <p style="  font-weight: bold;">
                        {{ formatoPesosColombianos(curentProduct.price)  }}
                    </p>

                </div>

                <div class="title" style="border-radius: 20px;">
                    <p style="   font-weight: bold; padding-top: 2rem;" class="text-4xl ">
                        Descripcion
                    </p>

                    <p class="text-xl pb-4">
                        {{ curentProduct.description }}

                    </p>
                    

                    <div class=" col  pb-8 "
                        style="background-color: rgba(255, 98, 0, 0.184); width: 100%;border-radius: 20px;overflow: hidden;">



                        <div class="  salsas grid  "
                            style="width:100% ; display: flex; flex-direction: column; overflow: hidden;">
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

                            <div v-for="i in adiciones.salsas" class="col-  "
                                style="display: ;  justify-content: start; ; padding-bottom: 0.5rem; padding-left: 1rem;">

                                <div class="salsa "
                                    style=" margin: 0; padding: 0;width:500px; display: flex; justify-content: start; align-items: center;">
                                    <p class="texto  " style="margin: 0; width:300px"> {{ i }}
                                    </p>

                                    <span
                                        style="; width:100% ; overflow: hidden; border-top: 2px  ;  border-bottom: 5px  ;height: 1px; border-top-style: dotted; color:; margin-right:1rem ;">
                                        <p></p>
                                    </span>

                                    <Checkbox v-model="checked.papas" :binary="true" style="margin-right: 1rem; " />


                                </div>
                            </div>
                        </div>




                        <div class="  adiciones grid col-12 ">
                            <div class="title col-12" style="overflow: hidden;">
                                <p style="   font-weight: bold; width:100%; overflow: hidden; display: flex; align-items: center; gap: 5%;"
                                    class="text-4xl p-o">

                                    <span style="padding: 0;">
                                        ADICIONES
                                    </span>
                                    <span
                                        style="; width: 100%; overflow: hidden; border-top: 5px solid var(--primary-color)  ;  border-bottom: 5px  ;height: 1px; border-top-style:solid ; color: ;">
                                        <p></p>
                                    </span>


                                </p>
                            </div>

                            <div v-for="i in adiciones.salchipapas" class="   "
                                style="min-width: 50%; padding-bottom: 0.5rem; padding-left: 1rem;">
                                <div class="salsa m-0 p-0" style=" align-items: center; justify-content: start; ">
                                    <div style="display: flex;">
                                        <Checkbox v-model="checked.papas" :binary="true" style="margin-right: 1rem; m " />

                                        <p class="texto text m-0" style="width:max-content"> {{ i.name }}
                                        </p>
                                    </div>

                                    <span
                                        style="; width:100% ; overflow: hidden; border-top: 2px  ;  border-bottom: 5px  ;height: 1px; border-top-style: dotted; color:; margin-right:1rem ;">
                                        <p></p>
                                    </span>

                                    <p class="texto text m-0 " style="font-weight: bold; margin-left: ;">${{ i.price }}
                                    </p>

                                </div>
                            </div>
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
// import Crud from '@/views/pages/Crud.vue'



const router = useRouter();
const checked = ref({ papas: false })
// const checked = false

const errorImage = (event) => {
    event.target.src = 'https://novatocode.online/assets/logo-f2daca0e.png'
}

onMounted(() => {


    if (JSON.parse(localStorage.getItem('product')).product_id == Number(router.currentRoute._value.params.product_id)) {
        curentProduct.value = JSON.parse(localStorage.getItem('product'))
    } else {
        curentProduct.value = buscarProductoPorId(menuGlobal, Number(router.currentRoute._value.params.product_id))
        localStorage.setItem('product', JSON.stringify(buscarProductoPorId(menuGlobal, Number(router.currentRoute._value.params.product_id))))
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

    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.4);



}

.img-cont {
    background-color: var(--primary-color);
    /* display: flex; */
    /* justify-content: flex-start; */
    align-items: start;
    
    box-shadow: 20px 0px 20px rgba(0, 0, 0, 0.3);
    height: 100%;
    /* flex-direction: column; */
}



.imagen {
    /* position: fixed; */
    width: 100%;
    height: auto;
    object-fit: cover;
    transition: all ease .3s;
    /* margin-left: 1vw; */
    border-radius: 50px;

    /* filter: drop-shadow(-2px 2px 15px rgba(0, 0, 0, 0.7)); */

}
.llamas{
    width: 100%;

    object-fit: cover;
    transition: all ease 0.5s;
    /* margin-left: 1vw; */
    border-radius: 10px;
}
.img-cont:hover .imagen{
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