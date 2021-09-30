<template>
    <div class="d-flex">
        <div class="mt-3 w-100" :class="showChat ? 'chat-block-max d-md-block d-none': ''">
            <ChatName
                v-for="item in fetchedChats"
                :key="item.id"
                :item="item"
                @set_chat_page="setChatPage"
            />
        </div>
        <div class="w-100" v-if="showChat">
            <SingleChatPage @change_view="changeView"
                :second-user="chatUserObject"
            />
        </div>
    </div>
</template>

<script>
import ChatName from '@/components/Chat/ChatName'
import SingleChatPage from '@/components/Pages/SingleChatPage'
import { UserModule } from '@/store/user'
import { computed, ref } from 'vue'
import { useApi } from '@/compositions/useApi'


export default {
    components: { ChatName, SingleChatPage },
    
    setup(){
        const showChat = ref(false)
        const chatUserObject = ref({})
        
        const { exec, result, error } = useApi({
            method: 'GET',
            url: '/chats',
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
.chat-block-max {
    max-width: 400px;
}
</style>