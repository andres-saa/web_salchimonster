<template>
    <Dialog v-model:visible="store.visibles.currentSite"
        :style="{ width: '380px' }" header="Seleccion de sede" :modal="true" class="p-fluid m-3"
        style=" background-color: white;position: relative; border-radius: 1rem;padding-top: 2rem;">




       <b style="color:black">
        <!-- {{ store.location }} -->
       </b>

        <!-- <div class="notch"
            style="display: flex; align-items: center; width: 30%; background-color: black; border-radius: 0 0 1rem 1rem; height: 2rem; position: absolute; top: 0rem; left: 35%;">
            <div class="led"
                style="position:absolute ;right: 1rem; width: 0.7rem; height: 0.7rem; background-color: var(--primary-color); border-radius: 50%;: 1rem">
            </div>

        </div> -->


        <div
            style="width: 100%;display: flex; flex-direction: column; align-items: center; border-radius: ;background-color: ">

            <!-- <img style="width: 50px;" src="http://localhost:5173/src/images/logo.png" alt=""> -->

    
            <div class="field col-12 pb-0 p-0" style="width: 100%;">
                <div style="display: flex; ;width: min-content; justify-content:start;gap: 1rem;align-items: center;"> 
                <label for="site_id" style="color: black; min-width: max-content;">en que ciudad te encuentras?   </label> 
                
                <ProgressSpinner v-if="spinnersView.ciudad" style="width: 20px; height: 20px" strokeWidth="8" fill="var(--white)"
                
    animationDuration=".5s" aria-label="Custom ProgressSpinner" /> 

</div>
                <Dropdown class="" @click="() => currenNeigborhood = {
                    site: {
                        site_name: 'default'
                    }   
                }" v-model="currenCity" :options="cities" placeholder="SELECCIONA UNA CIUDAD" optionLabel="city_name" required="true" />

            </div>
     

            <div class="field col-12 mt-0 pt-0 p-0" style="width: 100%;gap: ; display: block;">
                <div style="display: flex;width: min-content; justify-content:start;gap: 1rem;align-items: center;"> 
                <label for="site_id" style="color: black;min-width: max-content;">Cual es tu barrio?   </label> 
                
                
                <div v-if="spinnersView.barrio" style="display: flex; min-width: max-content;">
                    <ProgressSpinner  style="width: 20px;  height: 20px" strokeWidth="8" fill="var(--white)"
                
                animationDuration=".5s" aria-label="Custom ProgressSpinner" /> 
                
                <p class="pl-2" style="color: black;">buscando barrios...</p>
                </div>  
                
                

</div>
 
                <Dropdown style="" filter v-model="currenNeigborhood" :disabled="!possibleNeigborhoods"
          :options="possibleNeigborhoods" optionLabel="name" required="true"
          placeholder="Selecciona un barrio" filterPlaceholder="Escribe el nombre de tu barrio" />

          

                <!-- <Dropdown v-model="seleFcarrctedCity" editable :options="possibleNeigborhoods"  placeholder="Select a City" class="w-full md:w-14rem" /> -->

            </div>

            <div class="field col-12 p-0" style="width: 100%; height:15rem ; position: relative;">


                <div class="img-cont col-12 p-0" style="overflow: hidden;position: relative;">

                    

                    



                    <img v-if="currenNeigborhood?.site_id" :src="`${URI}/read-product-image/600/site-${currenNeigborhood?.site_id}`"
                        :class="currenNeigborhood.site?.name == 'default' ? 'default-image' : ''"
                        style="border: 1px solid rgb(255, 255, 255); width: 100%;background-color: rgb(255, 255, 255); height: 100%; object-fit: cover; border-radius: 0.2rem;"
                        alt="">


                    <div
                        style=" position: absolute; top: 0; left: 0; width: 100%; height: 100%; display:flex; padding: ; align-items: end;border-radius: 0.5rem; ">
                        <p v-if="currenNeigborhood?.site_id" class="col-12 py-1"
                            style="background-color: black; text-align: center; height: min-content;  width: 100%;  font-weight: 500; background-color: rgba(0, 0, 0, 0.7);">
                            <span  class="text-xl lg:text-lg p-0" style=""> SALCHIMONSTER</span> <span
                                style="text-transform: uppercase;" class="text-xl lg:text-lg p-0">{{
                                    currentSite?.site_name }}</span>
                        </p>
                    </div>
                </div>






            </div>

            <div class="field col-12 p-0" style="width: 100%;  ;">
                <Button label="Guardar" @click="setNeigborhood" :disabled="!currenNeigborhood?.name"
                    style="width: max-content;border: none; padding: 10px 20px;width: 100%; text-align: center;background-color: black;" b>
                    
                </Button>

            </div>


        </div>
 
       



    </Dialog>
