import { createApp } from 'vue'
import {store} from './store'


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import '@/assets/main.scss'

import App from './App.vue'



import {beforeLoad} from "@/libs/beforeLoad"
beforeLoad().then(() => {
    const app = createApp(App, store)

    // app.use(VModal)
    app.use(store).mount('#app')
})



// console.log(useCookie().set("titlle", "adfasdf", 234234))


// export default app
