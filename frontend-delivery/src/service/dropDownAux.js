

import { FilterMatchMode } from 'primevue/api';
import { ref, onMounted, onBeforeMount } from 'vue';
import ProductService from '@/service/ProductService';
import { useToast } from 'primevue/usetoast';
import { URI } from './conection';

const sitesDropValues = ref([{}])
const curentSite = ref([])
const curentSiteDocuments = ref([])



const GenderDropValues = ref([
    'Masculino', 
    'Femenino', 
]);

const epsDropValues = ref([
    "COOSALUD EPS-S",
    "NUEVA EPS", 
    "MUTUAL SER",
    "ALIANSALUD EPS",
    "SALUD TOTAL EPS S.A.", 
    "EPS SANITAS", 
    "EPS SURA", 
    "FAMISANAR EPS", 
    "SERVICIO OCCIDENTAL DE SALUD EPS (SOS EPS)",
    "SALUD MIA EPS",
    "COMFENALCO VALLE EPS",
    "COMPENSAR EPS", 
    "EPM - EMPRESAS PUBLICAS DE MEDELLIN",
    "FONDO DE PASIVO SOCIAL DE FERROCARRILES NACIONALES DE COLOMBIA",
    "CAJACOPI ATLANTICO",
    "CAPRESOCA EPS", 
    "COMFACHOCO", 
    "COMFAORIENTE",
    "EPS FAMILIAR DE COLOMBIA",
    "ASMET SALUD",
    "EMSSANAR E.S.S.",
    "CAPITAL SALUD EPS-S",
    "SAVIA SALUD EPS",
    "DUSAKAWI EPSI",
    "ASOCIACION INDIGENA DEL CAUCA EPSI",
    "ANAS WAYUU EPSI",
    "MALLAMAS EPSI",
    "PIJAOS SALUD EPSI",
    "SALUD BÓLIVAR EPS SAS",
])


const maritalStatusDropValues = ref([
    "Soltero/a",
    "Casado/a",
    "Divorciado/a",
    "Union libre",
])

const educationLevelDropValues = ref([
    "Primaria",
    "Secundaria",
    "Técnico/tecnológico",
    "Universitario/a",
    "Posgrado",
])

const employmentContractTypeDropValues = ref([
    "Fijo 3 meses",
    "Turneros", 
    "Indefinido",
])


const housingTypesDropValues = ref([
    "Propia", 
    "Arrendada", 
    "Familiar", 
    "Otra",
  ]);

  const shirtSizesDropValues = ref([
    "XS", 
    "S",
    "M",
    "L",
    "XL", 
    "XXL",
  ]);
  
  const pantSizesDropValues = ref([
    "28", 
    "30", 
    "32", 
    "34", 
    "36", 
    "38", 
    "40", 
    "42",
  ]);

  const vehicleTypesDropValues = ref([
    "Carro",
    "Moto",
    // { name: "Camión", code: "TRUCK" },
    // { name: "Bicicleta", code: "BICYCLE" },
    // { name: "Otros", code: "OTHER" }
  ]);
  
const PositionDropValues = ref([
     'Coordinador de Sedes Cali',
     'Coordinador de Sede Bogotá',
     'Líder de Punto',
     'Cajero',
     'Auxiliar de Cocina',
     'Jefe de Cocina', 
     'Domiciliario', 
     'Gerencia General', 
     'Jefe de Gestión Humana', 
     'Aprendiz SENA',
     'Jefe de Producción',
     'Líder de Producción', 
     'Auxiliar de Producción', 
     'Contadora', 
     'Auxiliar de Contabilidad',
     'Coordinador de Inventarios',
     'Auxiliar de Logística',
     'Conductor',
     'Jefe de Compras',
     'Auxiliar de Compras',
     'Gerente de Marketing',
     'Diseñador',
     'Community Manager',
]);




