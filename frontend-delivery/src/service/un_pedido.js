import { ref } from "vue";
import { URI } from "./conection";
const gruposPedidos = ref({})
const miAudio = new Audio('sound/pip.mp3');
const curentSite = ref(0)

const grupos = [
  {name:'RECIBIDOS',order_status:'generada'}, 
  {name:'EN PREPARACION',order_status:'en preparacion'}, 
  {name:'ENVIADOS',order_status:'enviada'}]


const pedido = ref({
  "order_id": 2,
  "order_products": [
  ],
      
  // "user_id": 1,
  // "site_id": 1,
  "order_status": {
    "status": "En preparación",
    "timestamp": "2023-11-21 12:00:00"
  },
  "payment_method": "Efectivo",
  "delivery_person_id": 1,
  "status_history": [
    {
      "status": "En preparación",
      "timestamp": "2023-11-21 12:00:00"
    }
  ]
}) 


const pedidos = ref([])
const dialog_pedido_visible = ref(false)

const getOrders = async()=> {

  if (!localStorage.getItem('siteId')){
    return
  }
  curentSite.value = localStorage.getItem('siteId') 
  // Define la URL del servicio que proporciona los pedidos
  const apiUrl = `${URI}/orders_by_site/${curentSite.value}`;

  // Realiza una solicitud GET utilizando la función fetch
  fetch(apiUrl)
    .then(response => {
      // Verifica si la respuesta es exitosa (código de estado 200-299)
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
      // Convierte la respuesta a formato JSON
      return response.json();
    })
    .then(data => {
      // La variable "data" contiene los pedidos recuperados
      console.log('Pedidos:', data);

      // Obtén las órdenes almacenadas en el localStorage
      const storedOrders = JSON.parse(localStorage.getItem('orders')) || [];

      // Extrae los order_id de las órdenes almacenadas
      const storedOrderIds = storedOrders.map(order => order.order_id);

      // Filtra las nuevas órdenes
      const newOrders = data.filter(order => !storedOrderIds.includes(order.order_id));

      // Si hay nuevas órdenes generadas, emite un sonido
      if (newOrders.some(order => order.order_status.status === 'generada')) {
        miAudio.play(); 
        
      }

      // Almacena las órdenes actuales en el localStorage
      localStorage.setItem('orders', JSON.stringify(data));

      // Actualiza las variables de vue (asumo que usas Vue.js)
      pedidos.value = data;
      // pedido.value = pedidos.value[0];

      grupos.map( grup => {
        gruposPedidos.value[grup.order_status] = filtrarPorEstado(pedidos.value,grup.order_status)
      })

      


    })
    .catch(error => {
      console.error('Error al obtener los pedidos:', error);
    });




    
    
    
}
const intervalID = setInterval(getOrders, 30000);
// const emitirSonido = async () => {
//   // Implementa la lógica para emitir el sonido que desees
//   console.log('Sonido emitido');
//   document.addEventListener('click', () => {
//     miAudio.play(); // Esta función debería emitir el sonido que desees
//   }, { once: true });
//   ocume.click()
// }



// Llama a la función para obtener pedidos
getOrders();


// Función para formatear un número como pesos colombianos
function formatoPesosColombianos(numero) {
    return new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', minimumFractionDigits: 0, maximumFractionDigits: 0 }).format(numero);
  }
  


const set_dialog_order = (order) =>{
  pedido.value = order
}

function filtrarPorEstado(orders, estado) {
  // Utiliza el método filter para obtener solo los objetos que coinciden con el estado proporcionado
  const ordersFiltradas = orders.filter(order => order.order_status.status === estado);
  
  return ordersFiltradas;
}




function prepararPedido(order) {
  // Cambiar el estado a "En preparación" con la hora actual

  const timestampActual = new Date().toLocaleString();
  order.order_status.status = "en preparacion";
  order.order_status.timestamp = timestampActual;

  // Agregar el nuevo estado al historial de estados
  const nuevoEstado = {
      "status": "en preparacion",
      "timestamp": timestampActual
  };
  order.status_history.push(nuevoEstado);

  // Enviar la orden actualizada al servidor
  console.log(order)
  enviarOrdenActualizada(order);
  dialog_pedido_visible.value = false
}


function cancelarPedido(order) {
  // Cambiar el estado a "En preparación" con la hora actual

  const timestampActual = new Date().toLocaleString();
  order.order_status.status = "cancelada";
  order.order_status.timestamp = timestampActual;

  // Agregar el nuevo estado al historial de estados
  const nuevoEstado = {
      "status": "cancelada",
      "timestamp": timestampActual,
      "reazon":"faltaba"
  };
  order.status_history.push(nuevoEstado);

  // Enviar la orden actualizada al servidor
  console.log(order)
  enviarOrdenActualizada(order);
  dialog_pedido_visible.value = false
}

function marcarComoEnviado(order) {
  // Cambiar el estado a "Enviado" con la hora actual
  const timestampActual = new Date().toLocaleString();
  order.order_status.status = "enviada";
  order.order_status.timestamp = timestampActual;

  // Agregar el nuevo estado al historial de estados
  const nuevoEstado = {
      "status": "enviada",
      "timestamp": timestampActual
  };
  order.status_history.push(nuevoEstado);

  // Enviar la orden actualizada al servidor
  
  enviarOrdenActualizada(order);
  dialog_pedido_visible.value = false

}



function enviarOrdenActualizada(order) {
  const url = `${URI}/order/${order.order_id}`;

  // Configurar la solicitud PUT
  fetch(url, {
      method: 'PUT',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(order),
  })
  .then(response => {
      if (!response.ok) {
          throw new Error(`Error al enviar la orden: ${response.status}`);
      }
      return response.json();
  })
  .then(data => {
      console.log('Orden enviada con éxito:', data);
  })
  .catch(error => {
      console.error('Error al enviar la orden:', error);
  });
}




























export {getOrders,curentSite, cancelarPedido,miAudio, gruposPedidos,grupos,pedido,pedidos,formatoPesosColombianos,dialog_pedido_visible,set_dialog_order,filtrarPorEstado,marcarComoEnviado,prepararPedido}