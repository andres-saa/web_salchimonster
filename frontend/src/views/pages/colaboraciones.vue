<template>
    <div class="col-12 mx-auto px-2 pb-4 my-0 container py-4" style=" max-width: 1024px;">

        <div style="display: flex;left: 100%;gap:4rem;  flex-direction: column; position:absolute;">

            <img style="width:15vw;" v-for="character in [1, 2, 3, 4, 5]" :src="`/images/characters/line/${character}.png`"
                alt="">

        </div>

        <div style="display: flex;right: 100%;gap:4rem; flex-direction: column;position: absolute">


            <img style="width:15vw;" v-for="character in [1, 2, 3, 4, 5].reverse()"
                :src="`/images/characters/line/${character}.png`" alt="">


        </div>
        <p class="text-2xl md:text-2xl lg:text-6xl my-4 text-center copy"
            style=" text-transform: uppercase; font-family: Titan One, sans-serif;font-weight: 400;font-style: normal;" > LA PRE-PAGO</p>
        <img src="/images/banners/banner-0.jpeg" class="shadow-6" alt="" style="width: 100%;border-radius: .5rem; max-width: 1024px;">

        <p class="text-2xl md:text-2xl lg:text-6xl my-4 text-center copy"
            style=" text-transform: uppercase; font-family: Titan One, sans-serif;font-weight: 400;font-style: normal;"> SALCHIMONSTER X PAPI KEICY</p>



        <iframe class="shadow-5" width="100%" height="100%" style="aspect-ratio: 16 / 9;width: 100%;border-radius: .5rem; max-width: 1024px;"
            src="https://www.youtube.com/embed/VR6N9AhyRVQ"
            title="Como hacer la salchipapa Pre-pago| Colaboración ​⁠​⁠@papi-keicy salchimonster la mejor de Colombia"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>

</template>

<script>
import { ref, onMounted } from 'vue';

export default {
    setup() {
        // Crear un ref reactivo para el ID del video
        const videoId = ref('ID_DEL_VIDEO_DE_YOUTUBE');
        // Crear un ref reactivo para la URL de inserción
        const embedUrl = ref('');

        // Lógica para construir la URL de inserción cuando el componente se monta
        onMounted(() => {
            embedUrl.value = `https://www.youtube.com/embed/${videoId.value}`;
        });

        // Exponer las variables al template
        return {
            embedUrl
        };
    }
};
</script>

<style scoped>


.copy{
    color: #fff;
}

@media (width < 768px) {
    .container{
        background-color: var(--primary-color);
    }

}

</style>