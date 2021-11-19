<template>
  <v-app-bar color="green" elevation="2" flat>
    <h1>DOCTOR</h1>
    <v-spacer></v-spacer>
    <router-link style="text-decoration: none" to="/myPatients">
      <v-btn><h2>PACIENTES</h2></v-btn>
    </router-link>
    <v-spacer></v-spacer>
    <router-link style="text-decoration: none" to="/myTeam">
      <v-btn><h2>MI EQUIPO</h2></v-btn>
    </router-link>
    <v-spacer></v-spacer>
    <router-link style="text-decoration: none" to="/doctor/profile">
      <v-btn><h2>MI CUENTA</h2></v-btn>
    </router-link>
    <v-spacer></v-spacer>
    <v-btn><h2>CERRAR SESIÓN</h2></v-btn>
  </v-app-bar>
</template>

<script>
import axios from "axios";
let API_URL= 'https://9d9f-2806-2f0-9000-f884-cdbc-861c-b45f-61a3.ngrok.io';
export default {
  name: "DoctorNavBar",
  data () {
    return {
      docId:1,
    }
  },
  methods:{
    async getPatients(){
      console.log("get");
      // GET request using axios with set headers
      const headers = { "Content-Type": "application/json" };
      const response = await axios.get(API_URL + '/api/doctor/patients', {headers}, {params: this.docId});//.then(response => this.totalVuePackages = response.data.total);
      console.log(response);
      console.log("get");
    },
  }
}
</script>

<style scoped>
</style>