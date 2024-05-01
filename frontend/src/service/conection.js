// const URI = 'https://backend.novatocode.online'
// const URI = 'https://backend.novatocode.online'
// const URI = 'http://localhost:8100'
// http://192.168.1.142:5173/
// const URI = 'http://localhost:8000'
// const URI = 'http://167.71.178.54:8200'
// const URI = 'http://back.novatocode.online'
const URI = 'https://backend.salchimonster.com'
const URI_SOCKET = 'backend.salchimonster.com'
// const URI_SOCKET = 'localhost:8000'
export {URI,URI_SOCKET}
    

// const products = [
//     {
//       "product_id": 603,
//       "name": "SHOW DE MEGA QUESO x 400 gr",
//       "price": 19500,
//       "description": " ",
//       "category_id": 6,
//       "porcion": "1",
//       "state": "active",
//       "grupo_salsa_id": 9,
//       "grupo_topping_id": null,
//       "grupo_acompanante_id": null,
//       "grupo_cambio_id": null,
//       "grupo_adicional_id": null,
//       "site_id": 1,
//       "number_of_acompanantes": 0
//     },
//     {
//       "product_id": 627,
//       "name": "SHOW DE CARNE ASADA 450 gr",
//       "price": 32500,
//       "description": "   ",
//       "category_id": 6,
//       "porcion": "1",
//       "state": "inactive",
//       "grupo_salsa_id": 9,
//       "grupo_topping_id": null,
//       "grupo_acompanante_id": 2,
//       "grupo_cambio_id": null,
//       "grupo_adicional_id": null,
//       "site_id": 1,
//       "number_of_acompanantes": 0
//     },
//     {
//       "product_id": 615,
//       "name": "SHOW DE CHICHARRON x 450 gr",
//       "price": 35000,
//       "description": "  ",
//       "category_id": 6,
//       "porcion": "1",
//       "state": "active",
//       "grupo_salsa_id": 9,
//       "grupo_topping_id": null,
//       "grupo_acompanante_id": 2,
//       "grupo_cambio_id": null,
//       "grupo_adicional_id": null,
//       "site_id": 1,
//       "number_of_acompanantes": 0
//     },
//     {
//       "product_id": 639,
//       "name": "SHOW DE COSTILLA x 450 gr",
//       "price": 32500,
//       "description": "    ",
//       "category_id": 6,
//       "porcion": "1",
//       "state": "inactive",
//       "grupo_salsa_id": 9,
//       "grupo_topping_id": null,
//       "grupo_acompanante_id": 2,
//       "grupo_cambio_id": null,
//       "grupo_adicional_id": null,
//       "site_id": 1,
//       "number_of_acompanantes": 0
//     }
//   ]


//   const guardar = () => {
//     products.forEach( async(product) => {

//         try {
//             const response = await axios.post(`${URI}/products`, product);
//             if (response.status === 200) { // Asumiendo que 201 Created es el código de estado para una creación exitosa
//                 return response.data;
//             } else {
//                 console.error('An error occurred while creating the recipe:', response.status);
//                 return null;
//             }
//         } catch (error) {
//             console.error('An error occurred while creating the recipe:', error);
//             return null;
//         }


//   })
//   }
// guardar()