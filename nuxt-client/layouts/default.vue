<template>
  <div class="container-fluid" id="default_layout_main">
    <div class="container">

      <div class="row">
        <TopNav />
      </div>
      
      <div class="row">
        <nuxt />
      </div>
    </div>
  </div>
</template>

<script>
import TopNav from '../components/TopNav'
import checkLogin from '../helpers/checkLogin.js'

export default {
  components: {
    TopNav
  },
  async beforeMount () {
    if (this.$route.query.ref == 'logged_in') window.location.href = '/api/auth'
    await checkLogin()
  },
  mounted () {
    var mainComponent = document.getElementById('default_layout_main')
    mainComponent.style.marginTop = '2px'
    this.$nextTick(() => {
      this.$nuxt.$loading.start()
      setTimeout(() => {
        this.$nuxt.$loading.finish()
        mainComponent.style.marginTop = '0px'
      }, 2000)
    })

    let user = JSON.parse(localStorage.getItem('user'))
  }
}
</script>

<style>
body {
  font-size: .875rem;
  scrollbar-color: white white;
  background-color: white;
}

.admin-warning {
  margin-left: 20px;
  padding: 10px;
  border: 1px dashed #EA9000;
  /* color: #252F35; */
  color: red;
  margin: 15px;
  margin-left: 40px;
}

@media only screen and (min-width: 0px) and (max-width: 767px) {
  main {
    margin-left: 0px!important;
    border-radius: 0px!important;
  }
  .admin-warning { margin-left: 15px!important; }
}
</style>