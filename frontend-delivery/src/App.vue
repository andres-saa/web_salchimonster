<script setup>

import { curentSite } from './service/un_pedido';
// import { menuOptions } from './service/menuOptions';
import {onBeforeUnmount} from 'vue'
// // import {sumarAdiciones, showSiteDialog, setShowDialog,showProductDialog,setProductDialog,productDialog,checkedSalsas,checkedAdiciones,currentAditions,currentSalsas, calcularTotalCarrito } from './service/state';
// import { carro } from './service/cart';

// import { useToast } from 'primevue/usetoast';


// import { menuGlobal } from './service/menu/menu';


// import router from '@/router/index.js'
// import { useCart } from './service/cart';
 
// const screenWidth = ref(window.innerWidth);
// console.log(screenWidth.value)
// // Función para actualizar el valor del ancho de la pantalla
// const updateScreenWidth = () => {
//   screenWidth.value = window.innerWidth;
// };

// const toast = useToast();
// // Escuchar el evento de cambio de tamaño de la ventana
// window.addEventListener('resize', updateScreenWidth);

// // Limpieza al desmontar el componente
onBeforeUnmount(async() => {
  
  const serverTimeResponse = await fetch('https://backend.salchimonster.com/server_time');
  fechaHoy.value = await serverTimeResponse.json();
  localStorage.setItem("fecha_server",JSON.stringify(fechaHoy.value) )
});



// const c_neigbor = ref(localStorage.getItem('currentNeigborhood'))



  



// })
// const sitesImages = ref({
//   Caney: 'https://drive.google.com/file/d/1LpmzmgBDOR-YAT4_SstyAldl1Nid-CF2/view?usp=sharing',
//   'La Flora': 'https://backend.novatocode.online/read-site-cover/IMPERIO%20CANEY',
//   Palmira: '	https://backend.novatocode.online/read-site-cover/IMPERIO%20PALMIRA',
//   Bretaña: 'https://backend.novatocode.online/read-site-cover/IMPERIO%20BRETA%C3%91A',
//   Jamundi: 'https://backend.novatocode.online/read-site-cover/IMPERIO%20JAMUNDI',
//   Tulua: 'https://backend.novatocode.online/read-site-cover/IMPERIO%20TULUA',
//   default: ''
// })
// const currenNeigborhood = ref({
//   site: {
//     name: 'default'
//   }
// })
// const possibleNeigborhoods = ref()

// const ruta = ref(router.currentRoute)
// const vueMenu = ref(false)

// const addcar =(product) => {

//     const product_new = {... product}
    
//     product_new.price = product_new.price + sumarAdiciones(currentAditions)
//     product_new.salsas = currentSalsas.value
//     product_new.adiciones = currentAditions.value
//     useCart.add(product_new)  
//     toast.add({ severity: 'success', summary: 'Agregado al carrito', detail: productDialog.value.name, life: 3000 });
// }
// const currenCity = ref({})

// const changePossiblesNeigborhoods = () => {
//   const neigborhoods = []

//   currenCity.value.sites.map(site => {
//     site.neigborhoods.map(neigborhood => {
//       neigborhoods.push({ name: neigborhood.name, neigborhood: neigborhood, site: site })
//       console.log(site)
//     })
//   })

//   possibleNeigborhoods.value = neigborhoods
// }
// watch(currenCity, () => { changePossiblesNeigborhoods() })

// const setNeigborhood = () => {
//   localStorage.setItem('currentNeigborhood', JSON.stringify({ currenCity: currenCity.value.name, currenNeigborhood: currenNeigborhood.value.neigborhood, currenSite: currenNeigborhood.value.site.name }))
//   console.log(localStorage.getItem('currentNeigborhood'))
//   // setShowDialog()
//   location.reload();
// }



// const searchCountry = (event) => {
//   setTimeout(() => {
//     if (!event.query.trim().length) {
//       autoFilteredValue.value = [...autoValue.value];
//     } else {
//       autoFilteredValue.value = autoValue.value.filter((country) => {
//         return country.name.toLowerCase().startsWith(event.query.toLowerCase());
//       });
//     }
//   }, 250);
// };

// console.log(router.currentRoute)

// const topbarMenuClasses = computed(() => {
//   return {
//     'layout-topbar-menu-mobile-active': topbarMenuActive.value
//   };
// });

// const topbarMenuActive = ref(false);





// const cargarAdiciones = (item) => {
//   console.log('hola');

//   // Asegúrate de que checkedAdiciones y currentAditions estén definidos en el ámbito adecuado

//   if (checkedAdiciones.value[item.name]) {
//     // Si el checkbox está marcado, agregar el elemento a la lista
//     currentAditions.value.push(item);
//   } else {
//     // Si el checkbox está desmarcado, quitar el elemento de la lista
//     const index = currentAditions.value.findIndex((el) => el.name === item.name);
//     if (index !== -1) {
//       currentAditions.value.splice(index, 1);
//     }
//   }
// };



// const cargarSalsas = (item) => {
//   console.log('hola');

//   if (checkedSalsas.value['TODAS LAS SALSAS']) {
//     // Si seleccionas 'TODAS LAS SALSAS', deselecciona las otras opciones
//     checkedSalsas.value['SIN BURGER DE LA CASA'] = false;
//     checkedSalsas.value['SIN VERDE DE LA CASA'] = false;
//     checkedSalsas.value['SIN PIÑA'] = false;
//     checkedSalsas.value['SIN BBQ'] = false;

//     // Limpia la lista currentSalsas y agrega 'TODAS LAS SALSAS'
//     currentSalsas.value = ['TODAS LAS SALSAS'];
//   } else {
//     // Asegúrate de que checkedSalsas y currentSalsas estén definidos en el ámbito adecuado

//     // Si el checkbox está marcado, agregar el elemento a la lista
//     if (checkedSalsas.value[item]) {
//       // Agrega 'TODAS LAS SALSAS' solo si no está presente
//       if (!currentSalsas.value.includes('TODAS LAS SALSAS')) {
//         currentSalsas.value.push(item);
//       }
//     } else {
//       // Si el checkbox está desmarcado, quitar el elemento de la lista
//       const index = currentSalsas.value.findIndex((el) => el === item);
//       if (index !== -1) {
//         currentSalsas.value.splice(index, 1);
//       }
//     }
//   }
// };







// const visible = ref(true)





</script>

<template>
 <!-- <audio id="notificacion_pedido" src="sound/pip.mp3"></audio> -->
  <router-view  style="overflow-x: hidden;" class="col-12 p-0 m"   />


 



</template>

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
  background-color: #ffffff;
  overflow-x: hidden;
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


@media print {
    /* Estilos para la impresión */
    *{
      display: none;
      width: 500px;
      overflow:hidden
    }}


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
  background-color: rgba(177, 99, 9, 0.1);
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
  background-color:rgb(255, 226, 192);
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
</style>
