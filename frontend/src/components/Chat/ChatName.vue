<template>
    <div class="rounded-4 mt-1 background-black mx-1" @click="$emit('set_chat_page', item.member)">
        <div class="container p-2">
            <div class="d-flex px-2 py-2 align-items-center justify-content-between">
                <div class="d-flex">
                    <img :src="item.member.avatarUrl" class="avatar-element" alt/>
                    <div class="px-3">
                        <h3 class="text-color-light chat-title">{{ item.member.name }}</h3>
                        <p class="text-color-dark chat-subtitle">{{ item.last_message.content }}</p>
                    </div>
                </div>
<!--                <div class="d-flex justify-content-center align-items-center col-1">-->
<!--                    <div class="badge">1</div>-->
<!--                </div>-->
            </div>
        </div>
    </div>
</template>

<script>
import { UserModule } from '@/store/user'


export default {
    components: { },
    props: {
        item: Object
    },

    setup(){
        return {
            UserModule
        }
    }
};
</script>

<style>

</style>