import { createRouter, createWebHashHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';
import axios from 'axios';

import { URI } from '@/service/conection'
import { menuOptions } from '@/service/menuOptions';
import { ableMenu } from '../service/menuOptions';

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      component: AppLayout,
      children: [
        {
          path: '/',
          name: 'Home',
          component: () => import('@/views/pages/Home.vue'),
          // meta: { requiresAuth: true },
        },

        {
          path: '/sedes',
          name: 'sedes',
          component: () => import('@/views/pages/sedes.vue'),
          // meta: { requiresAuth: true },
        },
        {
          path: '/menu',
          name: 'menu',
          component: () => import('@/views/pages/MenuView.vue'),
          // meta: { requireMenu: true },
        },
        {
          path: '/menu-admin',
          name: 'menuAdmin',
          component: () => import('@/views/pages/MenuViewAdmin.vue'),
          // meta: { requireMenu: true },
        },

        {
          path: '/cart',
          name: 'cart',
          component: () => import('@/views/pages/cart.vue'),
          // meta: { requireMenu: true },
        },
        {
          path: '/pay',
          name: 'pay',
          component: () => import('@/views/pages/pay.vue'),
          // meta: { requireMenu: true },
        },



        {
          path: '/product/:product_id',
          name: 'product',
          component: () => import('@/views/pages/ProductView.vue'),
          // meta: { requireMenu: true },
          // meta: { requiresAuth: true },
        },
        {
          path: '/combo/:combo_id',
          name: 'combo',
          component: () => import('@/views/pages/ComboView.vue'),
          // meta: { requireMenu: true },
          // meta: { requiresAuth: true },
        },
        // {
        //     path: '/uikit/formlayout',
        //     name: 'formlayout',
        //     component: () => import('@/views/uikit/FormLayout.vue')
        // },
        // {
        //     path: '/uikit/input',
        //     name: 'input',
        //     component: () => import('@/views/uikit/Input.vue')
        // },
        // {
        //     path: '/uikit/floatlabel',
        //     name: 'floatlabel',
        //     component: () => import('@/views/uikit/FloatLabel.vue')
        // },
        // {
        //     path: '/uikit/invalidstate',
        //     name: 'invalidstate',
        //     component: () => import('@/views/uikit/InvalidState.vue')
        // },
        // {
        //     path: '/uikit/button',
        //     name: 'button',
        //     component: () => import('@/views/uikit/Button.vue')
        // },
        // {
        //   path: '/uikit/table',
        //   name: 'table',
        //   component: () => import('@/views/uikit/Table.vue')
        // },

        // {
        //   path: '/pages/sites',
        //   name: 'sites',
        //   component: () => import('@/views/pages/ManageSites.vue')
        // },

        // {
        //   path: '/pages/site/:site_id',
        //   name: 'site',
        //   component: () => import('@/views/pages/ManageSite.vue')
        // },


        // {
        //     path: '/uikit/tree',
        //     name: 'tree',
        //     component: () => import('@/views/uikit/Tree.vue')
        // },
        // {
        //     path: '/uikit/panel',
        //     name: 'panel',
        //     component: () => import('@/views/uikit/Panels.vue')
        // },

        // {
        //     path: '/uikit/overlay',
        //     name: 'overlay',
        //     component: () => import('@/views/uikit/Overlay.vue')
        // },
        // {
        //     path: '/uikit/media',
        //     name: 'media',
        //     component: () => import('@/views/uikit/Media.vue')
        // },
        // {
        //     path: '/uikit/menu',
        //     component: () => import('@/views/uikit/Menu.vue'),
        //     children: [
        //         {
        //             path: '/uikit/menu',
        //             component: () => import('@/views/uikit/menu/PersonalDemo.vue')
        //         },
        //         {
        //             path: '/uikit/menu/seat',
        //             component: () => import('@/views/uikit/menu/SeatDemo.vue')
        //         },
        //         {
        //             path: '/uikit/menu/payment',
        //             component: () => import('@/views/uikit/menu/PaymentDemo.vue')
        //         },
        //         {
        //             path: '/uikit/menu/confirmation',
        //             component: () => import('@/views/uikit/menu/ConfirmationDemo.vue')
        //         }
        //     ]
        // },
        // {
        //     path: '/uikit/message',
        //     name: 'message',
        //     component: () => import('@/views/uikit/Messages.vue')
        // },
        // {
        //     path: '/uikit/file',
        //     name: 'file',
        //     component: () => import('@/views/uikit/File.vue')
        // },
        // {
        //     path: '/uikit/charts',
        //     name: 'charts',
        //     component: () => import('@/views/uikit/Chart.vue')
        // },
        // {
        //     path: '/uikit/misc',
        //     name: 'misc',
        //     component: () => import('@/views/uikit/Misc.vue')
        // },
        // {
        //     path: '/blocks',
        //     name: 'blocks',
        //     component: () => import('@/views/utilities/Blocks.vue')
        // },
        // {
        //     path: '/utilities/icons',
        //     name: 'icons',
        //     component: () => import('@/views/utilities/Icons.vue')
        // },
        // {
        //     path: '/pages/timeline',
        //     name: 'timeline',
        //     component: () => import('@/views/pages/Timeline.vue')
        // },
        // {
        //     path: '/pages/empty',
        //     name: 'empty',
        //     component: () => import('@/views/pages/Empty.vue')
        // },

        // {
        //   path: '/pages/cumples',
        //   name: 'cumples',
        //   component: () => import('@/views/pages/cumples.vue'),
        //   // meta: { requiresAuth: true },
        // },
        // {
        //     path: '/pages/sitesCrud',
        //     name: 'sitesCrud',
        //     component: () => import('@/views/pages/sitesCrud.vue')
        // },
        // {
        //     path: '/documentation',
        //     name: 'documentation',
        //     component: () => import('@/views/utilities/Documentation.vue')
        // }
      ]
    },

    // {
    //     path: '/landing',
    //     name: 'landing',
    //     component: () => import('@/views/pages/Landing.vue')
    // },
    // {
    //     path: '/pages/notfound',
    //     name: 'notfound',
    //     component: () => import('@/views/pages/NotFound.vue')
    // },

    // {
    //   path: '/login',
    //   name: 'login',
    //   component: () => import('@/views/pages/auth/Login.vue')
    // },
    // {
    //     path: '/auth/access',
    //     name: 'accessDenied',
    //     component: () => import('@/views/pages/auth/Access.vue')
    // },
    // {
    //     path: '/auth/error',
    //     name: 'error',
    //     component: () => import('@/views/pages/auth/Error.vue')
    // }
  ]
});

router.beforeEach((to, from, next) => {
  const reqMenu = to.matched.some((record) => record.meta.requireMenu);

  if (reqMenu) {
    // Verifica si el usuario tiene un token de acceso válido en el Local Storage
    const menu = ableMenu.value

    if (!menu) {
      // Si no tiene un token válido, redirige al inicio de sesión
      next('/menu');
    } else {
      // Si tiene un token válido, verifica su validez en el backend con fetch

      // Si la ruta no requiere autenticación, permite el acceso
      next();
    }

  }else{
    next()
  }});


export default router;


