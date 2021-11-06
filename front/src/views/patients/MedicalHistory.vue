<template>
  <v-container fluid class="ma-0 pa-0">
    <v-app-bar color="green" elevation="2" flat>
      <!--v-app-bar-nav-icon></v-app-bar-nav-icon-->
    </v-app-bar>
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
          <v-card-title>HISTORIAL MÉDICO</v-card-title>
          <v-row>
            <v-col cols="3">
              <v-card-text>Padecimiento</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="suffering" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Diagnosis</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="diagnosis" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Treatment</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="treatment" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Analysis</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="analysis" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Results</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="results" required></v-text-field>
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
let API_URL= 'https://5503-2806-2f0-9000-f884-3c43-128c-f17d-cfb9.ngrok.io';
export default {
  name: "MedicalHistory",
  data: () => ({
    patient: 1,
    doctor: 1,
    suffering: '',
    diagnosis: '',
    treatment: '',
    analysis: '',
    results: '',
    postId: -1,
    dialog: false,
  }),
  computed:{

  },
  methods:{
    async register(){
      if(this.suffering!='' && this.diagnosis!='' && this.treatment!='' && this.analysis!='' && this.results!=''){
        this.dialog=false;
        // POST request using fetch with async/await
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({patient: this.patient, doctor: this.doctor,suffering: this.suffering, diagnosis: this.diagnosis, treatment: this.treatment, analysis: this.analysis, results: this.results})
        };
        console.log(requestOptions.body);
        const response = await fetch(API_URL+"/api/history/create", requestOptions).then(async response => {
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

        console.log(this.suffering+' '+this.diagnosis+' '+this.treatment+' '+this.analysis+' '+this.results);
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