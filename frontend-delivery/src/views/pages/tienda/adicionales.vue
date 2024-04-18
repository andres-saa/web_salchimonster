<template>
    <div class="m-auto" style="max-width: 1024px;">
        <p class="text-center text-3xl col-12" style="font-weight: bold; display: flex; gap: 1rem; align-items: center;">
            <div style="width: 100%; height: 5px; background-color: #ff6200"></div>
                ADICIONALES
            <div style="width: 100%; height: 5px; background-color: #ff6200"></div>
        </p>
    </div>

    <div class="m-auto col-12" style="max-width: 600px;" v-for="(items, grupo) in adicionales" :key="grupo">
        <p class="text-center text-2xl" style="font-weight: bold;text-transform: capitalize;">{{ grupo }}</p>
        <DataTable :value="items">
            <Column style="text-transform: capitalize;" class="p-0" field="aditional_item_name" header="Nombre">
            
                <template #body="adicion">

                <span style="text-transform: uppercase;"> {{ adicion.data.aditional_item_name }}</span>
                
                </template>
            
            </Column>
            <Column class="p-0" field="aditional_item_price" header="Precio">
             <template  #body="adicion">
                <span style="font-weight: bold;">
                    {{ formatoPesosColombianos(adicion.data.aditional_item_price) }}

                </span>
            
            </template>
            
            </Column>
            <Column class="py-0 pl-4" header="Estado" headerStyle="width:1rem">
                <template #body="adicion">
                    <InputSwitch v-model="adicion.data.status" @change="updateStatus(adicion.data.aditional_item_instance_id, adicion.data.status)" />
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script setup>
import { adicionalesService } from '@/service/restaurant/aditionalService';
import { onMounted, ref } from 'vue';
import { formatoPesosColombianos } from '../../../service/formatoPesos';

const adicionales = ref({});

onMounted(async () => {
   adicionales.value = await adicionalesService.getAllAditions();
});

const updateStatus = async (aditional_item_instance_id, status) => {
    try {
        const updateData = { status }; // This can be expanded to include other fields if necessary
        const result = await adicionalesService.toggleAditionalStatus(aditional_item_instance_id, updateData);
        if (!result) {
            throw new Error("Failed to update the status");
        }
        console.log('Status updated successfully:', result);
    } catch (error) {
        console.error('Error updating status:', error);
    }
}
</script>


<style scoped>
*{
    text-transform: uppercase;
}
</style>