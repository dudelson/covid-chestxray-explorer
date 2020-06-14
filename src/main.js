import Vue from 'vue';
import App from './App.vue';
import router from './router';

import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import Cloudinary from 'cloudinary-vue';

Vue.use(BootstrapVue);
Vue.use(Cloudinary, {
  configuration: {
    cloudName: 'dmcs4ohin',
    secure: true,
  }
});

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
