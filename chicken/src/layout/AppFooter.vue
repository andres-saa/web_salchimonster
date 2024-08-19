<script setup>
import { useLayout } from '@/layout/composables/layout';
import { computed } from 'vue';

const { layoutConfig } = useLayout();

const logoUrl = computed(() => {
    return `layout/images/${layoutConfig.darkTheme.value ? 'logo-white' : 'logo-dark'}.svg`;
});
</script>

<template>
    <div class="layout-footer">
        <div style="height: 20rem;top: 100%; width: 100%; background-color: var(--primary-color);">

        </div>
    </div>
</template>
<style lang="scss" scoped></style>
