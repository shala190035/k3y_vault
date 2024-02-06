<template>
  <div class="landing-page">
    <header class="hero">
      <div class="hero-content">
        <h1>Welcome to K3Y-Vault</h1>
        <p>Your secure wallet solution for both cash and keys.</p>
        <router-link to="/features" class="cta-button">Explore Features</router-link>
      </div>
    </header>

    <section class="features">
      <h2>Why Choose K3Y-Vault?</h2>
      <div class="feature-list">
        <div class="feature-item">
          <img src="wallet-icon.png" alt="Wallet Icon">
          <h3>Dual Functionality</h3>
          <p>Store your money and keys securely in one compact wallet.</p>
        </div>
        <div class="feature-item">
          <img src="secure-icon.png" alt="Secure Icon">
          <h3>Ultimate Security</h3>
          <p>Advanced encryption technology ensures the safety of your belongings.</p>
        </div>
        <div class="feature-item">
          <img src="convenience-icon.png" alt="Convenience Icon">
          <h3>Convenience</h3>
          <p>Enjoy the convenience of carrying everything you need in one place.</p>
        </div>
      </div>
    </section>

    <footer class="footer">
      <p>&copy; 2024 K3Y-Vault. All rights reserved.</p>
    </footer>
  </div>
</template>

<style scoped>
.landing-page {
  text-align: center;
}

.hero {
  background-color: #f4f6f9; /* Soft blue-gray */
  padding: 100px 0;
}

.hero-content {
  max-width: 600px;
  margin: 0 auto;
}

.cta-button {
  display: inline-block;
  background-color: #2ecc71; /* Soft green */
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  margin-top: 20px;
  transition: background-color 0.3s ease;
}

.cta-button:hover {
  background-color: #27ae60; /* Darker green on hover */
}

.features {
  padding: 50px 0;
}

.feature-list {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

.feature-item {
  flex: 1 1 300px;
  margin: 20px;
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

.feature-item:hover {
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
}

.feature-item img {
  width: 80px;
  height: 80px;
}

.footer {
  background-color: #34495e; /* Soft dark blue */
  color: #fff;
  padding: 20px 0;
}
</style>
