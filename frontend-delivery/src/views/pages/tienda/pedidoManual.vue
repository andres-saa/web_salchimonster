<template>
    <iframe 
        width="100%" 
        style="height: 99vh;" 
        :src="iframeSrc" 
        frameborder="0">
    </iframe>
</template>

<script>
export default {
    data() {
        return {
            iframeSrc: ''
        }
    },
    mounted() {
        this.iframeSrc = `https://salchimonster.com/?nocache=${new Date().getTime()}`;
    }
}
</script>