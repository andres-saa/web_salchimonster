<template>



<Dialog v-model:visible="cancelDialogVisible" closeOnEscape :closable="true" modal style="width: 30rem;">
    <template #header>
      <h3>Cancelar Orden</h3>
    </template>
    <form @submit.prevent="submitCancel" style="display: flex;gap: 1rem; flex-direction: column;">
      
        <span for="responsible">Responsable</span>
        <Dropdown id="responsible" v-model="cancelData.responsible" :options="responsibles" optionLabel="name" placeholder="Selecciona un responsable"></Dropdown>
  
 
        <span for="reason">Razón</span>
        <Textarea style="resize: none; text-transform: lowercase;" id="reason" v-model="cancelData.reason" rows="5" placeholder="Escribe la razón de la cancelación"></Textarea>
    
      <Button label="Cancelar Orden" type="submit" class="p-button-danger"/>
    </form>
  </Dialog>



  <Dialog closeOnEscape :closable="false" v-model:visible="store.visibles.currentOrder" modal style="width: 30rem;max-height: 80vh;position: relative;">
   <div id="factura">

    <div class="p-0  col-12" style="width: 100%;">
    <div style="position: sticky; top: 5rem;border-radius: 0.5rem; z-index: 1000;" class="col-12 p-3  m-0 p-0 ">

      <p class="text-center text-xl" style="font-weight: bold;color: black;"> #{{ store.currentOrder.order_id }} </p>


      
<div class="grid my-3">
  <div class="p-0 m-0 col-12 ">
        <span class="p-0 m-0">
         fecha: {{ store.currentOrder.latest_status_timestamp?.split('T')[0] }}
        </span>
      </div>
</div>
      

      <div class="grid my-2 pb-0 py-0 px-1" style="font-weight: bold;color:white;background-color: black;align-items: center;justify-content: center;">

        
        
        <div class="col-6 p-0 my-0">
     
          <b> productos</b>

         
        </div>
        <div class="col-1 my-0 p-0   text-center">
          <b>
            
            x
          </b>
        </div>
        <div class="col-2 my-0  p-0  ">
          <b>
            <!-- {{ formatoPesosColombianos(product.price) }} -->
            val
          </b>
        </div>
        <div class="col-3 my-0 p-0   text-right">
          <b>
            total
          </b>
        </div>

      </div>

      <div class="grid my-0 py-0" v-for="product in store.currentOrder.products">

        <div class="col-6 p-0  my-0">
          <span>
           
            {{ product.name }}
          </span>
        </div>
        <div class="col-1 my-0 p-0  text-center">
          <span>
            <!-- {{ formatoPesosColombianos(product.price) }} -->
            {{ product.quantity }}
          </span>
        </div>
        <div class="col-2 my-0 p-0   ">
          <span>
            <!-- {{ formatoPesosColombianos(product.price) }} -->
            {{ formatoPesosColombianos(product.price) }}
          </span>
        </div>
        <div class="col-3 my-0 p-0  text-right ">
          <span>
            <!-- {{ formatoPesosColombianos(product.price) }} -->
            {{ formatoPesosColombianos(product.total_price) }}
          </span>
        </div>

          <div class="col-12 p-0 m-0" style="background-color: rgba(0, 0, 0, 0.286); height: 1px;">

          </div>
      </div>



 
        <div class="grid my-1 p-0" v-for="(items, grupo) in store.currentOrder.additional_items" :key="grupo"
          style="position: relative;">


         
            <span class="my-2 col-12 py-0 px-1" style="background-color: black;color: white;">
              <b>{{ grupo }}</b>

            </span>


            <div class="col-12 m-0 p-0"  v-for="aditional in items">
              <div class=" grid m-0 p-0">

              <div class="col-6 p-0  my-0">
              <span>
                {{ aditional.aditional_name }}
              </span>
            </div>
            <div class="col-1 m-0 p-0  text-center">
              <span>
                <!-- {{ formatoPesosColombianos(product.price) }} -->
                {{ aditional.aditional_quantity }}
              </span>
            </div>
            <div class="col-2 m-0  p-0  ">
              <span>
                <!-- {{ formatoPesosColombianos(product.price) }} -->
                {{ formatoPesosColombianos(aditional.aditional_price) }}
              </span>
            </div>
            <div class="col-3 m-0 p-0  text-right ">
              <span>
                <!-- {{ formatoPesosColombianos(product.price) }} -->
                {{ formatoPesosColombianos(aditional.total_aditional_price) }}
              </span>
            </div>
            </div>
            <div class="col-12 p-0 m-0" style="background-color: rgba(0, 0, 0, 0.286); height: 1px;">

