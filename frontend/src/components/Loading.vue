<template>

<Transition name="loading">
    <div v-if="store.loading.visible" class="col-12" v style="display: flex;flex-direction: column; pointer-events: none; align-items: center; justify-content: center; position: fixed;z-index: 100;left: 0;top: 0;backdrop-filter:blur(5px); height: 100vh;background-color: rgba(255, 255, 255, 0.537);">

<div class="p-5" style="background-color: ;height: min-content;display: flex;flex-direction: column;align-items: center;justify-content: center;


border-radius: 1rem;;">

<img  src="/images/logo.png" style="width: 5rem;"><img>


    <p class="text-3xl p-3 col-12 text-center" style="font-weight: bold;text-transform: uppercase; color: var(--orange-500);border-radius: 10rem;width: min-content ;background-color: rgba(255, 255, 255, 0);">{{store.loading.tittle      }}</p>
<div style="display: flex;">

    
        <ProgressSpinner   style="width: 100px; height: 100px" strokeWidth="4" fill="white"
        animationDuration=".5s" aria-label="Custom ProgressSpinner" />

    </div>
</div>
</div>
</Transition>


</template>


<script setup>
import {useReportesStore} from '@/store/ventas.js'
import {onUnmounted} from 'vue'
const store = useReportesStore()

const props = defineProps({
    tittle: {
        type: String,
        default: 'CARGANDO'
    },


});




onUnmounted(() => {
    store.setLoading(false);
});

</script>

<style scoped>

.loading-enter-active,.loading-leave-active {
  transition: all ease  .3s;
  
}


.noti-enter-active,.noti-leave-active {
  transition: all ease  1s;
  
}

 .loading-leave-to{
  opacity: 0;
  /* transform: translateY(0); */

}

/* .loading-enter-to  {
  opacity: 0;
  transform: translateX(20rem);
 
} */


.loading-leave-from  {
  opacity: 1;
  /* transform: translateY(20rem); */

}
 /*
*/

 .loading-enter-from {
  opacity: 0;
  transform: translateY(20rem);
  filter: blur(10px);
  /* filter: blur(0); */
  
}


.noti-enter-from {
  opacity: 0;
  transform: translateY(20rem);
  filter: blur(10px);
  /* filter: blur(0); */
  
}

.noti-enter-to {
    opacity: 1;
  filter: blur(0);
  
}



.loading-enter-to {
  opacity: 1;
  filter: blur(0);

  
} 

@keyframes saltitos {
    0%   { transform: scale(1,1)    translateY(0); }
        10%  { transform: scale(1.1,.9) translateY(0);  }
        30%  { transform: scale(.9,1.1) translateY(-100px); }
        50%  { transform: scale(1,1)    translateY(0); ; }
        57%  { transform: scale(1,1)    translateY(-7px); }
        64%  { transform: scale(1,1)    translateY(0) ; }
        100% { transform: scale(1,1)    translateY(0) ;; }
    }
    


img{
    animation: saltitos 2s ease-in-out infinite;
}

</style>