import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Login from "../components/commen/Login";
import Register from "../components/commen/Register";
import Course from "../components/commen/Course";
import Detail from "../components/commen/Detail";
import Cart from "../components/Cart";
import Order from "../components/Order";
import Payment from "../components/Payment";


Vue.use(Router);

export default new Router({
    mode:"history",
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
        {
              path: '/course',
              name:"Course",
              component: Course
        },
        {
              path: '/detail/:id',
              component: Detail
        },
        {
              path: '/cart',
              name:"Cart",
              component: Cart
        },
        {
              path: '/order',
              name:"Order",
              component: Order
        },
        {
              path: '/payments/result',
              name:"Order",
              component: Payment
        },
    ]
})
