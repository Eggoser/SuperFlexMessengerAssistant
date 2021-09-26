import firebase from 'firebase'
import {useApi} from '@/compositions/useApi'
import { ref, onUnmounted, computed } from 'vue'


firebase.initializeApp({
    apiKey: "AIzaSyASdoY79gcrVOtqazDvi7HHX_EK1bTeYnE",
    authDomain: "chat-levkovo.firebaseapp.com",
    projectId: "chat-levkovo",
    storageBucket: "chat-levkovo.appspot.com",
    messagingSenderId: "226695678832",
    appId: "1:226695678832:web:173f235245a232daf71db5",
    measurementId: "G-P558HHGX3P"
})

const auth = firebase.auth()

const sendAuthData = async function(_user) {
    if (_user){
        console.log(_user)
        const {exec, result, error} = useApi({
            method: 'GET',
            url: '/auth/login',
            // data: _user
        })
        await exec()
    }
}


export function  useAuth() {
    const user = ref(null)
    const unsubscribe = auth.onAuthStateChanged(async (_user) => {
        user.value = _user
        await sendAuthData(_user)
    })
    // onUnmounted(unsubscribe)
    const isLogin = computed(() => user.value !== null)

    const signIn = async () => {
        const googleProvider = new firebase.auth.GoogleAuthProvider()
        await auth.signInWithPopup(googleProvider)
    }
    const signOut = () => auth.signOut()

    return { user, isLogin, signIn, signOut }
}