<template>
    <div>
        <h1 class="title has-text-centered">Registrar Juego</h1>
    </div>
    <br>
    <div class="box has-text-centered">
        <form @submit.prevent = "submitGame">
            <p>Nombre: <input v-model="game.name" placeholder="Nombre" required/></p>
            <p>Plataforma: 
                <select v-model="game.platform">
                    <option disabled value="">Elegir Plataforma</option>
                    <option v-for="platform in platforms" :key="platform.name" :value="platform.name">
                        {{ platform.name_desc }}
                    </option>
                </select>
            </p>
            <p>MyScore: 
                <input type="number" 
                        v-model.number="game.score" 
                        :min="0"
                        :max="100"
                        required/> /100
            </p>
            <p>Descripción: <textarea v-model="game.description"></textarea></p>
            <p>Link Video (YouTube Embed): <input v-model="game.video" required/></p>
            <p>Image:
                <input
                    type="file"
                    accept="image/*"
                    @change="handleImageUpload"
                    required />
            </p>
            <button class="button is-primary" type="submit">Guardar</button>  
        </form>

        <p v-if="successMessage" class="has-text-success">{{ successMessage }}</p>
        <p v-if="errorMessage" class="has-text-danger">{{ errorMessage }}</p>

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
            successMessage: '',
            errorMessage: ''
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
                formData.append('slug', slug); // Puedes generarlo aquí si prefieres
                formData.append('score', this.game.score);
                if (this.game.image) {
                    formData.append('image', this.game.image); // Agregar archivo de imagen
                }
                formData.append('description', this.game.description);
                formData.append('video', this.game.video);
                console.log(formData)
                axios
                    .post('http://127.0.0.1:8000/api/games/', formData)
                    .then(response => {
                        console.log("BIEN")
                        console.log(response)
                    })
                    .catch(error => {
                        console.log("MAL")
                        console.log(error)
                    })

                this.successMessage = 'Juego registrado exitosamente!'
                this.errorMessage = ''
                this.resetForm()
        },
        resetForm() {
            this.game = {
                name: '',
                platform: '',
                score: '',
                description: '',
                video: '',
                image: null
            }
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
</style>