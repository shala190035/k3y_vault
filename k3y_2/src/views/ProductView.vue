<template>
    <div class="product-view">
      <ProductComponent />
    </div>
  </template>
  
  <script>
  import ProductComponent from '@/components/ProductsComponent.vue';
  
  export default {
    components: {
      ProductComponent,
    },
  }
  </script>
  
  <style scoped>
  .product-view {
    display: flex;
    justify-content: center;
    padding: 20px;
  }
  </style>
  