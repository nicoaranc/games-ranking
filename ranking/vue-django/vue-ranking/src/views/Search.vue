<template>
    <div class="page-search">
        <div>
            <div class="has-text-centered">
                <h1 class="title">Búsqueda</h1>

                <form @submit.prevent="searchGame">
                    <input class="input" v-model="query" placeholder="Juego a buscar" required/>
                    <button class="button is-primary input" type="submit">Buscar</button>
                </form>

                <br>
                <br>
                
                <div class="box has-text-centered" v-if="games.length != 0">
                    <h2 class="is-size-2 title"> Resultados para "{{ final_query }}" </h2>
                    <br>
                    <div class="columns is-multiline has-text-centered">
                        <div class="column is-3" v-for="game_p in games" v-bind:key="game_p.id">
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
            </div>
        </div>
        
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'Search-page',
    data() {
        return {
            games: [],
            query: '',
            final_query: ''
        }
    },
    components: {
    },
    methods: {
        searchGame() {
            axios
                .post('/api/search/', {'query': this.query})
                .then(response => {
                    console.log(response.data)
                    this.games = response.data
                    this.final_query = this.query
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>