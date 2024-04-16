<template>
  <div class="feature-item" style="padding: 10px;">
    <slot name="icon"></slot> <!-- Slot for the icon image -->
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    description: String,
  },
};
</script>

<style scoped src="@/css/styles.css"></style>
