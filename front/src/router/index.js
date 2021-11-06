import Vue from 'vue'
import VueRouter from 'vue-router'
import Registration from "../views/patients/Registration";
import DoctorRegistration from "../views/doctors/DoctorRegistration";
import Home from "../views/patients/Home";
import MedicalHistory from "../views/patients/MedicalHistory";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    //component: Home
    //component: Registration
    //component: DoctorRegistration
    component: MedicalHistory
  },
  {
    path: '/registration',
    name: 'Registration',
  },
  {
    path: '/doctorRegistration',
    name: 'DoctorRegistration',
  },
  {
    path: '/medicalHistory',
    name: 'MedicalHistory',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
