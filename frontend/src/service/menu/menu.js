

import { categoryBebidas} from "./categorias/Bebidas"
import { categoryHamburguers } from "./categorias/Hamburguesas"
import { categorySalchipapa } from "./categorias/salchipapas"
import { categoryMalteadas } from "./categorias/Malteadas"
import { categoryAlmuersos } from "./categorias/almuersos.js"
import {categoryCombos} from "./categorias/combos.js"

import { ref } from "vue"

const version_menu = ref(1.007)
const menuGlobal = {

    salchipapas:categorySalchipapa,
    burgers:categoryHamburguers,
  
    bebidas:categoryBebidas,
    malteadas:categoryMalteadas,

}
    
    // categoryCombos,
    // categoryAlmuersos,
   
    


export { menuGlobal,version_menu }