<template>
  <div>
    <Dialog v-model:visible="cancelDialogVisible" closeOnEscape :closable="true" modal style="width: 30rem;">
      <template #header>
        <h3> <b>Cancelar Orden</b> </h3>
      </template>
      <form @submit.prevent="submitCancel" style="display: flex;gap: 1rem; flex-direction: column;align-items:start">
  
        <span for="responsible">Responsable</span>
        <Dropdown style="width: 100%;" id="responsible" v-model="cancelData.responsible" :options="responsibles" optionLabel="name"
          placeholder="Selecciona un responsable"></Dropdown>
  
  
        <span for="reason">Razón</span>
        <Textarea style="resize: none; text-transform: lowercase; width:100%" id="reason" v-model="cancelData.reason" rows="5"
          placeholder="Escribe la razón de la cancelación"></Textarea>
  
        <Button style="width: 100%;border-radius:0.5rem" label="cancelar" type="submit" class="p-button-danger" />
      </form>
  </Dialog>



  <Dialog v-model:visible="cancelDialogVisibleAdmin" closeOnEscape :closable="true" modal style="width: 30rem;">
    <template #header>
      <h3> <b>Cancelar Orden</b> </h3>
    </template>
    <form @submit.prevent="sendRequest" style="display: flex;gap: 1rem; flex-direction: column;align-items:start">

      <span class="advert" style="text-transform: lowercase; color:red;  font-weight: bold;"> Desde el 16 de mayo de 2024, la cancelación de órdenes requerirá autorización.</span>
      <span for="responsible">Responsable</span>
      <Dropdown style="width: 100%;" id="responsible" v-model="cancelData.responsible" :options="responsibles" optionLabel="name"
        placeholder="Selecciona un responsable"></Dropdown>

      <span for="reason">Razón</span>
      <Textarea style="resize: none; text-transform: lowercase; width:100%" id="reason" v-model="cancelData.reason" rows="5"
        placeholder="Escribe la razón de la cancelación"></Textarea>

      <Button  style="width: 100%;border-radius:0.5rem" label="solicitar cancelacion" type="submit" class="p-button-danger" />
    </form>
  </Dialog>



  <Dialog :closable="false" style="width: 30rem;" modal v-model:visible="showDeleteDeliveryPrice">

   <span style="text-transform: capitalize;">
    Esta seguro de llevar a $0.00 el valor del domicilio para la orden <b>{{store.currentOrder.order_id}} </b> del cliente  <b>{{store.currentOrder.user_name}}</b>?
   </span> 
   
   
   <template #footer>

    <div class="col-12 mb-0 pb-0 px-0 m-0" style="display: flex;justify-content: space-between;gap: 1rem;">

      <Button  text size="small"
        @click="() => {orderService.deliveryZero(store.currentOrder.order_id); showDeleteDeliveryPrice = false} " style="border-radius: 0.3rem;width: 100%;"
        severity="danger" label="si"></Button>

      <Button @click="showDeleteDeliveryPrice = false"  size="small" style="border-radius: 0.3rem;width: 100%;" severity="danger"
        label="no"></Button>
    </div>




  </template>



  </Dialog>


  <Dialog class="mx-3"  closeOnEscape :closable="false" v-model:visible="store.visibles.currentOrder" modal
    style="max-height: 95vh;width: 35rem; position: relative;">

    <div class="">
        <div  >
           

            <p :class="`estado ${store.currentOrder?.current_status?.split(' ')[0]}`">
                {{ getOrderMessage(store.currentOrder) }}
            </p>

          
        </div>

    </div>
    
    <div id="factura" style="width: 100%;">

      <!-- {{ store.currentOrder.pe_json }} -->

      <Tag style="" class="tag mb-2" severity="success" v-if="store.currentOrder.responsible_id"> <i class="pi pi-whatsapp mr-2"></i>   TRANSFERENCIA APROBADA</Tag> <br> 
      
      <Tag class="tag" severity="success" v-if="store.currentOrder.responsible_id">  {{store.currentOrder.name}}</Tag>

     
    
      <div class="" style="width: auto;">
       
          <p class="" id="id" style="font-weight: bold;min-width: 100%; width: max-content; text-align: center; color: black; margin:0rem;"> ID:{{ store.currentOrder.order_id }} </p>


          <p class="" id="id" style="font-weight: bold;min-width: 100%; width: max-content; text-align: center; color: black; margin:0rem;"> {{ store.currentOrder.user_name }} </p>



          
              <p style="padding: 0;color: black;text-align: center; margin: auto; margin-bottom: 1rem; width: max-content;min-width: max-content;display: flex;justify-content: center; flex-direction: column ">
                <b>
                  fecha: {{ store.currentOrder.latest_status_timestamp?.split('T')[0] }}
                </b>

                <b>
                  Hora: {{ store.currentOrder.latest_status_timestamp?.split('T')[1]?.split(':')?.slice(0,2)?.join(':') }}

                </b>
              </p>
           

 <!-- <img src="https://cocina.salchimonster.com/images/logo.png" alt="" style="width: 2cm;"> -->
          <div class=""
            style="font-weight: bold;color:white;margin: 0; background-color: black;align-items: center;display: grid; grid-template-columns: auto auto; ">

            <div style="width: 100%;" >

              <b> productos</b>


            </div>
          
            <div >
              <p style="text-align: end;font-weight: bold;">
                <b>
                  total
                </b>
                
              </p>
            </div>

          </div>

         
          <div  v-for="product in store?.currentOrder?.pe_json?.listaPedidos">

            <div style="display: grid; grid-template-columns: auto auto;">
             
              <p class="p-0 m-0">
            (    {{ product.pedido_cantidad }} )
                {{ product.pedido_nombre_producto }}
                <br>
              </p>
          
              
              
          
            <!-- <div >
              <p style="text-align: end;color: black;">
                {{ formatoPesosColombianos(product.price) }}
              </p>
            </div> -->
            <div >
              <p v-if="product.pedido_base_price" style="text-align: end;color: black;">
                <!-- {{ formatoPesosColombianos(product.price) }} -->
                {{ formatoPesosColombianos(product.pedido_base_price * product.pedido_cantidad) }}
              </p>

              <p v-else style="text-align: end;color: black;">
                <!-- {{ formatoPesosColombianos(product.price) }} -->
                {{ formatoPesosColombianos(product.pedido_precio) }}
              </p>
            </div>


            </div>

            <p v-if="product.lista_productocombo?.length > 0" class="p-0 m-0"><b>COMBO INCLUYE</b></p>
            <p v-if="product.lista_productocombo" class="p-0 m-0 ml-5" style="" v-for="i in product.lista_productocombo" > -- <b>{{i.pedido_cantidad  }}</b>  {{i.pedido_nombre  }} </p> 


            <!-- <p> {{ product.modificadorseleccionList }} </p> -->


            <!-- {{ product.modificadorseleccionList.filter(p => p.pedido_productoid == product.pedido_productoid) }} -->

     
              <div style="display: flex;width: ; justify-content: space-between;" class="p-0 m-0" v-for="i in  product.modificadorseleccionList">
         
                <p class="p-0 m-0 " style="">
       
                  - ( {{ product.pedido_cantidad }} ) <b>{{ i.modificadorseleccion_cantidad  }}</b> {{ i.modificadorseleccion_nombre }}
                </p>

                <p class="p-0 m-0" style="text-align: end;"> {{ formatoPesosColombianos(i.pedido_precio * i.modificadorseleccion_cantidad * product.pedido_cantidad)  }} </p>

            </div>

            <div style="background-color: rgba(0, 0, 0, 0.286); height: 1px;">

