import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: "/index",
    },
    {
      path: "/index",
      name: "index",
      component: () => import("./components/Index.vue")
    },
    {
      path: "/gallery",
      name: "gallery",
      component: () => import("./components/XrayThumbnailList.vue")
    },
    {
      path: "/view/:id",
      name: "view-detail",
      component: () => import("./components/XrayDetail.vue")
    },
  ]
});
