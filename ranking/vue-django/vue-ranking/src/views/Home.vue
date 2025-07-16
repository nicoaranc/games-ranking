<template>
    <div class="columns is-multiline">
        <div class="column is-12 mb-4">
            <h2 class="is-size-1 has-text-centered">Mi Ranking de Mejores Juegos</h2>
        </div>
        
        <div class="box columns is-multiline">
            <div class="column is-3" v-for="game in bestGames" v-bind:key="game.id">
                <div class="box has-text-centered fixed-size">
                    <figure class="image mb-3">
                        <img :src="game.get_thumbnail">
                    </figure>

                    <h3 class="is-size-4 has-text-weight-bold">{{ game.name }}</h3>
                    <h4 class="is-size-6">{{ game.platform }}</h4>
                    <p class="is-size-6 has-text-grey">{{ game.score }}/100</p>

                    <router-link v-bind:to="game.get_absolute_url" class="button is-dark mt-4"> Ver juego </router-link>
                </div>
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
        },
    },
}
</script>

<style>
    @import '../assets/styles/box_size.css';
</style>