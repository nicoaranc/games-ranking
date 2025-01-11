<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Games ranking</strong></router-link>
        <router-link to="/" class="navbar-item"><strong>Ingresar Juego</strong></router-link>
        <router-link to="/" class="navbar-item"><strong>Buscar Plataforma</strong></router-link>
        <router-link to="/" class="navbar-item"><strong>Buscar Juego</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <!-- <router-link to="/log-in" class="button is-light">Log In</router-link> -->
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="hast-text-centered">Copyright (c) 2025</p>
    </footer>

  </div>
</template>



<style>
@import '../node_modules/bulma';
</style>