</div>

            




          </div>

        </div>












      <div class="grid mt-1">
        <div class="col-6 my-0 p-0 py-0">
          <span><b>Subtotal</b></span>
        </div>
        <div class="col-6 my-0 p-0  text-right py-0">
        <span>
          <b>{{ formatoPesosColombianos(store.currentOrder.total_order_price) }}</b>
        </span>  
        </div>

        <div class="col-6 my-0 p-0 py-0">
          <span><b>Domicilio</b></span>
        </div>
        <div class="col-6 my-0 p-0 text-right py-0">
          <span style=""> <b>
            {{ formatoPesosColombianos(store.currentOrder.delivery_price) }}
          </b>
          </span>
        </div>
        <div class="col-6 my-0 p-0 py-0">
          <span><b>Total</b></span>
        </div>
        <div class="col-6 my-0 p-0 text-right py-0">

          <span><b>{{formatoPesosColombianos(store.currentOrder.delivery_price + store.currentOrder.total_order_price)  }}</b></span>

        </div>
        <div class="col-12 p-1 mt-1 mb-2 border-1">
          <span><b>Notas:</b></span> <br>
          <span class="notas" >
            {{ store.currentOrder.order_notes }}
          </span>
        </div>


        <div class="col-12 tex my-0 p-0 py-0 px-1" style="background-color: black;color: white;">
          <p><b>cliente</b></p>
        </div>

        <div class="col-3 my-0 p-0 py-0" style="">
          <span><b>NOMBRE</b></span>
        </div>
        <div class="col-9 my-0 p-0  text-right py-0">
          <span>
        
            {{ store.currentOrder.user_name }}       
          </span>
          
        </div>
        <div class="col-4 my-0 p-0 py-0" style="">
          <span><b>telefono</b></span>
        </div>
        <div class="col-8 my-0 p-0  text-right py-0">
          <span>
   
              {{ store.currentOrder.user_phone }}
       

          </span>
        </div>
        <div class="col-4 my-0 p-0 py-0" style="">
          <span><b>direccion </b></span>
        </div>
        <div class="col-8 my-0 p-0  text-right py-0">
          <span>
      
              {{ store.currentOrder.user_address }}

    
          </span>
        </div>




        <div class="col-6 my-0 p-0 py-0" style="">
          <span><b>metodo de pago</b></span>
        </div>
        <div class="col-6 my-0 p-0  text-right py-0">
          <span>
   
              {{ store.currentOrder.payment_method }}
          </span>
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




   
   </div>

  <template #footer>

    <div class="col-12 mb-0 pb-0 px-0 m-0" style="display: flex;justify-content: space-between;gap: 1rem;">
      
      <Button  v-if="store.currentOrder.current_status == 'generada'" size="small" @click="orderService.prepareOrder(store.currentOrder.order_id)" style="border-radius: 0.3rem;width: 100%;" severity="success" label="Preparar" ></Button>

      <Button v-if="store.currentOrder.current_status != 'enviada' && store.currentOrder.current_status != 'cancelada'

      
      " size="small" @click="cancelDialogVisible = true" style="border-radius: 0.3rem;width: 100%;" severity="danger" label="cancelar" ></Button>


      <Button v-if="store.currentOrder.current_status == 'en preparacion'"  size="small" @click="orderService.sendOrder(store.currentOrder.order_id)" style="border-radius: 0.3rem;width: 100%;" severity="success" label="enviar" ></Button>
      <Button size="small"  style="border-radius: 0.3rem;width: 100%;" @click="IMPRIMIR" severity="warning" label="imprimir" ></Button>
    </div>

    
  </template>


  <Button class="shadow-4" @click="store.setVisible('currentOrder',false)" icon="pi pi-times" rounded severity="danger" style="position: absolute;top: 0;border-radius: 50%; right:-1rem; top: -1rem;"></Button>


  <!-- {{ store.currentOrder }} -->
  </Dialog>
 



</template>

<script setup>
import { formatoPesosColombianos } from '../../service/formatoPesos';
import {onMounted, ref} from 'vue'
import {useOrderStore} from '../../store/order'
import { orderService } from '../../service/orderService';











const store = useOrderStore()

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

    ventanaImpresion.document.write('<style> @media print { html{height: min-content;} .negrilla{background-color:black !IMPORTANT; color:white !IMPORTANT;} *{ font-family: sans-serif; padding: 0 !IMPORTANT; margin: 0rem !IMPORTANT; font-size:0.8rem !IMPORTANT} body { -webkit-print-color-adjust: exact; /* Chrome, Safari */ color-adjust: exact; /* Firefox */ } } </style>');
    ventanaImpresion.document.write('</head><body>');
    ventanaImpresion.document.write(contenidoFactura);

    ventanaImpresion.document.write('</body></html>');

    ventanaImpresion.document.close();

    // Imprimir la ventana
    ventanaImpresion.print();

    // Cerrar la ventana después de 1 segundo (puedes ajustar este tiempo)
    setTimeout(() => {
        ventanaImpresion.close();
    }, 0.01);
};

onMounted(async() => {
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

const  submitCancel = () => {
  if (cancelData.value.responsible ) {
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

* {
  text-transform: uppercase;
  font-size: 0.9rem;
  /* color: black; */
}


.notas{
  text-transform: lowercase;
}
.notas::first-letter{
  text-transform: uppercase;
}



span{
  color:black
}

*::first-letter {
  text-transform: uppercase;
}
</style>


















