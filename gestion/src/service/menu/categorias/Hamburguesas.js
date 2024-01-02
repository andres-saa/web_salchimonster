import { fotos } from "../fotos"
import { URI } from "../../conection";
const categoryHamburguers = {
    "category": { "id": 2, "name": "Burgers" },
    "products": [

        {
            id: 43,
            name: "BURGERMONSTER",
            price: 25000,
            description: "CARNE ANGUS 150 GR, CEBOLLA CARAMELIZADA, SALCHICHA RANCHERA, QUESO AMERICANO, PAN BRIOCHE, LECHUGA Y TOMATE",
            category_id: 2,

        },

        
        {
            id: 50,
            name: "1 burger monster + 1 malteada de ariquipe + papas",
            price: 35000,
            description: "",
            category_id: 2,
 
        },
        {
            id: 51,
            name: "burger monster + 1 malteada de frutos tropicales + papas",
            price: 35000,
            description: "",
            category_id: 2,
    
        },

        {
            id: 52,
            name: "burger monster + 1 malteada de chocolate  + papas",
            price: 35000,
            description: "",
            category_id: 2,
  
        },
       ]
}





// const productos = categoryHamburguers.products.map(producto => {
//     return {
//         name: producto.name,
//         price: producto.price,
//         description: producto.description,
//         category_id: 10,
//         porcion: "1", // Suponiendo que el número de personas siempre es el primer elemento en la cadena 'porcion'
//         state: "activo" // Añadir un valor predeterminado para 'state'
//     };
// });




//  // Reemplaza con la URI correcta



//  const enviarProducto = async (producto) => {
//     try {
//         const response = await fetch(`${URI}/products`, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(producto)
//         });

//         if (!response.ok) {
//             throw new Error(`HTTP error! status: ${response.status}`);
//         }

//         const data = await response.json();
//         console.log('Producto enviado con éxito:', data);
//     } catch (error) {
//         console.error('Error al enviar producto:', error);
//     }
// }

// const enviarTodosLosProductos = () => {
//     productos.forEach(producto => {
//         enviarProducto(producto);
//     });
// }

// enviarTodosLosProductos();

export {categoryHamburguers}