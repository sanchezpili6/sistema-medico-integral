<template>
  <v-container fluid class="ma-0 pa-0">
    <DoctorNavBar></DoctorNavBar>
    <v-card class="text-center">
      <v-card-title><v-spacer></v-spacer><h1>Pacientes</h1><v-spacer></v-spacer></v-card-title>
      <v-card-text>
        <v-simple-table>
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-center">
                Nombre
              </th>
              <th class="text-center">
                Póliza seguro
              </th>
              <th></th>
              <th></th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="item in patients"
                :key="item.name"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.poliza }}</td>
              <td>
                <v-btn color="green">Historial</v-btn>
              </td>
              <td>
                <v-btn color="green">Recetas</v-btn>
              </td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card-text>
    </v-card>
    <router-link to="/registration">
      <v-btn
          absolute
          fab
          large
          bottom
          right
          class="my-10"
          color="green"
      >
        <v-icon color="white" x-large>mdi-plus</v-icon>
      </v-btn>
    </router-link>
  </v-container>
</template>

<script>
import DoctorNavBar from "./DoctorNavBar";
export default {
  name: "MyPatients",
  components:{
    DoctorNavBar
  },
  data () {
    return {
      patients: [
        {
          name: 'Jackie bb',
          poliza: 1234
        },
        {
          name: 'Jackie bb',
          poliza: 1234
        },
        {
          name: 'Jackie bb',
          poliza: 1234
        },
        {
          name: 'Jackie bb',
          poliza: 1234
        },
      ],
    }
  },
}
</script>

<style scoped>
</style>
