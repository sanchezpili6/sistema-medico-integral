<template>
  <v-container fluid class="ma-0 pa-0">
    <NavBar></NavBar>
    <v-row class="text-center">
      <v-col class="mb-1">
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-title>Faltan datos</v-card-title>
            <v-card-text>
              Por favor asegúrese de llenar todos los campos o que no esté ya registrado
            </v-card-text>
          </v-card>
        </v-dialog>
        <v-card class="mx-auto my-10" max-width="600">
          <v-card-title>INICIAR SESIÓN</v-card-title>
          <v-row class="my-5">
            <v-spacer></v-spacer>
            <v-btn @click="displayPatient">PACIENTE</v-btn>
            <v-spacer></v-spacer>
            <v-btn @click="displayDoctor">DOCTOR</v-btn>
            <v-spacer></v-spacer>
            <v-btn @click="displayAdmin">ADMIN</v-btn>
            <v-spacer></v-spacer>
          </v-row>
          <v-row v-show="patient">
            <v-col cols="3">
              <v-card-text>NSS</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="nss" required></v-text-field>
            </v-col>
          </v-row>
          <v-row v-show="doctor">
            <v-col cols="3">
              <v-card-text>Cédula profesional</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="license" required></v-text-field>
            </v-col>
          </v-row>
          <v-row v-show="admin">
            <v-col cols="3">
              <v-card-text>Correo</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="email" required></v-text-field>
            </v-col>
          </v-row>
          <v-flex class="text-center" v-show="doctor">
            <v-btn @click="login_doctor" color="green" class="ma-4">Entrar doc</v-btn>
          </v-flex>
          <v-flex class="text-center" v-show="patient">
            <v-btn @click="login_patient" color="green" class="ma-4">Entrar paciente</v-btn>
          </v-flex>
          <v-flex class="text-center" v-show="admin">
            <v-btn @click="login_doctor" color="green" class="ma-4">Registrar</v-btn>
          </v-flex>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
let API_URL= 'https://e1aa-2806-2f0-9000-f884-c94c-ca23-2152-3e52.ngrok.io';
import NavBar from "./NavBar";
export default {
  name: "Login",
  components:{
    NavBar
  },
  data(){
    return{
      nss: '',
      license: '',
      email: '',
      patient: false,
      doctor: false,
      admin: false
    }
  },
  methods:{
    async login_doctor(){
      if(this.license!=''){
        this.dialog=false;
        // POST request using fetch with async/await
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({certificate: this.license})
        };
        console.log(requestOptions.body);
        const response = await fetch(API_URL+"/api/doctor/login", requestOptions).then(async response => {
          const data = await response.json();
          console.log(data)
          // check for error response
          if (!response.ok) {
            // get error message from body or default to response status
            const error = (data && data.message) || response.status;
            return Promise.reject(error);
          }
        }).catch(error => {
          this.errorMessage = error;
          console.error('There was an error!', error);
        });
      }
      else{
        this.dialog=true;
      }
    },
    async login_patient(){
      if(this.nss!=''){
        this.dialog=false;
        // POST request using fetch with async/await
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({nss: this.nss})
        };
        console.log(requestOptions.body);
        const response = await fetch(API_URL+"/api/patient/login", requestOptions).then(async response => {
          const data = await response.json();
          console.log(data)
          // check for error response
          if (!response.ok) {
            // get error message from body or default to response status
            const error = (data && data.message) || response.status;
            return Promise.reject(error);
          }
        }).catch(error => {
          this.errorMessage = error;
          console.error('There was an error!', error);
        });
      }
      else{
        this.dialog=true;
      }
    },
    displayDoctor(){
      this.patient = false
      this.doctor = true
      this.admin = false
    },
    displayPatient(){
      this.patient = true
      this.doctor = false
      this.admin = false
    },
    displayAdmin(){
      this.patient = false
      this.doctor = false
      this.admin = true
    }
  }
}
</script>

<style scoped>

</style>
