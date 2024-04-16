<template>
  <section class="features text-center">
    <h2>Why Choose K3Y-Vault?</h2>
    <div class="container feature-list">
      <div class="row">
        <div class="col-md-4">
          <FeatureItem
            title="Dual Functionality"
            description="Store your money and keys securely in one compact wallet.">
            <template #icon>
              <img src="@/assets/wallet-icon.png" alt="Wallet Icon">
            </template>
          </FeatureItem>
        </div>
        <div class="col-md-4">
          <FeatureItem
            title="Ultimate Security"
            description="Innovative design ensures the safety of your belongings.">
            <template #icon>
              <img src="@/assets/lock.png" alt="Lock Icon">
            </template>
          </FeatureItem>
        </div>
        <div class="col-md-4">
          <FeatureItem
            title="Convenience"
            description="Enjoy the convenience of having everything you need in one place.">
            <template #icon>
              <img src="@/assets/check.png" alt="Check Icon">
            </template>
          </FeatureItem>
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