</div>  

          </div>
          



<!-- 
          <div s  v-for="(items, grupo) in store.currentOrder.additional_items" :key="grupo"
            style="position: relative; margin-top: 0.5rem;">



            <p style="background-color: black;font-weight: bold; color: white; width: 100%;margin: 0;">
              <b>{{ grupo }}</b>

            </p>


            <div   v-for="aditional in items">
              <div style="display: grid; grid-template-columns: auto 20%;align-items: center;">

                <div >
                  <p >
                    {{ aditional.aditional_quantity }}  {{ aditional.aditional_name }}
                  </p>
                </div>

                <div >
                  <p style="text-align: end;color: black;">
                    {{ formatoPesosColombianos(aditional.total_aditional_price) }}
                  </p>
                </div>
              </div>
              <div style="background-color: rgba(0, 0, 0, 0.286); height: 1px;">

              </div>






            </div>

          </div>
 -->




 






          <div class="" style="display: grid ;color: ;margin-top: 0.5rem; grid-template-columns: auto auto">
            <div class="">
              <span style="font-weight: bold;"><b>Subtotal</b></span>
            </div>
            <div class="">
              <p  style="text-align: end;font-weight: bold; color: black;">
                <b >{{ formatoPesosColombianos(store.currentOrder.pe_json.delivery.delivery_pagocon -  store.currentOrder.pe_json.delivery.delivery_costoenvio) }}</b>
               
              </p>
            </div>


            <div class="">
              <span style="font-weight: bold;"><b>Domicilio</b></span>
            </div>

            <div class="">
              <p style="text-align: end;font-weight: bold;color: black;"> <b>
               
                  {{ formatoPesosColombianos(store.currentOrder.pe_json.delivery.delivery_costoenvio) }}
                </b>
              </p>
            </div>















            <div class="">
              <span  style="font-weight: bold;color: black;" ><b>Total</b></span>
            </div>
            <div class="">

              <p style="text-align: end;color: black;font-weight: bold;"><b>{{ formatoPesosColombianos(store.currentOrder.pe_json.delivery.delivery_pagocon)
              }}</b></p>

            </div>
            <div class="">
              
            </div>

          </div>
          <p  style="font-weight: bold;background-color: black;color: white;padding: 0; margin: 0; margin-top: 0.5rem;"><b>Notas</b></p>
          <p
              class="notas"
              style="border: 1px solid; margin: 0; color: black; padding: 0.5rem;"
              v-html="formattedNotes"
            ></p>

           



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





            <div class="" style="">
              <span><b>Metodo de entrega</b></span>
            </div>
            <div class="">
              <p style="text-align: end;color: black;">

                {{ store.currentOrder.order_type }}
              </p>

            </div>




            <div class="" style=""  v-if="store.currentOrder.placa">
              <span><b>Placa del vehiculo</b></span>
            </div>
            <div class=""  v-if="store.currentOrder.placa">
              <p style="text-align: end;color: black;">

                {{ store.currentOrder.placa }}
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
            <div style="" v-if="store.currentOrder.order_type != 'Pasar a recoger'">
              <span><b>direccion </b></span>
            </div>
            <div v-if="store.currentOrder.order_type != 'Pasar a recoger'" >
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

  


        <Button v-if="store.currentOrder.current_status == 'en preparacion'" size="small"
          @click="orderService.sendOrder(store.currentOrder.order_id)" style="border-radius: 0.3rem;width: 100%;"
          severity="success" label="enviar"></Button>
        <Button size="small" style="border-radius: 0.3rem;width: 100%;" @click="IMPRIMIR" severity="warning"
          label="imprimir"></Button>

          <Button  size="small" style="border-radius: 0.3rem;width: 100%;" @click="cancelDialogVisibleAdmin = true" severity="danger"
          label="CANCELAR "></Button>  


  
      </div>


      <div class="mt-3">
        <Button       @click="changePaymentDialog = true"
        label="Cambiar metodo de pago" severity="success"></Button>
      </div>

    </template>


    <Button class="shadow-4" @click="store.setVisible('currentOrder', false)" icon="pi pi-times" rounded severity="danger"
      style="position: absolute;top: 0;border-radius: 50%; right:-1rem; top: -1rem;"></Button>



  </Dialog>

  </div>
  

  <Dialog v-model:visible="changePaymentDialog" closeOnEscape :closable="true" modal style="width: 30rem;">
  <template #header>
    <h3><b>Cambiar Método de Pago</b></h3>
  </template>
  <form @submit.prevent="submitChangePayment" style="display: flex; gap: 1rem; flex-direction: column; align-items: start">
    <span for="paymentMethod">Método de Pago actual</span>

    <Tag class="px-4" severity="warning">
      <span for="paymentMethod"> <b>{{ store.currentOrder.payment_method }}</b></span>

    </Tag>

    <span for="paymentMethod">Nuevo método de Pago</span>
    <Dropdown
      style="width: 100%;"
      id="paymentMethod"
      v-model="newPaymentMethod"
      :options="paymentMethods"
      optionLabel="name"
      optionValue="id"
      placeholder="Selecciona un método de pago"
      required
    ></Dropdown>
    <Button
      style="width: 100%; border-radius: 0.5rem"
      label="Cambiar"
      type="submit"
      class="p-button-help"
    />
  </form>
