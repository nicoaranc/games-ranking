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
</template>

<script>
import axios from 'axios'

export default {
    name: 'Game-page',
    data() {
        return {
            game: {},
            quantity: 1
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
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>
