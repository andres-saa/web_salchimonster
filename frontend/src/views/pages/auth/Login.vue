<template>

    <div style="height: 80vh; display: flex; align-items: center; justify-content: center;" class="col-12 md:col-5">
    
        <div  style="box-shadow: 0 0 20px; border-radius: 1rem;">
      <h1 class="text-center">Login</h1>
      <form @submit.prevent="login" class="p-6 grid" style="gap: 0.1rem;border-radius: 1rem;">
        <label for="username" class="col-12">Username:</label>
        <input class="col-12" v-model="username" type="text" id="username" required>
        <br>
        <label class="col-12" for="password">Password:</label>
        <input class="col-12" v-model="password" type="password" id="password" required>
        <br>
        <button class="col-12" type="submit">Login</button>
      </form>
    </div>
    
    </div>
    
  </template>
  
  <script>
  import { ref } from 'vue';
  import router from '../../../router';
  
  export default {
    setup() {
      const username = ref('');
      const password = ref('');
  
      const login = async () => {
        try {
          const formData = new FormData();
          formData.append('username', username.value);
          formData.append('password', password.value);
  
          const response = await fetch('https://backend.salchimonster.com/token', {
            method: 'POST',
            body: formData,
          });
  
          if (!response.ok) {
            throw new Error('Login failed');
          }
  
          const data = await response.json();
          const token = data.token;
          localStorage.setItem('token-admin-fotos', token);
            router.push('/admin-products/Salchipapas');
        } catch (error) {
          console.error('Login failed', error);
          // Puedes manejar el error de la forma que prefieras (mostrar un mensaje, etc.)
        }
      };
  
      return { username, password, login };
    },
  };
  </script>
  