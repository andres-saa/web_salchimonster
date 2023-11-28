
import { fotos } from "../fotos"
const categoryMalteadas = {
    "category": { "id": 4, "name": "Malteadas" },
    "products": [

        {
            id: 47,
            name: "CHOCOMONSTER",
            price: 10000,
            description: "TRITURADO DE GALLETA DE CHOCOLATE",
            category_id: 4,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
    
        },
        // este es un ejemplo vacio
        {
            id: 48,
            name: "TROPIMONSTER",
            price: 10000,
            description: "LLUVIA DE CHOCOLATE",
            category_id: 4,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
        },
        {
            id: 49,
            name: "QUIPEMONSTER",
            price: 10000,
            description: "BROWNIE TRITURADO",
            category_id: 4,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
        },

       ]
}

export {categoryMalteadas}