// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'; // Asegúrate de que la ruta sea correcta
import Game from '../views/Game.vue';
import Platforms from '../views/Platform.vue'
import RegisterGame from '../views/Register.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home, // Muestra Home.vue cuando se navegue a "/"
  },
  {
    path: '/:platform_slug/:game_slug/',
    name: 'Game',
    component: Game,
  },
  {
    path: '/platforms',
    name: 'Platforms',
    component: Platforms
  },
  {
    path: '/register-game',
    name: 'RegisterGame',
    component: RegisterGame
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
