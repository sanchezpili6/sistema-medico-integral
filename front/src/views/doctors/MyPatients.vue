<template>
  <v-container fluid class="ma-0 pa-0">
    <DoctorNavBar></DoctorNavBar>
    <v-card class="text-center">
      <v-card-title class="my-3"><v-spacer></v-spacer><h1>Pacientes</h1><v-spacer></v-spacer></v-card-title>
      <v-card-text>
        <v-simple-table>
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-center">
                Nombre
              </th>
              <th class="text-center">
                Póliza seguro
              </th>
              <th></th>
              <th></th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="item in patients"
                :key="item.name"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.policy }}</td>
              <td>
                <v-btn color="green">Historial</v-btn>
              </td>
              <td>
                <v-btn color="green">Recetas</v-btn>
              </td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card-text>
    </v-card>
    <!--router-link to="/registration" :docID="docId"-->
    <router-link :to="{name:'Registration', params:{docID: docId}}">
      <v-btn
          absolute
          fab
          large
          bottom
          right
          class="my-10"
          color="green"
      >
        <v-icon color="white" x-large>mdi-plus</v-icon>
      </v-btn>
    </router-link>
  </v-container>
</template>

<script>
import DoctorNavBar from "./DoctorNavBar";
import axios from "axios";
let API_URL= 'https://53e6-2806-2f0-9000-f884-c94c-ca23-2152-3e52.ngrok.io';
export default {
  async beforeCreate() {
    const response = await axios.get(API_URL + '/api/doctor/patients',  {params: {pk: 1}});//.then(response => this.totalVuePackages = response.data.total);
    console.log(response.data);
    this.patients=response.data;
  },
  name: "MyPatients",
  components:{
    DoctorNavBar
  },
  props: {
    //patients: Array,
  },
  methods:{

  },
  data () {
    return {
      docId:1,
      patients: [],
      /*patients: [
        {
          name: 'Jackie bb',
          poliza: 1234
        },
        {
          name: 'Jackie bb',
          poliza: 1234
        },
        {
          name: 'Jackie bb',
          poliza: 1234
        },
        {
          name: 'Jackie bb',
          poliza: 1234
        },
      ],*/
    }
  },
}
</script>

<style scoped>
</style>
