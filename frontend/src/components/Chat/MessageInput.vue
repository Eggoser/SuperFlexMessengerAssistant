<template>
    <div class="message-input__container background-absolute-black">
        <div class="message-input">
            <form class="w-100 d-flex justify-content-between" @submit.prevent="submitForm">
                <div class="w-100">
                    <input
                        type="text"
                        placeholder="Сообщение"
                        v-model="formValue"
                        class="message-input__field background-black w-full px-3 py-2 rounded-4"
                        spellcheck="false"
                        autocomplete="false"
                    />
                </div>
                <img class="message-input__send" @click="submitForm" :src="require('@/assets/img/send.png')" alt>
            </form>
        </div>
    </div>
</template>

<script>
import {ref, watch, toRefs} from 'vue'
import { useApi } from '@/compositions/useApi'

export default {
    props: {
        item: Object
    },
    setup(props){
        const formValue = ref("")
        
        const submitForm = (e) => {
            console.log(props)
            if (formValue.value){
                const {exec, result, error} = useApi({
                    method: "POST",
                    url: "/send_message",
                    data: {
                        message: formValue.value,
                        googleId: props.item.googleId
                    }
                })
                
                exec()
                
                formValue.value = ""
            }

            e.preventDefault();
        }
        
        return {
            submitForm,
            formValue
        }
    }
}
</script>

<style lang="scss">
.message-input {
    position: relative;
    display: flex;
    width: 100%;
    align-items: flex-end;
    justify-content: space-between;
    
    &__container {
        height: 50px;
        width: 100%;
        position: fixed;
        bottom: 0;
        padding: 5px 5px;
    }
    
    &__field {
        width: 100%;
        border: none;
    }
    
    &__field:focus-visible {
        border: none;
        outline: none;
    }
    
    &__send {
        margin: 0 1rem;
        width: 30px;
    }
}
</style>