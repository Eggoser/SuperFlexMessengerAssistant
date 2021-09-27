import {
    getModule,
    VuexModule,
    Mutation,
    Action,
    Module
} from 'vuex-module-decorators';
import {plainToClass} from "class-transformer";
import {UserType} from '@/types/user'
import { store } from '.';
import { useApi } from '@/compositions/useApi'
import { useCookie } from '@/compositions/useCookie'


@Module({ dynamic: true, store, name: 'User' })
class User extends VuexModule {
    user = null
    token = null

    @Mutation
    setUser(value) {
        this.user = value
    }

    @Mutation
    setToken(value){
        this.token = value
    }

    @Mutation
    setTokenCookie({value, expiresIn}){
        this.token = value
        const cookie = useCookie()
        cookie.set("token", value, expiresIn)
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
            console.log("setting user")
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