</Dialog>

</template>


<script setup>
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { onMounted,computed, ref } from 'vue'
import { useOrderStore } from '../../store/order'
import { orderService } from '../../service/orderService';
import {fetchService} from '../../service/utils/fetchService'
import printJS from 'print-js';
import { URI } from '../../service/conection';
const cancelDialogVisibleAdmin = ref(false)
const store = useOrderStore()



function formatNotes(notes) {
  if (!notes) return ''

  // 1. Reemplazar saltos de línea
  let result = notes.replace(/\n/g, '<br>')

  // 2. Regex específica para el formato AAA-123
  //    - \b límites de palabra
  //    - [A-Za-z]{3} 3 letras
  //    - - guion
  //    - \d{3} 3 dígitos
  result = result.replace(/\b([A-Za-z]{3}-\d{3})\b/g, (match) => {
    return `<strong style="text-transform:uppercase">${match.toUpperCase()}</strong>`
  })

  return result
}
// Computed para formatear las notas en tiempo real (si cambian en el store)
const formattedNotes = computed(() => {
  return formatNotes(store.currentOrder.order_notes)
})
const getOrderMessage = (order) => {
    const hora = order.latest_status_timestamp?.split('T')[1]?.split(':')?.slice(0,2)?.join(':') 
    switch (order.current_status) {
        case "enviada":
            return `El pedido fue enviado a su domicilio a las ${hora}`;
        case "cancelada":
            return `El pedido fue cancelado a las ${hora}\nResponsable: ${order.responsible}\nRazón: ${order.reason}`;
        case "en preparacion":
            return `El pedido está en preparación desde las ${hora} y será enviado en breve.`;
        case "generada":
            return `Hemos recibido su pedido a las ${hora} y empezaremos a prepararlo en breve. Gracias por su espera.`;
        default:
            return "";
    }
};



