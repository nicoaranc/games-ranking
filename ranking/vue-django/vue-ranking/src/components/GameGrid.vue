<template>
  <div v-if="games.length === 0" class="has-text-centered">
    <p>{{ emptyMessage }}</p>
  </div>
  <div v-else class="columns is-multiline">
    <div class="column is-3" v-for="game in games" :key="game.id">
      <GameCard :game="game" />
    </div>
  </div>
</template>

<script>
import GameCard from './GameCard.vue';

export default {
  name: 'GameGrid',
  components: {
    GameCard,
  },
  props: {
    games: {
      type: Array,
      required: true,
    },
    emptyMessage: {
      type: String,
      default: 'No se encontraron juegos.',
    },
  },
};
</script>
