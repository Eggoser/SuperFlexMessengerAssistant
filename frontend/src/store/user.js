import {
    getModule,
    VuexModule,
    Mutation,
    Action,
    Module,
    MutationAction
} from 'vuex-module-decorators'
import {plainToClass} from "class-transformer";
import {connectSocket} from '@/compositions/useWebsocket'
import {UserType} from '@/types/user'
import { store } from '.';
import { useApi } from '@/compositions/useApi'
import { useCookie } from '@/compositions/useCookie'


@Module({ dynamic: true, store, name: 'User' })
class User extends VuexModule {
    user = null
    token = null
    modalContent = null
    messages = {}
    chats = []
    users = []

    @Mutation
    setUsers(value){
        this.users = value
    }

    @Mutation
    setMessageById({googleId, messages}){
        this.messages[googleId] = messages
    }

    @Mutation
    setModalContent(value){
        this.modalContent = value
    }

    @Mutation
    setChats(value){
        this.chats = value
    }

    @Mutation
    setUser(value) {
        this.user = value
    }

    @Mutation
    setToken(value){
        this.token = value
        connectSocket()
    }

    @Mutation
    setTokenCookie({token, expire}){
        this.token = token
        const cookie = useCookie()
        cookie.set("token", token, expire)
    }
    @Action
    async getToken(){
        const cookie = useCookie()

        const token = cookie.get("token")
        this.setToken(token)
    }

    @Action
    async init(){
        await this.getToken()
        if (this.token) {
            await this.fetchUser()
        }
    }

    @Action
    async fetchUser(){
        const {exec, result, error} = useApi(
            {
                method: "GET",
                url: "/user"
            }, {},
            (data) => {
                return plainToClass(UserType, data.data)
            }
        )
        await exec()

        if (!error.value) {
            this.setUser(result.value)
        } else {
            this.setUser(null)
            this.removeToken()
        }
    }

    @Action
    removeToken() {
        const cookie = useCookie()
        cookie.remove("token")
        this.setToken(null)
    }

    @Action
    logout() {
        this.removeToken()
        this.setUser(null)
    }
}

export const UserModule = getModule(User)
