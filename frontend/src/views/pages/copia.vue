<template>
     <div class="nombre-produc   col-12 p-1 " style="border-radius: 0 .0rem .5rem 0.5rem; background-color: #ffede1
;height:100% ;display: flex; flex-direction:column ;justify-content: space-between;overflow:  ">


<img class="     " style="background-color: #ffede1; object-fit: contain;height: 7rem;width: 7rem; border-radius:50% ;" :src="`${URI}/read_product_image/600/${product.product.id}`" alt="">


<div cla>
    <div class="col-12 mr-8"
                            style="background-color: ;text-transform: uppercase;  font-weight:bold ; width: 100%;height:1rem; display: flex;  justify-content: space-between;padding: 1rem; ">
                            <p class="xl:text-l md:text-l text-l" style="height: min-content;">{{ product.quantity }} {{
                                product.product.name }}</p>
                            <p class="xl:text-l md:text-xl" style="height: min-content;"> {{
                                formatoPesosColombianos(calcularPrecioTotal(product.product) * product.quantity) }}</p>


                        </div>

                        <div class="col-12"
                            style="text-transform: lowercase;text-align: ;  gap:2rem ;height: 4rem;overflow:hidden ; width: auto; display: flex; padding-right: 10rem ; justify-content: space-between; ; ">
                            <p v-if="!isSmallScreen" class="" style="height: auto;">{{ product.product.description }} </p>


                            <div class="contador ">

                                <button style="  
                            display: flex; 
                            align-items: center;
                            justify-content: center;  
                            border: none; 
                            /* font-size: 3vh;  */
                            background-color: transparent;
                            " @click="remove(product.product)"> <i :class="PrimeIcons.MINUS"> </i>

                                </button>

                                <input class="cantidad"
                                    style="font-size: 1.5rem; text-align: center; width: 30px; border: 1px none;  " readonly
                                    type="text" :value="product.quantity">

                                <button
                                    style="  display: flex; align-items: center;justify-content: center; border: none;font-weight: bold; font-size: 3vh;background-color: transparent;"
                                    @click="add(product.product)"> <i :class="PrimeIcons.PLUS"> </i> </button>


                            </div>

                        </div>
</div>

                       



                        <!-- <div class="triangulo"></div> -->
                    </div>
</template>