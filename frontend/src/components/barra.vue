<template >

<div v-if="
  !route.path.includes('cart') && 
  !route.path.includes('pay') && 
  !route.path.includes('menu') && 
  !route.path.includes('colaboraciones') && 
  !route.path.includes('pqrs-user') && 
  !route.path.includes('franquicias') && 
  !route.path.includes('gracias')  " 

  

class="col-12 py-0 px-4 background"   style="display: flex;position: fixed; bottom: 0; left: 0; ; justify-content: center">
  <div v-if=" store.cart.products.length > 0  " @click="enviarAlCarro" :style="!showElement? 'transform: translateY(5rem);opacity:0': ''"  class="barra-carrito  px-5 " style="  
                          
  /* width: auto; */
  display: flex;
  gap:2rem;
  border-radius: 10rem;
  align-items: center;  
  position: relative;
  z-index: 1000;
  bottom: 1rem;
  max-width: min-content;
  /* z-index: 999;  */
  justify-content:center ;
  /* margin: auto; */
  /* touch-action: none;  */
  /* width: %;  */
  height: 3.5rem;
  /* padding: 1rem; */
/* padding: 1rem;  */
  background-color: rgb(255, 255, 255); 
  
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);">
 
     


      <div    style="">
        <button class="    carro  " style="  
                            display: flex; 
                            background-color: ; 
                            align-items: center; 
                            justify-content: center;
                            gap: 1rem; 
                            background-color:;
                        

                            /* border-bottom: 4px solid rgb(0, 0, 0); */
                        
                            ">
 
 

          <i style="font-size: 2rem; " class="icono" :class="PrimeIcons.SHOPPING_CART"> </i>


          <div  style="position: relative;" :key="product.id" v-for="product in store.cart.products.slice(0, 4)">
            <Button class="p-0" :label="`${product.quantity}`" severity="danger" rounded style="width: 1.2rem;font-size: 0.8rem; height: 1.2rem;top: -.3rem; right: -.5rem; position: absolute;"/>
            <img class="img-cart" @mouseover="() => vueMenu = true" style="height: 2rem; object-fit: contain;"
            :src="`https://img.restpe.com/${product.product.productogeneral_urlimagen}`" alt="">
            
          </div>

          <div v-if="store.cart.products.length > 4 "
            style="width: auto; border-radius: 50%; ; height: 100%; object-fit: contain;" alt="">

            <p style="font-weight: bold; " class="text-xl">
              +{{ store.cart.products.length - 4 }}
            </p>
          </div>



        </button>
      </div>

      <p class="h2" style="position: absolute;top: 0;">
       

      </p>
      


      <a v-if="store.cart.products.length > 0" >



        <button class=" " style="
                            border: none; background-color:transparent; 
                            /* border-radius: 50%;  */
                            display: flex;align-items: center; justify-content: center;
                            


    
    ">
          
        </button>
      </a>


   



    
   





  </div>
  <div>
    
  </div>


  <div v-if="!route.path.includes('cart') && !route.path.includes('pay')" class="whatsapp"  :style="!showElement? 'transform: translateX(-2.2rem)': ''"  style="">
 

    <a href="https://wa.link/5mq1t0">  <button class="whatsapp-btn p-1" style="
                             border: none; background-color:transparent; 
                             transition: all ease .3s;
                             /* border-radius: 50%;  */
                             display: flex;align-items: center; justify-content: center;
 
 
     
 
     ">
           <i class="" :class="PrimeIcons.WHATSAPP"
             style=" ;position: relative;  font-weight:  bold; font-size: 1.8rem; color: rgb(255, 255, 255);width:auto">
           </i>
         </button></a>
 
        

         <a href="https://www.facebook.com/salchimonsterr">

          <button class="whatsapp-btn p-1" style="
                             border: none; background-color:transparent; 
                             transition: all ease .3s;
                             /* border-radius: 50%;  */
                             display: flex;align-items: center; justify-content: center;
 
 
     
 
     ">
           <i class="" :class="PrimeIcons.FACEBOOK"
             style=" ;position: relative;  font-weight:  bold; font-size: 1.8rem; color: rgb(255, 255, 255);width:auto">
           </i>
         </button>
         </a>
        
         

         <a href="https://www.instagram.com/salchimonsterr/">  <button class="whatsapp-btn p-1" style="
                             border: none; background-color:transparent; 
                             transition: all ease .3s;
                             /* border-radius: 50%;  */
                             display: flex;align-items: center; justify-content: center;
 
 
     
 
     ">
           <i class="" :class="PrimeIcons.INSTAGRAM"
             style=" ;position: relative;  font-weight:  bold; font-size: 1.8rem; color: rgb(255, 255, 255);width:auto">
           </i>
         </button></a>


         <a href="https://www.youtube.com/@Salchimonster/videos">  <button class="whatsapp-btn p-1" style="
                             border: none; background-color:transparent; 
                             transition: all ease .3s;
                             /* border-radius: 50%;  */
                             display: flex;align-items: center; justify-content: center;
 
 
     
 
     ">
           <i class="" :class="PrimeIcons.YOUTUBE"
             style=" ;position: relative;  font-weight:  bold; font-size: 1.8rem; color: rgb(255, 255, 255);width:auto">
           </i>
         </button></a>

        


        </div>
