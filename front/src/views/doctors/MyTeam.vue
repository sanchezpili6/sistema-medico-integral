<template>
  <v-container fluid class="ma-0 pa-0">
    <DoctorNavBar></DoctorNavBar>
    <v-card class="text-center">
      <v-card-title class="my-3"><v-spacer></v-spacer><h1>MI EQUIPO</h1><v-spacer></v-spacer></v-card-title>
      <v-card-subtitle class="my-3"><v-spacer></v-spacer><h1>Código de equipo: {{teamCode}}</h1><v-spacer></v-spacer></v-card-subtitle>
      <v-card-text>
        <v-simple-table>
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-center">
                Nombre
              </th>
              <th class="text-center">
                Especialidad
              </th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="item in team"
                :key="item.name"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.specialty }}</td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import DoctorNavBar from "./DoctorNavBar";
export default {
  name: "MyTeam",
  components:{
    DoctorNavBar
  },
  data () {
    return {
      teamCode: 1,
      team: [
        {
          name: 'Jackie bb',
          specialty: 'cardiología'
        },{
          name: 'Jackie bb',
          specialty: 'cardiología'
        },{
          name: 'Jackie bb',
          specialty: 'cardiología'
        },{
          name: 'Jackie bb',
          specialty: 'cardiología'
        },
      ],
    }
  },
}
</script>

<style scoped>

</style>
