<template>
  <div>
    <div class="home">
      <h1 class="title has-text-centered">Plataformas</h1>
    </div>
    <br />
    <div class="columns is-multiline">
      <div class="column is-3" v-for="platform in platforms" :key="platform.name">
        <div @click="getBestGames(platform.slug)" class="box is-clickable">
          <h3 class="is-size-4">{{ platform.name_desc }}</h3>
        </div>
      </div>
    </div>
    <br />
    <h1 class="title has-text-centered" v-if="selectedPlatform === ''">Mejores Juegos</h1>
    <h1 class="title has-text-centered" v-else>Mejores Juegos de {{ selectedPlatform }}</h1>
    <br />
    <div class="box" v-if="selectedPlatform === ''">
      <p class="has-text-centered">Seleccione una plataforma</p>
    </div>
    <div class="box" v-else>
      <GameGrid :games="bestGames" empty-message="No se encontraron juegos para esta plataforma." />
    </div>
  </div>
</template>

<script>
import GameGrid from '../components/GameGrid.vue';
import api from '../services/api.js';

export default {
  name: 'PlatformsPage',
  components: {
    GameGrid,
  },
  data() {
    return {
      platforms: [],
      bestGames: [],
      selectedPlatform: '',
    };
  },
  mounted() {
    this.getPlatforms();
  },
  methods: {
    getPlatforms() {
      api
        .getPlatforms()
        .then((response) => {
          this.platforms = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getBestGames(platformSlug) {
      api
        .getPlatformGames(platformSlug)
        .then((response) => {
          this.bestGames = response.data.games;
          this.selectedPlatform = response.data.name_desc;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
