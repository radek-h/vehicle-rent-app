<template>
  <div class="home">
<<<<<<< HEAD
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
=======
    <div class="container">
      <div class="row>">
        <div class="col s12 m6">
          <div class="card small" v-for="advert in adverts" :key="advert.pk">
            <div class="card-image" style="max-width: 250px">
              <img :src="getImg(advert.image)" />
            </div>
            <div class="card-content">
              <div class="vehicle-info-container">
                <div class="brand-content">
                  Brand:
                  <h6>
                    <span>{{ advert.vehicle_brand }}</span>
                  </h6>
                </div>

                <div class="model-content">
                  Model:
                  <h6>
                    <span>{{ advert.vehicle_model }}</span>
                  </h6>
                </div>
              </div>

              <div class="location-container">
                <div class="city-content">
                  City:
                  <h6>
                    <span>{{ advert.city }}</span>
                  </h6>
                </div>

                <div class="price-day-content">
                  Price for {{ advert.days_available }} days:
                  <h6>
                    <span>{{ getTotalPrice(advert) }}$</span>
                  </h6>
                </div>
              </div>

              <div class="availability-container">
                <div class="ava-from-content">
                  Available from:
                  <h6>
                    <span>{{ advert.available_from }}</span>
                  </h6>
                </div>
                <div class="ava-to-content">
                  Available to:
                  <h6>
                    <span>{{ advert.available_to }}</span>
                  </h6>
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
                <div class="purchasers-counter">
                  <p>
                    Purchasers:
                    <span>{{ advert.purchasers_count }}</span>
                  </p>
                </div>
              </div>
              <router-link
                :to="{ name: 'advert', params: { slug: advert.slug } }">
                <a class="waves-effect btn-flat">View details</a>
              </router-link>
              
              <!-- <a class="waves-effect waves-teal btn-flat">Make an order</a> -->
            </div>
          </div>
        </div>
      </div>
    </div>
>>>>>>> vuejs
  </div>
</template>

<script>
<<<<<<< HEAD
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "home",
  components: {
    HelloWorld
  }
};
</script>
=======
import { apiService } from "@/common/api.service";
export default {
  name: "home",
  data() {
    return {
      adverts: [],
    };
  },
  methods: {
    getAdverts() {
      let endpoint = "/api/adverts/";
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
  min-width: 20%;
}
.price-container {
  float: right;
  min-width: 40%;
  margin-bottom: 25px;
}
.purchasers-counter p,
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
  color: #6e6e6e !important;
  border: 1px solid #6e6e6e;
  border-radius: 10px;
  margin-right: 0px !important;
}
.card .card-action a:hover {
  color: white !important;
  background: #6e6e6e;
}
.card.small .card-content {
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
>>>>>>> vuejs