const submitChangePayment = async () => {
  if (newPaymentMethod.value) {
    try {
      await fetchService.put(
        `${URI}/change-method/${store.currentOrder.order_id}/${newPaymentMethod.value}`,
        
        `Cambiando método de pago para la orden ${store.currentOrder.order_id}`
      )

      // Opcional: Actualizar los datos de la orden si es necesario
      // await store.fetchCurrentOrder()

      // Cerrar el diálogo
      changePaymentDialog.value = false
      store.visibles.currentOrder= false
      store.getTodayOrders()
      // Opcional: Mostrar una notificación de éxito
      console.log('Método de pago cambiado exitosamente')
    } catch (error) {
      console.error('Error al cambiar el método de pago:', error)
      // Opcional: Mostrar una notificación de error
    }
  }
}




const travelDialog = ref(false);

const changePaymentDialog = ref(false)

// Variable para almacenar el nuevo método de pago seleccionado
const newPaymentMethod = ref(null)

// Variable para almacenar los métodos de pago obtenidos del backend
const paymentMethods = ref([])



onMounted(async () => {
  try {
    const response = await fetchService.get(`${URI}/payment_methods`)
    paymentMethods.value = response // Asegúrate de ajustar según la estructura de la respuesta
  } catch (error) {
    console.error('Error al obtener métodos de pago:', error)
    // Opcional: Manejar errores, mostrar notificaciones, etc.
  }})


