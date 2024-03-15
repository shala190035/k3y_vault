<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
      <div class="container">
        <a class="navbar-brand" href="#">
          <router-link to="/" class="nav-link active" aria-current="page">          <img src="../assets/logo_noname.png" alt="K3Y-Vault Logo" height="36" > </router-link>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link to="/" class="nav-link active" aria-current="page">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/link" class="nav-link">Link</router-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person" viewBox="1 1 16 16">
                  <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6m2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0m4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4m-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10s-3.516.68-4.168 1.332c-.678.678-.83 1.418-.832 1.664z"/>
                </svg>
              </a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="cartDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-cart-fill" viewBox="0 0 16 16">
                  <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L1.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zM4.5 8a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5V8z"/>
                </svg>
              </a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="cartDropdown">
                <div v-for="item in cartItems" :key="item.id" class="cart-item">
                  {{ item.title }} - {{ item.quantity }}x - {{ item.price }} €
                  <button @click.stop="removeItemFromCart(item.id)">remove</button>
                </div>

                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Warenkorb anzeigen</a></li>
              </ul>
            </li>

          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
    import { mapActions, mapGetters } from 'vuex';
    
    export default {
      computed: {
        ...mapGetters(['cartItems']),
      },
      methods: {
        ...mapActions(['removeFromCart']),
        removeItemFromCart(productId) {
          this.removeFromCart(productId);
        },
      },
    };
  </script>
  
  
  
  <style scoped src="@/css/styles.css"></style>