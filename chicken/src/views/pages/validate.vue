<template>
    <Dialog modal class="mx-2" style="width: 20rem; display: flex; flex-direction: column; background-color: #fff;"
    
        v-model:visible="visible.visible.show_validate" >
        <div style="display: flex; flex-direction: column; gap: 2rem;position: relative;">


            <div style="position: absolute;background-color: #ffffff9f; left: 0;right: 0;width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;" v-if="visible.loading.visible">
                <ProgressSpinner   style="width: 100px; height: 100px" strokeWidth="4" 
        animationDuration=".1s" aria-label="Custom ProgressSpinner" />
            </div>


            <img src="/images/characters/5.png" alt="" style="width: 100%; max-width: 10rem;">
            <p style="max-width: 100%; color: black;">Hemos enviado un código de 3 dígitos a tu WhatsApp. Introdúcelo para validar tu pedido.</p>
            <div style="display: flex; gap: 1rem; margin: auto;">
                <InputText v-model="otp.first" id="firstInput" style="width: 3rem; height: 2rem; text-align: center;" maxlength="1"
                    @input="handleInput('first', $event)" @keydown.backspace="handleBackspace('first', $event)" />
                <InputText v-model="otp.second" id="secondInput" style="width: 3rem; height: 2rem; text-align: center;" maxlength="1"
                    @input="handleInput('second', $event)" @keydown.backspace="handleBackspace('second', $event)" />
                <InputText v-model="otp.third" id="thirdInput" style="width: 3rem; height: 2rem; text-align: center;" maxlength="1"
                    @input="handleInput('third', $event)" @keydown.backspace="handleBackspace('third', $event)" />
            </div>
        </div>

        <template #footer>
            <div>
                <Button :disabled="visible.loading.visible" @click="validar" style="border: none; width: 100%; font-weight: bold;" label="Validar mi pedido" severity="help"></Button>
            </div>
        </template>
    </Dialog>

    

</template>

<script setup>
import { ref, nextTick } from 'vue';
import InputText from 'primevue/inputtext';
import { useReportesStore } from '../../store/ventas';
import { validationService } from '../../service/order/validateService';
import { usecartStore } from '../../store/shoping_cart';
import Loading from '../../components/Loading.vue';
import ProgressSpinner from 'primevue/progressspinner';
const store = usecartStore();

const visible = useReportesStore();
const otp = ref({
    first: '',
    second: '',
    third: ''
});

const handleInput = (key, event) => {
    const value = event.target.value;
    if (/^\d$/.test(value)) {  // Solo permite un solo dígito numérico
        otp.value[key] = value;
        nextTick(() => focusNext(key));
    } else {
        event.target.value = '';  // Borra cualquier valor no numérico
    }
};

const handleBackspace = (key, event) => {
    if (event.target.value === '') {
        nextTick(() => focusPrevious(key));
    }
};

const focusNext = (key) => {
    if (key === 'first') {
        otp.value['second'] = '';
        document.querySelector('#secondInput').focus()
        
    } else if (key === 'second') {
        otp.value['third'] = '';
        document.querySelector('#thirdInput').focus();
        
    }
};

const focusPrevious = (key) => {
    if (key === 'second') {
        otp.value['fist'] = '';
        document.querySelector('#firstInput').focus();
       
    } else if (key === 'third') {
        document.querySelector('#secondInput').focus();
    }
};

const validar = async () => {
    const data = {
        order_id: store.last_order,
        order_code: otp.value.first + otp.value.second + otp.value.third
    };
    await validationService.validateOrder(data);
};
</script>

<style scoped></style>
