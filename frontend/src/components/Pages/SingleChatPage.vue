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
    <div class="mx-2 position-relative mt-3" id="chat">
        <div class="d-flex justify-content-center align-items-center w-100 placeholder-height-100 overflow-hidden" v-if="!fetchedMessages">
            <Placeholder
                title="Сообщений нет"
                class="text-color-dark"
            />
        </div>
        
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
    <Modal
        v-if="showModalFlag"
        :item="showModalFlag"
        @modal_keypress="modal_keypress($event)"
    />
</template>

<script>
import Placeholder from '@/components/Chat/Placeholder.vue'
import Progress from '@/components/Chat/Progress.vue'
import Message from '@/components/Chat/Message.vue'
import Modal from "@/components/Modal.vue"
import MessageInput from '@/components/Chat/MessageInput.vue'
import { UserModule } from '@/store/user'
import {useWebsocket} from '@/compositions/useWebsocket'
import {computed, ref, watch} from 'vue'


export default {
    components: { Message, MessageInput, Progress, Modal, Placeholder },
    props: {
        secondUser: Object
    },
    
    methods: {
        change_view(){
            this.$emit("change_view")
        }
    },
    
    
    mounted() {
        setTimeout(this.scrollChats, 300)
    },
    
    setup(props){
        const {sendMessage} = useWebsocket()
    
        const modal_keypress = (val) => {
            const value = val.value
        
            if (value === 1){
                const {googleId, message} = UserModule.modalContent
            
                sendMessage({googleId, message}, true)
            }
            UserModule.setModalContent(null)
        }
        
        const scrollChats = () => {
            setTimeout(() => {
                window.scrollBy(0, 10000)
            }, 100)
        }
        
        const fetchedMessages = computed(() => {
            return UserModule.messages[props.secondUser.googleId]
        })
        
        
        const showModalFlag = computed(() => {
            return UserModule.modalContent
        })
        
        
        // важно ставить watch после функции
        watch(fetchedMessages, scrollChats)
        
        
        return {
            UserModule,
            fetchedMessages,
            showModalFlag,
            scrollChats,
            modal_keypress
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