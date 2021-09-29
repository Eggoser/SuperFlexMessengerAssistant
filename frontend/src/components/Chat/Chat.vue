<template>
    <div class="container-sm mt-20">
        <div class="mx-5">
<!--            <Message-->
<!--                v-for="{ id, text, userPhotoURL, userName, userId } in messages"-->
<!--                :key="id"-->
<!--                :name="userName"-->
<!--                :photo-url="userPhotoURL"-->
<!--                :sender="userId === user?.uid"-->
<!--            >-->
<!--                {{ text }}-->
<!--            </Message>-->
        </div>
    </div>

    <div ref="bottom" class="mt-20" />

    <div class="bottom">
        <div class="container-sm">
            <form v-if="UserModule.user" @submit.prevent="send">
                <input v-model="message" placeholder="Message" required />
                <button type="submit">
                    <SendIcon />
                </button>
            </form>
        </div>
    </div>
</template>

<script>
import { ref, watch, nextTick } from 'vue'
import {UserModule} from '@/store/user'

// import Message from './Message.vue'

export default {
    components: {},
    setup() {
        return {
            UserModule
        }
    }
}
</script>
