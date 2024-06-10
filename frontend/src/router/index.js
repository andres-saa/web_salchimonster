import { createRouter, createWebHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';

import pixel from './pixel';

import { URI } from '@/service/conection'
import { verCerrado } from '../service/state';
import { useSitesStore } from '../store/site';

















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
          path: '/ingreso-call-center',
          name: 'ingreso-call-center',
          component: () => import('@/views/pages/auth/login.vue'),
          meta: { requireOpen: true },
        },
        {
          path: '/pay',
          name: 'pay',
          component: () => import('@/views/pages/pay.vue'),
          meta: { requireOpen: true },
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
  const store  = useSitesStore()
  const site_id = store.location.site.site_id
  // alert(site_id)
  // console.log(site_id)
  const open = await estado(site_id)
  console.log(open)

  if (to.matched.some(record => record.meta.requireOpen)) {
    // const token = thanks_data.value?.user_data;

    if (open.status == 'closed') {
      verCerrado.value = true
      next('/')

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
router.afterEach((to, from) => {
  // Esto rastreará una "PageView" cada vez que el usuario cambie de ruta
  pixel.track('PageView');
});


export default router


