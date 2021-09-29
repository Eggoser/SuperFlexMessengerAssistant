<template>
    <div class="btn-menu ">
        <slot/>
    </div>
</template>

<script>
export default {
name: "BurgerMenu"
}
</script>

<style lang="scss">
.btn-menu {
    position: absolute;
    transform: scale3d(1, 1, 1);
    box-shadow: 0 2px 8px 1px rgba(0, 0, 0, .24);
    z-index: 3;
    border-radius: 10px;
    //width: 300px;
    //height: 300px;
    
    
    &__bottom-left {
        left: 4px;
        top: 60px
    }
    
    &__bottom-right {
        right: 4px;
        top: 60px
    }
}



</style>