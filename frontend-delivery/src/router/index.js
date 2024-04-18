import { createRouter, createWebHashHistory,createWebHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';
import axios from 'axios';

import { URI } from '@/service/conection'
import { menuOptions } from '@/service/menuOptions';
import { ableMenu } from '../service/menuOptions';

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
          component: () => import('@/views/pages/Home.vue'),
          meta: { requiresAuth: true }, 
          children: [
            {
              path: '/',
              name: 'pedidos',
              component: () => import('@/views/pages/pedidos.vue'),
              
            },
            {
              path: '/cuadre',
              name: 'cuadre',
              component: () => import('@/views/pages/cuadre.vue'),
              
            },
            {
              path: '/horarios',
              name: 'horarios',
              component: () => import('@/views/pages/horarios.vue'),
              
            },
            {
              path: '/historial',
              name: 'historial',
              component: () => import('@/views/pages/historial-pedidos.vue'),
              
            },
            {
              path: '/resumen-sedes',
              name: 'resumen-sedes',
              component: () => import('@/views/pages/views_admin/resumen_sedes.vue'),
              
            },
            {
              path: '/pedido-manual',
              name: 'pedido-manual',
              component: () => import('@/views/pages/tienda/pedidoManual.vue'),
              
            },

            {
              path: '/tienda-menu',
              name: 'menuTienda',
              component: () => import('@/views/pages/tienda/MenuTienda.vue'),
              children:[
                  {
                    path: 'productos/:menu_name/:category_id',
                    name: 'sesion',
                    component: () => import('@/views/pages/tienda/sesion.vue')
                    // meta: { requireMenu: true },
                    // meta: { requiresAuth: true },
                  },

                  {
                    path: 'productos/adicionales',
                    name: 'adicionales',
                    component: () => import('@/views/pages/tienda/adicionales.vue')
                    // meta: { requireMenu: true },
                    // meta: { requiresAuth: true },
                  },
                  // {
                  //     path: '/tienda-menu/productos/:sesion',
                  //     name: 'tienda-productos',
                  //     component: () => import('@/views/pages/tienda/sesion.vue')
                  // },
                  

              ]
          },
          
          ]
        },

      ]
    },

    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/pages/auth/Login.vue')
    },

  ]
});



router.beforeEach(async (to, from, next) => {
  // Verificar si la ruta requiere autenticación
  if (to.meta.requiresAuth) {
    // Obtener el token de acceso desde localStorage
    const accessToken = localStorage.getItem('accessToken');
    if (!accessToken) {
      // Si no hay un token de acceso, redirigir a la página de inicio de sesión
      next('/login');
    } else {
      // Si hay un token de acceso, continuar con la navegación
      next();
    }
  } else {
    // Si la ruta no requiere autenticación, continuar con la navegación
    next();
  }
});


export default router