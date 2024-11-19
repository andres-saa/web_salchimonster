<template>


<Dialog class="mx-4" v-model:visible="visibleDialog" modal style="width:30rem ;background-color: white;">

    <div style="height: auto;color: black;background-color: white; display: flex;flex-direction: column;justify-content: end;align-items: center;" >

        <h4>Hemos recibido su solicitud y ha quedado registrada con el id   </h4> <br><b> <p class="text-center" style="width: auto;font-size: 3rem;">{{ last_id }}</p></b>
        
        
        <router-link to="/">
            <Button class="m-auto" style="font-weight: bold;" severity="info" label="Listo"></Button>
        </router-link>
        
    </div>
</Dialog>





<Dialog class="mx-4" v-model:visible="visibleDialogGRacias" modal style="width: 30rem;background-color: white">

<div style="height: auto;color: black;display: flex;flex-direction: column;justify-content: end;align-items: center;" >

 <br><b> <p class="text-center" style="width: auto;font-size: 3rem;"> Muchas gracias</p></b>
    
    
    <router-link to="/">
        <Button class="m-auto" style="font-weight: bold;" severity="info" label="Listo"></Button>
    </router-link>
    
</div>
</Dialog>



    <div class="container mt-8 col-12 p-4 shadow-3" style="max-width: 400px; margin: auto;">
      <h2 class="mb-0">🔥 <b>MONSTER AYUDA</b> 🔥</h2>
      <h2 style="color: var(--primary-color)" class="my-0"><b>Cada dia mejoramos</b></h2>
      <img src="/public/images/characters/5.png">
  
      <div class="form" style="width: 100%; display: flex; flex-direction: column; gap: 1rem;">
        <!-- Selección de Tipo de Requerimiento -->
        <div class="input">
          <h5 class="field">¿Cómo te podemos ayudar?</h5>
          <Dropdown v-model="selectedType" optionValue="id" style="width: 100%; text-transform: uppercase;" :options="types.filter(t => t.show_on_web)" optionLabel="name"></Dropdown>
        </div>


         <!-- Selección de Sede -->
         <div class="input" v-if="(selectedType && selectedType != 8)" >
          <h5 class="field">Por favor clasifica tu inconveniente</h5>
          <Dropdown :options="tags" v-model="selecte_tag"   style="width: 100%;">
  
            <template #option="option">
                <div style="display: flex;align-items: center;gap: 1rem; ">
                  <Tag :style="`background-color:${option.option.color}`" style="height: 1.5rem;aspect-ratio: 1 / 1; border-radius:50%;">
                    
                  </Tag> <h6 class="p-0 m-0">{{ option.option.name }}</h6>
                </div>
            </template>



            <template #value="value">
                <div style="display: flex;align-items: center;gap: 1rem; ">
                  <Tag :style="`background-color:${value.value.color}`" style="height: 1.5rem;aspect-ratio: 1 / 1; border-radius:50%;">
                    
                  </Tag> <h6 class="p-0 m-0">{{ value.value.name }}</h6>
                </div>
            </template>
            
          </Dropdown>
        </div>
  
  
        <!-- Selección de Sede -->
        <div class="input" v-if="(selectedType)">
          <h5 class="field">Sede</h5>
          <Dropdown :options="sites.filter(s => s.show_on_web)" v-model="selecteSite" optionValue="site_id" optionLabel="site_name" style="width: 100%;"></Dropdown>
        </div>
  
        <!-- ID de la Orden -->
        <div class="input" v-if="selectedType && selectedType == 9">
          <h5 class="field">ID de la orden ejemplo <b>BRE-0554</b></h5>
          <InputText v-model="orderId" style="width: 100%;" placeholder="Escriba el número de la orden"></InputText>
        </div>
  
        <!-- Calificación -->
        <div class="input p-3" v-if="(selectedType && (selectedType == 9 || selectedType == 8))" style="background-color: #00f3ff29;">
          <h5 class="field">Califícanos</h5>
          <Rating v-model="rating" :cancel="false"></Rating>
        </div>
  
        <!-- Comentarios -->
        <div class="input" v-if="selectedType">
          <h5 class="field">Comentarios</h5>
          <Textarea v-model="comments" rows="5" style="width: 100%; resize: none;" placeholder="Deja tus comentarios"></Textarea>
        </div>
  
        <!-- Información del Usuario -->
        <div class="input" v-if="selectedType ">
          <h5 class="field">Nombre</h5>
          <InputText v-model="userName" style="width: 100%;" placeholder="Escriba su nombre por favor"></InputText>
        </div>
  
        <div class="input" v-if="selectedType ">
          <h5 class="field">Número de teléfono</h5>
          <InputNumber :useGrouping="false" v-model="userPhone" style="width: 100%;" placeholder="Escriba su número de teléfono"></InputNumber>
        </div>
  
        <div class="input" v-if="selectedType ">
          <h5 class="field">Dirección (opcional)</h5>
          <InputText v-model="userAddress" style="width: 100%;" placeholder="Escriba su dirección"></InputText>
        </div>
  
        <!-- Botón de Envío -->
        <div class="input" style="display: flex; justify-content: end;">
          <Button label="Enviar" style="font-weight: bold;" severity="info" @click="handleSubmit"> </Button>
        </div>
      </div>
    </div>
  </template>
