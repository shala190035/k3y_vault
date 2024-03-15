import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store'; 
import './css/styles.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';

const app = createApp(App);

app.use(router);
app.use(store);

// Warenkorb beim Start wiederherstellen
store.dispatch('initializeStore');

app.mount('#app');
