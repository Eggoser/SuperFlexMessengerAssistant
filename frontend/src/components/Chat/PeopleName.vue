<template>
    <div class="rounded-4 mt-1 background-black mx-1" @click="$emit('set_chat_page', item)">
        <div class="container p-2">
            <div class="d-flex px-2 py-2 align-items-center justify-content-between">
                <div class="d-flex">
                    <img :src="item.avatarUrl" class="avatar-element" alt/>
                    <div class="px-3">
                        <h3 class="text-color-light chat-title">{{ item.name }}</h3>
                        <p class="text-success chat-subtitle">Начните общаться</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { UserModule } from '@/store/user'


export default {
    components: { },
    // props: ["user"],
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