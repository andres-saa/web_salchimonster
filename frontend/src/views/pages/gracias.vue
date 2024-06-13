<template>
    <div class="p-2 col-12 my-3" style="height: auto;min-height: 90vh; display: flex; justify-content: center; align-items: center;">
        <div class="shadow-3 p-4" style="border-radius: 0.5rem; max-width: 500px;">
            <p class="text-4xl text-center mt-5" style="font-weight: bold;"> 🤩{{user.user.name.toUpperCase()}}🤩</p>
            <p class="text-2xl text-center mb-5" style="font-weight: bold;">🔥MUCHAS GRACIAS POR TU COMPRA!🔥</p>

            <p class="text-4xl text-center my-5" style="font-weight: bold; text-transform: uppercase;"> <span class="text-2xl">ID DEL PEDIDO</span>  <br> #{{ store.last_order }}</p>

             <!-- {{ store.cart }} -->
            <!-- <pre>{{ text }}</pre> -->

            
            <p class="text-2xl text-center my-3 p-3" style=" border-radius: .3rem; background-color: var(--primary-color); color: white;">Hemos recibido tu pedido y en breve será despachado</p>




            <div id="factura" style="width: 100%;text-transform: uppercase;">


     




<div class="" style="width: auto; color: black;">



    
        <!-- <p style="padding: 0;color: black; margin: auto; margin-bottom: 1rem; width: max-content;min-width: max-content; ">
          <b>
            fecha: {{ store.currentOrder.latest_status_timestamp?.split('T')[0] }}

          </b>
        </p> -->
     

<!-- <img src="https://cocina.salchimonster.com/images/logo.png" alt="" style="width: 2cm;"> -->
    <div class=""
      style="font-weight: bold;color:white;margin: 0; background-color: black;align-items: center;display: grid; grid-template-columns: auto auto; ">

      <div style="width: 100%;" class="p-1">

        <b> PRODUCTOS</b>


      </div>
    
      <div class=p-1 >
        <p style="text-align: end;font-weight: bold;">
          <b>
            TOTAL
          </b>
          
        </p>
      </div>

    </div>

    <div   v-for="product in store.cart.products">

      <div style="display: grid; grid-template-columns: auto auto;">
       
        <p class="p-0 m-0">
          {{ product.quantity }}
          {{ product.product.product_name }}
        </p>
    
    
      <!-- <div >
        <p style="text-align: end;color: black;">
          {{ formatoPesosColombianos(product.price) }}
        </p>
      </div> -->
      <div >
        <p style="text-align: end;color: black;">
          {{ formatoPesosColombianos(product.total_cost) }}
        </p>
      </div>

      </div>

      <div style="background-color: rgba(0, 0, 0, 0.286); height: 1px;">

</div>  

    </div>
    




    <div   v-for="(items, grupo) in {ADICIONES:store.cart.additions.filter(a => a.group == 'ADICIONES'),
                                    SALSAS:store.cart.additions.filter(a => a.group == 'SALSAS'),
                                    CAMBIOS:store.cart.additions.filter(a => a.group == 'CAMBIOS')} " :key="grupo"
      style="position: relative; margin-top: 0.5rem;">



      <p class="p-1" style="background-color: black;font-weight: bold; color: white; width: 100%;margin: 0;">
        <b>{{ grupo}}</b>

      </p>


      <div   v-for="aditional in items">
        <div style="display: grid; grid-template-columns: auto 20%;align-items: center;">

          <div >
            <p >
              {{ aditional.quantity }}  {{ aditional.name }}
            </p>
          </div>

          
                <div >
                  <p style="text-align: end;color: black;">
                    {{ formatoPesosColombianos(aditional.price * aditional.quantity) }}
                  </p>
                </div>
         
        </div>
        






      </div>

    </div>








    <div class="" style="display: grid ;color: ;margin-top: 0.5rem; grid-template-columns: auto auto">
            <div class="">
              <span style="font-weight: bold;"><b>Subtotal</b></span>
            </div>
            <div class="">
              <p  style="text-align: end;font-weight: bold; color: black;">
                <b >{{ formatoPesosColombianos(store.cart.total_cost) }}</b>
              </p>
            </div>
            <div class="">
              <span style="font-weight: bold;"><b>Domicilio</b></span>
            </div>
            <div class="">

            
              <p style="text-align: end;font-weight: bold;color: black;"> <b>
      
                  {{ formatoPesosColombianos(site.location?.neigborhood?.delivery_price) }}
                </b>
              </p>
            </div>
            <div class="">
              <span  style="font-weight: bold;color: black;" ><b>Total</b></span>
            </div>
            <div class="">

              <p style="text-align: end;color: black;font-weight: bold;"><b>{{ formatoPesosColombianos(site.location?.neigborhood?.delivery_price + store.cart.total_cost)
              }}</b></p>

            </div>
            <div class="">
              
            </div>

          </div>




   
      <!-- <div class="">

        <p style="text-align: end;color: black;font-weight: bold;"><b>{{ formatoPesosColombianos(store.currentOrder.delivery_price + store.currentOrder.total_order_price)
        }}</b></p>

      </div>
      <div class="">
        
      </div>

    </div>
    <p  style="font-weight: bold;background-color: black;color: white;padding: 0; margin: 0; margin-top: 0.5rem;"><b>Notas</b></p>
        <p class="notas" style="border: 1px solid;margin: 0;color: black; padding: 0.5rem;">
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

        </div> -->
   
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
   

            <div style="display: flex;flex-direction: column;gap: 1rem;">
             
                
                <router-link to="/rastrear-pedido">
                <Button class="mt-3" icon="pi " iconPos="right"  severity="warning" style="font-weight: bold; width: 100%;" label="PUEDES RASTREARLO AQUI"></Button>
                </router-link>
         

                <a  v-if="user.user.payment_method_option.id == 6" :href="whatsappUrl" target="_blank">                    <Button icon="pi pi-whatsapp" severity="danger" class="wsp" style="font-weight: bold;background-color: #00b66c; border: none; width: 100%;" label="REALIZAR TRANSFERENCIA"></Button>
                </a>
                <router-link to="/">
                    <Button  icon="pi pi-arrow-left" severity="danger" outlined style="font-weight: bold; border: none; width: 100%;" label="VOLVER AL MENU"></Button>
                </router-link>


               

            </div>
               
        </div>
    </div>
