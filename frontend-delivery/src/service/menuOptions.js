import { ref } from "vue"
import {getProductsByCategory} from './productServices.js'

const products = ref({})



//   console.log(products.value)
//   console.log(filtrarProductosPorCategoria(products.value,'salchipapa'))
// const createCategory = (category) => {
//     const prod = filtrarProductosPorCategoria(products.value,'')

//     return {
//         name: category,
//         imagen:'salchipapa-icono.png',
//         submenus: filtrarProductosPorCategoria(category)
        
//     }
// }

// console.log('aqui',createCategory('salchipapas'))

// const menuOptions = ref(
//     [
//         {
//             name: 'Menu',
//             menus: 
            
//             [
//                 {
//                     name: 'Salchipapas',
//                     imagen:'salchipapa-icono.png',
//                     submenus: [
//                     'La Mixtica',
//                     'Baconmonster',
//                     'PolliMonster',
//                     'CostiMonster',
//                     'RanchiMonster',
//                     ' Clasicmonster',
//                     ' MaduriMonster',
//                     ' ChoriMonster',
//                     ' La de Siempre',
//                     ' NachiMonster',
//                     ' La Mata Hambre',
//                     ' SalchiMonster'
//                     ],
                    
//                 },
//                 {
//                     name: 'Amburguesas',
//                     submenus: ["la potente",
//                         'la mas potente',
//                         'la mejor dicho pues',
//                         'la que manda'
//                     ],
//                     imagen:'amburguesa-icono.png'
//                 },
//                 {
//                     name: 'Bebidas',
//                     submenus: ["la potente",
//                         'la mas potente',
//                         'la mejor dicho pues',
//                         'la que manda'
//                     ],
//                     imagen:'bebidas-icono.png'
//                 },
//                 {
//                     name: 'Promo Monster',
//                     submenus: ["la potente",
//                         'la mas potente',
//                         'la mejor dicho pues',
//                         'la que manda'
//                     ],
//                     imagen:'promomoster-icono.png'
//                 },
//                 {
//                     name: 'Malteadas',
//                     submenus: ["la potente",
//                         'la mas potente',
//                         'la mejor dicho pues',
//                         'la que manda',
//                         'la que manda',
//                         'la que manda',
//                         'la que manda'
//                     ]
//                 },


//             ]
//         },
//         {
//             name: 'Sedes',
//             menus: [
//                 {
//                     name: 'Cali',
//                     submenus: ["la potente",
//                         'la mas potente',
                  
                      
//                     ]
//                 },
//                 {
//                     name: 'Bogota',
//                     submenus: ["la potente",
//                         'la mas potente',
//                         'la mejor dicho pues',
                        
//                     ]
//                 },
//                 {
//                     name: 'Palmira',
//                     submenus: ["la potente",
                 
                        
//                     ]
//                 }
//                 ,
//                 {
//                     name: 'Jamundi',
//                     submenus: ["la potente",
             
                        
//                     ]
//                 },
//                 {
//                     name: 'Tulua',
//                     submenus: ["la potente",
                      
                        
//                     ]
//                 }
            
//             ]
//         },
        
//     ]
// )

const menuOptions = ref(
    [

        {
            name: 'Menu',
            menus:[
                {
                    "category": {
                        "id": 1,
                        "name": "Salchipapas"
                    },
                    "products": []}]
        },



        {
            name: 'Sedes',
            menus: [
                {
                    name: 'Cali',
                    submenus: ["la potente",
                        'la mas potente',
                  
                      
                    ]
                },
                {
                    name: 'Bogota',
                    submenus: ["la potente",
                        'la mas potente',
                        'la mejor dicho pues',
                        
                    ]
                },
                {
                    name: 'Palmira',
                    submenus: ["la potente",
                 
                        
                    ]
                }
                ,
                {
                    name: 'Jamundi',
                    submenus: ["la potente",
             
                        
                    ]
                },
                {
                    name: 'Tulua',
                    submenus: ["la potente",
                      
                        
                    ]
                }
            
            ]
        },
        
    ]
)



const ableMenu = ref(false)
export {menuOptions,ableMenu}