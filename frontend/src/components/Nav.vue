<template>
    <nav>
        <div>
            <h1><strong>Vue</strong> Chat App</h1>

            <div v-if="UserModule.user" class="login">
                <Avatar :src="UserModule.user.avatarUrl" />
                <button class="text-gray-400 hover:text-white" @click="signOut">
                    Sign Out
                </button>
            </div>

            <button v-else class="bg-green-500 hover:bg-green-600" @click="signIn">
                Sign in
            </button>
        </div>
    </nav>
</template>

<script>
import Avatar from './Avatar.vue'
import {UserModule} from '@/store/user'
import {useAuth} from '@/compositions/useAuth'


export default {
    components: { Avatar },
    setup() {
        const { signIn } = useAuth()
        return { signIn, UserModule }
    }
}
</script>
