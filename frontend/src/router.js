import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
<<<<<<< HEAD
=======
import Advert from "./views/Advert.vue";
import AdvertEditor from "./views/AdvertEditor.vue";
>>>>>>> vuejs

Vue.use(Router);

export default new Router({
  mode: "history",
<<<<<<< HEAD
  base: process.env.BASE_URL,
=======
  // base: process.env.BASE_URL,
>>>>>>> vuejs
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
<<<<<<< HEAD
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    }
=======
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
>>>>>>> vuejs
  ]
});
