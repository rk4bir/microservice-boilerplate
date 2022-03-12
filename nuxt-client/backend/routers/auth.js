const express = require('express')
const axios = require('axios')
const cursor = require("../db")
const router = express.Router()

const APP_HOST = process.env.APP_HOST
const AUTH_HOST = process.env.AUTH_HOST
const CLIENT_ID = process.env.CLIENT_ID
const CLIENT_SECRET = process.env.CLIENT_SECRET

const redirect_uri = `${APP_HOST}/api/auth/callback`
const auth_uri = `${AUTH_HOST}/oauth2/authorize/`
const token_uri = `${AUTH_HOST}/oauth2/token/`
const client_id = CLIENT_ID
const client_secret = CLIENT_SECRET
const state_val = "aquickbrownfoxjumpsoverthelazydog"


router.all('/', (req, res) => {
    let url = `${auth_uri}?client_id=${client_id}&response_type=code&redirect_uri=${redirect_uri}&state=${state_val}`
    res.redirect(url)
})


router.all('/callback', async (req, res) => {
    let code = req.query.code || null
    let state = req.query.state || null
    let body = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    /* If state doesn't match then throw error and redirect back to fron-end */
    if ( state_val !== state ) return res.redirect('/login?status=false&msg=invalid_request')
    // obtain token pair
    const token_resp = await axios.post(token_uri, body)
    if (token_resp.status == 200) {
        let _tokens = token_resp.data
        // fetch user profile
        let headers = {'Authorization': `Bearer ${_tokens.access_token}`}
        const user_resp = await axios.get(`${AUTH_HOST}/api/users/me/`, { headers })
        if ( user_resp.status == 200 ) {
            let user = user_resp.data
            cursor.InsertTokens(user.username, _tokens.refresh_token, _tokens.access_token)
            // set session and success redirect
            req.session.user = user.username
            res.redirect(`/login?status=true&msg=success&username=${user.username}`)
        }
    }
    res.redirect('/login?status=false&msg=invalid_request')
})


router.get('/me', (req, res) => {
    let username = req.session.user
    cursor.getTokens(username, (r) => {
        // if user not found in the db then return error
        if (!r) res.json({'error': "Invalid token"})

        let headers = {'Authorization': `Bearer ${r.accessToken}`}
        axios.get(`${AUTH_HOST}/api/users/me`, { headers })
            .then(response => {
                res.json(response.data)
            })
            .catch(err => {
                res.json({'error': "Invalid token"})
            })
    })
})


router.all('/logout', (req, res) => {
    req.session.user = null
    // log out from authorization server as well
    res.redirect(`${AUTH_HOST}/sign-out/?next=${APP_HOST}/login?status=false&msg=logged_out`)
})


router.get('/token', (req, res) => {
    const username = req.session.user
    const slug = req.params.slug
    cursor.getTokens(username, (r) => {
        // if user not found in the db then return error
        if (r == null) {
            res.json({'error': "Invalid token"})
        } else {
            res.json({'token': r.accessToken})
        }
    })
})

module.exports = router;