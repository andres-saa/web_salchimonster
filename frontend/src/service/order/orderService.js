import { usecartStore } from "../../store/shoping_cart";
import { useSitesStore } from "../../store/site";
import { useUserStore } from '../../store/user';
import axios from "axios";
import { URI } from "../conection";
import { useReportesStore } from "../../store/ventas";
import { useRoute } from "vue-router";
import pixel from "../../router/pixel";
import router from '../../router/index'

import { Value } from "sass";
const report = useReportesStore()
const cart = usecartStore();
const site = useSitesStore();
const user = useUserStore();

const preparar_orden = () => {
  user.user.was_reserva = false
  cart.sending_order = true
  const order_products = cart.cart.products.map(p => {

    const generalPrice = p.product.productogeneral_precio;
                const presentationPrice = p.product.lista_presentacion?.[0]?.producto_precio;
    return { 


      pedido_productoid: p.product.producto_id, 
      pedido_cantidad: p.quantity,
      pedido_precio:generalPrice !== undefined ? generalPrice : presentationPrice || 0,
      pedido_escombo:p.product.productogeneral_escombo,
      pedido_nombre_producto:p.product.productogeneral_descripcion,
      lista_productocombo: p.product.lista_productobase?.map(p => 
          {
            return {
              "pedido_productoid":parseInt(p.producto_id)  ,
              "pedido_cantidad": parseInt(p.productocombo_cantidad),
              "pedido_precio": parseInt(p.productocombo_precio),
              "pedido_nombre":p.producto_descripcion
            }
           
          }
        
      ),
      modificadorseleccionList:cart.cart.additions.filter( add => add.parent_id == p.product.producto_id)?.map( ad => {
        return {
          "modificadorseleccion_cantidad": ad.quantity,
          "pedido_precio": ad.price,
          "modificador_id": ad.group_id,
          "modificadorseleccion_id": ad.id,
          "modificador_nombre":ad.name,
          "pedido_productoid":ad.parent_id
      }
      })  
    }
  });


  console.log(order_products)

  const order_aditionals = cart.cart.additions.map(a => {
    return {
      "aditional_item_instance_id": a.id,
      "quantity": a.quantity
    }
  })

  const site_id = site.location.site.site_id;
  const pe_site_id = site.location.site.pe_site_id;
  const payment_method_id = user.user.payment_method_option?.id;
  const delivery_price = payment_method_id === 7 ? 0 : site.location.neigborhood.delivery_price;

  const order_notes = cart.cart.order_notes;
  const user_data = {
    "user_name": user.user.name,
    "user_phone": user.user.phone_number?.split(' ').join(''),
    "user_address": ` ${user.user.address} ${site.location?.neigborhood?.name}` || ''
  };

  const order = {
    "order_products": [],
    "site_id": site_id,
    // "site_id": 12,
    // "pe_site_id":12,
    "pe_site_id":pe_site_id,
    "delivery_person_id": 4,
    "payment_method_id": payment_method_id,
    "delivery_price": delivery_price,
    "order_notes": order_notes || 'SIN NOTAS',
    "user_data": user_data,
    "order_aditionals":order_aditionals,
    "pe_json": order_products,
    "total":cart.cart.total_cost
  };

  return order
}


const preparar_orden_reserva = () => {

  user.user.was_reserva = true
  cart.sending_order = true
  const order_products = cart.cart.products.map(p => {
    return { product_instance_id: p.product.id, quantity: p.quantity };
  });



  const order_aditionals = []

  const site_id = site.location.siteReservas.site_id;
  const payment_method_id = user.user.payment_method_option?.id;
  const delivery_price = 0

  const order_notes = cart.cart.order_notes;
  const user_data = {
    "user_name": user.user.name,
    "user_phone": user.user.phone_number?.split(' ').join(''),
    "user_address": `Debe ir a la sede` || ''
  };

  const order = {
    "order_products": order_products,
    "site_id": site_id,
    // "site_id": 12,
    "delivery_person_id": 4,
    "payment_method_id": payment_method_id,
    "delivery_price": 0,
    "order_notes": order_notes || 'SIN NOTAS',
    "user_data": user_data,
    "order_aditionals":[]
  };

  return order
}



