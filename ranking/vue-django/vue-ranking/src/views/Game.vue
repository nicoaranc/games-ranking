<template>
    <div>
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="game.get_image">
                </figure>

                <h1 class="title">{{ game.name }}</h1>

                <p>{{ game.description }}</p>

            </div>

            <div class="column is-3">
                <p><strong>MyScore: </strong>{{ game.score }}</p>
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
