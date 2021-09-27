import {
    getModule,
    VuexModule,
    Mutation,
    Action,
    Module
} from 'vuex-module-decorators';
import { store } from '.';
import {useApi} from '@/compositions/useApi'
import useCookie from '@/compositions/useCookie'


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
    setTokenCookie(value, expiresIn){
        this.token = value
        const cookie = useCookie()
        cookie.set("token", value, expiresIn)
    }

    @Action
    async init(){
        this.getToken()
        const {exec, result, error} = useApi(
            {
                method: "GET",
                url: "user"
            }
        )

        await exec()
    }

    @Action
    fetchUser(){

    }

    @Mutation
    getToken(){
        const cookie = useCookie()
        const token = cookie.get("token")
        this.setToken(token)
    }

    @Mutation
    removeToken() {
        const cookie = useCookie()
        cookie.remove("token")
        this.setToken(null)
    }

    @Mutation
    logout() {
        this.removeToken()
        this.setUser(null)
    }
}

export const UserModule = getModule(User)
