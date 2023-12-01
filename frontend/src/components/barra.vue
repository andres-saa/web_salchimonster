<template >

            

    <div class=" p-0 m-0 " style="position: sticky;top: 5rem; background-color: rgb(255, 255, 255); display: flex;box-shadow: 0 0 10px rgba(0, 0, 0, 0.169);justify-content: center;">

        <div class=" p-2" style="display: flex; align-items: center; justify-content: center;gap: 1rem; width: 100%;background-color: rgb(251, 171, 171) ; overflow-x: auto">

            <div style="background-color: ;" v-for="i in menuOptions[0].menus"><button style="background-color: transparent; border: none;">{{ i.category.name }}</button> </div>
        
        </div>

       

</div>



</template>

<script setup>  import { menuOptions } from '@/service/menuOptions';
</script>

<style scoped></style>