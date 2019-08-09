<template>
  <div class="container">
    <div class="col s12 m6">
      <div class="card large">
        <!-- <div class="advert-title">
          <h3>Add an Advert!</h3>
        </div> -->
        <form @submit.prevent="validateAdvert">
          <div class="add-advert-container">
            <div class="add-advert-left-container">

              <md-field :class="getValidationClass('vehicleType')">
                <label for="vehicle-type">Vehicle type</label>
                <md-select v-model="form.vehicleType"
                           id="vehicle-type"
                           :disabled="sending">
                  <md-option value="Car">Car</md-option>
                  <md-option value="Motor">Motor</md-option>
                  <md-option value="Bike">Bike</md-option>
                  <md-option value="Boat">Boat</md-option>
                  <md-option value="Other">Other</md-option>
                </md-select>
                <span class="md-error" 
                      v-if="!$v.form.vehicleType.required">
                      The vehicle type is required
                </span>
              </md-field>
              
              <md-field :class="getValidationClass('vehicleBrand')">
                <label for="vehicle-brand">Vehicle Brand</label>
                <md-input v-model="form.vehicleBrand"
                          id="vehicle-brand"
                          :disabled="sending"></md-input>
                <span class="md-error" 
                      v-if="!$v.form.vehicleBrand.required">
                      The vehicle brand is required
                </span>
                <span class="md-error" 
                       v-else-if="!$v.form.vehicleBrand.minlength">
                       Invalid vehicle brand (min 3 chars)
                </span>
                <span class="md-error" 
                       v-else-if="!$v.form.vehicleBrand.maxlength">
                       Invalid vehicle brand (above 100 chars)
                </span>
              </md-field>

              <md-field :class="getValidationClass('vehicleModel')">
                <label for="vehicle-model">Vehicle Model</label>
                <md-input v-model="form.vehicleModel"
                          id="vehicle-model"
                          :disabled="sending"/>
                <span class="md-error" 
                      v-if="!$v.form.vehicleModel.required">
                      The vehicle model is required
                </span>
                <span class="md-error" 
                       v-else-if="!$v.form.vehicleModel.minlength">
                       Invalid vehicle model (min 3 chars)
                </span>
                <span class="md-error" 
                       v-else-if="!$v.form.vehicleModel.maxlength">
                       Invalid vehicle model (above 100 chars)
                </span>
              </md-field>

              <md-field :class="getValidationClass('city')">
                <label for="city-id">City</label>
                <md-input v-model="form.city"
                          id="city-id" 
                          :disabled="sending"/>
                <span class="md-error" 
                      v-if="!$v.form.city.required">
                      The city is required
                </span>
                <span class="md-error" 
                       v-else-if="!$v.form.city.minlength">
                       Invalid vehicle model
                </span>
              </md-field>

              <md-field>
                <label for="image">Add image</label>
                <md-file v-model="form.vehicleImage"
                         id="image"
                         :disabled="sending"/>
              </md-field>
            </div>

            <div class="add-advert-right-container">

              <label for="ava-from">Available from:</label>
              <md-datepicker :class="getValidationClass('availabilityFrom')"
                              v-model="form.availabilityFrom"
                              id="ava-from"
                              :disabled="sending"/>
              <span class="md-error" 
                    v-if="!$v.form.availabilityFrom.required">
                    The available start date is required
              </span>  
              <!-- <span class="md-error" 
                    v-else-if="!$v.form.city.minValue">
                    You cannot chose date before actual one
              </span>            -->
              
              <label for="ava-to">Available to:</label>
              <md-datepicker :class="getValidationClass('availabilityTo')"
                              v-model="form.availabilityTo"
                              id="ava-to"
                              :disabled="sending"/>
              <span class="md-error" 
                    v-if="!$v.form.availabilityTo.required">
                    The available end date is required
              </span>  
              <!-- <span class="md-error" 
                    v-else-if="!$v.form.city.minValue">
                    The start date cannot be before today
              </span>  -->

              <md-field :class="getValidationClass('price')">
                <label for="price">Price for all days</label>
                <md-input v-model="form.price"
                          type="number"
                          id="price"
                          :disabled="sending"/>
                <span class="md-error" 
                      v-if="!$v.form.price.required">
                      The price is required
                </span>
                <span class="md-error" 
                       v-else-if="!$v.form.city.minValue">
                       Minimum price value is 1
                </span>
              </md-field>

              <md-field>
                <label for="vehicle-desc">Description</label>
                <md-textarea v-model="form.description"
                             id="vehicle-desc"
                             :disabled="sending"/>
              </md-field>
            </div>
          </div>
          
          <md-progress-bar md-mode="indeterminate" v-if="sending" />

          <button class="btn waves-effect waves-light"
                  type="submit"
                  :disabled="sending">
                  Publish
              <i class="material-icons right">send</i>
          </button>
          
          <md-snackbar :md-active.sync="advertSaved">
            The advert was saved with success!
          </md-snackbar>

        </form>
        <!-- <p v-if="error" class="disable">{{ error }}</p> -->
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";
import { validationMixin } from 'vuelidate'
import {
    required,
    minLength,
    maxLength,
    minValue
} from 'vuelidate/lib/validators'
export default {
  name: "AdvertEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  mixins: [validationMixin],
  data:() => ({
    form: {
        city: null,
        price: null,
        vehicleType: null,
        vehicleBrand: null,
        vehicleModel: null,
        vehicleImage: null,
        vehicleContent: null,
        availabilityTo: null,
        availabilityFrom: null,
        description: null,
      },
      advertSaved: false,
      //properImageFormat: false,
      sending: false,
  }),
      validations: {
      form: {
        price: {
          required,
          minValue: minValue(1)
        },
        vehicleType: {
          required,
        },
        vehicleBrand: {
          required,
          minLength: minLength(3),
          maxLength: maxLength(100)
        },
        vehicleModel: {
          required,
          minLength: minLength(3),
          maxLength: maxLength(100)
        },
        city: {
          required,
          maxLength: maxLength(100)
        },
        availabilityFrom: {
          required,
          // minValue: value => value > new Date().toISOString(),
          
        },
        availabilityTo: {
          required,
          // Tutaj walidacja czy końcowa data wypożycz. nie jest większa niż dopuszczalna
          //minValue: value => value > new Date().toISOString(),
         
        },
      }
    },
  methods: { 
      // checkImageFormat(fieldName) {
      //   if (this.$v.form[fieldName]['type']==='image/jpg'){
      //     return this.properImageFormat
      //   }
      // },
      getValidationClass (fieldName) {
        const field = this.$v.form[fieldName]

        if (field) {
          return {
            'md-invalid': field.$invalid && field.$dirty
          }
        }
      },

      clearForm () {
        this.$v.$reset()
        this.form.city = null
        this.form.price = null
        this.form.vehicleType = null
        this.form.vehicleBrand = null
        this.form.vehicleModel = null
        this.form.vehicleImage = null
        this.form.availabilityFrom = null
        this.form.availabilityTo= null
        this.form.description = null
      },
      validateAdvert () {
        this.$v.$touch()

      if (!this.$v.$invalid) {
          this.saveAdvert()
        }
      },
      saveAdvert () {
        this.sending = true

        let endpoint = "/api/adverts/";
        let method = "POST";
        console.log(this.slug)
        // if (this.slug !== undefined) {
        //     endpoint += `${ this.slug }/`;
        //     method = "PUT";
        // }
      apiService(endpoint, method, { content: this.form })
      .then(advert_data => {
            this.$router.push({
              name: "advert",
              params: { slug: advert_data.slug }
            })
          this.advertSaved = true
          this.sending = false
          this.clearForm();
          });
      },
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
  padding: 30px;
  width: 70%;
  margin-left: auto;
  margin-right: auto;
}
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


