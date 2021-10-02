import {UserModule} from '@/store/user'

export const beforeLoad =  async function (){
    await UserModule.init()
}
