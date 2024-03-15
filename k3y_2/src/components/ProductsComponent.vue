<template>
  <div class="product-component">
    <div v-for="product in products" :key="product.id" class="product-card">
      <h3>{{ product.title }}</h3>
      <img :src="getImageUrl(product.image)" alt="Product Image" class="product-image"/>
      <p>{{ product.description }}</p>
      <p>{{ product.price }} €</p>
      <button @click="addToCart(product)">In Warenkorb hinzufügen</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      products: [],
      baseUrl: 'http://localhost:8000'
    };
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    ...mapActions(['addToCart']), // Verwendung von Vuex Aktionen
    getImageUrl(imagePath) {
      return `${this.baseUrl}/${imagePath}`;
    },
    getProducts() {
      axios.get('http://localhost:8000/products/')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
  }
}
</script>
