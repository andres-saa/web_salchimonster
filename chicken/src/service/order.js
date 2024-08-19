import { contarObjetosRepetidos, products } from "./cart";
import { ref } from "vue";
import {URI} from '@/service/conection'
import { domicilio } from "./cart";
import router from '@/router/index.js'
import { antojoVisible } from "./state";


import { useReportesStore } from "@/store/ventas";



// console.log(store)

const user_data = ref({})
const order_notes = ref("")
const showThaks = ref(false)

let currenNeigborhoodName = 'Valor por defecto'; // Establece un valor por defecto

try {
    // Intenta obtener el valor de 'currentNeigborhood' de localStorage
    const storedData = localStorage.getItem('currentNeigborhood');
    if (storedData) {
        const currenNeigborhood = JSON.parse(storedData).currenNeigborhood;
        if (currenNeigborhood && currenNeigborhood.name) {
            // Actualiza el nombre si existe en los datos almacenados
            currenNeigborhoodName = currenNeigborhood.name;
        }
    }
} catch (error) {
    // Manejo de errores si JSON.parse falla o los datos no son como se esperaban
    console.error("Error al obtener 'currenNeigborhood.name':", error);
}


const payMethod = ref('')
const payMethods = ref(["Recoger en local", "Efectivo", "Pago con tarjeta (datafono),","Transferencia"])
const invalid = ref({})
const thanks_data = ref()


const getUserID = async (userData) => {
    const userUrl = `${URI}/user`;
    userData.user_address = `${userData.user_address} ${currenNeigborhoodName} `
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






const sending_order = ref(false)




const send_order = async () => {
    const store = useReportesStore()
    store.setLoading(true,'enviando orden')

    // store.setLoading(true, 'enviando orden')
    const serverTimeResponse = await fetch( `${URI}/server_time`);
    const serverTimeData = await serverTimeResponse.json();

    // Extrae la fecha y la hora del objeto de respuesta
    const { fecha, hora } = serverTimeData;

    const user = user_data.value

    if (!user.user_name || !user.user_name.trim()) {
        invalid.value.user_name = true
        alert("El nombre es obligatorio.");
        antojoVisible.value = false
        
        return;
    }
    
    if (!user.user_phone || !user.user_phone.trim()) {
        alert("El teléfono es obligatorio.");
        antojoVisible.value = false
        return;
    }
    
    if (!user.user_address || !user.user_address.trim()) {
        alert("La dirección es obligatoria.");
        antojoVisible.value = false
        return;
    }
    if (!payMethod.value){
        alert("Por favor seleccione un metodo de pago");
        antojoVisible.value = false
        return;

    }
    

    
    user.site_id = 12; // Valor por defecto

// Intenta obtener el valor de 'currentNeighborhood' de localStorage
    let currentNeighborhood = localStorage.getItem('currentNeigborhood');
        if (currentNeighborhood) {
            try {
                // Parsea el JSON y verifica si el objeto tiene la propiedad 'currenSiteId'
                let neighborhoodData = JSON.parse(currentNeighborhood);
                if (neighborhoodData && typeof neighborhoodData.currenSiteId === 'number') {
                    user.site_id = neighborhoodData.currenSiteId;
                }
            } catch (error) {
                // Manejo de errores si JSON.parse falla
                console.error("Error al parsear 'currentNeigborhood':", error);
            }
        }
    const user_id = await getUserID(user);

    const data = {
        "order_products": JSON.parse(localStorage.getItem('cart')).products,
        "user_id": user_id,
        "user_data":{...user},
        "site_id":JSON.parse(localStorage.getItem('currentNeigborhood')).currenSiteId,
        // "site_id":12,
        "order_status": {
            "status": "generada",
            "timestamp":serverTimeData
        },
        "payment_method": payMethod.value,
        "delivery_person_id": 4,
        "status_history": [
            {
                
            }
        ],
        "delivery_price":domicilio.value.delivery_price,
        "order_notes":order_notes.value == null || order_notes.value == "" ? 'sin notas': order_notes.value
    }
    console.log(data)


    thanks_data.value = {...data}
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
    sending_order.value = true
    store.setLoading(true,'enviando orden')

   await fetch(queryUrl, requestOptions)
        .then(response => {
            if (!response.ok) {
                store.setLoading(false,'enviando orden')

                throw new Error(`Error en la solicitud: ${response.status}`);

            }
            // file.value? uploadUserPhotoProfile(file.value,data.dni): '' 


            
            return response.json();
            
        })
        .then(data => {
            // Aquí puedes trabajar con los datos actualizados
            console.log('Datos actualizados:', data);
            thanks_data.value.order_id = data.order_id
            // localStorage.removeItem('cart')
            antojoVisible.value = false
            sending_order.value = false
            store.setLoading(false,'enviando orden')
            
           

            setTimeout(() => {
                router.push('/gracias')
              }, 500);


           
           
            
            eliminarProductosDelCarrito();
            user_data.value = {}

            // 
            // showThaks.value = true
            
            // router.push('/')

        })
        .catch(error => {
            console.error('Error en la solicitud:', error);
            sending_order.value = false
            store.setLoading(false,'enviando orden')


            // toast.add({ severity: 'error', summary: 'llene todos los campos', detail: '', life: 3000 })

        });



        

}



function eliminarProductosDelCarrito() {
    // Obtener el carrito actual almacenado en el LocalStorage
    const cart = JSON.parse(localStorage.getItem('cart'));
  
    // Verificar si el carrito existe y tiene la propiedad "products"
    if (cart && cart.products) {
      // Vaciar el array de productos
      cart.products = [];
  
      // Actualizar el LocalStorage con el carrito modificado
      localStorage.setItem('cart', JSON.stringify(cart));
  
      console.log('Se eliminaron los productos del carrito y se actualizó el LocalStorage.');
    } else {
      console.log('El carrito no tiene la propiedad "products" o no existe en el LocalStorage.');
    }
  }


export{payMethods,payMethod,showThaks,sending_order,eliminarProductosDelCarrito, send_order,order_notes,user_data,invalid,thanks_data}