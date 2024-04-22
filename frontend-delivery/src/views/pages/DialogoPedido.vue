<template>
  <div>
    <Dialog v-model:visible="cancelDialogVisible" closeOnEscape :closable="true" modal style="width: 30rem;">
    <template #header>
      <h3>Cancelar Orden</h3>
    </template>
    <form @submit.prevent="submitCancel" style="display: flex;gap: 1rem; flex-direction: column;">

      <span for="responsible">Responsable</span>
      <Dropdown id="responsible" v-model="cancelData.responsible" :options="responsibles" optionLabel="name"
        placeholder="Selecciona un responsable"></Dropdown>


      <span for="reason">Razón</span>
      <Textarea style="resize: none; text-transform: lowercase;" id="reason" v-model="cancelData.reason" rows="5"
        placeholder="Escribe la razón de la cancelación"></Textarea>

      <Button label="Cancelar Orden" type="submit" class="p-button-danger" />
    </form>
  </Dialog>



  <Dialog  closeOnEscape :closable="false" v-model:visible="store.visibles.currentOrder" modal
    style="max-height: 80vh;width: 35rem; position: relative;">
    
    <div id="factura" style="width: 100%;">


     
    
      <div class="" style="width: auto;">
       
          <p class="" style="font-weight: bold;min-width: 100%; width: max-content; text-align: center; color: black;font-size: 1.7rem; margin:0rem;"> #{{ store.currentOrder.order_id }} </p>



          
              <p style="padding: 0; margin: auto;margin-bottom: 1rem; width: max-content;min-width: max-content; ">
                <b>
                  fecha: {{ store.currentOrder.latest_status_timestamp?.split('T')[0] }}

                </b>
              </p>
           

 <!-- <img src="https://cocina.salchimonster.com/images/logo.png" alt="" style="width: 2cm;"> -->
          <div class=""
            style="font-weight: bold;color:white;margin: 0; background-color: black;align-items: center;display: grid; grid-template-columns: 60%  20% 20%; ">

            <div style="width: 100%;" >

              <b> productos</b>


            </div>
            <!-- <div >
              <b>

                x
              </b>
            </div> -->
            <div>
              <p style="text-align: end;font-weight: bold;">
            
                <b style="text-align: end;">
                  valor
                </b>
              </p>
            </div>
            
            <div >
              <p style="text-align: end;font-weight: bold;">
                <b>
                  total
                </b>
                
              </p>
            </div>

          </div>

          <div  v-for="product in store.currentOrder.products">

            <div style="display: grid; grid-template-columns: 60%  20% 20%;">
              <div >
              <span>
                {{ product.quantity }}
                {{ product.name }}
              </span>
            </div>
          
            <div >
              <p style="text-align: end;color: black;">
                <!-- {{ formatoPesosColombianos(product.price) }} -->
                {{ formatoPesosColombianos(product.price) }}
              </p>
            </div>
            <div >
              <p style="text-align: end;color: black;">
                <!-- {{ formatoPesosColombianos(product.price) }} -->
                {{ formatoPesosColombianos(product.total_price) }}
              </p>
            </div>

            </div>

            <div style="background-color: rgba(0, 0, 0, 0.286); height: 1px;">

