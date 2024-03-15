<template>
  <div class="product-component">
    <div v-for="product in products" :key="product.id" class="product-card">
      <img :src="getImageUrl(product.image)" alt="Product Image" class="product-image"/>
      <h3>{{ product.title }}</h3>
      <p>{{ product.description }}</p>
      <div class="price">{{ product.price }} €</div>
      <button @click.stop="addToCart(product)" class="add-to-cart-button">add to card</button>
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
