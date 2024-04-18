<script setup>
import { ref, onUnmounted } from 'vue';
import { useToast } from 'primevue/usetoast';
import { useRouter } from 'vue-router';
import { URI ,URI_SOCKET} from '../../../service/conection';
import { useSitesStore } from '../../../store/site';

const store = useSitesStore()
const email = ref('');
const password = ref('');
const toast = useToast();
const router = useRouter();
let webSocket = null;

const getToken = async () => {
    try {
        if (!email.value || !password.value) {
            toast.add({ severity: 'error', summary: 'Campos vacíos', detail: 'Por favor, completa todos los campos', life: 3000 });
            return;
        }

        const formData = new FormData();
        formData.append('username', email.value);
        formData.append('password', password.value);

        const response = await fetch(`${URI}/token`, {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('accessToken', data.access_token);
            localStorage.setItem('siteId', data.site_id);
            connectWebSocket(data.site_id);
            store.setSite(data)
            router.push('/');
            toast.add({ severity: 'success', summary: 'Bienvenido', detail: '', life: 3000 });
        } else {
            console.error('Error de inicio de sesión:', response.statusText);
            toast.add({ severity: 'error', summary: 'Usuario o contraseña incorrectos', detail: '', life: 3000 });
        }
    } catch (error) {
        console.error('Error al enviar la solicitud:', error);
        toast.add({ severity: 'error', summary: 'Error en la solicitud', detail: 'Por favor, intenta de nuevo más tarde', life: 3000 });
    }
};


function connectWebSocket(siteId) {
    webSocket = new WebSocket(`wss://${URI_SOCKET}/ws/${siteId}`);
    webSocket.onopen = () => console.log("WebSocket connected");
    webSocket.onmessage = (message) => console.log("Message received:", message.data);
    webSocket.onclose = () => console.log("WebSocket disconnected");
    webSocket.onerror = (error) => console.error("WebSocket error:", error);
}






</script>

<template>
    <Toast />
    <div class="flex align-items-center justify-content-center min-h-screen min-w-screen overflow-hidden" >
        <div class="flex flex-column align-items-center justify-content-center" > 
            <!-- <img src="images/logo.png" alt=" logo" class="mb-5 w-6rem flex-shrink-0" /> -->
            <div style=" border-radius: 1rem; border: 3px solid var(--primary-color); border-radius: 2rem;">
                <div class="w-full surface py-6 px-2 sm:px-5" >
                    <div class="text-center mb-5">
                        <img src="/images/logo.png" alt="Image" height="50" class="mb-3" />
                        <div style="color: black;" class="text-balck text-3xl font-medium mb-3">Bienvenido, Admin!</div>
                        <span class="text-600 text-white font-medium">Inicia sesion para continuar</span>
                    </div>

                    <div>
                        <label for="email1" class="block text-900 text-xl font-medium mb-2">Usuario</label>
                        <InputText id="email1" type="text" placeholder="Usuario" class="w-full md:w-30rem mb-5" style="padding: 1rem" v-model="email" />

                        <label for="password1" class="block text-900 font-medium text-xl mb-2">Contrasena</label>
                        <Password id="password1" v-model="password" placeholder="contrasena" :toggleMask="true" class="w-full mb-3" inputClass="w-full" :inputStyle="{ padding: '1rem' }"></Password>

                        <div class="flex align-items-center justify-content-between mb-5 gap-5">
                            <div class="flex align-items-center">
                                <!-- <Checkbox v-model="checked" id="rememberme1" binary class="mr-2"></Checkbox> -->
                                <!-- <label for="rememberme1">Recuerdame</label> -->
                            </div>
                            <!-- <a class="font-medium no-underline ml-2 text-right cursor-pointer" style="color: var(--primary-color)">Forgot password?</a> -->
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
