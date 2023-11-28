<script setup>
import { useLayout } from '@/layout/composables/layout';
import { ref, computed } from 'vue';
import AppConfig from '@/layout/AppConfig.vue';
import router from '@/router/index.js'
import { useToast } from 'primevue/usetoast';
import {URI} from '@/service/conection'

const toast = useToast();
const { layoutConfig } = useLayout();
const email = ref('');
const password = ref('');
const checked = ref(false);


const send = () =>{
    console.log(email.value)
}

const getToken = async () => {
    // URL de la API para obtener el token (asegúrate de que sea la URL correcta)
    const formData = new FormData();
    formData.append('username', email.value);
    formData.append('password', password.value);
  
    try {
      // Realiza la solicitud POST al endpoint /token
      const response = await fetch(`${URI}/token`, {
        method: 'POST',
        body: formData,
        
      });
  
      if (response.ok) {
        // Si la respuesta es exitosa, obtén el token de acceso
        const data = await response.json();
        const accessToken = data.access_token;
        // Ahora puedes usar el token de acceso en tus solicitudes posteriores
        console.log('Token:', accessToken);

        localStorage.setItem('accessToken', accessToken);
        router.push('/');
        toast.add({ severity: 'succes', summary: 'Bienvenido', detail: '', life: 3000 })

        
    } else {
        // Si la respuesta no es exitosa, maneja el error de inicio de sesión
        console.error('Error de inicio de sesión:', response.statusText);
        toast.add({ severity: 'error', summary: 'Usuario o contrasea incorrectos', detail: '', life: 3000 })


      }
    } catch (error) {
      console.error('Error al enviar la solicitud:', error);
    }
};






</script>

<template>
    <Toast />
    <div class="flex align-items-center justify-content-center min-h-screen min-w-screen overflow-hidden" >
        <div class="flex flex-column align-items-center justify-content-center" > 
            <img src="@/images/logo.png" alt=" logo" class="mb-5 w-6rem flex-shrink-0" />
            <div style=" border-radius: 53px; border: 3px solid var(--primary-color); border-radius: 56px; padding: 0.3rem; background: linear-gradient(180deg, var(--primary-color) 10%, rgba(0, 0, 0, 0) 50%)">
                <div class="w-full surface py-8 px-5 sm:px-8" >
                    <div class="text-center mb-5">
                        <img src="/demo/images/login/avatar.png" alt="Image" height="50" class="mb-3" />
                        <div class="text-white text-3xl font-medium mb-3">Bienvenido, Admin!</div>
                        <span class="text-600 text-white font-medium">Inicia sesion para continuar</span>
                    </div>

                    <div>
                        <label for="email1" class="block text-900 text-xl font-medium mb-2">Correo Electronico</label>
                        <InputText id="email1" type="text" placeholder="correo electronico" class="w-full md:w-30rem mb-5" style="padding: 1rem" v-model="email" />

                        <label for="password1" class="block text-900 font-medium text-xl mb-2">Contrasena</label>
                        <Password id="password1" v-model="password" placeholder="contrasena" :toggleMask="true" class="w-full mb-3" inputClass="w-full" :inputStyle="{ padding: '1rem' }"></Password>

                        <div class="flex align-items-center justify-content-between mb-5 gap-5">
                            <div class="flex align-items-center">
                                <Checkbox v-model="checked" id="rememberme1" binary class="mr-2"></Checkbox>
                                <label for="rememberme1">Recuerdame</label>
                            </div>
                            <a class="font-medium no-underline ml-2 text-right cursor-pointer" style="color: var(--primary-color)">Forgot password?</a>
                        </div>
                        <Button label="Iniciar Sesion" class="w-full p-3 text-xl button-send" style=" border:none;background-color: var(--primary-color)" @click="getToken"></Button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <AppConfig simple />
</template>

<style scoped>
.pi-eye {
    transform: scale(1.6);
    margin-right: 1rem;
}

.pi-eye-slash {
    transform: scale(1.6);
    margin-right: 1rem;
}
.button-send:hover{
    filter: brightness(1.3);
    border: none;

}
</style>
