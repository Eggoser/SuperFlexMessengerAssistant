import {UserModule} from '@/store/user'

const socketUrl = process.env.NODE_ENV === 'production' ? "wss://ucabix.com:5050" : "ws://localhost:5050"

const messageTypes = ["users", "chats"]


const socket = {
    socket: null
}

export function connectSocket(func= null){
    socket.socket = new WebSocket(socketUrl)

    socket.socket.onopen = () => {
        if (socket.socket.readyState){
            socket.socket.send(JSON.stringify({
                "Authorization": UserModule.token,
                "types": messageTypes
            }))

            console.log("[+] Websocket connect success")

            if (func) {
                func()
            }
        }
    }

    socket.socket.onmessage = (event) => {
        const raw = JSON.parse(event.data)

        // console.log(raw)
        console.log("[+] Get websocket message")

        const {type, data} = raw
        console.log(type)
        types[type](data)
    }
}

connectSocket()


const types = {
    messages(data) {
        const {googleId, messages} = data

        console.log(googleId)

        UserModule.setMessageById({googleId, messages})
    },
    chats(data){
        UserModule.setChats(data)
    },
    users(data){
        UserModule.setUsers(data)
    },
    message(data){
        console.log(data)
        if (data.type === "success"){
            UserModule.setModalContent(null)
        }
        else {
            UserModule.setModalContent(data)
        }
    }
}


export const useWebsocket = () => {
    const send = ({types={}, params={}}) => {
        try {
            socket.socket.send(JSON.stringify({
                Authorization: UserModule.token,
                types: types,
                params: params
            }))
        } catch {
            connectSocket(() => {
                socket.socket.send(JSON.stringify({
                    Authorization: UserModule.token,
                    types: types,
                    params: params
                }))
            })
        }
    }
    const sendMessage = ({googleId, message}, ignore= false) => {
        send({ types: ["send_message"], params: {googleId: googleId, message: message, ignore: ignore}} )
    }

    const getMessages = (googleId) => {
        send({types: ["messages"], params: {googleId: googleId}})
    }
    return {
        send,
        sendMessage,
        getMessages
    }
}
