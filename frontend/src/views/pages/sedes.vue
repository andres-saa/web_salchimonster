

<template>
    <div class=" grid col-12 lg:col-10 m-auto p-3 m-0 mb-8" style="">

        <div style=" ;
        border-radius: 1rem; overflow: hidden;" class="col-12 lg:col-6 p-0 mb-3 lg:p-3 m-0" v-for=" sede in sedes">

            <div class="col-12 p-0 m-0" style="
         
            position: relative;overflow: hidden;height: min-content;box-shadow: 0 0 10px black; border-radius: 1rem;">



                <img style="object-fit:cover
                ; border-radius: 1rem; width: 100%;height: 30rem;"
                    :src="`${URI}/read_product_image/600/site-${ sede.site_id }`"
                    alt="">

                <div class="xl:pl-4 pl-2" style="
                width: 100%;height: 40%;
                background: linear-gradient(to top, black, transparent);
;
                position: absolute; 
                display: flex; flex-direction: column; justify-content: end;
                left: 0;bottom: 0;
                border-radius:0 0 1rem 1rem;">

                <p class="xl:text-xl text-l m-0 " style="font-weight: bold; color:var(--primary-color)"><span class="pr-4" style="text-transform: uppercase;"><i :class="PrimeIcons.MAP_MARKER" style="color: var(--primary-color); font-weight: bold;"></i></span>{{sede.Ciudad}} <span style="font-weight: normal; padding-left: 1rem; color: white;">{{ sede.Dirección }}</span> <p style="color: white;">SALCHIMONSTER {{sede.Nombre}}</p></p>



                <p class="xl:text-xl text-l   " style="font-weight:normal ; color:white"><span class="pr-4"><i class="text-l p-0" :class="PrimeIcons.WHATSAPP" style="font-weight: bold; color: rgb(58, 255, 58);"></i></span>{{ sede.WSP }}  </p>





                <div style="position: absolute; right: 0rem; width: 5rem;height: 5rem;bottom: 0; background-color:transparent;display: flex; padding: 1rem;">

                    <a :href="sede['Google Maps']" style="position:relative;">
                        <img style=" width: 100%; height: 100%; background-color: rebeccapurple; border-radius: 0.5rem;" src="https://th.bing.com/th/id/R.68201495ac2d0c4d1cd3cbf6d25f6755?rik=l%2bilUrRDF30tdw&pid=ImgRaw&r=0"/>
                        
                        

                    </a>
                    
                    
                
                
                </div>

                </div>

            </div>


        </div>

    </div>
</template>

<script setup>



import { PrimeIcons } from 'primevue/api';

import { URI } from "@/service/conection"

const sedes  = [
  {
    "site_id":1,
    "Nombre": "BRETAÑA",
    "Dirección": "Calle 10#21-42 Bretaña",
    "WSP": "3172373979",
    "Google Maps": "https://maps.app.goo.gl/6kCLNgDfz84224ZV9",
    "Ciudad": "Cali",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {
    "site_id":2,
    "Nombre": "LA FLORA",
    "Dirección": "Calle 44 Norte Av 3E-89 la Flora",
    "WSP": "3053447255",
    "Google Maps": "https://maps.app.goo.gl/U3mgpvq2579eFwzd9",
    "Ciudad": "Cali",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {
    "site_id":3,
    "Nombre": "CANEY",
    "Dirección": "Carrera 85 # 37-10. Caney",
    "WSP": "3202017941",
    "Google Maps": "https://maps.app.goo.gl/LZhCH5yJoXoPVKKc8",
    "Ciudad": "Cali",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {
    "site_id":4,
    "Nombre": "ALFAGUARA",
    "Dirección": "Carrera 22 # 5A sur - 60",
    "WSP": "3014344948",
    "Google Maps": "https://maps.app.goo.gl/j8aF4rQHarENfS3L7",
    "Ciudad": "Cali",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {
    "site_id":5,
    "Nombre": "PALMIRA",
    "Dirección": "Carrera 44 # 26-32",
    "WSP": "3207491902",
    "Google Maps": "https://maps.app.goo.gl/cXdY5245NutnWFjF6",
    "Ciudad": "Palmira",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {
    "site_id":6,
    "Nombre": "TULUA",
    "Dirección": "Carrera 40 # 21 -22",
    "WSP": "304 3783714",
    "Google Maps": "https://maps.app.goo.gl/a79GpFei41mWNYeG9",
    "Ciudad": "Tulua",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {
    "site_id":7,
    "Nombre": "MODELIA",
    "Dirección": "Carera 75 # 25C - 45",
    "WSP": "3004096439",
    "Google Maps": "https://maps.app.goo.gl/krfe3WeK3jbZzse96",
    "Ciudad": "Bogotá",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {"site_id":8,
    "Nombre": "SUBA",
    "Dirección": "Carera 92 # 147B -17",
    "WSP": "3135932936",
    "Google Maps": "https://maps.app.goo.gl/dbsagQttfBq6RcyAA",
    "Ciudad": "Bogotá",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {
    "site_id":9,
    "Nombre": "MONTES",
    "Dirección": "Calle 8sur #32a -08",
    "WSP": "3193028785",
    "Google Maps": "https://maps.app.goo.gl/ayhRgyU2T8BxSSnM6",
    "Ciudad": "Bogotá",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {
    "site_id":10,
    "Nombre": "KENNEDY",
    "Dirección": "Carrera 78b # 38sur-79",
    "WSP": "3006721974",
    "Google Maps": "https://maps.app.goo.gl/7Xd1zsYXKw1hC6SZ8?g_st=ic",
    "Ciudad": "Bogotá",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  },
  {
    "site_id":11,
    "Nombre": "LAURELES",
    "Dirección": "Transversal 39  #74 B-14 PRIMER PISO",
    "WSP": "3207950433",
    "Google Maps": "https://maps.app.goo.gl/SrTRXEbEC3fhnK5W7",
    "Ciudad": "Medellín",
    "Foto": "https://lh3.googleusercontent.com/p/AF1QipNacg4X8DwsUhEkQ9a-VMWg6RUgCX-NdrrExueh=s680-w680-h510"
  }
]

</script>


<style scoped>

*{
    text-transform: uppercase
}


</style>