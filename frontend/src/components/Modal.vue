<template>
    <div class="main-modal__container">
        <div class="main-modal__dark w-100 h-100"></div>
        <div class="main-modal__content background-black card rounded-5">
            <h5 class="text-color-light">Вы уверены, что хотите отправить сообщение?</h5>
            <div class="d-flex justify-content-between mt-4">
                <button class="btn btn-danger" @click="$emit('modal_keypress', {value: 0})">Нет</button>
                <button class="btn btn-success" @click="$emit('modal_keypress', {value: 1})">Да</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    methods: {},
    mount () {
        this.show()
    }
}
</script>

<style lang="scss">
    .main-modal {
        &__container {
            position: fixed;
            display: flex;
            width: 100%;
            height: 100%;
            justify-content: center;
            align-items: center;
        }
        
        &__dark {
            position: absolute;
            left: 0;
            background-color: rgba(0, 0, 0, .4);
            z-index: 3000;
        }
        
        &__content {
            display: flex;
            z-index: 4000;
            padding: 15px 25px;
            width: 80%;
        }
    }
</style>