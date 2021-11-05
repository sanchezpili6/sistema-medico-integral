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
              <v-card-text>Nombre</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="Nombre" :counter="10" :rules="nameRules" label="Nombre" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>NSS</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="NSS" label="Nss" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="3">
              <v-card-text>Póliza</v-card-text>
            </v-col>
            <v-col cols="8">
              <v-text-field v-model="Poliza" :counter="10" :rules="nameRules" label="Poliza" required></v-text-field>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Registration"
}
</script>

<style scoped>

</style>