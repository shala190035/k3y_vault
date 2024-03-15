import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      cart: [], // Anfangszustand des Warenkorbs
    };
  },
  mutations: {
    addToCart(state, product) {
        let found = state.cart.find(item => item.id === product.id);
        if (found) {
          found.quantity++;
        } else {
          state.cart.push({...product, quantity: 1});
        }
        localStorage.setItem('cart', JSON.stringify(state.cart)); // Warenkorb aktualisieren
    },
    setCart(state, cart) {
      state.cart = cart;
      // Warenkorb im localStorage aktualisieren
      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    removeFromCart(state, productId) {
        let found = state.cart.find(item => item.id === productId);
        if (found && found.quantity > 1) {
          found.quantity--;
        } else {
          state.cart = state.cart.filter(item => item.id !== productId);
        }
        localStorage.setItem('cart', JSON.stringify(state.cart)); // Warenkorb aktualisieren
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
