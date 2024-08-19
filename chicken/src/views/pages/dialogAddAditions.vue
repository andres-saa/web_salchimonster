
<template>
    <Dialog class="mx-3" :closable="true" style="background-color: white;"
        v-model:visible="store.visibles.addAdditionToCart" modal header="Header"
        :style="{ width: '30rem', 'border-radius': '0.5rem' }">


        <div style="color: black;" class="grid">


            <div class="col-12" style="" v-for="grupo in adicionales" :key="grupo.category">
                <div class="mb-2">
                    <span class="mb-2 text-center">
                        <b>{{ grupo.category }}</b>
                    </span>
                    <div class="mt-2">
                        <div v-for="item in grupo.items" :key="item.aditional_item_instance_id"
                            style="display: flex; gap: 1rem;">
                            <div v-if="store.cart.products.some(product => product.product.category_name == item.product_category_name)"
                                class="p-0" style="display: flex; width: 100%; gap: 1rem;">
                                <Checkbox class="my-1" :binary="true" v-model="item.checked"
                                    @change="() => handleAdditionChange(item, grupo.category)" />
                                <!-- {{ item.aditional_item_type_nameS }}
                    {{ store.cart.products }} -->
                                <div style="display: flex; width: 100%; gap: 1rem; justify-content: space-between;">
                                    <span class="text-sm adicion" style="text-transform: capitalize;">{{
                                        item.aditional_item_name }}</span>
                                    <span v-if="item.checked && grupo.category != 'SALSAS'" style="display: flex; align-items: center;">
                                        <span v-if="item.aditional_item_price > 0" class="pl-2 py-1 text-sm">
                                            <b>{{ formatoPesosColombianos(item.aditional_item_price *
                                                selectedAdditions[item.aditional_item_instance_id]?.quantity) }}</b>
                                        </span>

                                        <Button @click="decrement(item)" class="ml-2" severity="danger"
                                            style="width: 2rem; height: 1.5rem;border: none;" icon="pi pi-minus"></Button>
                                        <InputText
                                            :modelValue="selectedAdditions[item.aditional_item_instance_id]?.quantity"
                                            readonly style="width: 2rem;border: none; height: 1.5rem;"
                                            class="p-0 text-center" />
                                        <Button @click="increment(item)" severity="danger"
                                            style="width: 2rem;height: 1.5rem; border: none;" icon="pi pi-plus"></Button>
                                    </span>


                                    <span v-else-if="item.aditional_item_price > 0" class="pl-2 py-1 text-sm">
                                        <b>{{ formatoPesosColombianos(item.aditional_item_price) }}
                                        </b>
                                    </span>

                                </div>
                            </div>


                        </div>
                        <hr>
                    </div>
                </div>
            </div>
        </div>

        <template #footer>
            <div class=" col-12 p-0" style="display: flex; justify-content: center;font-weight: bold;">
                <Button @click="addToCart" style="width: auto;" severity="danger" label="Agregar al carrito">
                </Button>
            </div>

        </template>

        <Button @click="store.setVisible('addAdditionToCart', false)" icon="pi pi-times"
            style="position: absolute; right: -1rem; top: -1rem;" rounded severity="danger"> </Button>
    </Dialog>
</template>

<script setup>
import { storeToRefs } from "pinia";
import { ref, onMounted, watch } from "vue";
import { adicionalesService } from "../../service/restaurant/aditionalService";
const selectedAdditions = ref({});
import { usecartStore } from "../../store/shoping_cart";
import { formatoPesosColombianos } from "../../service/formatoPesos";
import { useSitesStore } from "../../store/site";
const sitestore = useSitesStore()
const store = usecartStore()
const handleAdditionChange = (item, group) => {
    if (item.checked) {

        const new_item = {
            id: item.aditional_item_instance_id,
            name: item.aditional_item_name,
            price: item.aditional_item_price,
            group: group
        }

        selectedAdditions.value[new_item.id] = {
            ...new_item,
            quantity: item.quantity || 1
        };
    } else {
        delete selectedAdditions.value[item.aditional_item_instance_id];
    }
};

const increment = (item) => {
    if (item.checked) {

        const new_item = {
            id: item.aditional_item_instance_id,
            name: item.aditional_item_name,
            price: item.aditional_item_price,
            // quantity:item.quantity
        }


        selectedAdditions.value[new_item.id].quantity++;
    }
};

const decrement = (item) => {

    if (selectedAdditions.value[item.aditional_item_instance_id].quantity > 1 && selectedAdditions.value[item.aditional_item_instance_id]) {
        selectedAdditions.value[item.aditional_item_instance_id].quantity--
    }

};

watch(() => store.visibles.addAdditionToCart, async (new_val) => {
    if (!new_val) {
        selectedAdditions.value = {}
        adicionales.value = []
        
    } else {
        const ids = store.cart.products.map(product => product.product.id)
        if (ids.length > 0) {
            adicionales.value = await adicionalesService.getAditionalGroup(ids,sitestore.location?.site?.site_id)
        }
    }
}, { deep: true })


const addToCart = () => {

    const additionsArray = Object.values(selectedAdditions.value)

    additionsArray.forEach(adition => {
        store.addAdditionToCart(adition)
        console.log(adition)
    })

    selectedAdditions.value = {}; // Resetear las adiciones seleccionadas


    store.setVisible('addAdditionToCart', false)

};

const adicionales = ref([])


const visible = ref(true);


onMounted(async () => {

    const ids = store.cart.products.map(product => product.product.id)
    if (ids.length > 0) {
        adicionales.value = await adicionalesService.getAditionalGroup(ids,sitestore.location?.site?.site_id)
    }
})

</script>
