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
              <td>
                <v-btn color="green" @click="savePatient(item.id, item.name)">Crear nueva receta</v-btn>
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
import router from "../../router";
let API_URL= 'https://9d9f-2806-2f0-9000-f884-cdbc-861c-b45f-61a3.ngrok.io';
export default {
  async beforeCreate() {
    this.docId=localStorage.getItem('ID'); //CERTIFICADO
    this.bdID=localStorage.getItem('bdID'); //ID DEL JSON
    console.log("ID: "+localStorage.getItem('bdID'));
    //console.log("holaaa "+this.docId);
    const response = await axios.get(API_URL + '/api/doctor/patients',  {params: {pk: this.bdID}});//.then(response => this.totalVuePackages = response.data.total);
    console.log(response.data);
    this.patients=response.data;
  },
  name: "MyPatients",
  components:{
    DoctorNavBar
  },
  data () {
    return {
      docId:'',
      bdID:'',
      patientID:'',
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
  methods:{
    async savePatient(newID, newName){
      this.patientID=newID
      localStorage.setItem('patientID', this.patientID)
      localStorage.setItem('patientName', newName)
      console.log("Patient ID "+ this.patientID)
      await router.push({name: 'Prescription'})
    }
  }
}
</script>

<style scoped>
</style>