</div>
            




</template>

<script setup>  

import { menuOptions } from '@/service/menuOptions';

// import { getProductsByCategory, getCategory, getMenu } from '@/service/productServices.js'
import { ref, onMounted, onUnmounted } from 'vue';
import { PrimeIcons } from 'primevue/api';
import { useRoute } from 'vue-router';
// import { changeProduct } from './service/productServices';
import { carro_para_la_barra_de_abajo } from '@/service/cart';
const wsp = ref(localStorage.getItem('currenSiteWsp'))
import {URI} from '@/service/conection'
import router from '@/router/index.js'
import { usecartStore } from '../store/shoping_cart';
const store = usecartStore()
// import router from '../router';
// import { PrimeIcons } from 'primevue/api';
import { formatoPesosColombianos } from '@/service/formatoPesos';
import { verCerrado } from '../service/state';
const ruta = ref(router.currentRoute)
let scrollTimer;



const route = useRoute()

const handleScroll = () => {
      showElement.value = false;
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(() => {
        showElement.value = true;
      }, 500); // 2000ms (2 segundos) de inactividad antes de ocultar el elemento
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
    });

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll);
      clearTimeout(scrollTimer);
    });


const showElement = ref(true);



const enviarAlCarro = ()=> {
  window.location.href = '/cart'
}



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

.imagen {
  margin: 200px;
  width: 100px;
  /* overflow: hidden;  */
  animation: rot 0.7s infinite;
  transform-origin: center bottom;
}



.img-cart {
  transition: all .3s ease;
}

.background {

  background: linear-gradient(to top, rgba(255, 255, 255, 1) , rgba(255, 255, 255, 0));

}

*{transition:  all .2s ease;}



@media (min-width: 767px) {
  .scroll{
  max-height:45rem ;overflow-y: auto;

}

.add-car{
  width: 50%;
}
}

.led{
    animation: cambiaColor 1s infinite; /* 3s de duración, animación infinita */
}
    @keyframes cambiaColor {
      0% { background-color: rgb(0, 0, 0); }
      50% { background-color: rgb(30, 255, 0); }
      100% { background-color: var(--primary-color); }
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

.fondo-movil{
  background-color: var(--primary-color);
}

.fondo-pc{
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
*:focus{
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

.selected{
  background-color:#ff620050 
}

.menu-button-new:hover {
  /* filter: brightness(1.5);  
   */
  background-color: black;
  cursor: pointer;

}




.cart {

  box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.4);



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
    width: 2.5rem;
    height: min-content;
    gap: .3rem;
    display: flex;
    flex-direction: column;
    /* gap: 1rem; */
    transition: all ease .3s;
    left: 0rem;
    bottom: 9rem;
    padding:  0.5rem 0;

    /* align-items: center; */
    justify-content: space-around;
    background-color: var(--primary-color);
    border-radius: 0  1rem   1rem 0; 
    position: absolute;
    box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.391);
 
  }
@media (max-width:500px)  {
  .whatsapp {
    /* background-color: red; */
    /* min-width: 1024px; */
   
    /* right: 5%; */
    bottom: 20vh;

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

a{
  text-decoration: none;
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
  width: 1rem; /* Ancho de la barra de desplazamiento */
  padding-top: 1rem;
  position: absolute;
  display: none;
}
.clase{
    
}
/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {
  background-color: rgb(255, 0, 0); /* Color del pulgar de la barra de desplazamiento */
  border-radius: 9px;
  border: 5px solid var(--primary-color);
  height: 10rem;
  width: 10rem;
  /* display: none;  */
}




.fondo-pc{
  background-color: rgb(247, 247, 247);
}

dialog{
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
    background-color:var(--primary-color);
    /* Color del pulgar de la barra de desplazamiento */
    border-radius: 9px;
    /* border: 5px solid var(--primary-color); */
    height: 10rem;
    width: 10rem;
    /* display: none;  */
}
}
</style>