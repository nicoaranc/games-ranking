<template>
    <div class="home">
        <h1>Mi Ranking de juegos</h1>
    </div>
    <div>
        <div>
            <h2>Mejores juegos</h2>
        </div>
        <div 
        v-for="game in Games"
        v-bind:key="game.id"
        >
        <h3>{{ game.name }}</h3>
        <p>{{ game.score }}</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'Home-page',
    data() {
        return {
            Games: []
        }
    },
    components: {
    },
    mounted() {
        this.getBestGames()
    },
    methods: {
        getBestGames() {
            axios
                .get('/api/games/')
                .then(response => {
                    this.Games = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>