<script setup>
import { ref, onMounted } from 'vue';
import { pqrsService } from '@/service/pqrs/pqrsService';
import { fetchService } from '@/service/utils/fetchService.js';
import { URI } from '../../service/conection';
import router from '../../router';

const last_id = ref()
const selecte_tag = ref({})
const visibleDialog = ref(false)
const pqrs = ref([]);
const visibleDialogGRacias = ref(false)
const selectedType = ref();
const selecteSite = ref();
const sites = ref([]);
const types = ref([]);
const orderId = ref('');
const userName = ref('');
const userPhone = ref('');
const userAddress = ref('');
const comments = ref('');
const rating = ref(null);
const tags = ref([{}])

const update = async () => {
  pqrs.value = await pqrsService.getPqrsByPlaceId(1);
};

const handleSubmit = async () => {
  // Validación de campos obligatorios
  if (!selectedType.value) {
    alert('Por favor, seleccione un tipo de requerimiento.');
    return;
  }
  if (selectedType.value == 9 && !orderId.value) {
    alert('Por favor, ingrese el ID de la orden.');
    return;
  }

  if ( selectedType.value != 8 && !selecte_tag.value) {
    alert('Por favor, Clasifica tu inconveniente');
    return;
  }



  if (selectedType.value != 8 && !comments.value) {
    alert('Por favor, Cuentenos lo sucedido');
    return;
  }


  if (selectedType.value != 8 && (!userName.value || !userPhone.value)) {
    alert('Por favor, complete los campos obligatorios (nombre y teléfono).');
    return;
  } 

  if (!selecteSite.value) {
    alert('Por favor, Seleccione la sede');
    return;
  }


  if ((selectedType.value == 8 && !rating.value)) {
    alert('Por favor, Seleccione una calificacion');
    return;
  }

  // Construcción del objeto de datos
  const data = {
    data: {
      reques_type_id: selectedType.value,
      content: comments.value || 'Sin comentarios',
      channel_id: 1, // Ajustar según el canal,
      rating:rating.value || null,
      site_id: selecteSite.value || null,
      order_id:orderId.value || null,
      network_id:4,
      tag_id:selecte_tag.value?.id || 7,
      restaurant_id:1
    },
    user: {
      user_name: userName.value || '',
      user_phone: userPhone.value?.toString() || '',
      user_address: userAddress.value || '',
      site_id: selecteSite.value || null
    }
  };

  // Envío de datos
  try {

    const result = await fetchService.post(`${URI}/create-pqr`, data);
   last_id.value = result?.pqr_id[0]?.id
   if (selectedType.value == 8){
    visibleDialogGRacias.value = true
    emi
   } else {
    visibleDialog.value = true
   }

  } catch (error) {

  }
};

onMounted(async () => {
  update();
  types.value = await fetchService.get(`${URI}/get-all-pqrs-types`);
  sites.value = await fetchService.get(`${URI}/sites`);
  tags.value = await fetchService.get(`${URI}/get-all-pqr-tags`);
  selectedType.value = 8;
});



</script>

<style scoped>
.pqrs {
    list-style: none;
    margin: 0;
    padding: 0;
    width: 100%;
    max-width: 900px;
}

.pqrs-element {
    border-radius: .3rem;
}

.field{
    margin:.5rem 0;
    
}

.bar {
    max-width: 900px;
    display: flex;
    justify-content: end;
}

.input{
    width: 100%;
}

.container {
    padding: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    margin-top: 3rem;
}

@keyframes an_show_actions {
    0% {
        opacity: 0;
        transform: translateX(20px);
    }

    100% {
        opacity: 1;
    }
}

@keyframes an_show_actions_2 {
    100% {
        opacity: 0;
        transform: translateX(20px);
    }

    0% {
        opacity: 1;
    }
}

.button-visible {
    animation: an_show_actions .3s ease;
}

.button-hide {
    animation: an_show_actions_2 .3s ease;
}

/* Transición de fade */
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>
