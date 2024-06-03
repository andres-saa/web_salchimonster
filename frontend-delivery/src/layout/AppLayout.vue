<script setup>
import { computed, watch, ref } from 'vue';
import AppTopbar from './AppTopbar.vue';
// import AppFooter from './AppFooter.vue';
import AppSidebar from './AppSidebar.vue';
import AppConfig from './AppConfig.vue';
import { useLayout } from '@/layout/composables/layout';
import Loading from '../components/Loading.vue';
import { useRoute } from 'vue-router';

const route = useRoute()


const { layoutConfig, layoutState, isSidebarActive } = useLayout();

const outsideClickListener = ref(null);

watch(isSidebarActive, (newVal) => {
    if (newVal) {
        bindOutsideClickListener();
    } else {
        unbindOutsideClickListener();
    }
});

const containerClass = computed(() => {
    return {
        'layout-theme-light': layoutConfig.darkTheme.value === 'light',
        'layout-theme-dark': layoutConfig.darkTheme.value === 'dark',
        'layout-overlay': layoutConfig.menuMode.value === 'overlay',
        'layout-static': layoutConfig.menuMode.value === 'static',
        'layout-static-inactive': layoutState.staticMenuDesktopInactive.value && layoutConfig.menuMode.value === 'static',
        'layout-overlay-active': layoutState.overlayMenuActive.value,
        'layout-mobile-active': layoutState.staticMenuMobileActive.value,
        'p-input-filled': layoutConfig.inputStyle.value === 'filled',
        'p-ripple-disabled': !layoutConfig.ripple.value
    };
});
const bindOutsideClickListener = () => {
    if (!outsideClickListener.value) {
        outsideClickListener.value = (event) => {
            if (isOutsideClicked(event)) {
                layoutState.overlayMenuActive.value = false;
                layoutState.staticMenuMobileActive.value = false;
                layoutState.menuHoverActive.value = false;
            }
        };
        document.addEventListener('click', outsideClickListener.value);
    }
};
const unbindOutsideClickListener = () => {
    if (outsideClickListener.value) {
        document.removeEventListener('click', outsideClickListener);
        outsideClickListener.value = null;
    }
};
const isOutsideClicked = (event) => {
    const sidebarEl = document.querySelector('.layout-sidebar');
    const topbarEl = document.querySelector('.layout-menu-button');

    return !(sidebarEl.isSameNode(event.target) || sidebarEl.contains(event.target) || topbarEl.isSameNode(event.target) || topbarEl.contains(event.target));
};


const { onMenuToggle } = useLayout();

</script>

<template>
    <div class="layout-wrapper col-12 " :class="containerClass">

        
        <div class="col-12"
            style=" height: 150vh;top: -1rem; position: fixed; background-color: red; z-index:9999; left: 100%;box-shadow: 0 0 30px rgba(0, 0, 0, 0.585);">

        </div>

        <!-- {{ onMenuToggle }} -->
        <div class="col-12"
            style=" height: 150vh;top: -1rem; position: fixed; background-color: red; z-index:9999; right: 100%;box-shadow: 0 0 30px  rgba(0, 0, 0, 0.585)">

        </div>

        <app-topbar v-if="route.path != '/pedido-manual'"></app-topbar>

        <router-link to="/">
            <Button v-if="route.path == '/pedido-manual'"  :icon="'pi pi-angle-double-left text-4xl'"  rounded=""  style="border: none;color: white;width: 3rem;height: 3rem; border-radius: 50%; position: absolute;background-color: rgb(255, 106, 0); left:1rem; top: 0.5rem;z-index: 9" class="p-2 shadow-5 boton"
           >
            </Button>
        </router-link>
      

        <div class="layout-sidebar" style="">
            
            <app-sidebar></app-sidebar>

           

            
        </div>

        <div class="layout-main-container  pr-0 pl-0  " :class="route.path != '/pedido-manual'?'pt-7':'pt-0 pb-0'" style="contain:paint ;">

            <div class="layout-main  ">
               

       
                    <router-view class="p-0"></router-view>
               
            </div>
            <!-- <app-footer></app-footer> -->
        </div>
        <div class="layout-mask"></div>
    </div>
</template>

<style lang="scss" scoped>

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

/* Estado Final de Salida: desvanecido y desplazado hacia la derecha */
.fade-leave-to {
  opacity: 0;
  transform: translateX(20rem);
}

/* Estado Inicial de Entrada: ligeramente desplazado hacia arriba y desenfocado */
.fade-enter-from {
  opacity: 0;
  transform: translateY(-10vh);
  filter: blur(10px);
}

/* Estado Final de Entrada: totalmente opaco, sin desplazamiento y enfocado */
.fade-enter-to {
  opacity: 1;
  transform: translateY(0);
  filter: blur(0);
}

.boton {
    animation: latido linear 1s infinite;
}
@keyframes latido {
        0% {  }
        100% { background-color:#5100ff;}
        
    }


</style>
