<template>
  <div class="home">
    <div class="container">
      <div class="row>">
        <div class="col s12 m6">
          <div class="card small" v-for="advert in adverts" :key="advert.pk">
            <div class="card-image" style="max-width: 250px">
              <img :src="getImg(advert.image)" :alt="advert.image" />
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
              <a class="waves-effect waves-teal btn-flat">Make an order</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";
export default {
  name: "home",
  data() {
    return {
      adverts: []
    };
  },
  methods: {
    getAdverts() {
      let endpoint = "api/adverts/";
      apiService(endpoint).then(data => {
        this.adverts.push(...data.results);
      });
    },
    getImg(img) {
      return require("@/assets/vehicles/" + img);
    },
    getTotalPrice(advert) {
      return advert.days_available * advert.price_per_day;
    }
  },
  created() {
    this.getAdverts();
    // console.log(this.adverts)
  }
};
</script>

<style>
.vehicle-info-container,
.availability-container,
.location-container {
  float: left;
  min-width: 200px;
  /* margin-right: 40px;  */
}
.price-container {
  float: left;
  min-width: 300px;
}
.posted-by p,
.advert-created p {
  margin: 0;
  opacity: 0.4;
}
.card-image {
  float: left;
  margin: 20px;
  max-height: 100% !important;
}
.card-action {
  padding: 16px !important;
}
.card .card-action a {
  float: right;
  color: #ee7c7c !important;
  border: 1px solid #ee7c7c;
  margin-right: 0px !important;
}
.card .card-action a:hover {
  color: white !important;
  background: red;
}
.card-content {
  max-height: 60% !important;
}
.brand-content,
.city-content,
.ava-from-content,
.price-tag {
  margin-bottom: 20px;
}
.desc span {
  border: 1px solid lightgray;
  padding: 5px;
}
.price-tag {
  text-align: center;
}
</style>
