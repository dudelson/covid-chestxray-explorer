import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: "/gallery/1",
    },
    {
      path: "/gallery/:pagenum",
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
