<template>
  <div>
    <div>
      <h1 class="title has-text-centered">Registrar Juego</h1>
    </div>
    <br />
    <div class="box my-custom-box m-auto">
      <form @submit.prevent="submitGame">
        <div class="field">
          <label class="label">Nombre: </label>
          <div class="control">
            <input class="input" v-model="game.name" placeholder="Nombre" required />
          </div>
          <br />
          <label class="label">Plataforma: </label>
          <div class="control">
            <select class="input" v-model="game.platform" required>
              <option disabled value="">Elegir Plataforma</option>
              <option v-for="platform in platforms" :key="platform.name" :value="platform.name">
                {{ platform.name_desc }}
              </option>
            </select>
          </div>
          <br />
          <label class="label">MyScore:</label>
          <div class="control">
            <input
              type="number"
              v-model.number="game.score"
              :min="0"
              :max="100"
              required
            />
            /100
          </div>
          <br />
          <label class="label">Descripción:</label>
          <div class="control">
            <textarea class="input" v-model="game.description"></textarea>
          </div>
          <br />
          <label class="label">Link Video (YouTube Embed):</label>
          <div class="control">
            <input class="input" v-model="game.video" required />
          </div>
          <br />
          <label class="label">Image:</label>
          <div class="control">
            <input
              class="input"
              type="file"
              accept="image/*"
              @change="handleImageUpload"
              ref="imageInput"
              required
            />
          </div>
        </div>
        <br />
        <button class="button is-primary input" type="submit">Guardar</button>
      </form>

      <p v-if="successMessage" class="has-text-success mt-3">{{ successMessage }}</p>
      <p v-if="errorMessage" class="has-text-danger mt-3">{{ errorMessage }}</p>
    </div>

    <div v-if="submitedGame" class="modal has-text-centered" :class="{ 'is-active': isModalActive }">
      <div class="modal-background" @click="closeModal"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">{{ submitedGame.name }} ha sido registrado exitosamente</p>
          <button class="delete" aria-label="close" @click="closeModal"></button>
        </header>
        <section class="modal-card-body">
          <GameCard :game="submitedGame" :show-action="false" :compact-image="true" />
        </section>
        <footer class="modal-card-foot is-justify-content-center">
          <router-link
            v-if="submitedGame.get_absolute_url"
            :to="submitedGame.get_absolute_url"
            class="button is-dark"
          >
            Ver juego
          </router-link>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import GameCard from '../components/GameCard.vue';
import api from '../services/api.js';

export default {
  name: 'RegisterGamePage',
  components: {
    GameCard,
  },
  data() {
    return {
      platforms: [],
      game: {
        name: '',
        platform: '',
        slug: '',
        score: '',
        image: null,
        thumbnail: null,
        description: '',
        video: '',
      },
      submitedGame: null,
      successMessage: '',
      errorMessage: '',
      isModalActive: false,
      specialChars: [':', '.', "'"],
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
    handleImageUpload(event) {
      const file = event.target.files[0];
      if (file && file.type.startsWith('image/')) {
        this.game.image = file;
        this.errorMessage = '';
      } else {
        this.errorMessage = 'Por favor selecciona un archivo de imagen válido';
        this.game.image = null;
      }
    },
    submitGame() {
      this.successMessage = '';
      this.errorMessage = '';

      const slug = this.processName(this.game.name);
      const platformSlug = this.game.platform.toLowerCase();
      const formData = new FormData();
      formData.append('name', this.game.name);
      formData.append('platform', this.game.platform);
      formData.append('slug', slug);
      formData.append('score', this.game.score);
      if (this.game.image) {
        formData.append('image', this.game.image);
      }
      formData.append('description', this.game.description);
      formData.append('video', this.game.video);

      api
        .createGame(formData)
        .then(() => {
          this.successMessage = 'Juego registrado exitosamente!';
          return this.fetchCreatedGame(platformSlug, slug);
        })
        .catch((error) => {
          console.error(error);
          this.errorMessage = 'Ocurrió un error al registrar el juego.';
        });
    },
    fetchCreatedGame(platformSlug, gameSlug) {
      return api
        .getGame(platformSlug, gameSlug)
        .then((response) => {
          this.submitedGame = response.data;
          this.isModalActive = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    resetForm() {
      this.game = {
        name: '',
        platform: '',
        slug: '',
        score: '',
        description: '',
        video: '',
        image: null,
        thumbnail: null,
      };

      if (this.$refs.imageInput) {
        this.$refs.imageInput.value = '';
      }
    },
    closeModal() {
      this.isModalActive = false;
      this.submitedGame = null;
      this.resetForm();
    },
    processName(name) {
      const escaped = this.specialChars.map((char) => `\\${char}`).join('');
      const regex = new RegExp(`[${escaped}]`, 'g');
      const slug = name.replace(regex, '').toLowerCase().replace(/ /g, '-');
      return this.quitarTilde(slug);
    },
    quitarTilde(name) {
      return name.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    },
  },
};
</script>

<style scoped>
textarea {
  resize: none;
}

.my-custom-box {
  width: 400px;
  height: 700px;
}
</style>
