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

    const user = user_data.value
    user.site_id = JSON.parse(localStorage.getItem('currentNeigborhood')).currenSiteId
    const user_id = await getUserID(user);

    const data = {
        "order_products": JSON.parse(localStorage.getItem('cart')).products,
        "user_id": user_id,
        "site_id": JSON.parse(localStorage.getItem('currentNeigborhood')).currenSiteId,
        "order_status": {
            "status": "generada",
            "timestamp": new Date().toLocaleString()
        },
        "payment_method": payMethod.value,
        "delivery_person_id": 4,
        "status_history": [
            {
                
            }
        ],
        "delivery_price":domicilio.value.deliveryPrice,
        "order_notes":order_notes.value == null || order_notes.value == "" ? 'sin notas': order_notes.value
    }
        
     
    let Method = "POST"
    const queryUrl = `${URI}/order`
    const requestOptions = {
        method: Method,
        headers: {
            'Content-Type': 'application/json' // Asegúrate de establecer el tipo de contenido adecuado
        },
        body: JSON.stringify(data)
    };
 
    // Realizar la solicitud Fetch
   await fetch(queryUrl, requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.status}`);
            }
            // file.value? uploadUserPhotoProfile(file.value,data.dni): '' 

            return response.json();
        })
        .then(data => {
            // Aquí puedes trabajar con los datos actualizados
            console.log('Datos actualizados:', data);
            localStorage.removeItem('cart')
            showThaks.value = true
            
        })
        .catch(error => {
            console.error('Error en la solicitud:', error);
            // toast.add({ severity: 'error', summary: 'llene todos los campos', detail: '', life: 3000 })
            
        });


}




export{payMethods,payMethod,showThaks,send_order,order_notes,user_data}