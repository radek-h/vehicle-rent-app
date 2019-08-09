import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Advert from "./views/Advert.vue";
import AdvertEditor from "./views/AdvertEditor.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  // base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/advert/:slug",
      name: "advert",
      component: Advert,
      props: true
    },
    {
      path: "/add-advert/:slug?",
      name: "advert-editor",
      component: AdvertEditor,
      props: true
    },
  ]
});
