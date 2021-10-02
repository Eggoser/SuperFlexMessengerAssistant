<template>
    <div class="d-flex" v-if="fetchedChats.length">
        <div class="mt-3 w-100" :class="showChat ? 'chat-block-max d-md-block d-none': ''">
            <PeopleName
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
    <div class="d-flex justify-content-center align-items-center w-100 placeholder-height-100 overflow-hidden" v-else>
        <Placeholder
            title="Нет людей для переписки"
            class="text-color-dark"
        />
    </div>
</template>

<script>
import Placeholder from '@/components/Chat/Placeholder'
import PeopleName from '@/components/Chat/PeopleName'
import SingleChatPage from '@/components/Pages/SingleChatPage'
import { UserModule } from '@/store/user'
import { computed, ref } from 'vue'
import { useApi } from '@/compositions/useApi'


export default {
    components: { PeopleName, SingleChatPage, Placeholder },
    
    setup(){
        const showChat = ref(false)
        const chatUserObject = ref({})
        
        // const { exec, result, error } = useApi({
        //     method: 'GET',
        //     url: '/users',
        // }, {})
        
        const changeView = () => {
            showChat.value = false
            // exec()
        }
        
        // exec()
        
        const fetchedChats = computed(() => {
            return UserModule.users
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