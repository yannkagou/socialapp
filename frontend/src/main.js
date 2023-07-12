import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App)

axios.defaults.baseURL='http://localhost:8000'
axios.defaults.withCredentials = true

app.use(createPinia())
app.use(router, axios)

app.mount('#app')
