<template>
    <div>
      <NavbarComponent />
      <div class="product-view">
        <h1>Products</h1>
        <div v-if="loading" class="loading">Loading...</div>
        <div v-else class="products-container">
          <div v-for="product in products" :key="product.id" class="product-card">
            <h2>{{ product.name }}</h2>
            <p>{{ product.description }}</p>
            <p class="price">Price: ${{ product.price }}</p>
          </div>
        </div>
      </div>
        <div style="position: bottom;">
            <FooterComponent />
        </div>
    </div>
  </template>
  
  <script>
  // Importing Navbar and Footer components to be used in the product view
  import NavbarComponent from '@/components/NavbarComponent.vue';
  import FooterComponent from '@/components/FooterComponent.vue';
  
  export default {
    name: "ProductView",
    components: {
      NavbarComponent,
      FooterComponent,
    },
    data() {
      return {
        products: [],
        loading: false,
      };
    },
    methods: {
      async fetchProducts() {
        this.loading = true;
        try {
          const response = await fetch("http://localhost:8000/products/");
          if (!response.ok) throw new Error("Failed to fetch");
          const data = await response.json();
          this.products = data;
          console.log(data);
        } catch (error) {
          console.error("Error fetching products:", error);
        } finally {
          this.loading = false;
        }
      },
    },
    mounted() {
      this.fetchProducts();
    },
  };
  </script>
  
  <style scoped>
  .loading {
    color: #999;
    text-align: center;
    margin-top: 20px;
  }
  .product-view {
    padding: 20px;
  }
  .products-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  .product-card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
    width: 300px;
    margin: 10px;
    padding: 20px;
    border-radius: 5px;
    text-align: center;
  }
  .product-card:hover {
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  }
  .price {
    color: #007BFF;
    font-weight: bold;
  }
  </style>
  