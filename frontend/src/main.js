import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
// import 'vue-material/dist/theme/default.css'

Vue.config.productionTip = false;

Vue.use(VueMaterial)

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");




// Vue.use(function(req, res, next) {
//   res.header("Access-Control-Allow-Origin", "*");
//   res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
//   next();
// });
