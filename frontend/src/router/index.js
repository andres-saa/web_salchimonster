import { createRouter, createWebHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';

import pixel from './pixel';

import { URI } from '@/service/conection'
import { verCerrado } from '../service/state';
import { useSitesStore } from '../store/site';
import {loginStore} from '@/store/userCall.js'
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';
















const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: AppLayout,
      children: [
        {
          path: '/',
          name: 'Home',
          component: () => import('@/views/pages/MenuView.vue'),
          children: [
            {
              path: '/:menu_name/:category_id',
              name: 'sesion',
              component: () => import('@/views/pages/sesion.vue'),
              meta: { title:'MENU' },
            },
            {
              path: '/',
              name: 'main',
              component: () => import('@/views/pages/sesion_main.vue'),
            },
          ]

        },

        {
          path: '/sedes',
          name: 'sedes',
          component: () => import('@/views/pages/sedes.vue'),
          meta: { title:'Sedes' },
        },

        {
          path: '/gracias',
          name: 'gracias',
          component: () => import('@/views/pages/gracias.vue'),
          meta: { requirePay: true, title:'Gracias' },
        },
        {
          path: '/menu-view',
          name: 'menu-view',
          component: () => import('@/views/pages/MenuView.vue'),
          meta: { title:'Menu' },
        },
        {
          path: '/menu',
          name: 'menu',
          component: () => import('@/views/pages/carta.vue'),
          meta: { title:'Carta' },
        },

        {
          path: '/rastrear-pedido',
          name: 'rastrear-pedido',
          component: () => import('@/views/pages/rastrear.vue'),
          meta: { title:'Rastrear pedido' },
        },

        {
          path: '/cart',
          name: 'cart',
          component: () => import('@/views/pages/cart.vue'),
         
        },
        {
          path: '/ingreso-call-center',
          name: 'ingreso-call-center',
          component: () => import('@/views/pages/auth/login.vue'),
        
        },
        {
          path: '/pay',
          name: 'pay',
          component: () => import('@/views/pages/pay.vue'),
          meta: { requireOpen: true, title:'Finalizar pedido' },
        },
        {
          path: '/colaboraciones',
          name: 'colaboraciones',
          component: () => import('@/views/pages/colaboraciones.vue'),
          meta: {  title:'colaboraciones' },
        },

        
        {
          path: '/pqrs-user',
          name: 'pqrs-user',
          component: () => import('@/views/pages/pqrUser.vue'),
         
        },


        {
          path: '*',
          name: 'all',
          component: () => import('@/views/pages/sesion_main.vue'),
          // meta: { requireOpen: true },
        },
      ]
    },
  ]
});




const estado = async(site_id) => {
  const response = await fetch(`${URI}/site/${site_id}/status`);
  const data = await response.json();
return data
// console.log(data)
}

router.beforeEach(async(to, from, next) => {
  
  


  if (to.params.menu_name) {
    // Configurar el título de la página usando el 'menu_name'
    document.title = `${to.meta.title} - ${to.params.menu_name}`;
  } else {
    // Configurar un título por defecto si no hay 'menu_name'
    document.title = to.meta.title || 'Salchimonster';
  }






  const store  = useSitesStore()
  const site_id = store.location.site.site_id
  // alert(site_id)
  // console.log(site_id)
  // const open = await estado(site_id)
  console.log(open)

  if (to.matched.some(record => record.meta.requireOpen)) {
    // const token = thanks_data.value?.user_data;

    if (store.status == 'cerrado' && site_id) {
      verCerrado.value = true
      next()

    } else {
      // Si hay token, permite el acceso
      next();
    }
  } else {
    // Si la ruta no requiere autenticación, permite el acceso
    next();
  }
});






pixel.init()
router.afterEach( ( to, from ) => {
  // Esto rastreará una "PageView" cada vez que el usuario cambie de ruta
  pixel.sendTrackingEvent( 'PageView');
});






// const validateToken = (token) => {

//   const store = loginStore()
//   if (!token){
//     return null
//   }
//   return axios.get(`${URI}/validate-token`, {
//     headers: {
//       Authorization: `Bearer ${token}`
//     }
//   })
//   .then(response => {
//     // Aquí manejas la respuesta positiva
//     if (response.data.access_token) {
//       store.setUserData(response.data)
//     }
//     return response.data;
//   })
//   .catch(error => {
//     // Manejo de errores si el token es inválido o expirado
//     console.error("Error durante la validación del token:", error);
//     throw error;
//   });
// }




// router.beforeEach(async(to, from, next) => {
//   console.log(to.meta)
//   const store = loginStore()
//   const token = store.userData.access_token
//   const validToken = await validateToken(token)
  
//   if (token && !validToken.access_token ) {
//     if (to.path !== '/ingreso-call-center' ) {
//       store.userData = {}
//       next({ path: '/ingreso-call-center' });
      
//     } else {
//       store.userData = {}

//       next();
//       return // Si ya está en la página de login, continúa
//     }
//   } else {

//     try {

//       let decoded = ''
//       if(token){
//          decoded = jwtDecode(token);
//       }else {
//         next();
//         return
//       }
      
//       if (!decoded || !decoded.rol) {
//         console.error("Rol no encontrado en el token");
//         next({ path: '/ingreso-call-center' });
//         return;
//       }

//       const userRole = decoded.rol?.split(" ").join('').toLowerCase();


//       const isRoleAuthorized = to.matched.some(record => {
//         if (!record.meta || !record.meta.roles) {
//           return false;
//         }

//         const routeRoles = record.meta.roles.map(role => role?.split(" ").join('').toLowerCase());
//         return routeRoles.includes(userRole);
//       });

//       if (isRoleAuthorized || !to.matched.some(record => record.meta?.roles)) {
//         next(); // Rol permitido o no se requiere control de rol
//       } else {
//         alert(`No tienes permitido entrar aqui`)
//         next('./'); // Rol no permitido
//       }
//     } catch (error) {
//       console.error("Error al decodificar el token:", error);
//       next({ path: '/error' }); // Error en el token o en la decodificación
//     }
//   }
// });

export default router


