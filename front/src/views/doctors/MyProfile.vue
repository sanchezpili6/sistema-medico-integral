<template>
  <v-container fluid class="ma-0 pa-0">
    <DoctorNavBar></DoctorNavBar>
    <v-row class="my-3 mx-3">
      <v-col cols="3">
        <v-avatar size="200" color="green"></v-avatar>
      </v-col>
      <v-col>
        <v-row><h2>Nombre: {{name}}</h2></v-row>
        <v-row><h2>Especialidad: {{specialty}}</h2></v-row>
        <v-row><h2>Cédula profesional: {{doctorId}}</h2></v-row>
      </v-col>
      <v-col>
        <v-row><h2>Universidad: {{college}}</h2></v-row>
        <v-row><h2>Afiliacion: {{affiliation}}</h2></v-row>
      </v-col>
    </v-row>
    <v-row>
      <v-spacer></v-spacer>
      <h1>MIS RECETAS</h1>
      <v-spacer></v-spacer>
    </v-row>
    <v-row class="my-5">
      <v-spacer></v-spacer>
      <v-card class="mx-10 my-5" v-for="receta in recetas" elevation="12">
        <v-card-title>
          Receta
        </v-card-title>
        <v-card-text>
          <v-list>
            <v-list-item>
              Paciente: {{receta.patient}}
            </v-list-item>
            <v-list-item>
              Nombre médico: {{receta.doctor}}
            </v-list-item>
            <!--v-list-item>
              Último tratamiento: {{receta.lastTreatment}}
            </v-list-item-->
            <v-list-item>
              Medicamento recetado: {{receta.medicine}}
            </v-list-item>
            <v-list-item>
              Cédula profesional: {{receta.license}}
            </v-list-item>
          </v-list>
          <v-btn color="green" @click="viewPDF()">IMPRIMIR PDF</v-btn>
        </v-card-text>
      </v-card>
      <v-spacer></v-spacer>
    </v-row>
  </v-container>
</template>

<script>
import pdf from 'vue-pdf'
let API_URL= 'https://9d9f-2806-2f0-9000-f884-cdbc-861c-b45f-61a3.ngrok.io';
let getPDF= 'https://583c-2806-2f0-9000-f884-c013-4193-53ee-aa14.ngrok.io/';
import DoctorNavBar from "./DoctorNavBar";
export default {
  name: "MyProfile",
  components:{
    DoctorNavBar,
    pdf
  },
  watch:{
    doctorId(newDoctorId){
      localStorage.doctorId = newDoctorId
    },
    doctorResponse(newDoctorName){
      localStorage.doctorName = newDoctorName
    },
  },
  async created() {
        // POST request using fetch with async/await
        let doctorId = this.$route.query.Id;
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({certificate: doctorId})
        };
        console.log(this.doctorId)
        const response =  await fetch(API_URL+"/api/doctor/login", requestOptions).then(async response => {
          this.doctorResponse = await response.json();
          this.bdID = this.doctorResponse.id
          this.name = this.doctorResponse.name
          this.specialty = this.doctorResponse.specialty
          this.college = this.doctorResponse.university
          this.affiliation = this.doctorResponse.affiliation
          this.doctorId = this.doctorResponse.certificate
          console.log(this.doctorResponse)
          localStorage.setItem('bdID', this.bdID)
          // check for error response
          if (!response.ok) {
            // get error message from body or default to response status
            const error = (this.doctorResponse && this.doctorResponse.message) || response.status;
            return Promise.reject(error);
          }
          else{
            localStorage.setItem('ID', doctorId)
          }
        }).catch(error => {
          this.errorMessage = error;
          console.error('There was an error!', error);
        });
  },
  data (){
    return {
      doctorId:'',
      name: '',
      specialty: '',
      college: '',
      affiliation: '',
      bdID:'',
      recetas:[
        { patient: 'Fersito',
          doctor: 'Pili',
          lastTreatment: '12-02-2021',
          medicine: 'Tempra',
          license: 6
        },
        { patient: 'Fersito',
          doctor: 'Pili',
          lastTreatment: '12-02-2021',
          medicine: 'Tempra',
          license: 6
        },
        { patient: 'Fersito',
          doctor: 'Pili',
          lastTreatment: '12-02-2021',
          medicine: 'Tempra',
          license: 6
        },
        { patient: 'Fersito',
          doctor: 'Pili',
          lastTreatment: '12-02-2021',
          medicine: 'Tempra',
          license: 6
        },
      ]
    }
  },
  methods:{
    viewPDF(){
      window.location.href = "https://paraimprimir.org/wp-content/uploads/2014/03/Formato-de-receta-medica-para-imprimir.pdf"
    }
  }
}
</script>

<style scoped>

</style>
