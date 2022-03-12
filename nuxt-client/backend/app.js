const bodyParser = require('body-parser')
var cookieSession = require('cookie-session')
const app = require('express')()
const middleware = require('./middleware')


app.use(bodyParser.json())
app.use(cookieSession({
    name: 'session',
    keys: ['KEY 1', 'Key 2'],
    // Cookie Options
    maxAge: 24 * 60 * 60 * 1000 // 24 hours
}))
// LOGGER MIDDLEWARE
app.use(middleware.logger)
// TOKEN RENEWAL MIDDLEWARE
app.use(middleware.tokenRenew)

// routers
app.all('/heartbeat', (req, res) => {
    // heartbeat for ECS health check
    res.json({'message': 'Working...'})
})
app.use('/auth', require('./routers/auth.js'))
app.use('/user', require('./routers/user.js'))
app.use('/product', require('./routers/product.js'))

module.exports = app