export const orderService = {

  async sendOrder() {

    const order = preparar_orden()
    const cart = usecartStore()



    if (!validateOrder(order)) {
      cart.sending_order = false
      return null;
      
    }

    try {
      report.setLoading(true,`enviando tu pedido ${user.user.name}`)
      const response = await axios.post(`${URI}/order`, order);
      if (response.status === 200) {
        cart.sending_order = false
        cart.last_order = response.data
        report.setLoading(false,"enviando tu pedido")



        pixel.sendTrackingEvent('Purchase', {
          total: cart.cart.total_cost, // Este es el total en COP o convertido a otra moneda
          currency: 'COP', // O la moneda a la que hayas convertido
          items: cart.cart.products.map(p => {
            return { 
              id: p.product.id,
              name: p.product.product_name,
              quantity: p.quantity,
              price: p.product.price
            };
          }),
          value:cart.cart.total_cost
        });

      
        

        // if (order.payment_method_id !== 6) {
        //   report.visible.show_validate = true
        // }else{
          router.push('/gracias')
        // }

    



      } else {
        console.error('An error occurred while sending the order:', response.status);
        alert('An error occurred while sending the order. Please try again.');
        report.setLoading(false,"enviando tu pedido" )
        cart.sending_order = false

    
        return null;
        
      }
    } catch (error) {
      console.error('An error occurred while sending the order:', error);
      report.setLoading(false,"enviando tu pedido")
      cart.sending_order = false

      alert('An error occurred while sending the order. Please check your internet connection and try again.');
      cart.sending_order = false
      return null;

    }
  },


  preparar_orden(){
    preparar_orden()
  },


  async sendOrderReserva() {

    const order = preparar_orden_reserva()
    const cart = usecartStore()

    user.user.was_reserva = true


    if (!validateOrder(order)) {
      cart.sending_order = false
      return null;
      
    }

    try {
      report.setLoading(true,`enviando tu pedido ${user.user.name}`)
      const response = await axios.post(`${URI}/order`, order);
      if (response.status === 200) {
        cart.sending_order = false
        cart.last_order = response.data
        report.setLoading(false,"enviando tu pedido")



        pixel.sendTrackingEvent('Purchase', {
          total: cart.cart.total_cost, // Este es el total en COP o convertido a otra moneda
          currency: 'COP', // O la moneda a la que hayas convertido
          items: cart.cart.products.map(p => {
            return { 
              id: p.product.id,
              name: p.product.product_name,
              quantity: p.quantity,
              price: p.product.price
            };
          }),
          value:cart.cart.total_cost
        });

      
        

        // if (order.payment_method_id !== 6) {
        //   report.visible.show_validate = true
        // }else{
          router.push('/gracias')
        // }

    



      } else {
        console.error('An error occurred while sending the order:', response.status);
        alert('An error occurred while sending the order. Please try again.');
        report.setLoading(false,"enviando tu pedido" )
        cart.sending_order = false

    
        return null;
        
      }
    } catch (error) {
      console.error('An error occurred while sending the order:', error);
      report.setLoading(false,"enviando tu pedido")
      cart.sending_order = false

      alert('An error occurred while sending the order. Please check your internet connection and try again.');
      cart.sending_order = false
      return null;

    }
  },



  
};


function validateOrder(order) {
  // const cart = usecartStore()
  // if (!order.order_products.every(p => p.product_instance_id && p.quantity)) {
  //   alert('Some products in your cart are missing details.');
  //   cart.sending_order = false

  //   return false;
  // }

  if (!order.user_data.user_name || order.user_data.user_name.trim() == '' ||
    !order.user_data.user_phone || order.user_data.user_phone.trim() == '' ||
    !order.user_data.user_address || order.user_data.user_address.trim() == ''
  ) {
    alert('Sus datos estan incompletos por favor reviselos');
    cart.sending_order = false

    return false;
  }

  if (!order.site_id || order.delivery_price == null) {
    alert('Site information is missing. Please select a valid site.');
    cart.sending_order = false

    return false;
  }

  return true;
}



