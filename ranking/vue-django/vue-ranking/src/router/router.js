// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'; // Asegúrate de que la ruta sea correcta

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home, // Muestra Home.vue cuando se navegue a "/"
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
