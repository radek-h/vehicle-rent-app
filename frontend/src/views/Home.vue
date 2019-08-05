<template>
  <div class="home">
    <div class="container">
      <div class="row>">
        <div class="col s12 m7">
          <div class="card small" 
               v-for="advert in adverts" 
               :key="advert.pk">
            <div class="card-image">
              <img :src="getImg(advert.image)" :alt="advert.image"/>
            </div>
            <div class="card-content">
              <div class="vehicle-content">
                 Brand: <h5><span>{{ advert.vehicle_brand }}</span></h5>
                 Model: <h5><span>{{ advert.vehicle_model }}</span></h5>
                 
                 Price per day: <h5><span>{{ advert.price_per_day }}</span>$</h5>
              </div>
              <div class="availability-content">
                City: <h5><span>{{ advert.city}}</span></h5>
                Available from: <h5><span>{{ advert.available_from}}</span></h5>
                Available to:<h5> <span>{{ advert.available_to}}</span></h5>
              </div>

             
            </div>
            <div class="card-action right">
              <div class="text left">
                <div class="posted-by">
                  <p>Posted by: <span>{{ advert.author }}</span></p>
                </div>
                <div class="advert-created">
                  <p>Advert created: <span>{{ advert.created_at }}</span></p>
                </div>
              </div>
              <a href="#">Make an order</a>
            </div>
          </div>
        </div>
      </div>
      <!-- <div v-for="advert in adverts"
           :key="advert.pk">
        <p>Posted by: <span>{{ advert.author }}</span></p>
        <h2>{{ advert }}</h2> -->
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service"
export default {
  name: "home",
  data() {
    return {
      adverts: []
    }
  },
  methods: {
    getAdverts() {
      let endpoint = "api/adverts/";
      apiService(endpoint)
        .then(data => {
          this.adverts.push(...data.results)
        })
    },
    getImg(img) {
      return require('@/assets/vehicles/'+img)
    }
  },
  created () {
    this.getAdverts()
    // console.log(this.adverts)
  }
};
</script>

<style>
.vehicle-content, .availability-content{
  float: left;
  margin-right: 10px; 
}
.posted-by p, .advert-created p{
  margin: 0;
  opacity: 0.4;
}
.card-image{
  float: left;
  margin: 20px;
  max-height: 100% !important;
}
.card-action {
  padding: 16px !important;
}
.card .card-action a{
  float: right;
  padding: 8px;
  border-radius: 10px;
  color: #ee7c7c !important;
  border: 1px solid #ee7c7c;
  margin-right: 0px !important;
}
.card .card-action a:hover{
  color: red !important;
  border-color: red;
}
</style>

