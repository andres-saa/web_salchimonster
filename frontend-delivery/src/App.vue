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
    if (store.Notification.readyState >= 2) { // Verifica que el audio esté suficientemente cargado para reproducirse
        store.Notification.play().then(() => {
            store.Notification.loop = true;
        }).catch(error => {
            console.error('Error playing sound:', error);
        });
    } else {
        console.error('Sound not ready for playback');
    }
};


onMounted(() => {
    requestNotificationPermission();
    const fetchOrdersAndNotify = async () => {
        try {
            const site_id = sitestore.site.site_id; // Asumiendo que `sitestore` está correctamente importado/inicializado
            const order_response = await orderService.is_recent_order_generated(site_id);
            if (order_response && store.last_order_id !== order_response) {
                store.last_order_id = order_response;
                await store.getTodayOrders(); // Asegúrate de actualizar el estado con el nuevo conteo
                playNotificationSound();
                
                if (Notification.permission === 'granted') {
                    const notification = new Notification('Nueva Orden en la página de WhatsApp', {
                        body: 'Nueva Orden en la página de WhatsApp',
                        icon: '/images/logo.png',
                        image: `${URI}/read-product-image/300/site-${site_id}`
                    });
                    notification.onclick = () => {
                        window.focus();
                    };
                }
            }
        } catch (error) {
            console.error('Error fetching orders:', error);
        }
    };
    
    const intervalId = setInterval(fetchOrdersAndNotify, 3000);
    onUnmounted(() => {
        clearInterval(intervalId);
    });
});

</script>

<template>
    <router-view class="col-12 p-0" />
</template>
