import Vue from 'vue'
import VueRouter from 'vue-router'
import Registration from "../views/patients/Registration";
import DoctorRegistration from "../views/doctors/DoctorRegistration";
import Home from "../views/patients/Home";
import MedicalHistory from "../views/patients/MedicalHistory";
import MyPatients from "../views/doctors/MyPatients";
import MyTeam from "../views/doctors/MyTeam";
import MyProfile from "../views/doctors/MyProfile";
import Welcome from "../views/Welcome";
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Welcome
  },
  {
    path: '/registration',
    name: 'Registration',
    component: Registration
  },
  {
    path: '/doctorRegistration',
    name: 'DoctorRegistration',
    component: DoctorRegistration
  },
  {
    path: '/medicalHistory',
    name: 'MedicalHistory',
    component: MedicalHistory
  },
  {
    path: '/myPatients',
    name: 'MyPatients',
    component: MyPatients
  },
  {
    path: '/myTeam',
    name: 'MyTeam',
    component: MyTeam
  },
  {
    path: '/doctor/profile',
    name: 'MyProfile',
    component: MyProfile
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
