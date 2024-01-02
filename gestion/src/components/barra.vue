<template >

            
<div v-if="ruta.fullPath != '/cart' && 
  !ruta.fullPath.includes('admin-products') &&
  !ruta.fullPath.includes('entregas')
   " class="barra-carrito col-12 " style=" 
                          /* width: auto; */
                            display: flex;
                            gap:2rem;
                            align-items: center;  
                            position: relative;
                            z-index: 1000;
                            /* z-index: 999;  */
                            justify-content:center ;
                            /* touch-action: none;  */
                            /* width: %;  */
                            height: 4rem;
                            /* padding: 1rem; */
                        /* padding: 1rem;  */
                            background-color: rgb(255, 255, 255); 
                            position: fixed; bottom: 0; left: 0; 
                            box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.5);">
 
     


      <RouterLink to="/cart" style="">
        <button class="    carro  " style="  
                            display: flex; 
                            background-color: ; 
                            align-items: center; 
                            justify-content: center;
                            gap: 1rem; 
                            background-color:;
                        

                            border-bottom: 4px solid rgb(0, 0, 0);
                        
                            ">
 
 

          <i style="font-size: 2rem; " class="icono" :class="PrimeIcons.SHOPPING_CART"> </i>


          <div v-for="product in carro_para_la_barra_de_abajo.products.slice(0, 5)">
            <img class="img-cart" @mouseover="() => vueMenu = true" style="height: 2rem; object-fit: contain;"
              :src="`${URI}/read_product_image/300/${product.id}`" alt="">

            <!-- <TarjetaMenu v-if="vueMenu" style="width: 200px;height: 200px;" :product="product"></TarjetaMenu> -->

          </div>

          <div v-if="carro_para_la_barra_de_abajo.products.length > 5 "
            style="width: auto; border-radius: 50%; ; height: 100%; object-fit: contain;" alt="">

            <p style="font-weight: bold; font-size: 2rem; ">
              +{{ carro_para_la_barra_de_abajo.products.length - 5 }}
            </p>
          </div>



        </button>
      </RouterLink>

      <p class="h2" style="position: absolute;top: 0;">
       

      </p>
      

      <!-- <RouterLink style="background-color: green;" to="/pay" v-if="carro.products.length > 0 && screenWidth>555">
        <button  class=" ordenar  " style="text-decoration: none;  display: flex;
                             background-color:var(--primary-color)  ; 
                             color: white; 
                             align-items: center;  
                         
                             gap: 20px; width: auto ;
                             background-color:;padding: 0.1rem 1rem;
                             height: 0%;">

          <i style="font-size: 2rem;color: white; " class="icono" :class="PrimeIcons.MONEY_BILL"> </i>


          <span style="font-size: 2rem; background-color: var();">
            Ordenar
          </span>
        </button>
      </RouterLink> -->


      <a v-if="carro_para_la_barra_de_abajo.products.length > 0 && screenWidth>720" >



        <button class=" " style="
                            border: none; background-color:transparent; 
                            /* border-radius: 50%;  */
                            display: flex;align-items: center; justify-content: center;
                            


    /* box-shadow: 0px 0px 10px rgb(255, 255, 255); */

    ">
          <span :class="topbarMenuClasses"  style="font-size:2rem ; font-weight: bold;">
            {{ formatoPesosColombianos(Number(calcularTotalCarrito())) }}</span>
        </button>
      </a>


   



    
    <a class="whatsapp" :href="wsp" style="
                            
                        
                            ">
 
 
 
         <button class="whatsapp-btn" style="
                             border: none; background-color:transparent; 
                             transition: all ease .3s;
                             /* border-radius: 50%;  */
                             display: flex;align-items: center; justify-content: center;
 
 
     
 
     ">
           <i class="" :class="PrimeIcons.WHATSAPP"
             style=" ;position: relative;  font-weight:  bold; font-size: 2rem; color: rgb(255, 255, 255);width:auto">
           </i>
         </button>
       </a>





  </div>



</template>

<script setup>  

import { menuOptions } from '@/service/menuOptions';

// import { getProductsByCategory, getCategory, getMenu } from '@/service/productServices.js'
import { ref } from 'vue';
import { PrimeIcons } from 'primevue/api';
// import { changeProduct } from './service/productServices';
import { carro_para_la_barra_de_abajo } from '@/service/cart';
const wsp = ref(localStorage.getItem('currenSiteWsp'))
import {URI} from '@/service/conection'
import router from '@/router/index.js'

// import { PrimeIcons } from 'primevue/api';
import { formatoPesosColombianos } from '@/service/formatoPesos';

const ruta = ref(router.currentRoute)
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

* *:focus{
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
    box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.391);
 
  }
@media (max-width:500px)  {
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