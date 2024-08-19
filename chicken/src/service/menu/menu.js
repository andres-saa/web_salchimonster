

import { categoryBebidas} from "./categorias/Bebidas"
import { categoryHamburguers } from "./categorias/Hamburguesas"
import { categorySalchipapa } from "./categorias/salchipapas"
import { categoryMalteadas } from "./categorias/Malteadas"
import { categoryAlmuersos } from "./categorias/almuersos.js"
import {categoryCombos} from "./categorias/combos.js"

import { ref } from "vue"
import { categoryShows } from "./categorias/Shows.js"

const version_menu = ref(1.042)
const menuGlobal = {

    salchipapas:categorySalchipapa,
    burgers:categoryHamburguers,
    shows:categoryShows,
    almuerzos:categoryAlmuersos,
    bebidas:categoryBebidas,
    malteadas:categoryMalteadas,
  

}
    
    // categoryCombos,
    // categoryAlmuersos,
   
    


export { menuGlobal,version_menu }