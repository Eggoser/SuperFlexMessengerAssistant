import firebase from 'firebase'
import {useApi} from '@/compositions/useApi'
import { ref, onUnmounted, computed, watch } from 'vue'
import { UserModule } from '@/store/user'


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
    if (!UserModule.token && _user) {
        const {Aa} = _user
        const { exec, result, error } = useApi({
            method: 'POST',
            url: '/auth/login',
            data: {
                token: Aa
            },
        }, {}, (data) => {
            UserModule.setTokenCookie(data.data)
            UserModule.init()
        })
        await exec()
    }
}


export function useAuth() {
    auth.onAuthStateChanged(async (_user) => {
        await sendAuthData(_user)
    })

    const signIn = async () => {
        const googleProvider = new firebase.auth.GoogleAuthProvider()
        await auth.signInWithPopup(googleProvider)
        await auth.signOut()
    }

    return { signIn }
}