<template>
  <v-container fluid class="ma-0 pa-0">
    <v-app-bar color="green" elevation="2" flat>
      <h1>SISTEMA MÉDICO INTEGRAL</h1>
      <v-spacer></v-spacer>
      <router-link style="text-decoration: none" to="/myPatients">
        <v-btn><h2>INICIAR SESIÓN</h2></v-btn>
      </router-link>
      <v-spacer></v-spacer>
      <router-link style="text-decoration: none" to="/myTeam">
        <v-btn><h2>REGISTRARSE</h2></v-btn>
      </router-link>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-row>
      <v-col cols="6" class="my-5">
        <v-img
            max-height="80%"
            src="https://as2.ftcdn.net/v2/jpg/04/26/99/95/1000_F_426999565_AJdlhzyu9f3kL5T6cXlZJfkg4AoCDc6E.jpg"
        >
        </v-img>
      </v-col>
      <v-col>
        <h1 class="welcome my-10"> Bienvenid@ a nuestro sistema médico integral </h1>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Welcome"
}
</script>

<style scoped>
.welcome{
  font-size: 100px;
}
</style>
