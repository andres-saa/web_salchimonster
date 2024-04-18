import { usecartStore } from "../../store/shoping_cart";
import { useSitesStore } from "../../store/site";
import { useUserStore } from '../../store/user';
import axios from "axios";
import { URI } from "../conection";

const cart = usecartStore();
const site = useSitesStore();
const user = useUserStore();

const preparar_orden = () => {
  const order_products = cart.cart.products.map(p => {
    return { product_instance_id: p.product.id, quantity: p.quantity };
  });



  const order_aditionals = cart.cart.additions.map(a => {
    return {
      "aditional_item_instance_id": a.id,
      "quantity": a.quantity
    }
  })

  const site_id = site.location.site.site_id;
  const delivery_price = site.location.neigborhood.delivery_price;
  const order_notes = cart.cart.order_notes;
  const user_data = {
    "user_name": user.user.name,
    "user_phone": user.user.phone_number?.split(' ').join(''),
    "user_address": ` ${user.user.address} ${site.location?.neigborhood?.name}` || ''
  };

  const order = {
    "order_products": order_products,
    "site_id": site_id,
    "delivery_person_id": 4,
    "payment_method_id": user.user.payment_method_option?.id,
    "delivery_price": delivery_price,
    "order_notes": order_notes || 'SIN NOTAS',
    "user_data": user_data,
    "order_aditionals":order_aditionals
  };

  return order
}




export const orderService = {

  async sendOrder() {

    const order = preparar_orden()

    if (!validateOrder(order)) {
      return null;
    }

    try {
      const response = await axios.post(`${URI}/order`, order);
      if (response.status === 200) {

      } else {
        console.error('An error occurred while sending the order:', response.status);
        alert('An error occurred while sending the order. Please try again.');
    
        return null;
        
      }
    } catch (error) {
      console.error('An error occurred while sending the order:', error);
      alert('An error occurred while sending the order. Please check your internet connection and try again.');
      return null;
    }
  },
};

function validateOrder(order) {
  if (!order.order_products.every(p => p.product_instance_id && p.quantity)) {
    alert('Some products in your cart are missing details.');
    return false;
  }

  if (!order.user_data.user_name || order.user_data.user_name.trim() == '' ||
    !order.user_data.user_phone || order.user_data.user_phone.trim() == '' ||
    !order.user_data.user_address || order.user_data.user_address.trim() == ''
  ) {
    alert('Sus datos estan incompletos por favor reviselos');
    return false;
  }

  if (!order.site_id || !order.delivery_price) {
    alert('Site information is missing. Please select a valid site.');
    return false;
  }

  return true;
}


