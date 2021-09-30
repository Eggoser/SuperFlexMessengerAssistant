<template>
    <people-page v-if="page_number_global === 0"/>
    <chat-page v-if="page_number_global === 1"/>
</template>

<script>
import ChatPage from '@/components/Pages/ChatPage.vue'
import PeoplePage from '@/components/Pages/PeoplePage'
import { UserModule } from '@/store/user'
import {computed, ref, watch} from 'vue'


export default {
    components: { ChatPage, PeoplePage },
    props: {
        page_number: Number,
        update_count: Number
    },
    
    watch: {
        // при изменении update_count
        update_count: function(newwal, oldwal) {
            const old_page_number = this.page_number
            this.page_number_global = 32
            console.log('lick')
            this.$nextTick(() => {
                this.page_number_global = old_page_number
            })
        }
    },
    
    setup(props){
        const page_number_global = ref(1)
        
        return {
            UserModule,
            page_number_global
        }
    }
};
</script>

<style>

</style>