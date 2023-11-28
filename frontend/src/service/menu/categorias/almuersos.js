
import { fotos } from "../fotos"
const categoryAlmuersos = {
    "category": { "id": 5, "name": "Almuersos" },
    "products": [

        {
            id: 53,
            name: "ARMA TU LONCH #2",
            price: 21000,
            description: "COMBO ALMUERZO 1 BASE + 2 ACOMPAÑANTES + GASEOSA 400 ML",
            category_id: 5,
            porcion: "1 PERSONA",
            acomp_cantidad:2,
            
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
        },
        {
            id: 54,
            name: "ARMA TU LONCH #1",
            price: 18000,
            description: "COMBO ALMUERZO 1 BASE + ENSALADA + 1 ACOMPAÑANTE + GASEOSA 400 ML",
            category_id: 5,
            porcion: "1 PERSONA",
            acomp_cantidad:1,

            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
        },
        {
            id: 55,
            name: "COMBO ALMUERZO #1",
            price: 15000,
            description: "ALMUERZO 1 BASE + ENSALADA + 1 ACOMPAÑANTE",
            category_id: 5,
            porcion: "1 PERSONA",
            acomp_cantidad:1,
            
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
        },

        {
            id: 56,
            name: "COMBO ALMUERZO #2",  
            price: 18000,
            description: "ALMUERZO 1 BASE + 2 ACOMPAÑANTES",
            category_id: 5,
            porcion: "1 PERSONA",
            acomp_cantidad:2,
            
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
        },
        
]
}

export {categoryAlmuersos}