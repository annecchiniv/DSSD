// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import store from './store';
import Router from './router';
import axios from 'axios';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

// Configuración de Axios
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      console.error('No autorizado, redirigiendo a login...');
    }
    return Promise.reject(error);
  }
);

// Crear la aplicación Vue
createApp(App)
  .use(Router)
  .use(store)
  .mount('#app');
