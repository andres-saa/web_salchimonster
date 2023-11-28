<template>
    <div>
        <Toolbar>
            <template #center>
                <div v-for="site in sites">

                    <button class="menu-button" @click="changeCity(site)"
                        :class="currentSite.ciudad == site.ciudad ? 'selected' : ''">
                        {{ site.ciudad }}
                    </button>
                </div>
            </template>


        </Toolbar>


        <div class="grid  m-auto  " :class="currentSite.sedes.length > 1 ? 'sites-2-3' : 'sites-1'">
            <div v-for="site in currentSite.sedes" class="col  ">
                <div class="cont-imagen" @mouseover="changeSelected(site.name)">

                    <img class="imagen" :src="`src/images/sedes images/${site.name}.jpeg`" alt="">
                    <a v-if="site.name == selected"
                        :href="site.whatsapp">

                        <button class="whatsapp-btn" style="
                border: none; background-color: #25D366; 
                border-radius: 50%; 
                width: 40px; 
                height: 40px;
                position: absolute;
                top: 80%;
                left: 80%;
                box-shadow: 0px 0px 10px rgb(255, 255, 255);
               
                ">
                            <i class="" :class="PrimeIcons.WHATSAPP"
                                style="font-weight:  bold; font-size: 24px; color: rgb(255, 255, 255);">
                            </i></button>
                    </a>


                    <div class="cont-site" style="
                position: absolute; 
                width: 100%; 
                padding: 10px 20px; 
                left: 0; top: 100%; 
                display: flex; 
                align-items: center; 
                justify-content: center;
                background-color: transparent">



                        <div class="name-sede" style="height: 100%; padding: 0 10px; font-weight: bold;">
                            {{ site.name.replace('IMPERIO', '') }}
                        </div>



                        <button class="btn-visitar" style="
                    background-color: var(--primary-color); 
                    padding: 10px 20px; 
                    color: white;
                    font-weight: bold;
                    border: none;">Ver mas</button>


                    </div>

                </div>


            </div>

        </div>
    </div>
</template>

<script setup>
import { PrimeIcons } from 'primevue/api';
import { ref } from 'vue';

const images = [
    'https://static.wikia.nocookie.net/p__/images/8/81/Goku_Super_Hero_Infobox.png/revision/latest?cb=20220220034848&path-prefix=protagonist',
    'https://static.wikia.nocookie.net/p__/images/8/81/Goku_Super_Hero_Infobox.png/revision/latest?cb=20220220034848&path-prefix=protagonist',

]

const changeCity = (city) => {
    currentSite.value = city
   
}

const changeSelected = (city) => {
    selected.value = city
}

const selected = ref({})
const sites = ref(
    [
        {
            ciudad: 'Bogota',
            sedes: [
                {
                    name: 'IMPERIO BRETAÑA',
                    whatsapp: 'http://wa.me/573172373979'
                },
                {
                    name: 'IMPERIO SUBA',
                    whatsapp: 'https://api.whatsapp.com/send/?phone=573172373979&text&type=phone_number&app_absent=0'
                },
                {
                    name: 'IMPERIO MODELIA',
                    whatsapp: 'https://api.whatsapp.com/send/?phone=573172373979&text&type=phone_number&app_absent=0'
                },
            ],
        },
        {
            ciudad: 'Cali',
            sedes: [
                {
                    name: 'IMPERIO FLORA',
                    whatsapp: 'http://wa.me/573053447255'
                },
                {
                    name: 'IMPERIO CANEY',
                    whatsapp: 'http://wa.me/573202017941'
                },
            ]
        },
        {
            ciudad: 'Palmira',
            sedes: [
                {
                    name: 'IMPERIO PALMIRA',
                    whatsapp: 'http://wa.me/573042558303'
                }
            ]
        },
        {
            ciudad: 'Tulua',
            sedes: [
                {
                    name: 'IMPERIO TULUA',
                    whatsapp: 'http://wa.me/573043783714'
                },

            ]
        },
        {
            ciudad: 'Jamundi',
            sedes: [
                {
                    name: 'IMPERIO JAMUNDI',
                    whatsapp: 'http://wa.me/573014344948'
                }

            ]
        }
    ]
)

const currentSite = ref(
    sites.value[0]
)
</script>

<style scoped>
.imagen {
    height: 30vh;
    object-fit: cover;
    width: 100%;
    /* max-width: 40vw; */
    margin: auto;
    transition: all 0.3s ease;
    border-radius: 20px;
    /* filter: blur(2px); */
}

.imagen:hover {
    filter: brightness(1.2);
    /* transform:  translateY(-10px); */
    /* border-bottom: 1px solid red; */
    box-shadow: 0px 10px 0px var(--primary-color);
}

.selected {
    box-shadow: 0px 5px 0px var(--primary-color);
    /* font-weight: bold; */

}

.cont-imagen {
    position: relative;
}

.site-name {
    /* font-weight: bold; */
    font-size: 20px;
    text-align: center;
}

.menu-button {
    background-color: transparent;
    padding: 1rem;
    margin: 0 1rem;
    border: none;
    font-size: 20px;
    /* transition: all  0.3s; */
    /* font-weight: bold; */
}

.menu-button:hover {
    /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5); */
    /* transform: scale(1.1); */
    /* border-bottom:  2px red; */
    color: var(--primary-color);


}

.sites-2-3 {
    margin: auto;
    padding: 0 10vw;
}

.sites-1 {
    margin: auto;
    padding: 0 20vw;
}

.btn-visitar:hover {
    filter: brightness(1.2);
    /* transform: translateX(10px) ; */
    padding: 20px;

}

.name-sede {
    transition: all ease .3s;
}

.cont-site:hover>.name-sede {
    filter: brightness(1.2);
    transform: translateX(-10px);
    color: var(--primary-color);

    padding: 20px;

}

.cont-site:hover>.btn-visitar {
    filter: brightness(1.2);
    transform: translateX(10px);
    color: var(--primary-color);

    padding: 20px;

}

.btn-visitar {
    transition: all ease 0.3s;
}

.cont-imagen:hover>a>.whatsapp-btn {

    transform: scale(1.5) translateY(-10px);
}

.whatsapp-btn {
    transition: all ease .3s;
}

.whatsapp-btn:hover {
    filter: brightness(1.4);
}</style>