import firebase from 'firebase'
import {useApi} from '@/compositions/useApi'
import {UserModule} from '@/store/user'
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
        UserModule.setUser(_user)

        const { Aa } = UserModule.user

        if (store.state.authToken) {
            const { exec, result, error } = useApi({
                method: 'POST',
                url: '/auth/login',
                data: {
                    token: Aa
                },
                headers: {
                    'content-type': 'application/json'
                }
            }, {}, (data) => {
                UserModule.login()
            })
            await exec()
        }
    }
}


const getUserData = async function(){
    const {exec, result, error} = useApi({
        method: 'GET',
        url: '/auth/login',
        // data: _user
    })
    await exec()
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

    const signOut = () => auth.signOut()

    return { signIn, signOut }
}