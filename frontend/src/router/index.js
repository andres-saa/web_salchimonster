import { createRouter, createWebHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';

import pixel from './pixel';
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
        },

        {
          path: '/gracias',
          name: 'gracias',
          component: () => import('@/views/pages/gracias.vue'),
          meta: { requirePay: true },
        },
        {
          path: '/menu-view',
          name: 'menu-view',
          component: () => import('@/views/pages/MenuView.vue'),
        },
        {
          path: '/menu',
          name: 'menu',
          component: () => import('@/views/pages/carta.vue'),
        },

        {
          path: '/rastrear-pedido',
          name: 'rastrear-pedido',
          component: () => import('@/views/pages/rastrear.vue'),
        },

        {
          path: '/cart',
          name: 'cart',
          component: () => import('@/views/pages/cart.vue'),
          meta: { requireOpen: true },
        },
        {
          path: '/pay',
          name: 'pay',
          component: () => import('@/views/pages/pay.vue'),
        },
      ]
    },
  ]
});





pixel.init()
router.afterEach((to, from) => {
  // Esto rastreará una "PageView" cada vez que el usuario cambie de ruta
  pixel.track('PageView');
});


export default router


