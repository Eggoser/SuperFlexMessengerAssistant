<template>
    <div>
        <nav class="position-fixed w-100">
            <div class="d-flex justify-content-between background-black">
                <div class="nav-block" @click="burgerMenuLeftController">
                    <div class="animated-menu-icon"></div>
                </div>
                
                <div class="col-5 d-flex justify-content-center align-items-center">
                    <img :src="require('@/assets/img/logo.png')" class="main-logo" alt="">
                </div>
                
                <div v-if="UserModule.user" class="nav-block">
                    <img :src="UserModule.user.avatarUrl" @click="burgerMenuRightController" alt class="avatar-element avatar-element__small"/>
                </div>
                <div v-else class="col-3 standard-block">
                    <a class="text-color-light" @click="signIn">
                        Sign in
                    </a>
                </div>
            </div>
            <div class="d-flex justify-content-between background-black">
    
            </div>
            <burger-menu v-show="showBurgerMenuLeft" class="btn-menu__bottom-left">
                <burger-menu-item
                    :src="require('@/assets/img/person.png')"
                    :title="'Люди'"
                    @click="showPeople()"
                />
                <burger-menu-item
                    :src="require('@/assets/img/chat.png')"
                    :title="'Чаты'"
                    @click="showChats()"
                />
            </burger-menu>
            <burger-menu v-show="showBurgerMenuRight" class="btn-menu__bottom-right">
                <burger-menu-item
                    :src="require('@/assets/img/logout.png')"
                    :title="'Выйти'"
                    @click="modifiedLogout()"
                />
            </burger-menu>
        </nav>
        <div class="padding-simple"></div>
    </div>
</template>

<script>
import {ref, computed} from 'vue'
import BurgerMenu from '@/components/BurgerMenu/BurgerMenu.vue'
import BurgerMenuItem from '@/components/BurgerMenu/BurgerMenuItem.vue'
import {UserModule} from '@/store/user'
import {useAuth} from '@/compositions/useAuth'


export default {
    components: { BurgerMenu, BurgerMenuItem },
    methods: {
        showPeople() {
            this.$emit("show_page", 0)
            this.disableWindows()
        },
        showChats() {
            this.$emit("show_page", 1)
            this.disableWindows()
        },
    },
    emits: ["show_page"],
    setup() {
        const showBurgerMenuLeft = ref(false)
        const showBurgerMenuRight = ref(false)
        
        const burgerMenuLeftController = () => {
            showBurgerMenuLeft.value = !showBurgerMenuLeft.value
            showBurgerMenuRight.value = false
        }
        const burgerMenuRightController = () => {
            showBurgerMenuRight.value = !showBurgerMenuRight.value
            showBurgerMenuLeft.value = false
        }
        
        const disableWindows = () => {
            showBurgerMenuLeft.value = false
            showBurgerMenuRight.value = false
        }
        
        const modifiedLogout = () => {
            UserModule.logout()
            disableWindows()
        }
        
        const { signIn } = useAuth()
        return {
            signIn,
            UserModule,
            showBurgerMenuLeft,
            showBurgerMenuRight,
            burgerMenuLeftController,
            burgerMenuRightController,
            disableWindows,
            modifiedLogout,
        }
    }
}
</script>

<style>
.nav-block {
    position: relative;
    width: 60px;
    height: 60px;
    flex: 0 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
}


nav {
    z-index: 999;
    top: 0
}

.padding-simple {
    height: 60px;
}
</style>