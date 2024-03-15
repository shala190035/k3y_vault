<template>
  <div class="product-view">
    <NavbarComponent />
    <div class="products-container">
      <ProductComponent />
    </div>
    <div class="bottom">
    <FooterComponent />
    </div>
  </div>
</template>

<script>
import NavbarComponent from '../components/NavbarComponent.vue';
import ProductComponent from '../components/ProductsComponent.vue';
import FooterComponent from '../components/FooterComponent.vue';

export default {
  components: {
    NavbarComponent,
    ProductComponent,
    FooterComponent,
  },
};
</script>

<style scoped>
@import "@/css/styles.css";

</style>
