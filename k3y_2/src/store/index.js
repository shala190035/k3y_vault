import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      cart: [], // Anfangszustand des Warenkorbs
    };
  },
  mutations: {
    addToCart(state, product) {
      state.cart.push(product);
    },
  },
  actions: {
    addToCart({ commit }, product) {
      commit('addToCart', product);
    },
  },
  getters: {
    cartItems: (state) => state.cart,
  },
});

export default store;
