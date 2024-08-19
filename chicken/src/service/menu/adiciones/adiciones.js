import { adicioneSalchipapas } from "./adicionesSalchipapas"
import { adicionesHamburguesas } from "./adicionesHamburguesas"
import { topings } from "./Topings"
import { salsas } from "./salsas"
import { toping_almuerzos } from "./toping_almuerzos"
import { acomp_almuerzos } from "./acomp_almuerzos"

const adiciones =
{
    hamburguesas:adicionesHamburguesas,
    salchipapas:adicioneSalchipapas,
    topings:topings,
    salsas:salsas,
    almuerzos:toping_almuerzos,
    shows:[],
    acomp_almuerzos:acomp_almuerzos

}

export {adiciones}