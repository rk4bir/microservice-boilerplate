"use strict";

const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('./backend/data/users.sqlite3')


const createTable = () => {
    db.run("CREATE TABLE users (userName TEXT, refreshToken TEXT, accessToken TEXT)")
}


const InsertTokens = (userName, refreshToken, accessToken) => {
    db.run(`INSERT INTO users VALUES ('${userName}', '${refreshToken}', '${accessToken}')`)
}


const getTokens = (userName, callback) => {
    var data = null
    db.serialize(() => {
        let query = `SELECT userName, refreshToken, accessToken FROM users WHERE userName='${userName}'`
        db.each(query, (err, row) => {
            if (err) {
                data = null
            } else {
                data = row
            }
        }, () => {
            callback(data)
        })
    })
}


module.exports = {
    createTable,
    InsertTokens,
    getTokens
}
