<template>
    <div class="p-1 my-5 md:my-0 col-12">
        <div style="position: sticky; top: 5rem;border-radius: 0.5rem; z-index: 1000;" class="col-12 p-3 p-shadow m-0  ">

            <h5> <b>Resumen</b> </h5>

            <h5> <b>productos</b> </h5>

            <div class="grid mb-0 pb-0" v-for="product in store.cart.products">

                <div class="col-6  py-2 mb-0 m-0">
                    <h6 class="m-0">
                        <span style="min-width: 3rem;width:100%1"><b>{{ product.quantity }} </b> </span>
                        {{ product.product.productogeneral_descripcion }}
                    </h6>



                
                   

                    <h6 class="m-0 ml-3 " style="width:340px;" v-for="i in product.product.lista_productobase">
                      -- <b>{{ parseInt( i.productocombo_cantidad * product.quantity) }}</b> <span style="font-weight: 400;">{{ i.producto_descripcion }}</span> 
                        
                        
                    </h6>
                </div>
                <div class="col-6 my-0  text-right py-2">
                    <h6>
                        {{ formatoPesosColombianos(product.total_cost) }}
                    </h6>
                </div>

            </div>

            <!-- <h5> <b>ADICIONALES</b> </h5> -->


            <div class="col-12 p-0 mt-1">
                    <div class="p-0 mb-2 " v-for="(items, grupo) in agrupados" :key="grupo" style="position: relative;border-radius: 0.3rem;">
                        
                       
                        <div class="mb-0">
                            <span class="mb-1 text-center">
                                <b>{{ grupo }}</b>

                            </span>
                            
                           
                                <div v-for="item in items" :key="item.aditional_item_instance_id"
                                    style="display: flex; gap: 1rem; align-items: center;">

                                    <div style="display: flex; width: 100%; gap: 1rem; justify-content: space-between;">

                                       
                                        <span class="text adicion" style="text-transform: ;"><span> <b> {{ item.quantity }}</b> </span>  {{ item.name
                                        }}</span>


                                        
                                            <span v-if="item.price > 0" class="pl-2  text-sm">
                                                <b>{{ formatoPesosColombianos(item.price * item.quantity) }}</b>
                                            </span>

                                            

                                
                                

                                    </div>

                                </div>

                               

                         
                        </div>
                        
                    </div>
                    

                </div>








            <hr class="p-0 mt-2">
            <div class="grid">

                <div class="col-6 my-0 py-0">
                    <span><b>Subtotal</b></span>
                </div>
                <div class="col-6 my-0  text-right py-0">
                    <span><b>{{ formatoPesosColombianos(store.cart.total_cost) }}</b></span>
                </div>

                <div class="col-6 my-0 py-0">
                    <span :style="siteStore.location.neigborhood.delivery_price == 0? 'text-decoration: line-through;':''"><b>Domicilio</b></span>
                </div>
                <div class="col-6 my-0  text-right py-0">
                    <!-- {{ siteStore.location }} -->
                    <span style="color: var(--primary-color);" v-if="siteStore.location.neigborhood.delivery_price == 0"> <b>{{route.path.includes('reservas')? 'Ir a la sede' : `Recoger en local`}}</b> </span>
                    <span v-else> <b>{{ formatoPesosColombianos(siteStore.location.neigborhood.delivery_price) }}</b></span>
                </div>
                <div class="col-6 my-0 py-0">
                    <span><b>Total</b></span>
                </div>
                <div class="col-6 my-0  text-right py-0">
                    <!-- {{ siteStore.location }} -->
                    <span><b>{{ formatoPesosColombianos(store.cart.total_cost +
                        siteStore.location.neigborhood.delivery_price) }}</b></span>
                </div>



            </div>



            <router-link to="/" v-if="route.path.includes('cart')">
                <Button outlined icon="pi pi-shopping-cart" label="Seguir comprando" class="mt-4" severity="danger"
                    style="outline: none;width: 100%;font-weight: bold; background-color: rgba(0, 0, 0, 0);"></Button>

            </router-link>

            <router-link to="/cart" v-else-if="route.path != '/reservas'">
                <Button outlined icon="pi pi-arrow-left" label="Volver al carrito" class="mt-4" severity="danger"
                    style="outline: none;width: 100%;font-weight: bold; background-color: rgba(0, 0, 0, 0);"></Button>

            </router-link>



            <Tag  v-if="siteStore.status == 'cerrado' && route.path != '/reservas'" style="width: 100%;height: 2.5rem;" class="mt-2" severity="danger"> Este Restaurante esta cerrado</Tag>
            <router-link to="/pay" v-if="route.path.includes('cart') && siteStore.status != 'cerrado' ">
                <Button iconPos="right" icon="pi pi-arrow-right" label="Pedir" class="mt-2" severity="help"
                    style="outline: none;width: 100%; border: none;font-weight: bold; background-color: black;"></Button>
            </router-link>

            <router-link to="/pay" v-else-if="route.path.includes('reservas')" >
                <Button  @click=" ()  => {
                    orderService.sendOrderReserva()
                    sending = true
                }" iconPos="right" icon="pi pi-arrow-right" label="Finalizar pedido"
                    class="mt-2" severity="help"
                    style="outline: none;width: 100%; border: none;font-weight: bold; background-color: black;"></Button>
            </router-link>

            <router-link to="/pay" v-else-if="siteStore.status != 'cerrado' " >
                <Button  @click=" ()  => {
                    orderService.sendOrder()
                    sending = true
                }" iconPos="right" icon="pi pi-arrow-right" label="Finalizar pedido"
                    class="mt-2" severity="help"
                    style="outline: none;width: 100%; border: none;font-weight: bold; background-color: black;"></Button>
            </router-link>


            

        </div>









    </div>
</template>

<script setup>
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { usecartStore } from '../../store/shoping_cart';
import { useSitesStore } from '../../store/site';
import { useRoute } from 'vue-router';
import { orderService } from '../../service/order/orderService';
import {onMounted, ref, watch} from 'vue'
import { useUserStore } from '../../store/user';


const sending = ref(false)
const route = useRoute()
const store = usecartStore()
const siteStore = useSitesStore()
const user = useUserStore()



const agrupados = ref({})



const update = () => {
    agrupados.value = store.cart.additions.reduce((acumulador, elemento) => {
        let grupo = elemento.group;

        if (!acumulador[grupo]) {
            acumulador[grupo] = [];
        }
        acumulador[grupo].push(elemento);

        return acumulador;
    }, {})
}




onMounted(() => {
    update()

    if (user.user.payment_method_option?.id != 7 && !route.path.includes('reservas'))
        siteStore.setNeighborhoodPrice()
    else {
        siteStore.setNeighborhoodPriceCero()

    }


})


watch(() => store.cart.additions, () => {
    update()
},{deep:true})



</script>
<style scoped>
.p-shadow {
    box-shadow: 0 .3rem 5px rgba(0, 0, 0, 0.15);
}

button {
    text-transform: uppercase;
}

* {
    text-transform: uppercase;
    font-size: 0.9rem;
}

*::first-letter {
    text-transform: uppercase;
}
</style>