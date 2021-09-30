export const useWebsocket = () => {
    return new WebSocket(process.env.NODE_ENV === 'production' ? "wss://ucabix.com:5050" : "ws://localhost:5050")
}
