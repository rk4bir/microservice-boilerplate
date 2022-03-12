<template>
  <div class="error-page">
    <h1 class="error-title" v-if="error.statusCode === 404">Page not found</h1>
    <h1 class="error-title" v-else>An error occurred</h1>
    <br>
    <br>
    <NuxtLink to="/">
        Goto homepage
    </NuxtLink>
  </div>
</template>

<script>
  export default {
    props: ['error'],
    layout: 'error', // you can set a custom layout for the error page
    head: {
        title: 'Error occured!',
    }
  }
</script>

<style scoped>
.error-page {
    padding: 0px;
    margin: 0 auto;
    widows: 100%;
    text-align: center;
    padding-top: 130px;
    font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; /* 1 */
}
a, a:hover, a:active {
    color: #f80808;
    font-weight: 400;
}

.error-title {
  display: block;
  font-weight: 300;
  font-size: 48px;
  color: #35495e;
  letter-spacing: 1px;
}
</style>