import { createApp } from 'vue'

import {store} from './store'
// import { VueCookieNext } from 'vue-cookie-next'


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import '@/assets/main.scss'

import App from './App.vue'



import {beforeLoad} from "@/libs/beforeLoad"
beforeLoad().then(() => {
    createApp(App, store).use(store).mount('#app')
})



// console.log(useCookie().set("titlle", "adfasdf", 234234))


// export default app
