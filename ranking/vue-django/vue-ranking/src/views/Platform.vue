<template>
    <div class="home">
        <h1 class="title has-text-centered"> Plataformas </h1>
    </div>
    <br>
    <div class="columns is-multiline">
        <div class="column is-3" v-for="platform in platforms" v-bind:key="platform.name">
            <div v-on:click="getBestGames(platform.slug)" class="box is-clickable">
                <h3 class="is-size-4">{{ platform.name_desc }}</h3>
            </div>
        </div>
    </div>
    <br>
    <h1 class="title has-text-centered" v-if="selected_platform === ''">Mejores Juegos</h1>
    <h1 class="title has-text-centered" v-else>Mejores Juegos de {{ selected_platform }}</h1>
    <br>
    <div class="box" v-if="bestGames.length === 0">
        <p class="has-text-centered ">Seleccione una plataforma</p>
    </div>
    <div class="columns is-multiline box has-text-centered" v-else>
        <div class="column is-3" v-for="game in bestGames" v-bind:key="game.id">
            <div class="box">
                <figure class="image mb-4">
                    <img :src="game.get_thumbnail">
                </figure>

                <h3 class="is-size-4 has-text-centered">{{ game.name }}</h3>
                <h4 class="is-size-6 has-text-centered">{{ game.platform }}</h4>
                <p class="is-size-6 has-text-grey has-text-centered">{{ game.score }}/100</p>

                <router-link v-bind:to="game.get_absolute_url" class="button is-dark mt-4"> Ver juego </router-link>
            </div>

        </div>
    </div>

</template>

<script>
import axios from 'axios'
    export default {
        name:'Platforms-page',
        data() {
            return {
                platforms: [],
                bestGames: [],
                selected_platform: ''
            }
        },
        components: {
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
            getBestGames(platform) {
                axios
                    .get(`http://127.0.0.1:8000/api/games/${platform}`)
                    .then(response => {
                        console.log(response.data)
                        this.bestGames = response.data.games;
                        console.log(this.bestGames)
                        this.selected_platform = response.data.name_desc
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
</script>