import { ref } from "vue";



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
    

export {productoAEliminar, showEliminarProducto, productoAEditar, showEditarProducto, productoEnviado,siteDropValues,isInitialWatchCall, showAgregarProducto,pastelColors, categoryValue,siteDropValue,grupoAdicionesDropValue,grupoCambiosDropValue,grupoSalsasdropValue,GrupoAcompananterDropvalue,GrupoToppingsDropValue}