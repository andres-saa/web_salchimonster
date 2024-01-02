<template>
    <div>
      <form @submit.prevent="login">
        <input v-model="credentials.username" type="text" placeholder="Username" />
        <input v-model="credentials.password" type="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { URI } from '../../../service/conection';
  import router from '@/router/index'
  export default {
    setup() {
      const credentials = ref({ username: '', password: '' });
  
      const login = async () => {
        const formData = new URLSearchParams();
        formData.append('username', credentials.value.username);
        formData.append('password', credentials.value.password);
  
        try {
            const response = await fetch(`${URI}/token-employer`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData,
          });
  
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
  
          const data = await response.json();
          localStorage.setItem('token', data.access_token);
          router.push('/actualizar-datos')
          // Redireccionar a la página de inicio o donde sea necesario
        } catch (error) {
          console.error(error);
        }
      };
  
      return { credentials, login };
    }
  };
  </script>
  