</template>

<script setup>







// import { getProductsByCategory, getCategory, getMenu } from '@/service/productServices.js'
import { onMounted, ref, watch } from 'vue';
import { PrimeIcons } from 'primevue/api';
import { showSiteDialog, setShowDialog } from '@/service/state';
import { URI } from '@/service/conection'
// import { cities } from '@/service/citiesService';
import {sitesService } from '../service/site/sitesService'
import {useSitesStore} from '../store/site'
import { usecartStore } from '../store/shoping_cart';

const store = useSitesStore()
const cart = usecartStore()

watch(() =>  store.location.site.site_id ,() => {
    
    cart.cart =  {
          products: [],
          total_cost: 0,
          additions: [],
    
}

location.reload()

} )

const spinnersView = ref({ciudad:false, barrio:false})
const cities = ref([]) 
const currentSite = ref({})
const currenCity = ref({})
const c_neigbor = ref(localStorage.getItem('currentNeigborhood'))
const currenNeigborhood = ref({
    site: {
        name: 'default'
    }
})

const possibleNeigborhoods = ref()
const changePossiblesNeigborhoods = () => {
    getNeighborhoodsByCityId(currenCity.value.city_id).then(data => possibleNeigborhoods.value = data)
}



watch(currenCity, () => { changePossiblesNeigborhoods() })




watch(currenNeigborhood, async() => { 
    
   currentSite.value =  await sitesService.getSiteById(currenNeigborhood.value.site_id).then((data) => currentSite.value = data)
 })












const setNeigborhood = async() => {

    const newLocation = {
        site:currentSite.value,
        neigborhood:currenNeigborhood.value,
        city:currenCity.value
    }
    
    store.setLocation(newLocation)
    store.setVisible('currentSite',false)
    showSiteDialog.value = false

}


const getCities = async() => {
    try {
    spinnersView.value.ciudad = true
     const response = await fetch(`${URI}/cities`)
     if(response.ok){
        const data = await response.json()
        spinnersView.value.ciudad = false
        // cities.value = data
        return data
     }
     
   } catch (error) {
    spinnersView.value.ciudad = false
    
   }
   
}











const getNeighborhoodsByCityId = async(city_Id) => {
    try {
        spinnersView.value.barrio = true
     const response = await fetch(`${URI}/neighborhoods/by-city/${city_Id}`)
     if(response.ok){
        const data = await response.json()
        // cities.value = data
        spinnersView.value.barrio = false

        return data
     }
     
   } catch (error) {
    spinnersView.value.barrio = false

    
   }
}

onMounted(async() => {
    getCities().then(data => cities.value = data)
})


</script>


<style scoped>
@keyframes rot {
    0% {
        transform: translatey(-50%) scale(1.25, 0.75);
    }

    50% {
        transform: translatey(-150%) scale(1, 1);
    }

    100% {
        transform: translatey(-50%) scale(1.25, 0.75);
    }
}

* *:focus {
    outline: none;
    border: none;
}

.imagen {
    margin: 200px;
    width: 100px;
    /* overflow: hidden;  */
    animation: rot 0.7s infinite;
    transform-origin: center bottom;
}

.img-cart:hover {
    transform: scale(1.3);
}

.img-cart {
    transition: all .3s ease;
}







@media (min-width: 767px) {
    .scroll {
        max-height: 45rem;
        overflow-y: auto;

    }

    .add-car {
        width: 50%;
    }
}

.led {
    animation: cambiaColor 1s infinite;
    /* 3s de duración, animación infinita */
}

@keyframes cambiaColor {
    0% {
        background-color: rgb(0, 0, 0);
    }

    50% {
        background-color: rgb(30, 255, 0);
    }

    100% {
        background-color: var(--primary-color);
    }
}

.img-before {
    /* background-color: rgba(0, 0, 0, 0.235); */
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0%;
    left: 0;
    z-index: 1;
    display: flex;
    align-items: center;
    justify-content: center;

}

.carro:hover {
    /* transform: scalex(1.2); */
    background-color: #ff62004a;
    cursor: pointer
}

.menu-button-new {
    background-color: var(--primary-color);
    /* padding: 1rem; */
    /* margin: 0 1rem; */
    border: none;
    font-size: 20px;
    /* transition: all  0.3s; */
    /* font-weight: bold; */
    border-radius: 10px;
    color: #fff;
    width: 300px;
    transition: all 0.3s ease;
    text-align: center;

}