const getSites = async ()=> {
    try {
      const response = await fetch(`${URI}/read/sites`);
      if (response.ok) {
        const data = await response.json();
        sitesDropValues.value = data;
      } else {
        console.error('Error al obtener los datos de la API');
      }
    } catch (error) {
      console.error('Error al obtener los datos de la API', error);
    }
  };

  const getSite = async (id)=> {
    try {
    const response = await fetch(`${URI}/read/site/${id}`)
    if (response.ok) {
        const data = await response.json();
        curentSite.value = data[0]
        return data
    } else {
        console.error('Error al obtener los datos de la API');
    }
    } catch (error) {
    console.error('Error al obtener los datos de la API', error);
    }
};


const bloodTypesDropValues = ref([
    "A+", 
    "A-", 
    "B+", 
    "B-", 
    "AB+", 
    "AB-", 
    "O+", 
    "O-", 
  ]) 

  const statusDropValues = ref([
    'activo',
    'inactivo',
    'Por remplazar'
]);


const pensionFundDropValues = [
    "Porvenir",
    "Proteccion",
    "Colfondos",
    "Skandia",
    "OldMutual",
    "Horizonte",
    "AFPSantander",
    "PorvenirPensionesCesantias",
    "Colpensiones",
    "ProteccionSA",
    "AFPHorizonteSA",
    "AFPCrecerSA"
];


const findByName = (toFindName,where) => {
    return where.value.find(item => item.name == toFindName);
}


function findSiteById(id) {
    return sitesDropValues.value.find(item => item.site_id == id);
}

function findByType(type,where) {
    return where.value.find(item => item.type == type);
}


// function findPositionByName(nameToFind) {
//     return PositionDropValues.value.find(item => item.name == nameToFind);
// }




const getSiteDocument = async (site_name, type_document) => {
  try {
    // Construye la URL con los parámetros
    const url = `${URI}/get-site-document/${site_name}/${type_document}/`;

    // Realiza la solicitud GET
    const response = await fetch(url);
    console.log(site_name,type_document,response)
    if (response.ok) {
      // Verifica el tipo de contenido de la respuesta para asegurarse de que sea un PDF
      const contentType = response.headers.get('content-type');
      if (contentType === 'application/pdf') {
        // Si la respuesta es un PDF, crea un objeto Blob a partir de los datos
        const pdfBlob = await response.blob();

        // Crea una URL del objeto Blob
        const pdfUrl = URL.createObjectURL(pdfBlob);
        

        // Abre el PDF en una nueva ventana o pestaña
        window.open(pdfUrl, '_blank');
      
      } else {
        console.error('La respuesta no es un PDF.');
      }
    } else {
      // Si la respuesta no es exitosa, maneja el error
      console.error('Error en la solicitud:', response.status, response.statusText);
    }
  } catch (error) {
    console.error('Error al enviar la solicitud:', error);
  }
};


const getSiteDocumentInfo = async (site_id) => {
  try {
    // Construye la URL con los parámetros
    const url = `${URI}/get-site-documents-info/${site_id}`;

    // Realiza la solicitud GET
    const response = await fetch(url);
    console.log(response)
    if (response.ok) {
      const data = await response.json();
      curentSiteDocuments.value = data
      }

  } catch (error) {
    console.error('Error al enviar la solicitud:', error);
  }
};


// Llama a la función para obtener y abrir el PDF
// getSiteDocument("imperio modelia", "bomberos");

export {
    sitesDropValues,
    getSites,
    GenderDropValues,
    PositionDropValues,
    maritalStatusDropValues ,
    epsDropValues,
    educationLevelDropValues ,
    employmentContractTypeDropValues ,
    pantSizesDropValues ,
    shirtSizesDropValues ,
    bloodTypesDropValues ,
    housingTypesDropValues ,
    statusDropValues,
    vehicleTypesDropValues,
    findByName,
    findSiteById ,
    findByType,
    pensionFundDropValues,
    curentSite,
    getSite,
    getSiteDocument,
    curentSiteDocuments,
    getSiteDocumentInfo
}