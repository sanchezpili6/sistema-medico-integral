<template>
  <v-container fluid class="ma-0 pa-0">
    <DoctorNavBar></DoctorNavBar>
    <!--v-app-bar color="green" elevation="2" flat></v-app-bar-->
    <v-row class="text-center">
      <v-col class="mb-4 pa-15">
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-title>ERROR</v-card-title>
            <v-card-text>
              Por favor asegúrese de llenar el campo de tratamiento
            </v-card-text>
          </v-card>
        </v-dialog>
        <v-card class="mx-auto my-10" max-width="600">
          <v-card-title>AGREGAR TRATAMIENTO A: {{this.patientName}}</v-card-title>
          <v-row>
            <v-col cols="3">
              <v-card-text>Tratamiento</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="treatment" required></v-text-field>
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
import router from "../../router";
let API_URL= 'https://9d9f-2806-2f0-9000-f884-cdbc-861c-b45f-61a3.ngrok.io';
export default {
  name: "Prescription",
  components:{
    DoctorNavBar
  },
  created() {
    this.docID=localStorage.getItem('bdID');
    this.patientID=localStorage.getItem('patientID');
    this.patientName=localStorage.getItem('patientName');
    console.log('From Prescription docID: '+ this.docID+' patientID:'+this.patientID)
  },
  props: {
    //docID: Number,
  },
  data: () => ({
    docID:'',
    patientID:'',
    patientName:'',
    treatment: '',
    postId: -1,
    dialog: false,
  }),
  computed:{

  },
  methods:{
    async register(){
      if(this.treatment!='' ){
        this.dialog=false;
        // POST request using fetch with async/await
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({medicine: this.treatment, doctor: this.docID, patient: this.patientID})
        };
        console.log(requestOptions.body);
        const response = await fetch(API_URL+"/api/prescription/create", requestOptions).then(async response => {
          const data = await response.json();
          console.log(data);
          // check for error response
          if (!response.ok) {
            this.dialog=true
            // get error message from body or default to response status
            const error = (data && data.message) || response.status;
            return Promise.reject(error);
          }else{
            localStorage.setItem('prescriptionID', data.pk)
            await router.push({name: 'PDFPrescription'})
          }
          this.postId = data.id;
        }).catch(error => {
          this.dialog=true
          this.errorMessage = error;
          console.error('There was an error!', error);
        });

        //console.log(this.treatment);
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