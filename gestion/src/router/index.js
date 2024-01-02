import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';
import { roles } from '../service/roles';
import { getUserRole } from '../service/valoresReactivosCompartidos';
import { jwtDecode } from 'jwt-decode';// import { roles } from '../service/roles';
const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: AppLayout,
            children: [
                {
                    path: '/',
                    name: 'dashboard',
                    component: () => import('@/views/pages/tienda/MenuTienda.vue'),
                },
                {
                    path: '/tienda-menu',
                    name: 'menuTienda',
                    component: () => import('@/views/pages/tienda/MenuTienda.vue'),
                    children:[
                        {
                            path: '/tienda-menu/:adicionales',
                            name: 'tienda-adicionales',
                            component: () => import('@/views/pages/tienda/sesionAdicionales.vue')
                        },
                        {
                            path: '/tienda-menu/productos/:sesion',
                            name: 'tienda-productos',
                            component: () => import('@/views/pages/tienda/sesion.vue')
                        },
                        

                    ]
                },
                {
                    path: '/domicilios/',
                    name: 'domicilios',
                    component: () => import('@/views/pages/domicilios.vue')
                },
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
                {
                    path: '/sites',
                    name: 'sites',
                    component: () => import('@/views/pages/ManageSites.vue')
                },
                {
                    path: '/cumples',
                    name: 'cumples',
                    component: () => import('@/views/pages/cumples.vue')
                },

  
                {
                  path: '/site/:site_id',
                  name: 'site',
                  component: () => import('@/views/pages/ManageSite.vue'),
                  children:[
                    {
                        path: '/site/:site_id/documentos',
                        name: 'documentos',
                        component: () => import('@/views/pages/ShowFiles.vue'),
                      
                      },
                      {
                        path: '/site/:site_id/recibos',
                        name: 'resibos',
                        component: () => import('@/views/pages/ShowRecibos.vue'),
                      
                      },

                  ]
                
                },
                {
                    path: '/certificado-laboral',
                    name: 'certificado-laboral',
                    component: () => import('@/views/pages/generarCertificado.vue')
                  },
                  {
                    path: '/permiso',
                    name: 'permiso',
                    component: () => import('@/views/pages/permiso.vue')
                  },
                  {
                    path: '/permiso-vacaciones',
                    name: 'permiso-vacaciones',
                    component: () => import('@/views/pages/permiso-vacaciones.vue')
                  },
                  {
                    path: '/permiso-licencia',
                    name: 'permiso-licencia',
                    component: () => import('@/views/pages/permiso-licencia.vue')
                  },
                  {
                    path: '/actualizar-datos',
                    name: 'actualizar-datos',
                    component: () => import('@/views/pages/dialogoEditUser.vue')
                  },
  
  
                // {
                //     path: '/uikit/button',
                //     name: 'button',
                //     component: () => import('@/views/uikit/Button.vue')
                // },
                // {
                //     path: '/uikit/table',
                //     name: 'table',
                //     component: () => import('@/views/uikit/Table.vue')
                // },
                // {
                //     path: '/uikit/list',
                //     name: 'list',
                //     component: () => import('@/views/uikit/List.vue')
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
                {
                    path: '/pages/crud',
                    name: 'crud',
                    component: () => import('@/views/pages/Crud.vue'),
                    meta: { roles: roles.administracion } // Asignación correcta dentro de 'meta'

                },
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
        // // {
        //     path: '/pages/notfound',
        //     name: 'notfound',
        //     component: () => import('@/views/pages/NotFound.vue')
        // },

        {
            path: '/auth/login',
            name: 'login',
            component: () => import('@/views/pages/auth/Login.vue')
        },
        {
            path: '/error',
            name: 'error',
            component: () => import('@/views/pages/error.vue')
        },
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
    const token = localStorage.getItem('token');

    // Verifica si hay un token
    if (!token) {
        // Si la ruta actual no es la de login, redirige al login
        if (to.path !== '/auth/login') {
            next({ path: '/auth/login' });
        } else {
            next(); // Si ya está en la página de login, continúa
        }
    } else {
        try {
            const decoded = jwtDecode(token);

            if (!decoded || !decoded.rol) {
                console.error("Rol no encontrado en el token");
                next({ path: '/error' });
                return;
            }

            const userRole = decoded.rol.trim().toLowerCase();

            const isRoleAuthorized = to.matched.some(record => {
                if (!record.meta || !record.meta.roles) {
                    return false;
                }

                const routeRoles = record.meta.roles.map(role => role.trim().toLowerCase());
                return routeRoles.includes(userRole);
            });

            if (isRoleAuthorized || !to.matched.some(record => record.meta?.roles)) {
                next(); // Rol permitido o no se requiere control de rol
            } else {
                next({ path: '/acceso-denegado' }); // Rol no permitido
            }
        } catch (error) {
            console.error("Error al decodificar el token:", error);
            next({ path: '/error' }); // Error en el token o en la decodificación
        }
    }
});








export default router;
  


