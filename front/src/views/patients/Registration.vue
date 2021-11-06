<template>
  <v-container fluid class="ma-0 pa-0">
    <DoctorNavBar></DoctorNavBar>
    <!--v-app-bar color="green" elevation="2" flat></v-app-bar-->
    <v-row class="text-center">
      <v-col class="mb-4 pa-15">
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-title>Faltan datos</v-card-title>
            <v-card-text>
              Por favor asegúrese de llenar todos los campos y que su nss no esté ya registrado
            </v-card-text>
          </v-card>
        </v-dialog>
        <v-card class="mx-auto my-10" max-width="600">
          <v-card-title>REGISTRO PACIENTE {{this.$props.docID}}</v-card-title>
          <v-row>
            <v-col cols="3">
              <v-card-text>Nombre(s)</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="nombre" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Apellidos</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="apellidos" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>NSS</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="nss" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Póliza</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="poliza" required></v-text-field>
            </v-col>
          </v-row>
          <v-flex class="text-center">
              <v-btn @click="register" color="green" class="ma-4">Registrar</v-btn>
          </v-flex>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import DoctorNavBar from "../doctors/DoctorNavBar";
let API_URL= 'https://c775-2806-2f0-9000-f884-c94c-ca23-2152-3e52.ngrok.io';
export default {
  name: "Registration",
  components:{
    DoctorNavBar
  },
  props: {
    docID: Number,
  },
  data: () => ({
    apellidos: '',
    nombre: '',
    nss: '',
    poliza: '',
    postId: -1,
    dialog: false,
  }),
  computed:{

  },
  methods:{
    async register(){
      if(this.nombre!='' && this.apellidos!='' && this.nss!='' && this.poliza!=''){
        this.dialog=false;
        // POST request using fetch with async/await
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({name: this.nombre, last_name: this.apellidos, nss: this.nss, policy:this.poliza, doctor: this.$props.docID})
        };
        console.log(requestOptions.body);
        const response = await fetch(API_URL+"/api/patient/create", requestOptions).then(async response => {
          const data = await response.json();
          // check for error response
          if (!response.ok) {
            // get error message from body or default to response status
            const error = (data && data.message) || response.status;
            return Promise.reject(error);
          }

          this.postId = data.id;
        }).catch(error => {
              this.errorMessage = error;
              console.error('There was an error!', error);
            });

        console.log(this.nombre+" "+ this.apellidos+" "+this.nss+" "+ this.poliza+" "+this.$props.docID);
      }
      else{
        this.dialog=true;
      }
    }
  }
}
</script>

<style scoped>

</style>