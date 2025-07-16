<template>
    <div class="columns is-multiline">
        <div class="column is-12 mb-4">
            <h2 class="is-size-1 has-text-centered">Mi Ranking de Mejores Juegos</h2>
        </div>
        
        <div class="box columns is-multiline">
            <div class="column is-3" v-for="game in visibleGames" v-bind:key="game.id">
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
            <button id="prevButton" v-on:click="prevPage()" class="button is-dark mt-4" :disabled="disPrevButton">Previo</button>
            <button id="nextButton" v-on:click="nextPage()" class="button is-dark mt-4" :disabled="disNextButton">Siguiente</button>
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
        }
    },
}
</script>

<style>
    @import '../assets/styles/box_size.css';

    #nextButton {
        position: relative;
        margin-left: auto;
    }

</style>