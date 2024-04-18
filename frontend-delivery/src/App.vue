<script setup>
import { URI_SOCKET } from '@/service/conection';
import { onBeforeUnmount, onMounted ,ref} from 'vue';
import { useOrderStore } from './store/order';

let webSocket = null;
const store = useOrderStore();

const boton = ref(null)


function connectWebSocket(siteId) {
  if (webSocket !== null) {
    webSocket.close(); // Make sure to close any existing connections
  }
  
  webSocket = new WebSocket(`ws://${URI_SOCKET}/ws/${siteId}`);
  
  webSocket.onopen = () => console.log("WebSocket connected");
  webSocket.onmessage = (message) => {
    console.log("Message received:", message.data); // Log the received message data
    store.getTodayOrders();
    store.Notification.play()
    store.Notification.addEventListener('ended', function() {
    this.currentTime = 0;
    this.play();
}, false);  
    

  };
  webSocket.onclose = () => {
    console.log("WebSocket disconnected");
    webSocket = null; // Clean up the reference to the WebSocket
  };
  webSocket.onerror = (error) => console.error("WebSocket error:", error);
}

onMounted(() => {
  connectWebSocket(1);
});

onBeforeUnmount(() => {
  if (webSocket) {
    webSocket.close();
  }
});
</script>

<template>
  <router-view  class="col-12 p-0 " />

</template>