</div>  

          </div>
          




          <div s  v-for="(items, grupo) in store.currentOrder.additional_items" :key="grupo"
            style="position: relative; margin-top: 0.5rem;">



            <p style="background-color: black;font-weight: bold; color: white; width: 100%;margin: 0;">
              <b>{{ grupo }}</b>

            </p>


            <div   v-for="aditional in items">
              <div style="display: grid; grid-template-columns: 60%  20% 20%;">

                <div >
                  <p >
                    {{ aditional.aditional_quantity }}  {{ aditional.aditional_name }}
                  </p>
                </div>

                <div >
                  <p style="text-align: end;color: black;">
                    <!-- {{ formatoPesosColombianos(product.price) }} -->
                    {{ formatoPesosColombianos(aditional.aditional_price) }}
                  </p>
                </div>
                <div >
                  <p style="text-align: end;color: black;">
                    <!-- {{ formatoPesosColombianos(product.price) }} -->
                    {{ formatoPesosColombianos(aditional.total_aditional_price) }}
                  </p>
                </div>
              </div>
              <div style="background-color: rgba(0, 0, 0, 0.286); height: 1px;">

              </div>






            </div>

          </div>





 






          <div class="" style="display: grid ;color: ;margin-top: 0.5rem; grid-template-columns: auto auto">
            <div class="">
              <span style="font-weight: bold;"><b>Subtotal</b></span>
            </div>
            <div class="">
              <p  style="text-align: end;font-weight: bold; color: black;">
                <b >{{ formatoPesosColombianos(store.currentOrder.total_order_price) }}</b>
              </p>
            </div>

            <div class="">
              <span style="font-weight: bold;"><b>Domicilio</b></span>
            </div>
            <div class="">
              <p style="text-align: end;font-weight: bold;color: black;"> <b>
                  {{ formatoPesosColombianos(store.currentOrder.delivery_price) }}
                </b>
              </p>
            </div>
            <div class="">
              <span  style="font-weight: bold;color: black;" ><b>Total</b></span>
            </div>
            <div class="">

              <p style="text-align: end;color: black;font-weight: bold;"><b>{{ formatoPesosColombianos(store.currentOrder.delivery_price + store.currentOrder.total_order_price)
              }}</b></p>

            </div>
            <div class="">
              
            </div>

          </div>
          <p  style="font-weight: bold;background-color: black;color: white;padding: 0; margin: 0; margin-top: 0.5rem;"><b>Notas</b></p>
              <p class="notas" style="border: 1px solid;margin: 0; padding: 0.5rem;">
                {{ store.currentOrder.order_notes }}
              </p>




              <p  style="background-color: black;font-weight: bold;margin-top: 1rem; color: white;">
              <b>cliente</b>
              </p>

              <div style="display: grid; grid-template-columns: auto auto;">
                <div class="" style="">
              <span><b>NOMBRE</b></span>
            </div>
            <div class="">
              <p style="text-align: end;color: black;">

                {{ store.currentOrder.user_name }}
              </p>

            </div>
            <div  style="">
              <span><b>telefono</b></span>
            </div>
            <div>
              <p style="text-align: end;color: black;">

                {{ store.currentOrder.user_phone }}


              </p>
            </div>
            <div style="">
              <span><b>direccion </b></span>
            </div>
            <div >
              <p style="text-align: end;color: black;">

                {{ store.currentOrder.user_address }}


              </p>
            </div>




            <div>
              <span><b>metodo de pago</b></span>
            </div>
            <div >
              <p style="text-align: end;color: black;">

                {{ store.currentOrder.payment_method }}
              </p>
            </div>

              </div>
           
          <!-- 
            <router-link to="/SALCHIPAPAS/3" v-if="route.path.includes('cart')">
                <Button outlined icon="pi pi-shopping-cart" label="Seguir comprando" class="mt-4" severity="danger"
                    style="outline: none;width: 100%;font-weight: bold; background-color: rgba(0, 0, 0, 0);"></Button>

            </router-link>

            <router-link to="/cart" v-else>
                <Button outlined icon="pi pi-arrow-left" label="Volver al carrito" class="mt-4" severity="danger"
                    style="outline: none;width: 100%;font-weight: bold; background-color: rgba(0, 0, 0, 0);"></Button>

            </router-link>


            <router-link to="/pay" v-if="route.path.includes('cart')">
                <Button iconPos="right" icon="pi pi-arrow-right" label="Pedir" class="mt-2" severity="help"
                    style="outline: none;width: 100%; border: none;font-weight: bold; background-color: black;"></Button>
            </router-link>

            <router-link to="/pay" v-else>
                <Button @click="orderService.sendOrder()" iconPos="right" icon="pi pi-arrow-right" label="Finalizar pedido"
                    class="mt-2" severity="help"
                    style="outline: none;width: 100%; border: none;font-weight: bold; background-color: black;"></Button>
            </router-link> -->

   








      </div>





    </div>

    <template #footer>

      <div class="col-12 mb-0 pb-0 px-0 m-0" style="display: flex;justify-content: space-between;gap: 1rem;">

        <Button v-if="store.currentOrder.current_status == 'generada'" size="small"
          @click="orderService.prepareOrder(store.currentOrder.order_id)" style="border-radius: 0.3rem;width: 100%;"
          severity="success" label="Preparar"></Button>

        <Button v-if="store.currentOrder.current_status != 'enviada' && store.currentOrder.current_status != 'cancelada'


          " size="small" @click="cancelDialogVisible = true" style="border-radius: 0.3rem;width: 100%;" severity="danger"
          label="cancelar"></Button>


        <Button v-if="store.currentOrder.current_status == 'en preparacion'" size="small"
          @click="orderService.sendOrder(store.currentOrder.order_id)" style="border-radius: 0.3rem;width: 100%;"
          severity="success" label="enviar"></Button>
        <Button size="small" style="border-radius: 0.3rem;width: 100%;" @click="IMPRIMIR" severity="warning"
          label="imprimir"></Button>
      </div>


    </template>


    <Button class="shadow-4" @click="store.setVisible('currentOrder', false)" icon="pi pi-times" rounded severity="danger"
      style="position: absolute;top: 0;border-radius: 50%; right:-1rem; top: -1rem;"></Button>



  </Dialog>
  </div>

