<template>
  <div class="page-search">
    <div class="has-text-centered">
      <h1 class="title">Búsqueda</h1>

      <form @submit.prevent="searchGame">
        <input class="input mb-3" v-model="query" placeholder="Juego a buscar" required />
        <button class="button is-primary input" type="submit">Buscar</button>
      </form>

      <br />
      <br />

      <div class="box has-text-centered" v-if="hasSearched">
        <h2 class="is-size-2 title">Resultados para "{{ finalQuery }}"</h2>
        <br />
        <GameGrid :games="games" />
      </div>
    </div>
  </div>
</template>

<script>
import GameGrid from '../components/GameGrid.vue';
import api from '../services/api.js';

export default {
  name: 'SearchPage',
  components: {
    GameGrid,
  },
  data() {
    return {
      games: [],
      query: '',
      finalQuery: '',
      hasSearched: false,
    };
  },
  methods: {
    searchGame() {
      api
        .searchGames(this.query)
        .then((response) => {
          this.games = Array.isArray(response.data) ? response.data : [];
          this.finalQuery = this.query;
          this.hasSearched = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
