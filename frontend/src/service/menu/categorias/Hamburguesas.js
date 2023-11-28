import { fotos } from "../fotos"
const categoryHamburguers = {
    "category": { "id": 2, "name": "Hamburguesas" },
    "products": [

        {
            id: 43,
            name: "BURGERMONSTER",
            price: 25000,
            description: "CARNE ANGUS 150 GR, CEBOLLA CARAMELIZADA, SALCHICHA RANCHERA, QUESO AMERICANO, QUESO MOZZARELLA, PAN BRIOCHE, LECHUGA Y TOMATE",
            category_id: 2,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
            
        },

        
        {
            id: 50,
            name: "QUIPEBURGER + PAPAS",
            price: 35000,
            description: "",
            category_id: 2,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
            
        },
        {
            id: 51,
            name: "TROPIBURGER + PAPAS",
            price: 35000,
            description: "",
            category_id: 2,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
            
        },

        {
            id: 52,
            name: "CHOCOBURGER + PAPAS",
            price: 35000,
            description: "",
            category_id: 2,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
            
        },
       ]
}

export {categoryHamburguers}