import { ref } from "vue";
import { URI } from "./conection";
const gruposPedidos = ref({})
const miAudio = new Audio('sound/pip.mp3');
const curentSite = ref(0)
const ordenes_de_hoy = ref([])

const fechaHoy = ref({ "d": "02", "m": "12", "a": "2023" });
const fechaHoyFormateada = ref("");

function convertirA12h(tiempo) {
  var horas = parseInt(tiempo.h, 10);
  var minutos = parseInt(tiempo.m, 10);

  var periodo = horas >= 12 ? "pm" : "am";
  horas = horas > 12 ? horas - 12 : horas;
  horas = horas === 0 ? 12 : horas;

  return horas.toString().padStart(2, '0') + ':' + minutos.toString().padStart(2, '0') + ' ' + periodo;
}

const grupos = [
  { name: 'RECIBIDOS', order_status: 'generada' },
  { name: 'EN PREPARACION', order_status: 'en preparacion' },
  { name: 'ENVIADOS', order_status: 'enviada' }]


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




const filtrarOrdenesHoy = async() => {
 

  
  

 const ordenesFiltradas = pedidos.value.filter( orden => {
  if (! orden.order_status.timestamp.fecha){
    return false
  }
  return orden.order_status.timestamp.fecha.d == fechaHoy.value.fecha.d})


 ordenes_de_hoy.value = ordenesFiltradas
  
}





async function obtenerFechaDelServidor() {
    try {
        const serverTimeResponse = await fetch('https://backend.salchimonster.com/server_time');
        fechaHoy.value = await serverTimeResponse.json();
    } catch (error) {
        console.error("Error al obtener la fecha del servidor:", error);
    }
}



// Llamada asíncrona para obtener la fecha del servidor











const pedidos = ref([])
const dialog_pedido_visible = ref(false)

const getOrders = async () => {

  const serverTimeResponse = await fetch('https://backend.salchimonster.com/server_time');
  fechaHoy.value = await serverTimeResponse.json();
  localStorage.setItem("fecha_server",JSON.stringify(fechaHoy.value) )



  if (!localStorage.getItem('siteId')) {
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
      pedidos.value = [... data];

      filtrarOrdenesHoy()
      // pedido.value = pedidos.value[0];

      grupos.map(grup => {
        gruposPedidos.value[grup.order_status] = filtrarPorEstado(pedidos.value, grup.order_status)
      })




    })
    .catch(error => {
      console.error('Error al obtener los pedidos:', error);
    });







}
const intervalID = setInterval(getOrders, 3000);
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



const set_dialog_order = (order) => {
  pedido.value = order
}

function filtrarPorEstado(orders, estado) {
  // Utiliza el método filter para obtener solo los objetos que coinciden con el estado proporcionado
  const ordersFiltradas = orders.filter(order => order.order_status.status === estado);

  return ordersFiltradas;
}




const prepararPedido = async (order) => {
  // Cambiar el estado a "En preparación" con la hora actual
  const serverTimeResponse = await fetch('https://backend.salchimonster.com/server_time');
  const serverTimeData = await serverTimeResponse.json();
  miAudio.pause();
  miAudio.currentTime = 0
  const timestampActual = new Date().toLocaleString();
  order.order_status.status = "en preparacion";
  order.order_status.timestamp = serverTimeData;

  // Agregar el nuevo estado al historial de estados
  const nuevoEstado = {
    "status": "en preparacion",
    "timestamp": serverTimeData
  };
  order.status_history.push(nuevoEstado);

  // Enviar la orden actualizada al servidor
  console.log(order)
  enviarOrdenActualizada(order);
  dialog_pedido_visible.value = false
}


const cancelarPedido = async (order) => {
  const serverTimeResponse = await fetch('https://backend.salchimonster.com/server_time');
  const serverTimeData = await serverTimeResponse.json();
  // Cambiar el estado a "En preparación" con la hora actual
  miAudio.pause();
  miAudio.currentTime = 0
  const timestampActual = new Date().toLocaleString();
  order.order_status.status = "cancelada";
  order.order_status.timestamp = serverTimeData;

  // Agregar el nuevo estado al historial de estados
  const nuevoEstado = {
    "status": "cancelada",
    "timestamp": serverTimeData,
    "reazon": "faltaba"
  };
  order.status_history.push(nuevoEstado);

  // Enviar la orden actualizada al servidor
  console.log(order)
  enviarOrdenActualizada(order);
  dialog_pedido_visible.value = false
}

const marcarComoEnviado = async (order) => {
  const serverTimeResponse = await fetch('https://backend.salchimonster.com/server_time');
  const serverTimeData = await serverTimeResponse.json();
  // Cambiar el estado a "Enviado" con la hora actual
  const timestampActual = new Date().toLocaleString();
  order.order_status.status = "enviada";
  order.order_status.timestamp = serverTimeData;

  // Agregar el nuevo estado al historial de estados
  const nuevoEstado = {
    "status": "enviada",
    "timestamp": serverTimeData
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





async function filtrarOrdenesPorFecha(ordenes) {
  // Obtener la fecha actual del servidor
  const serverTimeResponse = await fetch('https://backend.salchimonster.com/server_time');
  const serverTimeData = await serverTimeResponse.json();
  const fechaActualServidor = serverTimeData.fecha;

  // Filtrar las órdenes por la fecha actual
  const ordenesFiltradas = ordenes.filter(orden => {
    const fechaOrden = orden.order_status.timestamp.fecha;
    return (
      fechaOrden.d === fechaActualServidor.d &&
      fechaOrden.m === fechaActualServidor.m &&
      fechaOrden.a === fechaActualServidor.a
    );
  });

  return ordenesFiltradas;
}























export {fechaHoyFormateada, fechaHoy, convertirA12h, ordenes_de_hoy, getOrders, curentSite, cancelarPedido, miAudio, gruposPedidos, grupos, pedido, pedidos, formatoPesosColombianos, dialog_pedido_visible, set_dialog_order, filtrarPorEstado, marcarComoEnviado, prepararPedido }