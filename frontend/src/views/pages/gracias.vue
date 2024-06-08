<template>
    <div class="p-2 col-12 my-3" style="height: auto;min-height: 90vh; display: flex; justify-content: center; align-items: center;">
        <div class="shadow-3 p-4" style="border-radius: 0.5rem; max-width: 500px;">
            <p class="text-4xl text-center mt-5" style="font-weight: bold;"> 🤩{{user.user.name.toUpperCase()}}🤩</p>
            <p class="text-2xl text-center mb-5" style="font-weight: bold;">🔥MUCHAS GRACIAS POR TU COMPRA!🔥</p>

            <p class="text-4xl text-center my-5" style="font-weight: bold; text-transform: uppercase;"> <span class="text-2xl">ID DEL PEDIDO</span>  <br> #{{ store.last_order }}</p>

             <!-- {{ store.cart }} -->
            <!-- <pre>{{ text }}</pre> -->
            
            <p class="text-2xl text-center my-3 p-3" style=" border-radius: .3rem; background-color: var(--primary-color); color: white;">Hemos recibido tu pedido y en breve será despachado</p>
   

            <div style="display: flex;flex-direction: column;gap: 1rem;">
             
                
                <router-link to="/">
                <Button icon="pi " iconPos="right"  severity="help" style="font-weight: bold; background-color: black; width: 100%;" label="PUEDES RASTREARLO AQUI"></Button>
                </router-link>
         
                <router-link to="/">
                    <Button icon="pi pi-arrow-left" severity="danger" outlined style="font-weight: bold; border: none; width: 100%;" label="VOLVER AL MENU"></Button>
                </router-link>

            </div>
               
        </div>
    </div>
</template>

<script setup>

import { ref, onMounted,onBeforeUnmount,onBeforeMount } from 'vue';
import { usecartStore } from '../../store/shoping_cart';
import {useUserStore} from '../../store/user'
import { useSitesStore } from "../../store/site";
import router from '../../router';
const site = useSitesStore();

const text = ref('');
const store = usecartStore();
const user = useUserStore()
onMounted(() => {
    text.value = `Hola soy *${user.user.name.toUpperCase()}* 🤗 acabo de hacer el siguiente pedido en la página web. El número de la orden es *#${store.last_order}*.\n
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

// onBeforeMount(() => {
//     store.cart.products.length <= 0? router.push('/'):''
// })

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