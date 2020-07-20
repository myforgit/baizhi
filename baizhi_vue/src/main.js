// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/index'

Vue.config.productionTip = false


import axios from "axios";

Vue.prototype.$axios = axios;


import settings from "./settings";

Vue.prototype.$settings = settings;

import "../static/js/gt"

require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');
import VideoPlayer from 'vue-video-player'

Vue.use(VideoPlayer);

//element-ui
import Element from "element-ui"
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Element);
/* eslint-disable no-new */

import '../static/css/global.css'


new Vue({
    el: '#app',
    router,
    store,
    components: {App},
    template: '<App/>'
})
