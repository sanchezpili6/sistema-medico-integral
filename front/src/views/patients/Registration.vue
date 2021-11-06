<template>
  <v-container fluid class="ma-0 pa-0">
    <v-app-bar color="green" elevation="2" flat>
      <!--v-app-bar-nav-icon></v-app-bar-nav-icon-->
    </v-app-bar>
    <v-row class="text-center">
      <v-col class="mb-4 pa-15">
        <v-card class="mx-auto my-10" max-width="600">
          <v-card-title>REGISTRO PACIENTE</v-card-title>
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
export default {
  name: "Registration",
  data: () => ({
    apellidos: '',
    nombre: '',
    nss: '',
    poliza: '',
  }),
  computed:{

  },
  methods:{
    register:function(){
      console.log(this.nombre+" "+ this.apellidos+" "+this.nss+" "+ this.poliza);
    }
  }
}
</script>

<style scoped>

</style>