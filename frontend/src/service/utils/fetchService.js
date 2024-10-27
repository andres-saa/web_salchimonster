import axios from 'axios'
// import { useReportesStore } from '@/store/reportes';
import router from '@/router'

export const fetchService = {
  router: router,

  async get(url, loadingMessage, options = {}) {
    // const store = useReportesStore()
    try {
      if (loadingMessage) {
        // store.setLoading(true, loadingMessage)
      } else {
        // store.setLoading(true, 'cargando')
      }

      // Configura los headers si están presentes en las opciones
      const config = {
        headers: options.headers || {},
      }

      // Realizar la solicitud GET con los headers configurados
      const response = await axios.get(url, config)

      // Comprobar el estado de la respuesta
      if (response.status === 200) {
        // Desactivar el estado de carga
        // store.setLoading(false)
        return response.data
      } else {
        // Desactivar el estado de carga
        // store.setLoading(false)
        console.error('An error occurred while fetching data:', response.status)
        return null
      }
    } catch (error) {
      // Desactivar el estado de carga
      //   store.setLoading(false)
      console.error('An error occurred while fetching data:', error)
      return null
    }
  },

  async post(url, data, loadingMessage, redirectPath = null) {
    // const store = useReportesStore()
    try {
      // Establecer el mensaje de carga y activar el estado de carga
      //   store.setLoading(true, loadingMessage)

      // Realizar la solicitud POST
      const response = await axios.post(url, data)

      // Comprobar el estado de la respuesta
      if (response.status === 200 || response.status === 201) {
        // Desactivar el estado de carga
        // store.setLoading(false)

        // Redirigir si se ha proporcionado una ruta
        if (redirectPath) {
          this.router.push(redirectPath)
        }

        return response.data
      } else {
        // Desactivar el estado de carga
        // store.setLoading(false)
        console.error('An error occurred while posting data:', response.status)
        return null
      }
    } catch (error) {
      // Desactivar el estado de carga
      //   store.setLoading(false)
      console.error('An error occurred while posting data:', error)
      return null
    }
  },

  async put(url, data, loadingMessage, redirectPath = null) {
    // const store = useReportesStore()
    try {
      //   store.setLoading(true, loadingMessage)
      const response = await axios.put(url, data)
      if (response.status === 200 || response.status === 204) {
        // store.setLoading(false)
        if (redirectPath) {
          this.router.push(redirectPath)
        }
        return response.data
      } else {
        // store.setLoading(false)
        console.error('An error occurred while updating data:', response.status)
        return null
      }
    } catch (error) {
      //   store.setLoading(false)
      console.error('An error occurred while updating data:', error)
      return null
    }
  },

  async delete(url, loadingMessage, redirectPath = null) {
    // const store = useReportesStore()
    try {
      //   store.setLoading(true, loadingMessage)
      const response = await axios.delete(url)
      if (response.status === 200 || response.status === 204) {
        // store.setLoading(false)
        if (redirectPath) {
          this.router.push(redirectPath)
        }
        return response.data
      } else {
        // store.setLoading(false)
        console.error('An error occurred while deleting data:', response.status)
        return null
      }
    } catch (error) {
      //   store.setLoading(false)
      console.error('An error occurred while deleting data:', error)
      return null
    }
  },
}
