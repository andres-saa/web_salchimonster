<script setup>
import { computed, watch, ref } from 'vue';
import AppTopbar from './AppTopbar.vue';
// import AppFooter from './AppFooter.vue';
import AppSidebar from './AppSidebar.vue';
import AppConfig from './AppConfig.vue';
import { useLayout } from '@/layout/composables/layout';
import Loading from '../components/Loading.vue';

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
</script>

<template>
    <div class="layout-wrapper col-12 " :class="containerClass">
        <div class="col-12"
            style=" height: 150vh;top: -1rem; position: fixed; background-color: red; z-index:9999; left: 100%;box-shadow: 0 0 30px rgba(0, 0, 0, 0.585);">
        </div>

        <div class="col-12"
            style=" height: 150vh;top: -1rem; position: fixed; background-color: red; z-index:9999; right: 100%;box-shadow: 0 0 30px  rgba(0, 0, 0, 0.585)">

        </div>

        <app-topbar></app-topbar>
        <loading style="top: 0px;"></loading>
        <div class="layout-sidebar">
            <app-sidebar></app-sidebar>
        </div>
        <div class="layout-main-container  pr-0 pl-0 pt-7 " style="contain:paint ;">

            <div class="layout-main  ">
               

                <transition name="fade">
                    <router-view class="p-0"></router-view>
                </transition>
            </div>
            <!-- <app-footer></app-footer> -->
        </div>
        <div class="layout-mask"></div>
    </div>
</template>

<style lang="scss" scoped>

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.1s ease, transform 0.1s ease;
}

.fade-leave-to {
  opacity: 0;
}

.fade-enter-from {
  opacity: 0;

}

.fade-enter-to {
  opacity: 1;

}
</style>
