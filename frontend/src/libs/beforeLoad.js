import {UserModule} from '@/store/user'

export const beforeLoad =  async function (){
    console.log("hello world")
    await UserModule.init()
}
