<template>
  <div class="box has-text-centered fixed-size game-card">
    <figure class="image mb-4" :class="{ 'is-compact': compactImage }">
      <img :src="game.get_thumbnail" :alt="game.name" />
    </figure>

    <h3 class="is-size-5 has-text-weight-bold">{{ game.name }}</h3>
    <h4 class="is-size-6">{{ game.platform }}</h4>
    <p class="is-size-6 has-text-grey">{{ game.score }}/100</p>

    <router-link
      v-if="showAction && game.get_absolute_url"
      :to="game.get_absolute_url"
      class="button is-dark mt-4"
    >
      Ver juego
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'GameCard',
  props: {
    game: {
      type: Object,
      required: true,
    },
    showAction: {
      type: Boolean,
      default: true,
    },
    compactImage: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped>
.fixed-size {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.game-card .button {
  margin-top: auto;
}

.is-compact img {
  max-width: 200px;
  height: auto;
  margin: 0 auto;
}
</style>
