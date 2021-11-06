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
        <v-row><h2>Cédula profesional: {{license}}</h2></v-row>
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
            <v-list-item>
              Último tratamiento: {{receta.lastTreatment}}
            </v-list-item>
            <v-list-item>
              Medicamento recetado: {{receta.medicine}}
            </v-list-item>
            <v-list-item>
              Cédula profesional: {{receta.license}}
            </v-list-item>
          </v-list>
          <v-btn color="green">IMPRIMIR PDF</v-btn>
        </v-card-text>
      </v-card>
      <v-spacer></v-spacer>
    </v-row>
  </v-container>
</template>

<script>
import DoctorNavBar from "./DoctorNavBar";
export default {
  name: "MyProfile",
  components:{
    DoctorNavBar
  },
  data (){
    return {
      name: 'Pili',
      specialty: 'mimir',
      license: '6',
      college: 'udemy',
      affiliation: 'none',
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
  }
}
</script>

<style scoped>

</style>
