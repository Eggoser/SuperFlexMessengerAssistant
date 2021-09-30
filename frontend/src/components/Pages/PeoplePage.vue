<template>
    <div class="mt-3" v-if="!showChat">
        <PeopleName
            v-for="item in fetchedChats"
            :key="item.id"
            :item="item"
            @set_chat_page="setChatPage"
        />
    </div>
    <SingleChatPage @change_view="changeView"
        v-else
        :second-user="chatUserObject"
    />
</template>

<script>
import PeopleName from '@/components/Chat/PeopleName'
import SingleChatPage from '@/components/Pages/SingleChatPage'
import { UserModule } from '@/store/user'
import { computed, ref } from 'vue'
import { useApi } from '@/compositions/useApi'


export default {
    components: { PeopleName, SingleChatPage },
    
    setup(){
        const showChat = ref(false)
        const chatUserObject = ref({})
        
        const { exec, result, error } = useApi({
            method: 'GET',
            url: '/users',
        }, {})
        
        const changeView = () => {
            showChat.value = false
            exec()
        }
        
        exec()
        
        const fetchedChats = computed(() => {
            return result.value
        })
    
        const setChatPage = (e) => {
            showChat.value = true
            chatUserObject.value = e
        }
        
        return {
            UserModule,
            fetchedChats,
            showChat,
            changeView,
            chatUserObject,
            setChatPage
        }
    }
};
</script>

<style>

</style>