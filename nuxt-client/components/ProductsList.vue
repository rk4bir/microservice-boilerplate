<template>
  <section class="container-fluid mt-0 pt-0">
    <div v-if="product != '' && product != 'not found'" class="row p-0 m-0">
       <!--img-->
      <div class="col-md-6 p-0 mb-5">
        <img class="img-fluid" v-lazy="product.photo" alt="">
      </div>
      <div class="col-md-6 mb-5">
        <!--titles-->
        <h2 class="text-secondary ">
          {{ product.brand_title }} - {{ product.title }}
        </h2>
        <h4 class="text-muted">{{ product.category_title }}</h4>
        <h4 class="text-primary">
          ${{ product.price | commaSeperatedPrice }}
        </h4>
        <h4>
          <a :href="`/orders/${product.slug}/create`" class="btn btn-sm btn-theme pl-3 pr-3">Order now!</a>
        </h4>
        <hr style="border: 1px solid #EA9000">
        <!--overview-->
        <p
          class="mt-4 text-justify"
          v-if="product.overview != ''" 
          v-html="product.overview.replace('[', '').replace(']', '')"
        ></p>
      </div>

      <!--specs-->
      <div class="col-12 p-0 mb-3" v-if="product.specs.length > 0">
        <h3>Features</h3>
        <ul class="specs-list row">
          <li class="col-md-6" v-for="spec in product.specs" :key="spec.id">
            {{ spec.title }} {{ spec.value }}
          </li>
        </ul>
      </div>

      <!--manuals-->
      <!-- <div class="col-12 p-0 mb-5" v-if="product.manuals.length > 0">
        <h3>Documents</h3>
        <div v-for="(manual, index) in product.manuals" :key="manual.id" class="mt-3">
          <a :href="manual.file">{{index+1 }}. {{ manual.file.split('/')[manual.file.split('/').length - 1] }}</a>
        </div>
      </div> -->

      <!--gallery-->
      <div v-if="galleryImages.length > 0" class="col-12 p-0">
        <h3>Gallery</h3>
        <img class="img-fluid image p-0 col-4 gallery-img" v-for="(image, i) in galleryImages" :key="image" v-lazy="image" @click="index = i">
        <vue-gallery-slideshow :images="galleryImages" :index="index" @close="index = null"></vue-gallery-slideshow>
      </div>
    </div>

    <!-- not found message -->
    <div v-else-if="product == 'not found'" class="row">
      <div class="col-12 mt-5 text-center text-danger">
        Product not found!
      </div>
    </div>

    <!--loader-->
    <div v-else class="row">
      <div class="col-12 mt-3 mb-3 text-muted text-center">
        <b-spinner variant="primary" label="Loading"></b-spinner>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import VueGallerySlideshow from 'vue-gallery-slideshow'

export default {
  components: {
    VueGallerySlideshow,
  },
  data () {
    return {
      product: '',
      galleryImages: [],
      index: null
    }
  },
  methods: {
    updateProductsData (url) {
      if (url) {
        axios.get(`/api/auth/token`)
        .then(response => {
          let token = response.data.token || undefined
          if ( token ) {
            /* update request */
            let headers = { 'Authorization': `Bearer ${token}` }
            axios.get(url, { headers })
              .then(r => {
                this.product = r.data
                this.galleryImages = this.generateGallery(r.data.gallery)
              })
              .catch(e => {
                this.product = 'not found'
                console.error(e);
              })
          }
        })
      }
    },
    generateGallery (gallery) {
      let _gallery = []
      gallery.forEach(item => {
        let link = process.env.NODE_ENV == 'production' ? item.file : process.env.apiURL + item.file
        _gallery.push(link)
      })
      return _gallery
    }
  },
  mounted () {
    this.updateProductsData(`${process.env.apiURL}/v1/products/${this.$route.params.slug}/`)
  }
}
</script>

<style scoped>
.page-title {
  font-family: 'Lato-bold', sans-serif;
}
/* override gallery behaviour */
.lingalleryContainer img {
  width: 100%!important;
  height: 500px!important;
}

.gallery-img { height: 220px; }

@media only screen and
(min-width: 200px) and 
(max-width: 575px)
{
  .gallery-img { height: 120px; }
}

@media only screen and
(min-width: 576px) and 
(max-width: 767px)
{
  .gallery-img { height: 140px; }
}

@media only screen and
(min-width: 768px) and 
(max-width: 991px)
{
  .gallery-img { height: 160px; }
}

/* specs style */

.specs-list {
  list-style: none;
  padding: 0;
  margin-top: 20px;
  margin-bottom: 50px;
}

.specs-list li {
  padding-left: 1em;
  margin-bottom: 10px;
  font-size: 18px;
}

.specs-list li:before {
  content: "\f058"; /* FontAwesome Unicode */
  font-family: FontAwesome;
  color: #EA9000;
  font-size: 18px;
  display: inline-block;
  width: 1em; /* same as padding-left set on li */
  margin-right: 10px;
}


</style>

