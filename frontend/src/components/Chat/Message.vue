<template>
    <div class="message mt-2" :class="right ? 'message__right-parent' : 'message__left-parent'">
        <div class="message__child" :class="right ? 'message__right' : 'message__left'">
            <div class="message__header">
                {{ name }}
            </div>
            <div class="message__content">
                {{ content }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        right: Boolean,
        content: String,
        name: String
    }
}
</script>

<style lang="scss">
.message {
    display: flex;
    
    //max-width: calc(100% - 5.5625rem);
    
    &__header {
        padding: 5px 9px 0 9px;
        font-weight: 500 !important;
        font-size: .9rem;
        color: rgb(252, 92, 81);
    }
    &__child {
        position: relative;
        border-radius: 6px 12px 12px 6px;
        //display: flex;
        max-width: calc(100% - 5.5625rem);
    }
    &__content {
        padding: 0 .5rem .375rem .625rem;
        line-height: 1.3125;
        word-break: break-word;
        white-space: pre-wrap;
    }
    
    &__left-parent {
        justify-content: flex-start;
    }
    
    &__right-parent {
        justify-content: flex-end;
    }
}
</style>