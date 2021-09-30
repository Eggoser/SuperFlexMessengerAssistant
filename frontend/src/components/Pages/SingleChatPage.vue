<template>
    <div class="chat-header background-black">
        <div class="chat-header__wrapper d-flex justify-content-between">
            <div class="chat-header__block col-2" @click="change_view">
                <img class="chat-header__image" :src="require('@/assets/img/arrow-left.png')" alt="">
            </div>
            <div class="chat-header__block">
                <img :src="secondUser.avatarUrl" class="avatar-element avatar-element__small me-3" alt="">
                <h6 class="text-color-light">{{ secondUser.name }}</h6>
            </div>
            <div class="col-3 chat-header__block pt-2 pb-3">
                <Progress :height="50" name="Карма"/>
            </div>
        </div>
    </div>
    <div class="mx-2 position-relative" id="chat">
        <Message
            v-for="item in fetchedMessages"
            :key="item.id"
            :content="item.content"
            :name="item.googleId === UserModule.user.googleId ? UserModule.user.name : secondUser.name"
            :right="item.googleId === UserModule.user.googleId"
        />
    </div>
    <div class="p-4 my-2"></div>
    <MessageInput :item="secondUser"/>
</template>

<script>
import Progress from '@/components/Chat/Progress.vue'
import Message from '@/components/Chat/Message.vue'
import MessageInput from '@/components/Chat/MessageInput.vue'
import { UserModule } from '@/store/user'
import {computed, ref, watch} from 'vue'
import { useApi } from '@/compositions/useApi'
import { useWebsocket } from '@/compositions/useWebsocket'


export default {
    components: { Message, MessageInput, Progress },
    props: {
        secondUser: Object
    },
    
    methods: {
        change_view(){
            this.$emit("change_view")
            // this.$vfm.show("test")
            
            console.log("chat view")
        }
    },
    
    setup(props){
        const { exec, result, error } = useApi({
            method: 'POST',
            url: '/messages',
            data: {
                googleId: props.secondUser.googleId
            }
        }, {})
        const scrollChats = () => {
            setTimeout(() => {
                window.scrollBy(0, 10000)
            }, 100)
        }
        exec()
    
        watch(result, scrollChats)
        
    
        const fetchedMessages = computed(() => {
            return result.value
        })
    
    
        const connection = useWebsocket()
    
        connection.onopen = (event) => {
            connection.send(JSON.stringify({
                googleId: UserModule.user.googleId
            }))
        }
    
        connection.onmessage = (event) => {
            console.log("message")
            exec()
            scrollChats()
        }
        
        
        return {
            UserModule,
            fetchedMessages
        }
    }
};
</script>

<style lang="scss">
.chat-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1999;
    height: 70px;
    
    &__wrapper {
        width: 100%;
        height: 70px;
        position: relative;
    }
    
    &__block {
        height: 100%;
        justify-content: center;
        align-items: center;
        display: flex;
        position: relative;
    }
    
    &__image {
        width: 32px;
    }
}
</style>