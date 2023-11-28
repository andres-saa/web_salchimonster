import { fotos } from "../fotos"
import { adicionesHamburguesas } from "../adiciones/adicionesHamburguesas"
import { adicioneSalchipapas } from "../adiciones/adicionesSalchipapas"
import { topings } from "../adiciones/Topings"

const categoryCombos = {
    "category": { "id": 6, "name": "Bebidas" },
    "products": [

        {
            id: 90,
            name: "BURGERMONSTER 3X2",
            price: 50000,
            description: "",
            category_id: 6,
            adiciones:adicionesHamburguesas,

        },
        {
            id: 90,
            name: "MADURIMONSTER+GASEOSA 400 ML",
            price: 35500,
            description: "",
            category_id: 6,
            adiciones:adicioneSalchipapas,
         },
        {
            id: 90,
            name: "PORKYMONSTER + GASEOSA 400 ML",
            price: 49000,
            description: "",
            category_id: 6,
            adiciones:adicioneSalchipapas,

        },
        {
            id: 90,
            name: "RANCHIMONSTER + GASEOSA 400 ML",
            price: 46000,
            description: "",
            category_id: 6,
            adiciones:adicioneSalchipapas,
 
        },
      
       ]
}

export {categoryCombos}