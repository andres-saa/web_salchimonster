<template>

<Dialog class="dialogo" style="padding-bottom: 7rem; border-radius: 1rem; overflow: hidden; background-color: rgb(255, 255, 255); color: black" v-model:visible="dialog_pedido_visible" modals header="name" :style="{ width: '40rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">

<button class="btn_cerrar" @click="dialog_pedido_visible = !dialog_pedido_visible"
                            style="z-index: 99; background-color: var(--primary-color); padding: 0.5rem 1rem; border: none;border-radius: 0.5rem; color: white; position: absolute; right: 2rem;">
                            <i style="color: white; font-weight: bold; border-radius: 1rem;" :class="PrimeIcons.TIMES" ></i>
                    </button>


<Factura class="factura" id="factura">



</Factura>



<div class="btn_accion_dialogo" style="position: absolute; top:90%; display: flex; gap: 2rem">
<button v-if="pedido.order_status.status == 'generada' && pedido.order_status.status != 'enviada' " @click="prepararPedido(pedido) " style="border: none;box-shadow: 0 0 1rem rgba(0, 0, 0, 0.5); padding: 0rem 2rem;border-radius: 0.5rem; background-color: rgb(0, 255, 106);" ><span class="text-xl p-0" style="border: none; font-weight: bold; ">PREPARAR</span>
</button>

<button v-if="pedido.order_status.status == 'en preparacion' && pedido.order_status.status != 'enviada'  "  @click="marcarComoEnviado(pedido)" style="border: none;box-shadow: 0 0 1rem rgba(0, 0, 0, 0.5); padding: 0rem 2rem;border-radius: 0.5rem; background-color: rgb(0, 255, 0);" ><span class="text-xl p-0" style="border: none; font-weight: bold; ">ENVIAR</span>
</button>

<button @click="cancelarPedido(pedido)" v-if="pedido.order_status.status != 'enviada'  " style="border: none;box-shadow: 0 0 1rem rgba(0, 0, 0, 0.5); padding: 1rem 2rem;border-radius: 0.5rem; background-color: rgb(255, 120, 120);" ><span class="text-xl" style="border: none; font-weight: bold; ">CANCELAR</span>
</button>

<button @click="IMPRIMIR" style="border: none;box-shadow: 0 0 1rem rgba(0, 0, 0, 0.5); padding: 1rem 2rem;border-radius: 0.5rem; background-color: rgb(255, 246, 120);" ><span class="text-xl" style="border: none; font-weight: bold; ">IMPRIMIR</span>
</button>



</div>



</Dialog>
</template>

<script setup>

import {pedido,dialog_pedido_visible} from '@/service/un_pedido'
// import { PrimeIcons } from 'primevue/api';


// import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
// import { formatoPesosColombianos } from '../../service/formatoPesos';
import { PrimeIcons } from 'primevue/api';
// import { useCart, eliminarAdicionDelCarrito,agregarAdicionAlCarrito, products, updateCart, contarObjetosRepetidos, quitarElementos } from '../../service/cart';
// import { useRoute } from 'vue-router';
// import { calcularPrecioTotal, calcularTotalCarrito } from '../../service/state';
// import { adiciones } from '../../service/menu/adiciones/adiciones';
import Factura from './factura.vue';
import { prepararPedido,marcarComoEnviado, cancelarPedido } from '../../service/un_pedido';
import factura from './factura.vue';



const IMPRIMIR = () => {
    const contenidoFactura = document.getElementById('factura').innerHTML;

    // Abrir una nueva ventana para imprimir
    const ventanaImpresion = window.open('', '_blank');
    
    ventanaImpresion.document.write('<html><head><title>Factura</title>');

    // Copiar estilos CSS de la página principal a la ventana de impresión
    const estilosPagina = document.getElementsByTagName('style');

    for (let i = 0; i < estilosPagina.length; i++) {
        ventanaImpresion.document.write(estilosPagina[i].outerHTML);
    }

    ventanaImpresion.document.write('</head><body>');
    ventanaImpresion.document.write(contenidoFactura);
   
    ventanaImpresion.document.write('</body>   <style>  *{font-family: sans-serif; padding: 0 !IMPORTANT; margin: 0 !IMPORTANT; font-size:0.8rem !IMPORTANT} </style>      </html> ');
    

    ventanaImpresion.document.close();

    // Imprimir la ventana
    ventanaImpresion.print();

    // Cerrar la ventana después de 1 segundo (puedes ajustar este tiempo)

    ventanaImpresion.close();
    // print()
  
};























</script>

<style scoped>

.texto-negro{
    color: black;
}

.before{
    background-color: rgba(0, 0, 0, 0.8);width: 100vw;height: 100vh; z-index: 999;
    position: absolute; top: 0;left: 0;
    transform: scale(2);
}




.contenido-dialogo{
    background-color: rgb(255, 0, 0);
}


@media print {

  
    /* Estilos para la impresión */
    *{
      display: inline;
      
    }

    ::-webkit-scrollbar {
    width: 0.5rem;
    /* Ancho de la barra de desplazamiento */
    padding-top: 1rem;
    position: absolute;
    display: none;
}



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


