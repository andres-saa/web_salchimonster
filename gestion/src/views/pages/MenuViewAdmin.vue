<template>
    <div>
        <p style="text-align: center; width: 100%; font-size: 36px; font-weight: bold;">
            Monster <span style="color:var(--primary-color) ;">Menu  </span> <sup style="font-weight: bold; font-size: 20px;">Admin</sup>
        </p>
        <Toolbar>
            <template #center>
                <div v-for="section in menuOptions[0].menus">


                    <button class="menu-button"
                        @click="changesection({ category: section.category, products: section.products })"
                        :class="currentSection.category.name == section.category.name ? 'selected' : ''">
                        {{ section.category.name }}

                    </button>



                </div>
                <button class="menu-button-new" @click="showDialog">
                    <i :class="PrimeIcons.PLUS"></i> Registrar {{ currentSection.category.name }}
                </button>

            </template>
        </Toolbar>

        <div class="grid col-10 m-auto">

            <div class="grid col-12 m-auto">
                <div v-if="currentSection" v-for="product in currentSection.products" class="col-3">
                    <tarjetamenuAdmin :product="product" class="col-12 m-auto"></tarjetamenuAdmin>

                    <!-- <TarjetaMenu class=""></TarjetaMenu> -->

                </div>

            </div>

            <Dialog v-model:visible="productDialog" :style="{ width: '500px' }" header="Registrar un Usuario" :modal="true"
                class="p-fluid" style="background-color: white;">


                <div class="cont-dialog">


                    <div class="foto">
                        <img src="https://i.ebayimg.com/images/g/mGMAAOSwdUdjM4BG/s-l800.jpg" alt="">

                    </div>

                    <div class="dialog-container">


                        <div class="field">
                            <label for="name">Nombre </label>
                            <InputText id="name" v-model.trim="product.name" required="true" autofocus />
                        </div>

                        <div class="field">
                            <label for="name">categoria </label>
                            <InputText disabled id="name" v-model.trim="currentSection.category.name" required="true"
                                autofocus />
                        </div>

                        <div class="field">
                            <label for="name">precio </label>
                            <InputText id="name" v-model.trim="product.pecio" required="true" autofocus />
                        </div>
                        <div class="field">
                            <label for="name">precio </label>
                            <InputText id="name" v-model.trim="product.pecio" required="true" autofocus />
                        </div>
                        <div class="field">
                            <label for="name">precio </label>
                            <InputText id="name" v-model.trim="product.pecio" required="true" autofocus />
                        </div>
                        <div class="field">
                            <label for="name">precio </label>
                            <InputText id="name" v-model.trim="product.pecio" required="true" autofocus />
                        </div>

                        <div class="field">
                            <label for="name">precio </label>
                            <InputText id="name" v-model.trim="product.pecio" required="true" autofocus />
                        </div>



                        <p style="text-align: start; width: 100%; font-size: 24px;font-weight: bold; ">
                            <span style="color:var(--primary-color) ;">Salsas disponibles</span>
                        </p>


                        <div class="salsa" style="padding: 0 1rem;">
                            <p class="texto text-2xl m-0 " style="font-weight: bold;"> Todas
                            </p>
                            <Checkbox v-model="checked.papas" :binary="true" />
                        </div>
                        <div class=" col-12 salsas grid ">

                        
                            <div v-for="i in [1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]"
                                class="lg:col-12 md:col-6 sm:col-12 pb-0 pt-0  ">
                                <div class="salsa">
                                    <p class="texto text-xl m-1"> Costilla Ahumada en salsa bufalo
                                    </p>
                                    <p class="texto text-xl m-0 " style="font-weight: bold;"> $30.000
                                    </p>
                                    <Checkbox v-model="checked.papas" :binary="true" />
                                </div>
                            </div>
                        </div>


                        <p style="text-align: start; width: 100%; font-size: 24px;font-weight: bold; padding-top: 2rem; ">
                            <span style="color:var(--primary-color) ;">Adiciones disponibles</span>
                        </p>


                        <div class="salsa" style="padding: 0 1rem;">
                            <p class="texto text-2xl m-0 " style="font-weight: bold;"> Todas
                            </p>
                            <Checkbox v-model="checked.papas" :binary="true" />
                        </div>
                        <div class=" col-12 salsas grid ">

                        
                            <div v-for="i in [1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]"
                                class="lg:col-12 md:col-6 sm:col-12 pb-0 pt-0  ">
                                <div class="salsa">
                                    <p class="texto text-xl m-1"> Costilla Ahumada en salsa bufalo
                                    </p>
                                    <p class="texto text-xl m-0 " style="font-weight: bold;"> $30.000
                                    </p>
                                    <Checkbox v-model="checked.papas" :binary="true" />
                                </div>
                            </div>
                        </div>

                        <div class=""
                            style="display: flex; justify-content: space-between; width: 100%; padding:  1rem 0; padding-top: 2rem; margin: 0;">
                            <button style="width: max-content; padding: 10px 20px" class="menu-button-new"
                                @click="showDialog">
                                <i :class="PrimeIcons.PLUS"></i> Registrar
                            </button>
                            <button style="width: max-content; padding: 10px 20px" class="menu-button-new"
                                @click="showDialog">
                                <i :class="PrimeIcons.TIMES"></i> cancelar
                            </button>
                        </div>

                    </div>





                </div>





            </Dialog>


        </div>
    </div>
