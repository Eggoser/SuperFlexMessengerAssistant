import firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/firestore'

import Filter from 'bad-words'
import { ref, onUnmounted } from 'vue'

//
// const firestore = firebase.firestore()
// const messagesCollection = firestore.collection('messages')
// const messagesQuery = messagesCollection.orderBy('createdAt', 'desc').limit(100)
const filter = new Filter()

export function useChat() {
    const messages = ref([])
    const unsubscribe = messagesQuery.onSnapshot(snapshot => {
        messages.value = snapshot.docs
            .map(doc => ({ id: doc.id, ...doc.data() }))
            .reverse()
    })

    onUnmounted(unsubscribe)

    const { user, isLogin } = useAuth()
    const sendMessage = text => {
        if (!isLogin.value) return
        const { photoURL, uid, displayName } = user.value
        messagesCollection.add({
            userName: displayName,
            userId: uid,
            userPhotoURL: photoURL,
            text: filter.clean(text),
            createdAt: firebase.firestore.FieldValue.serverTimestamp()
        })
    }

    console.log(messages.value)

    return { messages, sendMessage }
}
