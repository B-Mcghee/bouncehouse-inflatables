import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
  },
  {
    path: '/products/',
    name: 'ProductList',
    component: function () {
      return import(/* webpackChunkName: "products" */ '../views/products/ProductList.vue')
    }
  },
  {
    path:'/products/inflatable/:slug',
    name: 'SingleProduct',
    component:function(){
      return import('../views/products/Product.vue')
    },
    props:true
    // children:[
    //   {
    //     path: 'inflatable/:slug',
    //     name:'SingleProduct',
    //     component: function () {
    //       return import('../views/products/Product.vue')
    //     }
    //   }
    // ]
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: function () {
      return import(/* webpackChunkName: "products" */ '../views/checkout/Review.vue')
    },
    children:[
      {
        path: 'customer',
        name: 'Customer',
        component: function () {
          return import(/* webpackChunkName: "products" */ '../views/checkout/Customer.vue')
        }
      },
    ]
  },
  // {
  //   path: '/checkout/customer',
  //   name: 'Customer',
  //   component: function () {
  //     return import(/* webpackChunkName: "products" */ '../views/checkout/Customer.vue')
  //   }
  // },
  {
    path: '/checkout/payment',
    name: 'Payment',
    component: function () {
      return import(/* webpackChunkName: "products" */ '../views/checkout/Payment.vue')
    }
  },
  {
    path:"*",
    redirect:'/'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
