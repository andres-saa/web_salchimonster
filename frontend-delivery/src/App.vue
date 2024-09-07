<script setup>
import { onBeforeUnmount, onMounted, onUnmounted, ref } from 'vue';
import router from './router';
import { useOrderStore } from './store/order';
import { useSitesStore } from './store/site';
import { orderService } from './service/orderService';
import { URI } from './service/conection';




const sitestore = useSitesStore();
const store = useOrderStore();

const requestNotificationPermission = async () => {
    const permission = await Notification.requestPermission();
    if (permission !== 'granted') {
        alert('Las notificaciones están deshabilitadas. Por favor, habilite las notificaciones para obtener alertas en tiempo real.');
    }
};


const playNotificationSound = () => {

        store.Notification.play().then(() => {
            store.Notification.loop = true;

})
}

const stopNotificationSound = () => {
  
        store.Notification.loop = false; // Desactivar el bucle
        store.Notification.pause(); // Pausar la reproducción
        store.Notification.currentTime = 0; // Reiniciar el tiempo a 0

};


onMounted(() => {
    requestNotificationPermission();

    const fetchOrdersAndNotify = async () => {
        try {
            const site_id = sitestore.site.site_id;
            const order_response = await orderService.is_recent_order_generated(site_id);
            if (order_response) {
                 store.last_order_id != order_response?  await store.getTodayOrders() : ''
                    store.last_order_id = order_response;
                
                playNotificationSound();
                
            
            } else{
                stopNotificationSound()
            }
        } catch (error) {
            console.error('Error fetching orders:', error);
        }
    };
    
    const intervalId = setInterval(fetchOrdersAndNotify, 15000);    
    onUnmounted(() => {
        clearInterval(intervalId);
    });
});

const notif = ref(true)



const sonido = new Audio('/sound/beep.mp3')
const acept = () => {
    notif.value = false
    sonido.play()
}
</script>

<template>
    <div  style="width:100vw;height:100vh;display:flex;position: absolute; align-items:center;justify-content:center; z-index: 999;top:0;left:0;background-color:rgba(0,0,0,0.5)" :closable="false" v-if="notif">
        <div style="width:20rem;display:flex; gap:1rem;flex-direction:column;justify-content:center;align-items:center">
            <img style="width:100%;" src="/images/NOTI.png" alt="">
            <Button  rounded @click="acept" style="width:max-content;border-radius:2rem" severity="help" icon="pi pi-bell" label="Aceptar notificaciones"></Button>
        </div>
    </div>
    <router-view class="col-12 p-0" />
</template>
