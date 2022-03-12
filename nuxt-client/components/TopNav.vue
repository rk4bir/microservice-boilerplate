<template>
    <div class="sticky-top p-3 top_nav col-12">
        <div class="row">
            <div class="col-6 text-left">
                <h2 class="text-primary">Oauth2 Client</h2>
            </div>
            <div class="col-6 text-right">
                <ul class="top_nav_links">
                    <li class="mr-2 name">
                        <span class="first_name">{{ user.first_name }}</span><br>
                        <span class="last_name">{{ user.last_name }}</span>
                    </li>
                    <li class="ml-3 align-self-center ml-3">
                        <span 
                            style="font-size: 24px"
                            class="fa fa-chevron-down text-primary"
                            type="button"
                            id="topNavDropDown" 
                            data-toggle="dropdown" 
                            aria-haspopup="true" 
                            aria-expanded="false"
                        ></span>
                        <!--drowpdown menu-->
                        <div 
                            class="dropdown-menu top_nav_dropown_menu bg-secondary" 
                            aria-labelledby="topNavDropDown"
                        >
                            <a 
                                v-for="item in dropdownItems" 
                                :key="item.link"  
                                class="dropdown-item" 
                                :href="item.link"
                            >
                                <span :class="item.iconClass"></span>{{ item.title }}
                            </a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "TopNav",
    data () {
        return {
            user: false,
            mobileMenuClassName: 'col-12 d-none',
            mobileMenuTogglerClassName: 'fa fa-bars text-white',
            dropdownItems: [
                { title: 'Sign out', link: '/logout', iconClass: 'fa fa-sign-out mr-1' }
            ]
        }
    },
    methods: {
        toggleMobileMenu () {
            if ( this.mobileMenuClassName == 'col-12 d-none' ) {
                // show mobile menu
                this.mobileMenuClassName = 'col-12'
                this.mobileMenuTogglerClassName = 'fa fa-close text-white'
            } else {
                // hide mobile menu
                this.mobileMenuClassName = 'col-12 d-none'
                this.mobileMenuTogglerClassName = 'fa fa-bars text-white'
            }
        }
    },
    mounted () {
        let user = JSON.parse(localStorage.getItem('user'))
        this.user = user ? user : false
        if (this.user && process.env.NODE_ENV != 'production') {
            this.user.photo = 'http://localhost:8000' + this.user.photo
        }
    }
}
</script>

<style>
.top_nav {
    background-color: white;
    z-index: 99999999;
}
/* left section */
/* .left_search_section {

} */
.search-input {
    border-color: #28a745!important;
    width: 90%!important;
}
.search-submit-button, .search-submit-button:hover {
    width: 10%!important;
    margin-left: -10px;
    border: 1px solid #28a745!important;
    border-top-right-radius: 7px;
    border-bottom-right-radius: 7px;
}
/* right section */
.top_nav_links {
    display: inline-flex;
}
.top_nav_links li {
    list-style: none;
}

.top_nav_links .name {
    font-size: 18px;
    font-style: normal;
    line-height: 20px;
    text-align: right;
    padding-top: 8px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}
.top_nav_links .name .first_name { font-family: 'Lato-bold', sans-serif; }
.top_nav_links .name .last_name { font-family: 'Lato-thin', sans-serif; }

.profile_photo {
    width: 50px;
    height: 50px;
    border-radius: 50px;
    border: 1px solid #28a745;
}

.top_nav_dropown_menu {
    margin-top: 20px!important;
    margin-left: -140px!important;
    position: relative;
    z-index: 99999;
}

.top_nav_dropown_menu:before {
  position: absolute;
  top: -8px;
  right: 6px; /* Example: right:10px; */
  display: inline-block;
  border-right: 8px solid transparent;
  border-bottom: 8px solid #343f46;
  border-left: 8px solid transparent;
  border-bottom-color: rgba(0, 0, 0, 0.2);
  content: '';
}

.top_nav_dropown_menu:after {
  position: absolute;
  top: -7px;
  right: 6px; /* Example: right:10px; */
  display: inline-block;
  border-right: 7px solid transparent;
  border-bottom: 7px solid #343f46;
  border-left: 7px solid transparent;
  content: '';
}
.top_nav_dropown_menu a { color: white!important; }
.top_nav_dropown_menu a:hover{ color: #28a745!important; }
.top_nav_dropown_menu a:focus { color: white!important; }

@media only screen and 
(min-width: 0px) and 
(max-width: 767px)
{
    .top_nav {
        border-bottom: 1px dashed #28a745;
        margin-bottom: 40px;
    }
}

</style>