import { usecartStore } from "../../store/shoping_cart";
import { useSitesStore } from "../../store/site";
import { useUserStore } from '../../store/user';
import axios from "axios";
import { URI } from "../conection";
import { useReportesStore } from "../../store/ventas";
import { useRoute } from "vue-router";
import pixel from "../../router/pixel";
import router from '../../router/index'





export const validationService = {

    
  async validateOrder(data) {

    const report = useReportesStore()

    try {
      report.setLoading(true, 'cargando')
      const response = await axios.post(`${URI}/validate-order-code`, data);
      if (response.status === 200) {


        if(response.data.valid){
            
            router.push('/gracias')
            report.visible.show_validate = false
        } else {
            alert('codigo incorrecto')
            
        }
  

        report.setLoading(false,`validando tu orden`)


      } else {
        report.setLoading(false,`validando tu orden`)
        alert('error, intentalo de nuevo')
        return null;
        
      }
    } catch (error) {
        report.setLoading(false,`validando tu orden`)
      console.error('An error occurred while sending the order:', error);
      alert('error, intentalo de nuevo')


    //   alert('An error occurred while sending the order. Please check your internet connection and try again.');
      return null;

    }
  },
};


