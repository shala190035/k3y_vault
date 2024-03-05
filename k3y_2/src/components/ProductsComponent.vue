<template>
    <div class="product-component">
      <div v-for="product in products" :key="product.id" class="product">
        <h3>{{ product.title }}</h3>
        <img :src="`/images/${product.image}`" alt="Product Image" class="product-image"/>
        <p>{{ product.description }}</p>
        <p>{{ product.price }} €</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        products: [],
      };
    },
    mounted() {
      this.getProducts();
    },
    methods: {
      getProducts() {
        axios.get('http://localhost:8000/products/')
          .then(response => {
            this.products = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  }
  </script>
  
  <style scoped>
  .product {
    border: 1px solid #eee;
    padding: 20px;
    margin-bottom: 20px;
  }
  .product-image {
    width: 100%;
    max-width: 300px;
  }
  </style>
  