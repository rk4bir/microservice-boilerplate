const express = require('express')
const axios = require('axios')
const router = express.Router()
const cursor = require("../db")

const API_URL = process.env.API_URL


router.get('/list', async (req, res) => {
    let username = req.session.user
    cursor.getTokens(username, (r) => {
        // if user not found in the db then return error
        if (r == null) {
            res.json({'error': "Invalid token"})
        } else {
            let headers = {'Authorization': `Bearer ${r.accessToken}`}
            axios.get(`${API_URL}/products/`, { headers })
                .then(response => {
                    let data = response.data
                    data["status"] = true
                    res.json(data)
                })
                .catch(() => {
                    console.log('/api/product/list: invalid token')
                    res.json({"status": false, "error": "Invalid token"})
                })
        }
    })
})


module.exports = router;