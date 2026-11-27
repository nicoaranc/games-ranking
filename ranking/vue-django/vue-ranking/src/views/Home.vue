<template>
  <div class="columns is-multiline">
    <div class="column is-12 mb-4">
      <h2 class="is-size-1 has-text-centered">Mi Ranking de Mejores Juegos</h2>
    </div>

    <div id="game-container" class="box column is-12">
      <GameGrid :games="visibleGames" />
    </div>

    <div class="column is-12 is-flex is-justify-content-space-between">
      <button
        id="prev-button"
        type="button"
        @click="prevPage"
        class="button is-dark mt-4"
        :disabled="!hasPrevPage"
      >
        Anterior
      </button>
      <button
        id="next-button"
        type="button"
        @click="nextPage"
        class="button is-dark mt-4"
        :disabled="!hasNextPage"
      >
        Siguiente
      </button>
    </div>
  </div>
</template>

<script>
import GameGrid from '../components/GameGrid.vue';
import api from '../services/api.js';

export default {
  name: 'HomePage',
  components: {
    GameGrid,
  },
  data() {
    return {
      currentPage: 0,
      perPage: 12,
      bestGames: [],
    };
  },
  computed: {
    visibleGames() {
      const start = this.currentPage * this.perPage;
      return this.bestGames.slice(start, start + this.perPage);
    },
    hasPrevPage() {
      return this.currentPage > 0;
    },
    hasNextPage() {
      return (this.currentPage + 1) * this.perPage < this.bestGames.length;
    },
  },
  mounted() {
    this.getBestGames();
  },
  methods: {
    getBestGames() {
      api
        .getGames()
        .then((response) => {
          this.bestGames = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    prevPage() {
      if (!this.hasPrevPage) return;
      this.currentPage -= 1;
      this.autoScroll();
    },
    nextPage() {
      if (!this.hasNextPage) return;
      this.currentPage += 1;
      this.autoScroll();
    },
    autoScroll() {
      window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth',
      });
    },
  },
};
</script>

<style scoped>
#game-container {
  width: 100%;
}
</style>
