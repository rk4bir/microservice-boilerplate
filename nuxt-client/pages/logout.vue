<template>
    <div>Logging out...</div>
</template>

<script>
export default {
    mounted () {
        localStorage.removeItem('user')
        window.location.href = '/api/auth/logout'
    }
}
</script>
