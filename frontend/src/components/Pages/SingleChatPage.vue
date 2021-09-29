<template>
    <div class="mx-2">
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
import Message from '@/components/Chat/Message.vue'
import MessageInput from '@/components/Chat/MessageInput.vue'
import { UserModule } from '@/store/user'
import {computed, ref, watch} from 'vue'
import { useApi } from '@/compositions/useApi'


export default {
    components: { Message, MessageInput },
    props: {
        secondUser: Object
    },
    
    setup(props){
        console.log(props.secondUser)
        const { exec, result, error } = useApi({
            method: 'POST',
            url: '/messages',
            data: {
                googleId: props.secondUser.googleId
            }
        }, {})
    
        exec()
    
        const fetchedMessages = computed(() => {
            return result.value
        })
        
        
        return {
            UserModule,
            fetchedMessages
        }
    }
};
</script>

<style>

</style>