<template>
    <div class="columns is-multiline">
        <div class="column is-12 mb-4">
            <h2 class="is-size-1 has-text-centered">Mi Ranking de Mejores Juegos</h2>
        </div>
        
        <div id="game-container" class="box columns is-multiline">
            <div class="column is-3" v-for="game in visibleGames" v-bind:key="game.id">
                <div class="box has-text-centered fixed-size">
                    <figure class="image mb-3">
                        <img :src="game.get_thumbnail">
                    </figure>

                    <h3 class="is-size-5 has-text-weight-bold">{{ game.name }}</h3>
                    <h4 class="is-size-6">{{ game.platform }}</h4>
                    <p class="is-size-6 has-text-grey">{{ game.score }}/100</p>

                    <router-link v-bind:to="game.get_absolute_url" class="button is-dark mt-4"> Ver juego </router-link>
                </div>
            </div>
        </div>

        <button id="prev-button" v-on:click="prevPage()" class="button is-dark mt-4" :disabled="disPrevButton">Anterior</button>
        <!-- <p id="page-index" class="mt-5">Página actual: {{ currentPage + 1 }}</p> -->
        <button id="next-button" v-on:click="nextPage()" class="button is-dark mt-4" :disabled="disNextButton">Siguiente</button>

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
            disPrevButton: true,
            disNextButton: true,
            currentPage: 0,
            perPage: 12,
            bestGames: [],
            visibleGames: []
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
                    this.updateVisibleGames()
                })
                .catch(error => {
                    console.log(error)
                })
        },
        updateVisibleGames() {
            this.visibleGames = this.bestGames.slice(this.currentPage * this.perPage, (this.currentPage * this.perPage) + this.perPage)
            this.setButtons()
            this.autoScroll()
        },
        prevPage() {
            this.currentPage -= 1;
            this.updateVisibleGames()
        },
        nextPage() {
            this.currentPage += 1;
            this.updateVisibleGames()
        },
        setButtons() {
            if (this.currentPage == 0){
                this.disPrevButton = true;
            }
            if (this.currentPage > 0){
                this.disPrevButton = false;
            }
            if ((this.currentPage * this.perPage) + this.perPage < this.bestGames.length){
                this.disNextButton = false;
            }
            if ((this.currentPage * this.perPage) + this.perPage >= this.bestGames.length){
                this.disNextButton = true;
            }
        },
        autoScroll() {
            window.scroll({
                top: 0,
                left: 0,
                behaviour: "smooth", 
            })
        }
    },
}
</script>

<style>
    @import '../assets/styles/box_size.css';

    #next-button {
        margin-left: auto;
    }

    #game-container {
        width: 100%;
    }

    #page-index {
        margin-left: 39%;
    }

</style>