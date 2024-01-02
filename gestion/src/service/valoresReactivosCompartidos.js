import { ref } from "vue";
    
import {jwtDecode} from 'jwt-decode';


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

const pastelColors = {

    
    salsas: '#FFF',
    toppings: '#fff',
    cambios: '#fff',
    adicionales: '#fff',
    acompanantes:'#fff'
    
    
    
    }

const getUserRole = () => {
    const token = localStorage.getItem('token');
    if (token) {
    try {
        const decoded = jwtDecode(token);
        return decoded.rol; // Asegúrate de que 'rol' es la propiedad correcta en tu token
    } catch (error) {
        console.error('Error decodificando el token:', error);
        return null;
    }
    }
    return null;
}

const getUserDni = () => {
    const token = localStorage.getItem('token');
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
export {getUserDni, getUserRole, productoAEliminar, showEliminarProducto, productoAEditar, showEditarProducto, productoEnviado,siteDropValues,isInitialWatchCall, showAgregarProducto,pastelColors, categoryValue,siteDropValue,grupoAdicionesDropValue,grupoCambiosDropValue,grupoSalsasdropValue,GrupoAcompananterDropvalue,GrupoToppingsDropValue}