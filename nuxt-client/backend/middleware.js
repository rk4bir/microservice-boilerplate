const cursor = require('./db')
const axios = require('axios')

const APP_HOST = process.env.APP_HOST
const AUTH_HOST = process.env.AUTH_HOST
const CLIENT_ID = process.env.CLIENT_ID
const CLIENT_SECRET = process.env.CLIENT_SECRET

const redirect_uri = `${APP_HOST}/api/auth/callback`
const token_uri = `${AUTH_HOST}/oauth2/token/`
const client_id = CLIENT_ID
const client_secret = CLIENT_SECRET


function logger (req, res, next) {
    let log = `[${req.method}: ${req.originalUrl} <- ${req.headers.referer}] - ${req.session.user} - ${req.headers['user-agent']}`
    if ( process.env.NODE_ENV == 'production' ) console.log(log)
    next()
}


// TOKEN RENEWAL MIDDLEWARE
function tokenRenew (req, res, next) {
    const AUTH_HOST = process.env.AUTH_HOST
    let username = req.session.user
    console.log(`tokenRenew -> username: ${username}`);
    if (username) {
        cursor.getTokens(username, (dbData) => {
            // if user not found in the db then return error
            if (!dbData) {
                console.log('tokenRenew: token is not found in sqlite3')
                // unset session.user
                req.session.user = null
            } else {
                let headers = {'Authorization': `Bearer ${dbData.accessToken}`}
                axios.get(`${AUTH_HOST}/api/users/me`, { headers })
                    .then(response => {
                        // token still valid
                        console.log('tokenRenew: Token is still valid')
                    })
                    .catch(err => {
                        // token expired, renew with a request
                        let body = {
                            "refresh_token": dbData.refreshToken,
                            "grant_type": "refresh_token",
                            "client_id": client_id,
                            "client_secret": client_secret,
                            "redirect_uri": redirect_uri
                        }
                        axios.post(token_uri, body)
                            .then(r => {
                                var _token = r.data
                                // fetch user info
                                let headers = {'Authorization': `Bearer ${_token.access_token}`}
                                axios.get(`${AUTH_HOST}/api/users/me/`, { headers })
                                    .then(response => {
                                        let user = response.data
                                        if ( user.user_type == 'user' || user.user_type == 'admin') {
                                            cursor.InsertTokens(user.username, _token.refresh_token, _token.access_token)
                                            console.log('tokenRenew: Token renewed')
                                        } else {
                                            // unset session.user
                                            req.session.user = null
                                            console.log('tokenRenew: invalid user')
                                        }
                                    })
                                    .catch(err => {
                                        // unset session.user
                                        req.session.user = null
                                        console.log('tokenRenew: permission denied')
                                    })
                            })
                            .catch(err => {
                                // unset session.user
                                req.session.user = null
                                console.log('tokenRenew: invalid request')
                            })
                    })
            }
        })
    }
    // next ->
    next()
}

module.exports = {
    tokenRenew,
    logger
}