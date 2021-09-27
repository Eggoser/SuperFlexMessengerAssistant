import { createApp } from 'vue'

import {store} from './store'
import { VueCookieNext } from 'vue-cookie-next'


import App from './App.vue'

import './main.css'


createApp(App, store).use(VueCookieNext).use(store).mount('#app')


// import {beforeLoad} from "@/libs/beforeLoad"
// beforeLoad().then()


// console.log(useCookie().set("titlle", "adfasdf", 234234))


// export default app
