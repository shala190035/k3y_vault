<!-- FeatureItem.vue -->
<template>
    <div class="feature-item" style="padding: 10px;">
      <img :src="iconSrc" :alt="title" class="feature-icon">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      iconSrc: String,
      title: String,
      description: String,
    },
  };
  </script>
  
  <style scoped src="@/css/styles.css"></style>
  