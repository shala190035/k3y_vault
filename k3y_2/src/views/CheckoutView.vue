<template>
  <div class="checkout-page">
    <!-- Zurück-Pfeil -->
    <div class="back-to-products">
      <router-link to="/products">
        <i class="fas fa-arrow-left"></i> Zurück zu den Produkten
      </router-link>
    </div>
    <h1 class="page-title">Kasse</h1>
    <div class="checkout-content">
      <div class="cart-details">
        <h2>Deine Bestellung</h2>
        <ul class="cart-items-list">
          <li v-for="item in cartItems" :key="item.id" class="cart-item">
            <div class="item-info">
              <span class="item-title">{{ item.title }}</span>
              <span class="item-quantity">Menge: {{ item.quantity }}</span>
              <span class="item-price">{{ item.price }} €</span>
              <button @click.stop="removeItemFromCart(item.id)" class="button remove-from-cart-button">Entfernen</button>
            </div>
          </li>
        </ul>
        <div class="cart-total">
          Gesamt: <strong>{{ total }} €</strong>
        </div>
      </div>
      <div class="checkout-form">
        <h2>Lieferadresse</h2>
        <form @submit.prevent="submitOrder">
          <div class="form-group">
            <label for="email">E-Mail</label>
            <input type="email" id="email" required v-model="order.email">
          </div>
          <div class="form-group">
            <label for="address">Adresse</label>
            <input type="text" id="address" required v-model="order.address">
          </div>
          <div class="form-group">
            <label for="payment">Zahlungsmethode</label>
            <select id="payment" required v-model="order.payment">
              <option value="creditCard">Kreditkarte</option>
              <option value="paypal">PayPal</option>
              <option value="invoice">Rechnung</option>
            </select>
          </div>
          <button type="submit" class="submit-order-btn">Bestellung abschicken</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  data() {
    return {
      order: {
        email: '',
        address: '',
        payment: ''
      }
    };
  },
  computed: {
    ...mapGetters(['cartItems']),
    total() {
      return this.cartItems.reduce((acc, item) => acc + (item.price * item.quantity), 0).toFixed(2);
    }
  },
  methods: {
    ...mapActions(['removeFromCart']),
    removeItemFromCart(productId) {
      this.removeFromCart(productId);
    },
    submitOrder() {
      console.log("Bestellung aufgegeben:", this.order, "mit Warenkorb", this.cartItems);
      // Implementiere hier die Logik, um die Bestellung zu verarbeiten
    }
  }
}
</script>

<style scoped>
/* Deine vorhandenen Stile */
.remove-from-cart-button {
  background-color: #e74c3c;
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  margin-top: 10px;
}
.remove-from-cart-button:hover {
  background-color: #c0392b;
}
.checkout-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.page-title {
  text-align: center;
  margin-bottom: 40px;
}

.checkout-content {
  display: flex;
  justify-content: space-between;
}

.cart-details,
.checkout-form {
  flex: 1;
  margin: 0 10px;
}

.cart-items-list {
  list-style: none;
  padding: 0;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.item-info {
  display: flex;
  flex-direction: column;
}

.item-title,
.item-quantity,
.item-price {
  margin: 0;
}

.cart-total {
  margin-top: 20px;
  font-size: 20px;
  font-weight: bold;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.submit-order-btn {
  display: block;
  width: 100%;
  background-color: #2ecc71;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-order-btn:hover {
  background-color: #27ae60;
}
.back-to-products {
  margin-bottom: 20px;
}

.back-to-products a {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.back-to-products i {
  margin-right: 5px;
}

</style>
