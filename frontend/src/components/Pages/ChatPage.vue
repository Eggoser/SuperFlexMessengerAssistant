<template>
    <div class="mt-3" v-if="showChatList">
        <ChatName
            v-for="item in fetchedChats"
            :key="item.id"
            :item="item"
            @set_chat_page="setChatPage"
        />
    </div>
    <SingleChatPage
        v-else
        :second-user="chatUserObject"
    />
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
        const showChatList = ref(true)
        const chatUserObject = ref({})
        
        const { exec, result, error } = useApi({
            method: 'GET',
            url: '/chats',
        }, {})
        
        exec()
        
        const fetchedChats = computed(() => {
            return result.value
        })
        
        const setChatPage = (e) => {
            showChatList.value = false
            chatUserObject.value = e
        }
        
        return {
            UserModule,
            fetchedChats,
            showChatList,
            chatUserObject,
            setChatPage
        }
    }
};
</script>

<style>

</style>