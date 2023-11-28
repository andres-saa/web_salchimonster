import Vuex from 'vuex';

const store = new Vuex.Store({
  state: {
    barrioActual: localStorage.getItem('currentNeigborhood') || '', // Inicializa el valor del localStorage en el estado de Vuex
  },
  mutations: {
    actualizarValorLocalStorage(state, nuevoValor) {
      state.barrioActual = nuevoValor;
    },
  },
});


export {store}