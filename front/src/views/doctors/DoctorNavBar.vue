<template>
  <v-app-bar color="green" elevation="2" flat>
    <h1>DOCTOR</h1>
    <v-spacer></v-spacer>
    <router-link style="text-decoration: none" to="/myPatients">
      <v-btn><h2>PACIENTES</h2></v-btn>
    </router-link>
    <v-spacer></v-spacer>
    <router-link style="text-decoration: none" to="/myTeam">
      <v-btn><h2>MI EQUIPO</h2></v-btn>
    </router-link>
    <v-spacer></v-spacer>
    <router-link style="text-decoration: none" to="/doctor/profile">
      <v-btn><h2>MI CUENTA</h2></v-btn>
    </router-link>
    <v-spacer></v-spacer>
    <v-btn><h2>CERRAR SESIÓN</h2></v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: "DoctorNavBar"
}
</script>

<style scoped>

</style>
