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
      // Warenkorb im localStorage speichern
      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    setCart(state, cart) {
      state.cart = cart;
      // Warenkorb im localStorage aktualisieren
      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    removeFromCart(state, productId) {
        const index = state.cart.findIndex(item => item.id === productId);
        if (index !== -1) {
            state.cart.splice(index, 1);
            // Aktualisierten Warenkorb im localStorage speichern
            localStorage.setItem('cart', JSON.stringify(state.cart));
        }
    },
  },
  actions: {
    addToCart({ commit }, product) {
      commit('addToCart', product);
    },
    initializeStore({ commit }) {
      const storedCart = localStorage.getItem('cart');
      if (storedCart) {
        commit('setCart', JSON.parse(storedCart)); // Warenkorb aus localStorage wiederherstellen
      }
    },
    removeFromCart({ commit }, productId) {
        commit('removeFromCart', productId);
    },
  },
  getters: {
    cartItems: (state) => state.cart,
  },
});

export default store;
