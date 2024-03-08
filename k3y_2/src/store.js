// store.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cart: [],
  },
  mutations: {
    addToCart(state, product) {
      let found = state.cart.find(item => item.id == product.id);
      if (found) {
        found.quantity++;
      } else {
        state.cart.push(product);
        Vue.set(product, 'quantity', 1);
      }
    },
  },
});
