import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import the router instance
import './css/styles.css';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';

createApp(App).use(router).mount('#app'); // Use the router
