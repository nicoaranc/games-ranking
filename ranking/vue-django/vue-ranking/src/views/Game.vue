<template>
    <div class="columns">
        <div class="column">
            <h1 class="title">{{ game.name }}</h1>
            <div class="columns">
                <div class="column is-4 ">
                    <figure class="image mb-6">
                        <img v-bind:src="game.get_image">
                        <br>
                        <p class="has-text-centered"><strong>MyScore: </strong>{{ game.score }}/100</p>
                        <p class="has-text-centered"><strong>Platform: </strong>{{ game.platform }}</p>
                    </figure>
                </div>
                <div class="column">
                    <p class="has-text-centered">Descripción</p>
                    <br>
                    <p class="has-text-centered">

                            {{ game.description }}

                    </p>
                </div>
            </div>

        </div>
        <div class="column has-text-centered">
            <h1 class="title">Video/Trailer</h1>
            <iframe width="560" 
            height="315" 
            v-bind:src="game.video" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
    </div>
    <div class="box has-text-centered">
        <h1 class="title">Más juegos de {{ game.platform }}</h1>
        <br>
        <div class="columns is-multiline has-text-centered">
            <div class="column is-3" v-for="game_p in bestGames" v-bind:key="game_p.id">
                <div class="box">
                    <figure class="image mb-4">
                        <img :src="game_p.get_thumbnail">
                    </figure>

                    <h3 class="is-size-4 has-text-centered">{{ game_p.name }}</h3>
                    <h4 class="is-size-6 has-text-centered">{{ game_p.platform }}</h4>
                    <p class="is-size-6 has-text-grey has-text-centered">{{ game_p.score }}/100</p>

                    <router-link v-bind:to="game_p.get_absolute_url" class="button is-dark mt-4"> Ver juego </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Game-page',
    data() {
        return {
            game: {},
            quantity: 1,
            bestGames: []
        }
    },
    mounted() {
        this.getGame()
        
    },
    methods: {
        getGame() {
            const platform_slug = this.$route.params.platform_slug
            const game_slug = this.$route.params.game_slug
            
            axios
                .get(`http://127.0.0.1:8000/api/games/${platform_slug}/${game_slug}`)
                .then(response => {
                    this.game = response.data
                    this.getBestPlatformGames()
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getBestPlatformGames() {
            const platform_slug = this.$route.params.platform_slug

            axios
                .get(`http://127.0.0.1:8000/api/games/${platform_slug}/`)
                .then(response => {
                    this.bestGames = response.data.games
                    this.deleteMainGame()
                })
                .catch(error => {
                    console.log(error)
                })
        },
        deleteMainGame() {
            for (let i = 0; i < this.bestGames.length; i++){
                if (this.bestGames[i].id == this.game.id) {
                    this.bestGames.splice(i,1)
                    break
                }
            }
        }
    }
}
</script>
