<template>
  <div class="container">
    <div class="col s12 m6">
      <div class="card large">
        <div class="advert-title">
          <h3>Add an Advert!</h3>
        </div>
        <form @submit.prevent="onSubmit">
          <div class="add-advert-container">
            <div class="add-advert-left-container">
              <md-field>
                <label for="vehicle-type">Vehicle type</label>
                <md-select v-model="advert_vehicle_type" id="vehicle-type" required>
                  <md-option value="Car" selected>Car</md-option>
                  <md-option value="Motor">Motor</md-option>
                  <md-option value="Bike">Bike</md-option>
                  <md-option value="Boat">Boat</md-option>
                  <md-option value="Other">Other</md-option>
                </md-select>
              </md-field>

              <md-field>
                <label>Vehicle Brand</label>
                <md-input v-model="advert_brand" required></md-input >
              </md-field>

              <md-field>
                <label>Vehicle Model</label>
                <md-input v-model="advert_model" required></md-input>
              </md-field>

              <md-field>
                <label>City</label>
                <md-input v-model="advert_city" required></md-input>
              </md-field>

              <md-field>
                <label>Add image</label>
                <md-file v-model="advert_image" />
              </md-field>
            </div>

            <div class="add-advert-right-container">
              <md-datepicker v-model="advert_ava_from" required>
                <label>Available from:</label>
              </md-datepicker>

              <md-datepicker v-model="advert_ava_to">
                <label>Available to:</label>
              </md-datepicker>

              <md-field>
                <label style="margin-top: 5px;">Description</label>
                <md-textarea v-model="advert_content"></md-textarea>
              </md-field>
            </div>
          </div>
          
            <button class="btn waves-effect waves-light" type="submit" name="action">
              Publish
              <i class="material-icons right">send</i>
            </button>
          
        </form>
        <p v-if="error" class="disable">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";
export default {
  name: "AdvertEditor",
  data() {
    return {
      advert_vehicle_type: null,
      advert_brand: null,
      advert_model: null,
      advert_city: null,
      advert_ava_from: null,
      advert_ava_to: null,
      advert_body: null,
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (this.advert_brand.length > 100 || this.advert_model.length > 100 || this.advert_city.length > 100) {
        this.error = "Length of vehicle brand must be less than 100 chars";
      } else {
        let endpoint = "/api/questions/";
        let method = "POST";
        apiService(endpoint, method, { content: this.advert_brand }).then(
          advert_data => {
            this.$router.push({
              name: "advert",
              params: { slug: advert_data.slug }
            });
          }
        );
      }
    }
  },
  created() {
    document.title = "Editor - VehicleRent";
  }
};
</script>

<style scoped>
button {
  display: block;
  margin: 0 auto;
}
/* .md-datepicker-header, .md-datepicker-body {
  background-color: white;
} */
.md-field + .md-has-textarea:not(.md-autogrow) {
  margin-top: 0px;
}
.md-textarea {
  border: 1px solid lightgray !important;
  border-radius: 10px !important;
}
.md-field {
  margin: 0px;
}
.btn-small {
  height: 2rem !important;
  line-height: 2rem !important;
}
.advert-title {
  text-align: center;
}
.add-advert-container {
  width: 70%;
  margin-left: auto;
  margin-right: auto;
}
/* .publish-btn {
  margin-left: auto;
  margin-right: auto;
} */
.add-advert-left-container {
  min-height: 350px;
  width: 45%;
  float: left;
}
.add-advert-right-container {
  min-height: 350px;
  width: 45%;
  float: right;
}
</style>


