import { fotos } from "../fotos"
import { adicionesHamburguesas } from "../adiciones/adicionesHamburguesas"
import { adicioneSalchipapas } from "../adiciones/adicionesSalchipapas"
import { topings } from "../adiciones/Topings"
import { toping_almuerzos } from "../adiciones/toping_almuerzos"

const categoryCombos = {
    "category": { "id": 6, "name": "COMBOS" },
    "products": [

        {
            id: 91,
            name: "BURGERMONSTER 3X2",
            price: 50000,
            description: "",
            category_id: 6,
            adiciones:adicionesHamburguesas,
            
        },
        {
            id: 92,
            name: "MADURIMONSTER+GASEOSA 400 ML",
            price: 36500,
            description: "",
            category_id: 6,
            adiciones:adicioneSalchipapas,
            
        },
        {
            id: 93,
            name: "PORKYMONSTER + GASEOSA 400 ML",
            price: 49000,
            description: "",
            category_id: 6,
            adiciones:adicioneSalchipapas,
            
        },
        {
            id: 94,
            name: "RANCHIMONSTER + GASEOSA 400 ML",
            price: 46500,
            description: "",
            category_id: 6,
            adiciones:adicioneSalchipapas,
           
        },
        {
            id: 95,
            name: "COMBO ALMUERZO #1 : 1 BASE + ENSALADA + 1 ACOMPAÑANTE + GASEOSA 400 ML",
            price: 19000,
            description: "",
            category_id: 6,
            adiciones:toping_almuerzos,
           
        },
        {
            id: 96,
            name: "COMBO ALMUERZO # 2: 1 BASE + 2 ACOMPAÑANTES + GASEOSA 400 ML",
            price: 21500,
            description: "",
            category_id: 6,
            adiciones:toping_almuerzos,
           
        },
      
      





       ]
}

export {categoryCombos}