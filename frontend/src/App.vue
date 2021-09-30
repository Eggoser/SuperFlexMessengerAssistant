<template>
    <Nav @show_page="setNewPage"/>
<!--    <Modal/>-->
    <ContentView v-if="UserModule.user" :page_number="nowPageGlobal" :update_count="updateCount"/>
</template>

<script>
import Nav from '@/components/Nav.vue'
import Modal from "@/components/Modal.vue"
import ContentView from '@/components/Content.vue'
import {UserModule} from '@/store/user'
import {ref} from 'vue'


export default {
    name: 'App',
    components: {
        Nav,
        ContentView,
        // Modal
    },
    mounted() {
    
    },
    setup(){
        const nowPageGlobal = ref(1)
        const updateCount = ref(0)
        const setNewPage = (e) => {
            nowPageGlobal.value = e
            updateCount.value ++
        }
        return {
            nowPageGlobal,
            updateCount,
            UserModule,
            setNewPage
        }
    }
}
</script>
