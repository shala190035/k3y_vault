<template>
  <section class="features text-center">
    <h2>Why Choose K3Y-Vault?</h2>
    <div class="container feature-list">
      <div class="row">
        <div class="col-md-4">
          <FeatureItem
            iconSrc="/src/assets/wallet-icon.png"
            title="Dual Functionality"
            description="Store your money and keys securely in one compact wallet."
          />
        </div>
        <div class="col-md-4">
          <FeatureItem
            iconSrc="/src/assets/lock.png"
            title="Ultimate Security"
            description="Innovative design ensures the safety of your belongings."
          />
        </div>
        <div class="col-md-4">
          <FeatureItem
            iconSrc="/src/assets/check.png"
            title="Convenience"
            description="Enjoy the convenience of having everything you need in one place."
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import FeatureItem from './FeatureItem.vue';

export default {
  components: {
    FeatureItem,
  },
};
</script>

<style scoped src="@/css/styles.css"></style>
