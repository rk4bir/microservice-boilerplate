module.exports = {
  // server setup
  server: {
    port: process.env.MODE == 'dev' ? 3001 : 80,
    host: '0.0.0.0', // default: localhost,
    timing: false
  },
  /*
  ** Headers of the page
  */
  head: {
    title: 'Client Type: authorization-code',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
    ],
    script:[
      { src: '/js/jquery.min.js' },
      { src: '/js/bs.bundle.min.js' },
      { src: '/js/fa.min.js' }
    ],
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#28a745' },

  // server middlewares + APIs
  serverMiddleware: [
    { path: "/api", handler: "~/backend/app.js" },
  ],

  /* material vue plugin */
  plugins: [
    '~/plugins/bootstrap.js',
  ],

  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extractCSS: {
      ignoreOrder: false
    },
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  },

  // environment variables for both client and server side
  env: {
    apiURL: process.env.API_URL,
    authHost: process.env.AUTH_HOST,
    devMode: process.env.MODE
  },
}
