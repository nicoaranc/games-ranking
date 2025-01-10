import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router.js'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)

app.use(router,axios)
app.mount('#app')
