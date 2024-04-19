<script setup>
import { URI_SOCKET } from '@/service/conection';
import { onBeforeUnmount, onMounted ,ref} from 'vue';
import router from './router';
import { useOrderStore } from './store/order';
import { useSitesStore } from './store/site';
const sitestore = useSitesStore()
const store = useOrderStore();



const requestNotificationPermission = async () => {
    const permission = await Notification.requestPermission();
    if (permission !== 'granted') {
        alert('Las notificaciones están deshabilitadas. Por favor, habilite las notificaciones para obtener alertas en tiempo real.');
    }
}

onMounted(async() => {


  requestNotificationPermission()
  const site_id = await sitestore.site.site_id
  
  if(sitestore.site.site_id){

    store.connectWebSocket(site_id );
  } else{
    router.push('/login')
  }

});

onBeforeUnmount(() => {
  if (store.webSocket) {
    store.webSocket.close();
  }
});


const visibleNotifications = ref(true)


</script>

<template>
  <!-- {{ sitestore }} -->

  <Dialog  class="" style="overflow: hidden;display: flex;" modal :closable="false" v-model:visible = "visibleNotifications">
    <div style="background-color: transparent; display: flex ; flex-direction: column; gap: 1rem;">
      <i  class="pi pi-bell col-12 text-center p-0 m-0" style="font-size: 5rem;color: #a855f7;"></i>
      <Button @click="() => {
        visibleNotifications = false
        store.getTodayOrders()

      }" severity="help"  label="Aceptar las notificaciones"> </Button>
    </div>

  </Dialog>
  <router-view  class="col-12 p-0 " />

</template>

