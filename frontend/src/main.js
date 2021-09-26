import Vue, { createApp } from 'vue'
import store from './store'
import App from './App.vue'

import './main.css'


createApp(App, store).use(store).mount('#app')
