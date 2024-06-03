import { ref } from "vue";
    
import {jwtDecode} from 'jwt-decode';
import {loginStore} from '@/store/user.js'

import { URI } from "./conection";
const categoryValue = ref()
const siteDropValue = ref()
const grupoSalsasdropValue = ref()
const grupoAdicionesDropValue = ref()
const grupoCambiosDropValue = ref()
const GrupoAcompananterDropvalue = ref()
const GrupoToppingsDropValue = ref()
const showAgregarProducto = ref(false)
const showEditarProducto = ref(false)
const isInitialWatchCall = ref(true)
const siteDropValues = ref()
const productoEnviado = ref(1)
const productoAEditar = ref({})
const productoAEliminar = ref({})
const showEliminarProducto = ref(false)
const verInfo = ref(true)
const showDotation = ref(false)

const pastelColors = {

    
    salsas: '#FFF',
    toppings: '#fff',
    cambios: '#fff',
    adicionales: '#fff',
    acompanantes:'#fff'
    
    
    
    }

const getUserRole = () => {
  
    const store = loginStore()
    const token = store.userData.access_token
    if (token) {
    try {
        const decoded = jwtDecode(token);
        return decoded.rol;
         // Asegúrate de que 'rol' es la propiedad correcta en tu token
    } catch (error) {
        console.error('Error decodificando el token:', error);
        return null;
    }
    }
    return null;
}

const getUserDni = () => {
  const store = loginStore()
  const token = store.userData.access_token
    if (token) {
    try {
        const decoded = jwtDecode(token);
        return decoded.dni; // Asegúrate de que 'rol' es la propiedad correcta en tu token
    } catch (error) {
        console.error('Error decodificando el token:', error);
        return null;
    }
    }
    return null;
}



const getUserBasic = async (id) => {
    try {
      // Obtiene el token de acceso desde el Local Storage
      // const accessToken = localStorage.getItem('accessToken');
  
      // Verifica si el token de acceso existe
      // if (!accessToken) {
      //   // Si no hay token de acceso, puedes manejar el error o redirigir al usuario a iniciar sesión
      //   console.error('Token de acceso no encontrado');
      //   // return null;
      // }
  
      // Configura el encabezado de la solicitud con el token de acceso
      // const headers = {
      //   'Authorization': `Bearer ${accessToken}`,
      //   'Content-Type': 'application/json', // Ajusta según tus necesidades
      // };
  
      // Realiza la solicitud HTTP con el encabezado configurado
      const response = await fetch(`${URI}/employer-basic/${id}`, {
        method: 'GET',
        // headers: headers,
      });
  
      // Verifica si la respuesta es exitosa
      if (response.ok) {
        const data = await response.json();
        
        return data;
      } else {
        // Puedes manejar errores de autenticación o cualquier otro tipo de error aquí
        console.error('Error al obtener usuarios:', response.statusText);
        return null;
      }
    } catch (error) {
      console.error('Error al obtener usuarios:', error);
      return null;
    }
  };



  const currentDotacion  = ref(    {
   
  },)

const getUserId = () => {
  const store = loginStore()
  const token = store.userData.access_token
    if (token) {
    try {
        const decoded = jwtDecode(token);
        return decoded.id; // Asegúrate de que 'rol' es la propiedad correcta en tu token
    } catch (error) {
        console.error('Error decodificando el token:', error);
        return null;
    }
    }
    return null;
}


const getUsersBasic = async (id) => {
  try {
    const response = await fetch(`${URI}/employers-basic`, {
      method: 'GET',
      // headers: headers,
    });

    // Verifica si la respuesta es exitosa
    if (response.ok) {
      const data = await response.json();
      
      return data;
    } else {
      // Puedes manejar errores de autenticación o cualquier otro tipo de error aquí
      console.error('Error al obtener usuarios:', response.statusText);
      return null;
    }
  } catch (error) {
    console.error('Error al obtener usuarios:', error);
    return null;
  }
};
const salesReport= ref({})
function formatToColombianPeso(number) {
  if(!number){
    return
  }
  return number.toLocaleString('es-CO', {
    style: 'currency',
    currency: 'COP',
    minimumFractionDigits: 0, // Opcional: ajusta a 0 para no mostrar decimales
  });
}
export {showDotation,getUserDni,formatToColombianPeso,verInfo,currentDotacion,salesReport, getUserRole,getUserId,getUserBasic,getUsersBasic, productoAEliminar, showEliminarProducto, productoAEditar, showEditarProducto, productoEnviado,siteDropValues,isInitialWatchCall, showAgregarProducto,pastelColors, categoryValue,siteDropValue,grupoAdicionesDropValue,grupoCambiosDropValue,grupoSalsasdropValue,GrupoAcompananterDropvalue,GrupoToppingsDropValue}
