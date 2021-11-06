<template>
  <v-app-bar color="green" elevation="2" flat>
    <h1>SISTEMA MÉDICO INTEGRAL</h1>
    <v-spacer></v-spacer>
    <router-link style="text-decoration: none" to="/login">
      <v-btn><h2>INICIAR SESIÓN</h2></v-btn>
    </router-link>
    <v-spacer></v-spacer>
    <router-link style="text-decoration: none" to="/myTeam">
      <v-btn><h2>REGISTRARSE</h2></v-btn>
    </router-link>
    <v-spacer></v-spacer>
  </v-app-bar>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style scoped>

</style>
