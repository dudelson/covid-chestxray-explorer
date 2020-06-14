import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

import XrayThumbnailList from './components/XrayThumbnailList.vue';
import XrayDetail from './components/XrayDetail.vue';

export default new Router({
  routes: [
    {
      path: "/",
      redirect: "/gallery/1",
    },
    {
      path: "/gallery/:pagenum",
      name: "gallery",
      component: XrayThumbnailList,
    },
    {
      path: "/view/:id",
      name: "view-detail",
      component: XrayDetail,
    },
  ]
});
