// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ProductView from '../views/ProductView.vue';
import CheckoutView from '../views/CheckoutView.vue'; // Importieren Sie Ihre CheckoutView
import OrderTrackingView from '../views/OrderTrackingView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/products',
      name: 'Products',
      component: ProductView,
    },
    {
      path: '/checkout',
      name: 'Checkout',
      component: CheckoutView, // Fügen Sie Ihre Route hinzu
    },
    {
      path: '/track-order',
      name: 'TrackOrder',
      component: OrderTrackingView,
    },
  ],
});

export default router;
