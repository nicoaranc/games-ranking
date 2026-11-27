<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Games ranking</strong></router-link>
        <a
          role="button"
          class="navbar-burger"
          :class="{ 'is-active': isMenuOpen }"
          aria-label="menu"
          :aria-expanded="isMenuOpen.toString()"
          data-target="navbar-menu"
          @click="isMenuOpen = !isMenuOpen"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" :class="{ 'is-active': isMenuOpen }">
        <div class="navbar-start">
          <router-link to="/register-game" class="navbar-item"><strong>Ingresar Juego</strong></router-link>
          <router-link to="/platforms" class="navbar-item"><strong>Buscar Plataforma</strong></router-link>
          <router-link to="/search" class="navbar-item"><strong>Buscar Juego</strong></router-link>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2025</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isMenuOpen: false,
    };
  },
  watch: {
    $route() {
      this.isMenuOpen = false;
    },
  },
};
</script>

<style>
@import '../node_modules/bulma';
</style>
