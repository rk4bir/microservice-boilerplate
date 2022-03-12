<template>
    <section class="container-fluid p-0 m-0">
        <!--bg img-->
        <div class="row p-0 m-0 img-container"> </div>
        <div class="row main-container">
            <div class="col-lg-4 offset-lg-4 col-md-6 offset-md-3 col-sm-8 offset-sm-2 col-10 offset-1">
                <div class="content-area">
                    <h1>
                        Login
                    </h1>
                    <div class="auth-content">
                        <h4>[?] {{ authMessage }}</h4>
                        <a 
                            class="auth-link" 
                            href="/api/auth"
                        >
                            Login with Identity Server
                        </a>
                    </div>
                </div>

                <div class="copyright text-center">
                    &copy; {{ copyrightYear }} all rights reserved rk4bir.github.io
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import loggedInRedirect from '../helpers/loggedInRedirect'

export default {
    layout: 'auth',
    components: {},
    data () {
        return {
            loading: true,
            authMessage: '',
            copyrightYear: new Date().getFullYear()
        }
    },
    async mounted () {
        // handle login: redirected
        if ( this.$route.query.status == 'true' ) {
            let params = {'username': this.$route.query.username}
            axios.get('/api/user/me', {params})
                .then(data => {
                    if (!data.error) {
                        // store data
                        //this.$store.commit('auth/updateUser', data.data)
                        localStorage.setItem('user', JSON.stringify(data.data))
                        this.$router.push('/')
                    } else {
                        this.loading = false
                    }
                })
        } else {
            // check if user already logged in
            await loggedInRedirect()
            this.loading = false
            this.authMessage = this.$route.query.msg
        }
    }
}
</script>

<style scoped>
.img-container {
    background-image: url('~assets/auth-bg.jpeg');
    background-repeat: no-repeat;
    background-position: center;
    background-position: fixed;
    background-size: cover;
    height: 100vh;
    filter:blur(5px);
    -o-filter:blur(5px);
    -ms-filter:blur(5px);
    -moz-filter:blur(5px);
    -webkit-filter:blur(5px);
    backdrop-filter: sepia();
    -webkit-backdrop-filter: sepia();
}
section {
    /* background-color: #28a745; */
    height: 100vh;
    width: 100vw;

}

.main-container {
    background: rgba(0,0,0,0.6);
    background-size: cover;
    /* background-color: #28a745; */
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
}

.content-area {
    z-index: 10;
    margin-top: 30%;
    text-align: center;
    filter: opacity(0.85);
    background: #28a745;
    padding-top: 20px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
}

.content-area h1 {
    font-family: 'Lato-bold';
    margin-bottom: 20px;
    color: #343f46;
    font-size: 2.2rem!important;
}

.auth-content {
    border-radius: 10px;
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    background-color: #343f46;
    /* padding */
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 40px;
    padding-bottom: 50px;
}

.auth-content h4 {
    font-size: 18px;
    font-weight: bold;
    color: red;
    margin-top: 20px;
    margin-bottom: 40px;
}

.auth-link {
    font-size: 16px; 
    text-decoration: none; 
    border: 2px solid #28a745; 
    border-radius: 7px;
    padding-left: 15px;
    padding-right: 15px;
    padding-top: 7px;
    padding-bottom: 7px;
}
.auth-link img {
    height: 14px; 
    margin-left: 3px
}
.auth-link:hover {
    color: #28a745;
}

.copyright {
    margin-top: 50px;
    font-size: 13px;
    color: #f5f5f5;
}


@media only screen and
(min-width: 200px) and 
(max-width: 575px)
{
    .content-area h1 { font-size: 1.4rem!important }
    .auth-link { 
        font-size: 14px; 
        padding-right: 10px; 
        padding-left: 10px; 
        padding-top: 5px; 
        padding-bottom: 7px;
    }
    .auth-link img { height: 12px; }
}

@media only screen and
(min-width: 576px) and 
(max-width: 767px)
{
    .content-area h1 { font-size: 2rem }
}
/* 
@media only screen and
(min-width: 768px)
{
    .content-area h1 { font-size: 2rem }
} */


@media only screen and
(min-width: 290px) and 
(max-width: 554px)
{
    .content-area h1 { font-size: 2rem }
}
</style>