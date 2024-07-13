
<template>
    <Dialog style="width: 30rem; background-color: #fff;" v-model:visible="visible" modal>
    <div class="card flex justify-content-center">
        <InputOtp v-model="value">
            <template #default="{ attrs, events }">
                <input type="text" v-bind="attrs" v-on="events" class="custom-otp-input" />
            </template>
        </InputOtp>
    </div>
</Dialog>
</template>

<script setup>
import { ref } from 'vue';

const value = ref(null);
</script>

<style scoped>
.custom-otp-input {
    width: 40px;
    font-size: 36px;
    border: 0 none;
    appearance: none;
    text-align: center;
    transition: all 0.2s;
    background: transparent;
    border-bottom: 2px solid var(--surface-500);
}

.custom-otp-input:focus {
    outline: 0 none;
    border-bottom-color: var(--primary-color);
}
</style>
