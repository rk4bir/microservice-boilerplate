<template>
  <section class="container-fluid mt-0 pt-0">
    <div v-if="!loading" class="row p-0 m-0">
      <!--title and add product button-->
      <div class="col-12 mb-2">
        <div class="row">
          <!-- page title-->
          <div class="mb-2 p-0">
            <h1 class="">Products</h1>
            <div class="text-muted">
              <strong>Total:</strong>
              <small>{{ products.length }}</small>
            </div>
          </div>
        </div>
      </div>
      <!--products list-->
      <div v-if="products.length > 0" class="col-12 mb-3 p-0 m-0">
        <b-list-group v-for="product in products" :key="product.slug">
          <b-list-group-item class="d-flex justify-content-between align-items-center">
            {{ product.title }}
            <b-badge variant="primary" pill>{{ product.price }}</b-badge>
          </b-list-group-item>
        </b-list-group>
      </div>

      <!--if product not found-->
      <div v-else class="col-12 text-center mt-5">
        <div class="text-danger">No products found!</div>
      </div>
    </div>

    <!--loader-->
    <div v-else class="row mt-5">
      <div class="col-12 mb-3 mt-5 text-muted text-center">
        <b-spinner variant="primary" label="Loading"></b-spinner>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      products: [],
      loading: true
    }
  },
  async mounted () {
    const resp = await axios.get(`/api/product/list`)
    if (resp.status == 200) {
      this.products = resp.data
      this.loading = false
    } else {
      this.loading = false
    }
  }
}
</script>


