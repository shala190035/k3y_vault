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
  <div class="cart-view">
    <h2>Warenkorb</h2>
    <div v-for="item in cart" :key="item.id" class="cart-item">
      <h3>{{ item.title }}</h3>
      <p>{{ item.price }} €</p>
    </div>
  </div>
</template>

  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        products: [],
        cart: [],
        baseUrl: 'http://localhost:8000'
      };
    },
    mounted() {
      this.getProducts();
    },
    methods: {
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
      addToCart(product) {
      this.cart.push(product);
      alert(`${product.title} wurde zum Warenkorb hinzugefügt.`);
    }
    }
    
  }
  </script>
  

  <style scoped src="@/css/styles.css"></style>
  