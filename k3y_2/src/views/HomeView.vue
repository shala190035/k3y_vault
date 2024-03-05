<template>
  <div class="home">
    <NavbarComponent />
    <HeroComponent />
    <FeaturesComponent />
    <FooterComponent />
  </div>
</template>

<script>
// Import your componentsbar
  import NavbarComponent from '@/components/NavbarComponent.vue';
  import HeroComponent from '../components/HeroComponent.vue';
  import FeaturesComponent from '../components/FeaturesComponent.vue';
  import FooterComponent from '../components/FooterComponent.vue';

export default {
  name: 'HomeView',
  components: {
    NavbarComponent,
    HeroComponent,
    FeaturesComponent,
    FooterComponent,
  },
};
</script>

<style scoped src="@/css/styles.css"></style>