const sendRequest = async() => {
  const data = {
    "order_id": store.currentOrder.order_id,
    "responsible": cancelData.value.responsible?.name,
    "reason": cancelData.value.reason
  }
  await orderService.create_cancellling_request(data)
  cancelDialogVisibleAdmin.value = false
  store.Notification.pause()
  store.Notification.currentTime = 0
}

const subtotal = computed(() => {
  return store.currentOrder.pe_json.listaPedidos.reduce((acc, product) => {
    // Calcula el total del producto base
    let productTotal = product.pedido_cantidad * product.pedido_precio;

    // Verifica si el producto tiene modificadores
    // if (product.modificadorseleccionList && product.modificadorseleccionList.length > 0) {
    //   // Filtra los modificadores asociados a este producto
    //   const productModifiers = product.modificadorseleccionList?.filter(
    //     mod => mod.pedido_productoid == product.pedido_productoid
    //   );

    //   // Calcula el total de los modificadores
    //   const modifiersTotal = productModifiers.reduce((modAcc, modifier) => {
    //     return modAcc + modifier.modificadorseleccion_cantidad * modifier.pedido_precio;
    //   }, 0);

    //   // Agrega el total de los modificadores al total del producto
    //   productTotal += modifiersTotal;
    // }

    // Agrega el total del producto al acumulador
    return acc + productTotal;
  }, 0);
});


const total = computed(() => {
  return subtotal.value + store.currentOrder.delivery_price;
});

const showDeleteDeliveryPrice = ref(false)



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

  ventanaImpresion.document.write('<style>  @media print { html{height: min-content;}  *{text-transform:uppercase;align-items:center; width:100%; font-family: sans-serif;padding:0;margin:0; font-size:o.9rem !IMPORTANT} body { padding:0; -webkit-print-color-adjust: exact; /* Chrome, Safari */ color-adjust: exact; /* Firefox */ } }  </style>');
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


// const IMPRIMIR = () => {
//   printJS({
//     printable: 'factura',
//     type: 'html',
//     targetStyles: ['*'],
//     style: `
//       * { font-size: 30pt; }
//     `
//   });
// };


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



const deliveryZero = async(order_id) => {
    await orderService.deliveryZero(order_id)
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

.advert::first-letter{
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
  * {
    font-size: 30pt ; /* Ajusta el tamaño de fuente que necesites */
  }
  #id{
    font-size: 40pt;
  }

  .tag{
    display: none;
  }
}



sticky-header {
    /* background-color: white; */
    position: sticky;
    top: 3rem;
    z-index: -1;
}

.container {
    max-width: 1024px;
    margin: 0 auto;
    padding: 1rem;
}

/* Título */
.title {
    font-size: 2rem;
    font-weight: bold;
    text-align: center;
    padding: 1rem 0;
}

/* Contenedor de entrada */
.input-container {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.input-text {
    flex: 1;
    padding: 0.5rem;
    /* border: 1px solid; */
    /* box-shadow: 0 0 10px #00000030; */
    width: 3rem
}

.search-button {
    /* background-color: var(--p-primary-color); */
    font-weight: bold;
    border: none;
    padding: 0.5rem 1.5rem;
    min-width: max-content;
}

/* Mensajes de estado */
.estado {
    font-size: 1.25rem;
    text-transform: lowercase;
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
}

/* Colores por estado */
.generada {
    background-color: rgba(255, 255, 0, 0.8);
}

.enviada {
    background-color: rgb(153, 255, 0);
}

.en {
    background-color: rgb(84, 212, 255);
}

.cancelada {
    background-color: rgba(255, 84, 84, 0.7);
}

.no-existe {
    background-color: #f9741632;
    text-align: center;
}

/* Capitalización del primer carácter */
.estado::first-letter {
    text-transform: capitalize;
}


</style>


















