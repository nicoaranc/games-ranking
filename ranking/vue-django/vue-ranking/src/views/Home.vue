<template>
    <div class="home">
        <h1>Mi Ranking de juegos</h1>
    </div>

    <div class="columns is-multiline">
        <div class="column is-12">
            <h2 class="is-size-2 has-text-centered">Mejores juegos</h2>
        </div>
    

        <div class="column is-3" v-for="game in bestGames" v-bind:key="game.id">
            <div class="box">
                <h3 class="is-size-4">{{ game.name }}</h3>
                <p class="is-size-6 has-text-grey">{{ game.score }}</p>
            </div>

        </div>

        <div v-if="bestGames.length === 0">
            <p>No se encontraron juegos.</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'Home-page',
    data() {
        return {
            bestGames: []
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
                .get('http://127.0.0.1:8000/api/games/')
                .then(response => {
                    this.bestGames = response.data;
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>