.fondo-movil {
    background-color: var(--primary-color);
}

.fondo-pc {
    background-color: #626262;
    /* overflow-x: hidden; */
}

.img-cont {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    position: relative;
    overflow: hidden;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 10px;


}

.default-image {
    filter: blur(10px);
    position: relative;
}

*:focus {
    border: none;
    outline: none;
}

.default-image::before {
    content: 'hola';
    width: 100%;
    /* background-color: rgba(177, 99, 9, 0.1); */
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
}

.selected {
    background-color: #ff620050
}

.menu-button-new:hover {
    /* filter: brightness(1.5);  
   */
    background-color: black;
    cursor: pointer;

}




.cart {

    /* box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.4); */



}

.img-cont {
    /* background-color:rgb(255, 255, 255); */
    /* display: flex; */
    /* justify-content: flex-start; */
    align-items: start;

    /* box-shadow: 30px 0px 30px rgba(0, 0, 0, 0.5); */
    height: 100%;
    /* flex-direction: column; */
}



.imagen {
    /* position: fixed; */
    width: 100%;
    height: auto;
    object-fit: contain;
    transition: all ease 0.5s;
    /* margin-left: 1vw; */
    border-radius: 50px;

    /* filter: drop-shadow(-2px 2px 15px rgba(0, 0, 0, 0.7)); */

}

.imagen:hover {
    transform: scale(1.1);
    ;

    /* box-shadow: 0px 0px 30px rgba(0, 0, 0, 1); */
    filter: brightness(1.2) drop-shadow(-2px 2px 15px rgba(0, 0, 0, ));
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

.ordenar {
    transition: all 0.2s ease;
    border: 2px solid var(--primary-color);
    /* // font-weight: bold; */
    font-size: 20px;
    /* // margin-bottom: 200px; */
    background-color: transparent;
    border-radius: 5px;
}

.carro {

    border: none;
    /* // font-weight: bold; */
    /* font-size: 20px; */
    /* // margin-bottom: 200px; */
    background-color: transparent;
    border-radius: 5px;
    margin: auto;
    /* border-radius:; */
}

.whatsapp:hover {
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

.whatsapp {
    /* background-color: red; */
    /* min-width: 1024px; */
    width: 3rem;
    height: 3rem;
    display: flex;
    transition: all ease .3s;
    right: 5rem;
    bottom: 9rem;

    /* align-items: center; */
    justify-content: center;
    background-color: #25D366;
    border-radius: 50%;
    position: absolute;

}

@media (max-width:500px) {
    .whatsapp {
        /* background-color: red; */
        /* min-width: 1024px; */
        width: 4rem;
        height: 4rem;
        right: 5%;
        bottom: 130%;

    }
}


.led {
    animation: cambiaColor 1s infinite;
    /* 3s de duración, animación infinita */
}

@keyframes cambiaColor {
    0% {
        background-color: rgb(0, 0, 0);
    }

    50% {
        background-color: rgb(30, 255, 0);
    }

    100% {
        background-color: var(--primary-color);
    }
}

.adiciones {
    display: flex;
    padding: 0;
    margin: 0;

}

a {
    text-decoration: none;
}
 *{
    text-transform: uppercase;
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

::-webkit-scrollbar {
    width: 1rem;
    /* Ancho de la barra de desplazamiento */
    padding-top: 1rem;
    position: absolute;
    display: none;
}

.clase {}

/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {
    background-color: rgb(255, 0, 0);
    /* Color del pulgar de la barra de desplazamiento */
    border-radius: 9px;
    border: 5px solid var(--primary-color);
    height: 10rem;
    width: 10rem;
    /* display: none;  */
}




.fondo-pc {
    background-color: rgb(247, 247, 247);
}

dialog {
    ::-webkit-scrollbar {
        width: 0.5rem;
        /* Ancho de la barra de desplazamiento */
        padding-top: 1rem;
        position: absolute;
        /* display: none; */
    }

    .clase {}

    /* Estilo del pulgar de la barra de desplazamiento */
    /* WebKit (Chrome, Safari) */
    ::-webkit-scrollbar-thumb {
        background-color: var(--primary-color);
        /* Color del pulgar de la barra de desplazamiento */
        border-radius: 9px;
        /* border: 5px solid var(--primary-color); */
        height: 10rem;
        width: 10rem;
        /* display: none;  */
    }
}</style>
