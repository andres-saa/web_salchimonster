    import { defineStore } from "pinia";
    import { URI } from "../service/conection";


    export const usecartStore = defineStore('cart', {
        persist: {
            key: 'cart', 
            storage: localStorage,
            paths: ['cart','last_order']
        },
        state: () => ({
            currentProduct: {},
            visibles: {
                currentProduct: false,
                addAdditionToCart: false,
                last_order:''
            },
            cart: {
                products: [],
                total_cost: 0,
                additions: []  // Nueva propiedad para manejar las adiciones a nivel del carrito
            },
            last_order:'',
            sending_order:false
        }),
       
            getters: {
                totalItems: (state) => {
                    return state.cart.products.reduce((total, product) => total + product.quantity, 0);
                },
                totalAdditions: (state) => {
                    return state.cart.additions.reduce((total, addition) => total + (addition.price * addition.quantity), 0);
                },
                isProductInCart: (state) => (productId) => {
                    return state.cart.products.some(product => product.product.id === productId);
                }
            },
       
        actions: {

            incrementAdditionQuantity(additionId) {
                const addition = this.cart.additions.find(a => a.id === additionId);
                if (addition) {
                    addition.quantity += 1;
                    this.calculateCartTotal();
                }
            },
            removeAdditionCompletelyFromCart(additionId) {
                const additionIndex = this.cart.additions.findIndex(a => a.id === additionId);
                if (additionIndex > -1) {
                    this.cart.additions.splice(additionIndex, 1);
                    this.calculateCartTotal();
                }
            },
    
            decrementAdditionQuantity(additionId) {
                const addition = this.cart.additions.find(a => a.id === additionId);
                if (addition && addition.quantity > 1) {
                    addition.quantity -= 1;
                    this.calculateCartTotal();
                }
            },


            setCurrentProduct(product){
                this.currentProduct=product
            },

            setVisible(item,status){
                this.visibles[item]=status
            },

            addProductToCart(product, quantity = 1, additionalItems = []) {
                const cartProduct = this.cart.products.find(p => p.product.id === product.id);

                if (cartProduct) {
                    cartProduct.quantity += quantity;
                    cartProduct.total_cost += product.price * quantity
                } else {
                    this.cart.products.push({
                        product,
                        quantity,
                        additionalItems: this.groupAdditionalItems(additionalItems),
                        total_cost: this.calculateProductTotal(product, quantity, additionalItems)
                    });
                }
                this.calculateCartTotal();
            },

            removeProductFromCart(productId) {
                this.cart.products = this.cart.products.filter(product => product.product.id !== productId);
                this.calculateCartTotal();
            },

            addAdditionalItem(productId, additionalItem) {
                const product = this.cart.products.find(product => product.product.id === productId);
                if (product) {
                    product.additionalItems.push(additionalItem);
                    product.total_cost += additionalItem.price * additionalItem.quantity;
                    this.calculateCartTotal();
                }
            },
            removeAdditionalItem(productId, additionalItemId) {
                const product = this.cart.products.find(product => product.product.id === productId);
                if (product) {
                    const itemIndex = product.additionalItems.findIndex(item => item.id === additionalItemId);
                    if (itemIndex > -1) {
                        product.total_cost -= product.additionalItems[itemIndex].price * product.additionalItems[itemIndex].quantity;
                        product.additionalItems.splice(itemIndex, 1);
                        this.calculateCartTotal();
                    }
                }
            },
            groupAdditionalItems(additionalItems) {
                return additionalItems.reduce((acc, item) => {
                    (acc[item.type] = acc[item.type] || []).push(item);
                    return acc;
                }, {});
            },
            calculateProductTotal(product, quantity, additionalItems) {
                let total = product.price * quantity;
                additionalItems.forEach(item => {
                    total += item.price * item.quantity;
                });
                return total;
            },
            removeProductInstance(productId) {
                const cartProduct = this.cart.products.find(p => p.product.id === productId);
            
                if (cartProduct && cartProduct.quantity > 1) {
                    cartProduct.quantity -= 1;
                    cartProduct.total_cost -= cartProduct.product.price;
                    this.calculateCartTotal();
                } else if (cartProduct && cartProduct.quantity === 1) {
                    this.removeProductFromCart(productId);
                }
            },
            calculateCartTotal() {
                const productsTotal = this.cart.products.reduce((total, product) => total + product.total_cost, 0);
                const additionsTotal = this.totalAdditions;
                this.cart.total_cost = productsTotal + additionsTotal;
            },

            addAdditionToCart(addition) {
                const existingAddition = this.cart.additions.find(a => a.id === addition.id);
                if (existingAddition) {
                    existingAddition.quantity += addition.quantity;
                } else {
                    this.cart.additions.push({ ...addition});
                }
                this.calculateCartTotal();
            },
            removeAdditionFromCart(additionId) {
                const additionIndex = this.cart.additions.findIndex(a => a.id === additionId);
                if (additionIndex > -1) {
                    if (this.cart.additions[additionIndex].quantity > 1) {
                        this.cart.additions[additionIndex].quantity -= 1;
                    } else {
                        this.cart.additions.splice(additionIndex, 1);
                    }
                    this.calculateCartTotal();
                }
            },
        }
    });
