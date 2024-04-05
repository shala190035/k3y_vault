<template>
    <div class="order-tracking-page">
      <h1>Track Your Order</h1>
      <form @submit.prevent="trackOrder">
        <div class="form-group">
          <label for="orderNumber">Order Number</label>
          <input type="text" id="orderNumber" v-model="orderNumber" required>
        </div>
        <div class="form-group">
          <label for="address">Address</label>
          <input type="text" id="address" v-model="address" required>
        </div>
        <button type="submit">Track Order</button>
      </form>
  
      <div v-if="order">
        <h2>Order Details</h2>
        <!-- Display order details here -->
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        orderNumber: '',
        address: '',
        order: null, // To store the retrieved order details
        errorMessage: '', // To store error messages
      };
    },
    methods: {
      async trackOrder() {
        try {
          const response = await axios.post('http://localhost:8000/track-order', {
            order_id: parseInt(this.orderNumber), // Convert to integer to match backend expectation
            address: this.address,
          });
          this.order = response.data.order_details; // Assuming the API returns the order details wrapped in an object
          this.errorMessage = ''; // Clear any previous error messages
        } catch (error) {
          console.error('Error tracking order:', error);
          this.order = null; // Clear previous order details
          // Set an appropriate error message based on the error response
          if (error.response && error.response.status === 404) {
            this.errorMessage = 'Order not found or address does not match.';
          } else {
            this.errorMessage = 'There was an error processing your request. Please try again.';
          }
        }
      },
    },
  };
  </script>
    