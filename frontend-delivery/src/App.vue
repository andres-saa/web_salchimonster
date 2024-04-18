<script setup>
import { URI_SOCKET } from '@/service/conection';
import { onBeforeUnmount, onMounted ,ref} from 'vue';
import router from './router';
import { useOrderStore } from './store/order';
import { useSitesStore } from './store/site';
const sitestore = useSitesStore()
let webSocket = null;
const store = useOrderStore();

const boton = ref(null)



function connectWebSocket(siteId) {
  if (webSocket !== null) {
    webSocket.close(); // Make sure to close any existing connections
  }
  
  webSocket = new WebSocket(`wss://${URI_SOCKET}/ws/${siteId}`);
  
  webSocket.onopen = () => console.log("WebSocket connected");
  webSocket.onmessage = (message) => {
    console.log("Message received:", message.data); // Log the received message data
    store.getTodayOrders();
    store.Notification.play()
    // alert('hola')
    store.Notification.addEventListener('ended', function() {
    this.currentTime = 0;
    this.play();
}, false);  
    

  };
  webSocket.onclose = async() => {
    console.log("WebSocket disconnected");


    const site_id = await sitestore.site.site_id
    
    if(sitestore.site.site_id){

      connectWebSocket(site_id);
    } else{
      router.push('/login')
    }
    webSocket = null;
    // location.reload() // Clean up the reference to the WebSocket
  };
  webSocket.onerror = (error) => console.error("WebSocket error:", error);
}

onMounted(async() => {

  const site_id = await sitestore.site.site_id
  
  if(sitestore.site.site_id){

    connectWebSocket(site_id );
  } else{
    router.push('/login')
  }

});

onBeforeUnmount(() => {
  if (webSocket) {
    webSocket.close();
  }
});
</script>

<template>
  <!-- {{ sitestore }} -->
  <router-view  class="col-12 p-0 " />

</template>

