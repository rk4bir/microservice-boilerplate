import axios from 'axios'


export default async function checkLogin () {
    let result = await axios.get('/api/user/me')
    let data = await result.data
    if ( data.error ) window.location.href = '/login'
    return data
}
