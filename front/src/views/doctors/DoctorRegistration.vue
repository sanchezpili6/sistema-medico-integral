<template>
  <v-container fluid class="ma-0 pa-0">
    <v-app-bar color="green" elevation="2" flat>
      <!--v-app-bar-nav-icon></v-app-bar-nav-icon-->
    </v-app-bar>
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
          <v-card-title>REGISTRO DOCTOR</v-card-title>
          <v-row>
            <v-col cols="3">
              <v-card-text>Nombre</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="name" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Especialidad</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="specialty" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Certificado</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="certificate" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>University</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="university" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Affiliation</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="affiliation" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Team</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="team" required></v-text-field>
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
let API_URL= 'https://d730-2806-2f0-9000-f884-3c43-128c-f17d-cfb9.ngrok.io';
export default {
  name: "DoctorRegistration",
  data: () => ({
    name: '',
    specialty: '',
    certificate: '',
    university: '',
    affiliation: '',
    team: '',
    postId: -1,
    dialog: false,
  }),
  computed:{  },
  methods:{
    async register(){
      if(this.name!='' && this.specialty!='' && this.certificate!='' && this.university!='' && this.affiliation!='' && this.team!=''){
        this.dialog=false;
        // POST request using fetch with async/await
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({name: this.name, specialty: this.specialty, certificate: this.certificate, university:this.university, affiliation: this.affiliation, team: this.team})
        };
        console.log(requestOptions.body);
        const response = await fetch(API_URL+"/api/doctor/create", requestOptions).then(async response => {
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

        console.log(this.name+" "+ this.specialty+" "+this.certificate+" "+this.university+" "+this.affiliation+" "+this.team);
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