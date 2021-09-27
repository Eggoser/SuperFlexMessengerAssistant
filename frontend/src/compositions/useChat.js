import Filter from 'bad-words'
import { useApi } from '@/compositions/useApi'
import { useAuth } from '@/compositions/useAuth'


const filter = new Filter()


export function useChat() {
    const messages = ref([])

    const { user, isLogin } = useAuth()
    const sendMessage = async text => {
        if (!isLogin.value) return
        const { photoURL, uid, displayName } = user.value


        const {exec, result, error} = useApi({
            method: 'post',
            url: '/send_message',
            data: {
                userName: displayName,
                userId: uid,
                userPhotoURL: photoURL,
                text: text,
            }
        })
        await exec()
    }

    const fetchMessages = async () => {
        const {exec, result, error} = useApi({
            method: 'get',
            url: '/messages',
        })
        await exec()
    }

    const cleanText = (text) => {
        return filter.clean(text)
    }

    return { messages, sendMessage }
}
