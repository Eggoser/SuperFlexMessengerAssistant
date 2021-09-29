<template>
    <div class="btn-menu-item">
        <div class="btn-menu-item__container">
            <div class="btn-menu-item__icon">
                <img :src="src" class="btn-menu-item__icon" alt="">
            </div>
        </div>
        <div class="btn-menu-item__container ms-3">
            <span class="text-color-light">{{ title }}</span>
        </div>
    </div>
</template>

<script>
import {UserModule} from '@/store/user'

export default {
    name: 'BurgerMenuItem',
    props: {
        src: String,
        title: String
    },
    setup(props){
        console.log(props.src)
        return {
            UserModule
        }
    }
}
</script>

<style lang="scss">
.btn-menu-item {
    position: relative;
    padding: 0 30px 0 16px;
    display: flex;
    height: 50px;
    cursor: pointer !important;
    pointer-events: all !important;
    white-space: nowrap;
    font-size: 16px;
    
    
    &__icon {
        height: 24px;
        //width: 24px;
        display: block;
        padding: 0 2px;
    }
    
    &__container {
        display: flex;
        align-items: center;
    }
    
}

</style>