</template>

<script setup>
import TarjetaCombo from '../../components/TarjetaCombo.vue';
import TarjetaMenu from '../../components/TarjetaMenu.vue'
import tarjetamenuAdmin from '../../components/TarjetaMenuAdmin.vue'
import { menuOptions } from '../../service/menuOptions';
import { ref, onMounted, watch } from "vue"
import { PrimeIcons } from 'primevue/api';
import { curentProduct, changeProduct } from '../../service/productServices';
import { showSiteDialog } from '../../service/state';
const product = ref({})
const productDialog = ref(false)
const showDialog = () => {
    productDialog.value = !productDialog.value
}
const currentSection = ref(menuOptions.value[0].menus[0])
const currentMenu = ref({})
const changesection = (section) => {
    currentSection.value = section
    console.log(section)
}

const checked = ref({})
const setSection = () => {
    currentSection.value = { category: menuOptions.value[0].menus[1].category, products: menuOptions.value[0].menus[1].products }

    console.log('cambio')
}

watch(menuOptions, setSection);






onMounted(async () => {
    showDialog.value = false
    // changesection({category:localStorage.getItem('menu').category,products:localStorage.getItem('menu').products})
    // getMenu().then(products => currentSection.value = products[0])
});

</script>

<style scoped>
.boton-menu {
    margin: 0;
    border: none;
    background-color: transparent;
    font-size: 20px;
    padding: 0 20px;
}

.dialog-container {
    width: 100%;
    height: 100%;
    /* background-color: red; */
}

.salsa {
    display: flex;
    width: 100%;
    justify-content: space-between;
    align-items: start;
    padding: 0;
    margin: 0;
    color: black;


}

.salsas {
    display: flex;
    width: 100%;
    margin: 0;
    justify-content: space-around;
    color: black;
    padding: 0;

}

.texto {
    /* width: 40%; */
    /* min-width: 200px; */
    padding-right: 20px;
    /* min-width: 200px; */
    /* margin-right: 20px; */
}

.menu-button {
    background-color: transparent;
    padding: 1rem;
    margin: 0 1rem;
    border: none;
    font-size: 20px;
    /* transition: all  0.3s; */
    /* font-weight: bold; */
}

label {
    color: #000;
}

.menu-button-new {
    background-color: var(--primary-color);
    padding: 1rem;
    margin: 0 1rem;
    border: none;
    font-size: 20px;
    /* transition: all  0.3s; */
    /* font-weight: bold; */
    border-radius: 10px;
    color: #fff;
    width: 300px;
    transition: all 0.3s ease;
}

.menu-button-new:hover {
    /* filter: brightness(1.5);  
   */
    background-color: black;
    cursor: pointer;
}



.menu-button:hover {
    /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5); */
    /* transform: scale(1.1); */
    /* border-bottom:  2px red; */
    color: var(--primary-color);
    cursor: pointer;


}

.selected {
    box-shadow: 0px 5px 0px var(--primary-color);
    /* font-weight: bold; */

}

.cont-dialog {
    display: flex;
    width: 100%;
    flex-direction: column;
    gap: 40px;
    height: 100%;
    /* align-items: center; */
    justify-content: center;
    /* border: 1px solid red; */
}

.incluye {
    width: 100%;
    /* height: 400px; */
    /* height: 100%; */
    background-color: rgb(25, 0, 255);
}

.foto {
    width: 100%;
    height: 400px;
    /* height: 100%; */
    background-color: rgb(25, 0, 255);
}

.foto img {
    width: 100%;
    height: 100%;
    object-fit: cover;

    /* height: 100%; */
    /* background-color: rgb(25, 0, 255); */
}</style>