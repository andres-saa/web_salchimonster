<template>


    <div class="container col-12 px-2">
  


        <p class="my-6 text-2xl"><b> PQRS</b></p>
        <Accordion style="width: 100%;overflow: hidden; max-width: 800px;"  expandIcon="pi pi-plus" collapseIcon="pi pi-minus">
            <AccordionTab v-for="(pq, index) in pqrs" :key="pq.id">
                <template #header>
                    
                    <div>
                        
                    </div>
                        <p class="p-0 m-0 text-xl" style="width: 100%;">
                            {{ pq.question }}
                        </p>

                        
                
                </template>
                <p class="m-0">
                <p v-html="pq.answer"></p>
                </p>
            </AccordionTab>

        </Accordion>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { pqrsService } from '@/service/pqrs/pqrsService';

const pqrs = ref([]);


const update = async () => {
    pqrs.value = await pqrsService.getPqrsByPlaceId(1);
};


onMounted(async () => {
    update();
});




</script>

<style scoped>
.pqrs {
    list-style: none;
    margin: 0;
    padding: 0;
    width: 100%;
    max-width: 900px;
}

.pqrs-element {
    border-radius: .3rem;
}

.bar {
    max-width: 900px;
    display: flex;
    justify-content: end;
}

.container {
    padding: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    margin-top: 3rem;
}

@keyframes an_show_actions {
    0% {
        opacity: 0;
        transform: translateX(20px);
    }

    100% {
        opacity: 1;
    }
}

@keyframes an_show_actions_2 {
    100% {
        opacity: 0;
        transform: translateX(20px);
    }

    0% {
        opacity: 1;
    }
}

.button-visible {
    animation: an_show_actions .3s ease;
}

.button-hide {
    animation: an_show_actions_2 .3s ease;
}

/* Transición de fade */
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>
