import { contarObjetosRepetidos, products } from "./cart";
import { ref } from "vue";
import {URI} from '@/service/conection'
import { domicilio } from "./cart";
import router from '@/router/index.js'
const user_data = ref({})
const order_notes = ref("")
const showThaks = ref(false)
const currenNeigborhood = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood.name
const payMethod = ref('')
const payMethods = ref(["Recoger en local", "Efectivo", "Pago con tarjeta (datafono),"])




const getUserID = async (userData) => {
    const userUrl = `${URI}/user`;
    userData.user_address = `${userData.user_address} ${currenNeigborhood} `
    console.log(userData)
    const userRequestOptions = {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    };

    try {
        const response = await fetch(userUrl, userRequestOptions);
        if (!response.ok) {
            throw new Error(`Error en la solicitud para obtener user_id: ${response.status}`);
        }

        const userData = await response.json();
        return userData.user_id; // Asumiendo que el user_id se encuentra en la respuesta JSON
    } catch (error) {
        console.error('Error al obtener user_id:', error);
        throw error; // Puedes manejar el error según tus necesidades
    }
};









const send_order = async () => {
    // Obtiene la hora del servidor
    const serverTimeResponse = await fetch('https://backend.salchimonster.com/server_time');
    const serverTimeData = await serverTimeResponse.json();

    // Extrae la fecha y la hora del objeto de respuesta
    const { fecha, hora } = serverTimeData;

    // Construye el objeto de datos para la orden con la hora del servidor
    const user = user_data.value;
    user.site_id = JSON.parse(localStorage.getItem('currentNeigborhood')).currenSiteId;
    const user_id = await getUserID(user);

    const data = {
        "order_products": JSON.parse(localStorage.getItem('cart')).products,
        "user_id": user_id,
        "site_id": 12,
        // JSON.parse(localStorage.getItem('currentNeigborhood')).currenSiteId,
        "order_status": {
            "status": "generada",
            "timestamp": `${fecha.a}-${fecha.m}-${fecha.d} ${hora.h}:${hora.m}`
        },
        "payment_method": payMethod.value,
        "delivery_person_id": 4,
        "status_history": [{}],
        "delivery_price": domicilio.value.deliveryPrice,
        "order_notes": order_notes.value == null || order_notes.value == "" ? 'sin notas' : order_notes.value
    };

    // Resto del código para enviar la orden...
};




export{payMethods,payMethod,showThaks,send_order,order_notes,user_data}