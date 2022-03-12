const express = require('express')
const axios = require('axios')
const cursor = require("../db")
const router = express.Router()

const AUTH_HOST = process.env.AUTH_HOST


router.get('/me', (req, res) => {
    let username = req.session.user
    cursor.getTokens(username, (r) => {
        // if user not found in the db then return error
        if (r == null) {
            res.json({'error': "Invalid token"})
        } else {
            let headers = {'Authorization': `Bearer ${r.accessToken}`}
            axios.get(`${AUTH_HOST}/api/users/me`, { headers })
                .then(response => {
                    res.json(response.data)
                })
                .catch(() => {
                    console.log('/api/user/me: invalid token')
                    res.json({'error': "Invalid token"})
                })
        }
        
    })
})


module.exports = router;