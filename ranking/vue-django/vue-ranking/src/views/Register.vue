<template>
    <div>
        <h1 class="title has-text-centered">Registrar Juego</h1>
    </div>
    <br>
    <div class="box my-custom-box m-auto">
        <form @submit.prevent = "submitGame">
            <div class="field">
                <label class="label">Nombre: </label>
                <div class="control">
                    <input class="input" v-model="game.name" placeholder="Nombre" required/>
                </div>
                <br>
                <label class="label">Plataforma: </label>
                <div class="control">
                    <select class="input" v-model="game.platform">
                        <option disabled value="">Elegir Plataforma</option>
                        <option v-for="platform in platforms" :key="platform.name" :value="platform.name">
                            {{ platform.name_desc }}
                        </option>
                    </select>
                </div>
                <br>
                <label class="label">MyScore:</label>
                <div class="control">
                    <input type="number" 
                            v-model.number="game.score" 
                            :min="0"
                            :max="100"
                            required/> /100
                </div>
                <br>
                <label class="label">Descripción:</label>
                <div class="control">
                    <textarea class="input" v-model="game.description"></textarea>
                </div>
                <br>
                <label class="label">Link Video (YouTube Embed):</label>
                <div class="control">
                    <input class="input" v-model="game.video" required/>
                </div>
                <br>
                <label class="label"> Image: </label>
                <div class="control">
                    <input class="input"
                        type="file"
                        accept="image/*"
                        @change="handleImageUpload"
                        required />
                </div>
            </div>
            <br>
            <button class="button is-primary input" type="submit">Guardar</button>  
        </form>

        <p v-if="successMessage" class="has-text-success">{{ successMessage }}</p>
        <p v-if="errorMessage" class="has-text-danger">{{ errorMessage }}</p>

    </div>

    <div v-if="submitedGame" class="modal has-text-centered" :class="{'is-active': isModalActive}">
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <h3 class="modal-card-title">{{ submitedGame.name }} ha sido registrado exitosamente </h3>
                <button class="delete" aria-label="close" @click="closeModal()"></button>
            </header>
            <section class="modal-card-body">
                <div class="box has-text-centered">
                    <figure class="image mb-4">
                        <img :src="submitedGame.get_thumbnail">
                    </figure>

                    <h3 class="is-size-4">{{ submitedGame.name }}</h3>
                    <h4 class="is-size-6">{{ submitedGame.platform }}</h4>
                    <p class="is-size-6 has-text-grey">{{ submitedGame.score }}/100</p>
                </div>
            </section>
            <footer class="modal-card-foot">
                <router-link v-bind:to="submitedGame.get_absolute_url" class="button is-dark mt-4"> Ver juego </router-link>
            </footer>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Register-game-page',
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
            submitedGame: {},
            successMessage: '',
            errorMessage: '',
            isModalActive: false
        }
    },
    components:{
    },
    mounted() {
        this.getPlatforms()
    },
    methods: {
        getPlatforms() {
            axios
                .get('http://127.0.0.1:8000/api/platforms')
                .then(response => {
                    this.platforms = response.data;
                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleImageUpload(event) {
            const file = event.target.files[0];
            if (file && file.type.startsWith("image/")) {
                this.game.image = file;
            }
            else {
                this.errorMessage = 'Por favor selecciona un archivo de imagen valido'
                this.game.file = null
            }
        },
        submitGame() {
                const slug = this.game.name.toLowerCase().replace(/ /g, '-').replace(/:/g, '').replace(/'/g, '');
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
                console.log(formData)
                axios
                    .post('http://127.0.0.1:8000/api/games/', formData)
                    .then(response => {
                        console.log(response)
                        this.getGame(slug, this.game.platform.toLowerCase())
                    })
                    .catch(error => {
                        console.log("MAL")
                        console.log(error)
                    })

                this.successMessage = 'Juego registrado exitosamente!'
                this.errorMessage = ''
                
                
        },
        resetForm() {
            this.game = {
                name: '',
                platform: '',
                score: '',
                description: '',
                video: '',
                image: null,
            }
        },
        getGame(game_name, game_platform) {
            axios
                .get(`http://127.0.0.1:8000/api/games/${game_platform}/${game_name}`)
                .then(response => {
                    this.submitedGame = response.data
                    console.log('Datos del juego:', this.submitedGame);
                    this.isModalActive = true
                })
                .catch(error => {
                    console.log(error)
                })
        },
        closeModal() {
            this.isModalActive = false
            this.submitedGame = {}
            this.resetForm()
        }
    }
}
</script>

<style>
.image {
    margin-top: 1rem;
}
textarea {
    resize: none;
}
.my-custom-box {
    width: 400px;
    height: 700px;
}
</style>