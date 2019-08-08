<template>
    <div class="single-advert">
      <div class="container">
        <div class="col s12 m6">
          <div class="card small">
              {{ advert.city }}
            <div class="card-image" style="max-width: 250px">
              <img :src="`@/assets/vehicles/${advert.image}`"/>
            </div>
            <div class="card-content">
              <div class="vehicle-info-container">
                <div class="brand-content">
                  Brand:
                  <h5>
                    <span>{{ advert.vehicle_brand }}</span>
                  </h5>
                </div>

                <div class="model-content">
                  Model:
                  <h5>
                    <span>{{ advert.vehicle_model }}</span>
                  </h5>
                </div>
              </div>

              <div class="location-container">
                <div class="city-content">
                  City:
                  <h5>
                    <span>{{ advert.city }}</span>
                  </h5>
                </div>

                <div class="price-day-content">
                  Price for {{ advert.days_available }} days:
                  <h5>
                    <span>{{ getTotalPrice(advert) }}$</span>
                  </h5>
                </div>
              </div>

              <div class="availability-container">
                <div class="ava-from-content">
                  Available from:
                  <h5>
                    <span>{{ advert.available_from }}</span>
                  </h5>
                </div>
                <div class="ava-to-content">
                  Available to:
                  <h5>
                    <span>{{ advert.available_to }}</span>
                  </h5>
                </div>
              </div>

              <div class="price-container">
                <div class="price-tag">
                  Price per day:
                  <h2>
                    <span>{{ advert.price_per_day }}</span>
                    $
                  </h2>
                </div>
              </div>
            </div>
            <div class="card-action right">
              <div class="text left">
                <div class="posted-by">
                  <p>
                    Posted by:
                    <span>{{ advert.author }}</span>
                  </p>
                </div>
                <div class="advert-created">
                  <p>
                    Advert created:
                    <span>{{ advert.created_at }}</span>
                  </p>
                </div>
              </div>
              <!-- <router-link
                :to="{ name: 'advert', params: { slug: advert.slug } }"> -->
                <a class="waves-effect btn-flat">Make an order</a>
              <!-- </router-link> -->
              
              <!-- <a class="waves-effect waves-teal btn-flat">Make an order</a> -->
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
    name: "advert",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            advert: {}
        }
    },
    methods: {
        setPageTitle(title) {
            document.title = title;
        },
        getAdvertData() {
            let endpoint = `/api/adverts/${this.slug}/`;
            apiService(endpoint).then(data => {
                if (data) {
                    this.advert = data;
                    title = data.vehicle_brand + data.vehicle_model
                    this.setPageTitle(title)
                } else {
                    this.advert = null;
                    this.setPageTitle("404 Page Not Found")
                }
            })
        },
        getTotalPrice(advert) {
            return advert.days_available * advert.price_per_day;
        },
        created() {
            this.getAdvertData()
        },
    }
}
</script>

<style>

</style>