</template>

<script setup>

import { ref, onMounted,onBeforeUnmount,onBeforeMount,computed } from 'vue';
import { usecartStore } from '../../store/shoping_cart';
import {useUserStore} from '../../store/user'
import { useSitesStore } from "../../store/site";
import router from '../../router';
const site = useSitesStore();
import { formatoPesosColombianos } from '@/service/formatoPesos';
const text = ref('');
const store = usecartStore();
const user = useUserStore()


const obtenerHoraFormateadaAMPM = (fecha) => {
  const fechaParseada = new Date(fecha);
  const horas = fechaParseada.getHours();
  const minutos = fechaParseada.getMinutes();
  const ampm = horas >= 12 ? 'pm' : 'am';
  const hora12 = horas % 12 || 12;
  const horaFormateada = hora12 < 10 ? '0' + hora12 : hora12;
  const minutosFormateados = minutos < 10 ? '0' + minutos : minutos;

  return `${horaFormateada}:${minutosFormateados} ${ampm}`;
};






onMounted(() => {
    text.value = `Hola soy *${user.user.name.toUpperCase()}* 🤗 acabo de hacer el siguiente pedido en la página web. El número de la orden es *#${store.last_order}*.\n

*Escribo para Realizar la Transferecia*\n
*🛒 PRODUCTOS*\n${store.cart.products.map(product => `*${product.quantity}* ${product.product.product_name}`).join('\n')}\n\n`;

    if (store.cart.additions.length > 0) {
        text.value += `*➕ ADICIONES*\n${store.cart.additions.filter(a => a.group == 'ADICIONES').map(product => `*${product.quantity}* ${product.name}`).join('\n')}\n\n`;
    }

    if (store.cart.additions.filter(a => a.group == 'CAMBIOS').length > 0) {
        text.value += `*➕ CAMBIOS*\n${store.cart.additions.filter(a => a.group == 'CAMBIOS').map(product => `*${product.quantity}* ${product.name}`).join('\n')}\n\n`;
    }

    if (store.cart.additions.filter(a => a.group == 'SALSAS').length > 0) {
        text.value += `*➕ SALSAS*\n${store.cart.additions.filter(a => a.group == 'SALSAS').map(product => ` ${product.name}`).join('\n')}\n\n`;
    }

    text.value += `*📍 DIRECCIÓN*\n${user.user.address} BARRIO ${site.location?.neigborhood?.name}\n
*📞 TELEFONO*\n${user.user.phone_number}\n
*📝 NOTAS*\n${store.cart.order_notes || 'Sin notas'}\n
*💰 METODO DE PAGO*\n${user.user.payment_method_option.name}\n
*Muchas Gracias* 🙏`;

    console.log(text.value);

});



const whatsappUrl = computed(() => {
  const baseUrl = 'https://api.whatsapp.com/send';
  const urlParams = new URLSearchParams({
    phone: '573053447255',
    text: text.value
  });
  return `${baseUrl}?${urlParams.toString()}`;
});


onBeforeUnmount( () => {
    user.user = {
          name:'',
          neigborhood:'',
          address:'',
          phone_number:'',
          payment_method_option:''
      },

      store.cart = {
        products: [],
        total_cost: 0,
        additions: []  // Nueva propiedad para manejar las adiciones a nivel del carrito
    }
})

onBeforeMount(() => {
    store.cart.products.length <= 0? router.push('/'):''
})

</script>


<style scoped>

@keyframes parpadeo {
  0% { filter:brightness(1); }
  50% {filter:brightness(1.1);transform: scale(1.01); }

}

.wsp{
    animation:  parpadeo ease infinite .5s;
    transition: all ease .5s;
}
</style>