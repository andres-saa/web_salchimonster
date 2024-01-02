<template>



    <div class="col-12 p-0" style=" position: sticky;top: 4.7rem;z-index:300 ; box-shadow: 0 0 20px rgba(0, 0, 0, 0.37); max-width: ">

        <nav>
            <ul class="p-3"
                style="font-weight: 500; display: flex; list-style: none; align-items: center;justify-content: center; gap: 2rem;background-color: white; ">
                <li>
                    <span class="text-lg nav-item">NUEVOS</span>
                </li>
                <li>
                    <span class="text-lg nav-ite">EN VIAJE</span>
                </li>
                <li>
                    <span class="text-lg nav-ite">ENTREGADOS</span>
                </li>
            </ul>
        </nav>
    </div>


    <div class="col-12 " v-for="i in [1, 1, 1, 1, 1, 1,1,1,1,1,1,1]" >

        <div class="p-3 " style="width: 100%; background-color: white;display: flex;justify-content: space-between; border-radius: 1rem; box-shadow: 0 0 1rem rgba(0, 0, 0, 0.334);">


            <div style="width: 100%; display: flex;gap: 1rem;">
                <span  @click="showDomiDialog = !showDomiDialog" class="p-2" style="color: var(--primary-color);" > ID 445559</span>
                <span class="p-2" style="font-weight: bold;"> $4.000</span>
            </div>

            <div style="width: 100%;display: flex;  justify-content: end; gap:1rem" >
                <button class="m-0 p-2" style="background-color: rgb(193, 255, 193);"> aceptar</button>
                <button @click="confirmDialog = !confirmDialog" class="m-0 p-2" style="background-color: rgb(255, 193, 193);"> cancelar</button>
                
            </div>
           

        </div>
      


    </div>



    <Dialog class="" style="background-color: white; border-radius: 1rem;" v-model:visible="showDomiDialog" modal header="Header" :style="{ width: '30rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">


        <div class="col-12 py-0" style=" display: flex; justify-content: space-between;flex-direction: column;">
        <span class="" style="font-weight: bold; color: black;">DIRECCIÓN: </span>
        <span class="" style="color: black;">CALLE 5 #93-54 mELENDEZ </span>

        </div>

    

    <button @click="showDomiDialog = !showDomiDialog"
                            style="width: 2rem;height: 2rem; border: none; position: absolute; right: -1rem; top:-1rem;background-color: var(--primary-color); border-radius: 50%; display: flex; align-items: center;justify-content: center; z-index: 9;">
                            <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>

                        </button>


   
</Dialog>






<Dialog class="" style="background-color: white; border-radius: 1rem;" v-model:visible="confirmDialog" modal header="Header" :style="{ width: '30rem' }" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">


<div class="col-12 py-0" style=" display: flex; justify-content: space-between;flex-direction: column;">
<span class="" style="font-weight: bold; color: black;">ESTA SEGURO DE RECHAZAR ESTE DOMICILIO? </span>
<span class="" style="color: black;">CALLE 5 #93-54 mELENDEZ </span>

<div class="mt-4" style="width: 100%;display: flex;  justify-content: end; gap:1rem" >
                <button class="m-0 p-2" style="background-color: rgb(193, 255, 193);"> SI, CANCELAR</button>
                <button @click="confirmDialog = !confirmDialog" class="m-0 p-2" style="background-color: rgb(255, 193, 193);"> RECONSIDERAR</button>
                
            </div>

</div>



<!-- <button @click="confirmDialog = !confirmDialog"
                    style="width: 2rem;height: 2rem; border: none; position: absolute; right: -1rem; top:-1rem;background-color: var(--primary-color); border-radius: 50%; display: flex; align-items: center;justify-content: center; z-index: 9;">
                    <i :class="PrimeIcons.TIMES" style="color: white; font-weight: bold; " class="text-2xl"></i>

                </button> -->



</Dialog>

    
</template>



<script setup> 
import {ref} from 'vue'
import { PrimeIcons } from 'primevue/api';


const showDomiDialog = ref(false)
const confirmDialog = ref(false)



</script>
<style scoped>
.nav-item {
    border-bottom: 4px solid var(--primary-color);
    margin-bottom: -4px;
}

button{
    border: none;
    border-radius: 0.5rem;
}
</style>