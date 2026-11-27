<template>
  <div>
    <div class="columns">
      <div class="column">
        <h1 class="title">{{ game.name }}</h1>
        <div class="columns">
          <div class="column is-4">
            <figure class="image mb-6">
              <img :src="game.get_image" :alt="game.name" />
              <br />
              <p class="has-text-centered"><strong>MyScore: </strong>{{ game.score }}/100</p>
              <p class="has-text-centered"><strong>Platform: </strong>{{ platform }}</p>
            </figure>
          </div>
          <div class="column">
            <p class="has-text-centered">Descripción</p>
            <br />
            <p class="has-text-centered">
              {{ game.description }}
            </p>
          </div>
        </div>
      </div>
      <div class="column has-text-centered">
        <h1 class="title">Video/Trailer</h1>
        <iframe
          width="560"
          height="315"
          :src="game.video"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"
          allowfullscreen
        ></iframe>
      </div>
    </div>

    <div class="box has-text-centered">
      <h1 class="title">Más juegos de {{ platform }}</h1>
      <br />
      <GameGrid
        :games="bestGames"
        empty-message="No hay más juegos registrados para esta plataforma."
      />
    </div>
  </div>
</template>

<script>
import GameGrid from '../components/GameGrid.vue';
import api from '../services/api.js';

export default {
  name: 'GamePage',
  components: {
    GameGrid,
  },
  data() {
    return {
      game: {},
      bestGames: [],
      platform: '',
    };
  },
  watch: {
    '$route.params': {
      handler(params) {
        if (params.platform_slug && params.game_slug) {
          this.getGame();
        }
      },
      deep: true,
    },
  },
  mounted() {
    this.getGame();
  },
  methods: {
    getGame() {
      const { platform_slug: platformSlug, game_slug: gameSlug } = this.$route.params;

      api
        .getGame(platformSlug, gameSlug)
        .then((response) => {
          this.game = response.data;
          this.getBestPlatformGames(platformSlug);
          this.getPlatform();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getBestPlatformGames(platformSlug) {
      api
        .getPlatformGames(platformSlug)
        .then((response) => {
          this.bestGames = response.data.games.filter((item) => item.id !== this.game.id);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getPlatform() {
      api
        .getPlatforms()
        .then((response) => {
          const matched = response.data.find((item) => item.name === this.game.platform);
          this.platform = matched ? matched.name_desc : this.game.platform || '';
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
