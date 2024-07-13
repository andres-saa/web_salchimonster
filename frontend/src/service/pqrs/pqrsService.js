import axios from "axios";
import { useReportesStore } from "@/store/ventas";
import { URI } from "@/service/conection";


export const pqrsService = {
    store: useReportesStore(),

    resolve() {
        this.store.setLoading(false, '');
    },

    async getPqrsByPlaceId(placeId) {
        this.store.setLoading(true, 'Cargando PQRS');

        try {
            const response = await axios.get(`${URI}/get-pqrs-by-place-id/${placeId}`);

            if (response.status === 200) {
                this.resolve();
                return response.data;
            } else {
                console.error('No se ha podido cargar las PQRS');
                this.resolve();
                return null;
            }
        } catch (error) {
            console.error('Error al cargar las PQRS:', error);
            this.resolve();
            throw new Error('Error al cargar las PQRS');
        }
    },

    async createPqrs(pqrsData) {
        this.store.setLoading(true, 'Creando PQRS');

        try {
            const response = await axios.post(`${URI}/create_pqrs/`, pqrsData);

            if (response.status === 200) {
                this.resolve();
                return response.data;
            } else {
                console.error('No se ha podido crear la PQRS');
                this.resolve();
                return null;
            }
        } catch (error) {
            console.error('Error al crear la PQRS:', error);
            this.resolve();
            throw new Error('Error al crear la PQRS');
        }
    },
    
    async updatePqrs(pqrsData,id) {
        this.store.setLoading(true, 'Editando PQRS');

        try {
            const response = await axios.put(`${URI}/update_pqrs/${id}`, pqrsData);

            if (response.status === 200) {
                this.resolve();
                return response.data;
            } else {
                console.error('No se ha podido crear la PQRS');
                this.resolve();
                return null;
            }
        } catch (error) {
            console.error('Error al crear la PQRS:', error);
            this.resolve();
            throw new Error('Error al crear la PQRS');
        }
    },

    async deletePqrs(id) {
        this.store.setLoading(true, 'Eliminando PQRS');

        try {
            const response = await axios.delete(`${URI}/delete_pqrs/${id}`);

            if (response.status === 200) {
                this.resolve();
                return response.data;
            } else {
                console.error('No se ha podido crear la PQRS');
                this.resolve();
                return null;
            }
        } catch (error) {
            console.error('Error al crear la PQRS:', error);
            this.resolve();
            throw new Error('Error al crear la PQRS');
        }
    }

};