</template>

<script setup>
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { onMounted, ref } from 'vue'
import { useOrderStore } from '../../store/order'
import { orderService } from '../../service/orderService';
import printJS from 'print-js';








const store = useOrderStore()

// const IMPRIMIR = () => {
//   const contenidoFactura = document.getElementById('factura').innerHTML;

//   // Abrir una nueva ventana para imprimir
//   const ventanaImpresion = window.open('', '_blank');

//   ventanaImpresion.document.write('<html><head><title>Factura</title>');

//   // Copiar estilos CSS de la página principal a la ventana de impresión
//   const estilosPagina = document.getElementsByTagName('style');

//   for (let i = 0; i < estilosPagina.length; i++) {
//     ventanaImpresion.document.write(estilosPagina[i].outerHTML);
//   }

//   ventanaImpresion.document.write('<style>  @media print {  html{height: min-content;}  *{text-transform:uppercase;align-items:center; width:100%; font-family: sans-serif;padding:0;margin:0; font-size:o.9rem !IMPORTANT} body { padding:0; -webkit-print-color-adjust: exact; /* Chrome, Safari */ color-adjust: exact; /* Firefox */ } }  </style>');
//   ventanaImpresion.document.write('</head><body>');
//   ventanaImpresion.document.write(contenidoFactura);

//   ventanaImpresion.document.write('</body></html>');

//   ventanaImpresion.document.close();

//   // Imprimir la ventana
//   ventanaImpresion.print();

//   // Cerrar la ventana después de 1 segundo (puedes ajustar este tiempo)
//   setTimeout(() => {
//     ventanaImpresion.close();
//   }, 0.01);
// };


const IMPRIMIR = () => {
  printJS({
    printable: 'factura',
    type: 'html',
    targetStyles: ['*'],
    // style: `
    //   html, body {
    //     width: 100%;
    //   }
    //   #factura {
    //     width: 100%; // Asegúrate de que #factura es el ID del contenedor principal de tu contenido imprimible
    //     max-width: 100%;
    //   }
    //   .page-content { // Suponiendo que .page-content es una clase que puede estar afectando el contenido
    //     width: 100%;
    //     box-sizing: border-box;
    //     padding: 10mm;
    //   }
    // `
  });
};



onMounted(async () => {
  store.currentOrder.value = store.currentOrder
})


const cancelDialogVisible = ref(false);
const cancelData = ref({
  responsible: null,
  reason: 'Sin razon'
});
const responsibles = ref([
  { name: 'Restaurante', value: 'restaurant' },
  { name: 'Cliente', value: 'client' }
]);

const submitCancel = () => {
  if (cancelData.value.responsible) {
    orderService.cancelOrder(store.currentOrder.order_id, cancelData.value.reason, cancelData.value.responsible.name)
      .then(response => {
        if (response) {
          // Handle successful cancellation
          cancelDialogVisible.value = false;
          console.log('Order canceled successfully');
        }
      })
      .catch(error => {
        console.error('Failed to cancel order:', error);
      });
  }
}

</script>




<style scoped>
.p-shadow {
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.25);
}

button {
  text-transform: uppercase;
}



*{
  align-items: center;
}
* {
  text-transform: uppercase;
  font-size: 12pt;
  /* color: black; */
}


.notas {
  text-transform: lowercase;
}

.notas::first-letter {
  text-transform: uppercase;
}



span {
  color: black
}

*{
  text-transform: uppercase;
  /* color: black; */
}






  @media print {
    html, body {
      width: 100%;
      margin: 0;
      padding: 0;
      overflow: hidden; 
    }
    #factura {
      width: 100%;
      max-width: 100%;
      box-sizing: border-box; 
      font-size: 12pt;
    }
    .page-content {
      width: 100%;
      padding: 10mm;
    }
    #dialogo{
      width: 890rem !important; 
    }
  }




</style>


















