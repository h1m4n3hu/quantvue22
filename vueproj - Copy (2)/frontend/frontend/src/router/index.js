import Vue from "vue";
import VueRouter from "vue-router";
import Test from '../components/Test.vue'
import Trkrs from '../components/Trkrs.vue'
import Login from '../components/Login.vue'


Vue.use(VueRouter);

const routes = [
 {
   path : '/',
   name : 'Login',
   component : Login,
 },
 {
   path : '/test',
   name : 'Test',
   component : Test,
 },
 {
   path : '/trkrs',
   name : 'Trkrs',
   component : Trkrs,
 }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
