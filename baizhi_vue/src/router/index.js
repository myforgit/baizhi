import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Login from "../components/commen/Login";
import Register from "../components/commen/Register";

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name:"home",
            component: Home
        },
        {
            path: '/home',
            name:"home",
            component: Home
        },
        {
              path: '/home/login',
              name:"login",
              component: Login
        },
        {
              path: '/home/register',
              name:"register",
              component: Register
        },
    ]
})
