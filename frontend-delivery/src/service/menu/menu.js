

import { categoryBebidas} from "./categorias/Bebidas"
import { categoryHamburguers } from "./categorias/Hamburguesas"
import { categorySalchipapa } from "./categorias/salchipapas"
import { categoryMalteadas } from "./categorias/Malteadas"
import { categoryAlmuersos } from "./categorias/almuersos.js"

const menuGlobal = [
    categorySalchipapa,
    categoryHamburguers,
    categoryMalteadas,
    categoryAlmuersos,
    categoryBebidas
]

export { menuGlobal }