import {URI} from '@/service/conection'
import { ref } from 'vue';

const getProductsByCategory = async (category) => {
  try {
    const response = await fetch(`${URI}/products/${category}`);

    if (!response.ok) {
      throw new Error('La solicitud no fue exitosa.');
    }

    const data = await response.json();
    // console.log('Respuesta del servidor:', data);
    return data // Puedes usar .json() si esperas una respuesta JSON
  
  } catch (error) {
    console.error('Error en la solicitud:', error);
  }
}

const getCategory = async () => {
  try {
    const response = await fetch(`${URI}/category`);

    if (!response.ok) {
      throw new Error('La solicitud no fue exitosa.');
    }

    const data = await response.json();
    // console.log('Respuesta del servidor:', data);
    return data // Puedes usar .json() si esperas una respuesta JSON
  
  } catch (error) {
    console.error('Error en la solicitud:', error);
  }
}

const getMenu = async () => {
  try {
    const response = await fetch(`${URI}/menu`);

    if (!response.ok) {
      throw new Error('La solicitud no fue exitosa.');
    }

    const data = await response.json();

  
    // console.log('Respuesta del servidor:', data);
    return data // Puedes usar .json() si esperas una respuesta JSON
  
  } catch (error) {
    console.error('Error en la solicitud:', error);
  }
}
// const products = ref([])

const curentProduct = ref({})

const changeProduct = (product) => {
  
  localStorage.setItem('product',JSON.stringify(product))
  curentProduct.value = JSON.parse(localStorage.getItem('product'))
  console.log(JSON.parse(localStorage.getItem('product')))
}

export{getProductsByCategory,getCategory,getMenu,curentProduct,changeProduct}
