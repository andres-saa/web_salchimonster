<script setup>
import { URI_SOCKET } from '@/service/conection';
import { onBeforeUnmount, onMounted , onUnmounted,ref} from 'vue';
import router from './router';
import { useOrderStore } from './store/order';
import { useSitesStore } from './store/site';
const sitestore = useSitesStore()
const store = useOrderStore();
import { orderService } from './service/orderService';



const requestNotificationPermission = async () => {
    const permission = await Notification.requestPermission();
    if (permission !== 'granted') {
        alert('Las notificaciones están deshabilitadas. Por favor, habilite las notificaciones para obtener alertas en tiempo real.');
    }
}

onMounted(() => {
  // Solicitar permiso de notificación al cargar el componente
  requestNotificationPermission();

  // Definir una función que realiza las acciones deseadas
  async function fetchOrdersAndNotify() {
    try {
      const site_id = await sitestore.site.site_id; // Asumiendo que `sitestore` está correctamente importado/inicializado
      const count_orders = await orderService.getOrderCount(site_id); // Asumir `orderService` está importado

      if (store.currentCountOrders < count_orders) {
        store.currentCountOrders = count_orders;
        await store.getTodayOrders() // Asegúrate de actualizar el estado con el nuevo conteo
        await store.Notification.play();
        store.Notification.addEventListener('ended', function() {
          this.currentTime = 0;
          this.play();
        }, false);
      }
    } catch (error) {
      console.error('Error fetching orders:', error);
    }
  }



  async function fetchOrdersAndNotify() {
    try {
      const site_id = await sitestore.site.site_id; // Asumiendo que `sitestore` está correctamente importado/inicializado
      const order_response = await orderService.is_recent_order_generated(site_id); // Asumir `orderService` está importado

      if (order_response &&  store.last_order_id !== order_response) {
        store.last_order_id = order_response;
        await store.getTodayOrders() // Asegúrate de actualizar el estado con el nuevo conteo
        await store.Notification.play();
        store.Notification.addEventListener('ended', function() {
          this.currentTime = 0;
          this.play();
        }, false);
      }
    } catch (error) {
      console.error('Error fetching orders:', error);
    }
  }

  const intervalId = setInterval(fetchOrdersAndNotify, 3000);

  // Limpieza del intervalo cuando el componente se desmonte
  onUnmounted(() => {
    clearInterval(intervalId);
  });
});















</script>

<template>

  <router-view  class="col-12 p-0 " />

</template>

