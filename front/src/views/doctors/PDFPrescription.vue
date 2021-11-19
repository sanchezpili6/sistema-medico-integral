<template>
  <v-container fluid class="ma-0 pa-0">
    <DoctorNavBar></DoctorNavBar>
    <p>AQUI VAL PDF</p>
    <v-row class="text-center">
      <v-col class="mb-4 pa-15">
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-title>ERROR</v-card-title>
            <v-card-text>
              Lo sentimos. No hemos podido cargar el pdf. Inténtelo más tarde
            </v-card-text>
          </v-card>
        </v-dialog>
        <pdf :src="pdfsrc"></pdf>
        <!--v-btn @click="getPdf">CREAR PDF</v-btn-->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import DoctorNavBar from "./DoctorNavBar";
import router from "../../router";
import axios from "axios";
import pdf from 'vue-pdf';
let API_URL= 'https://9d9f-2806-2f0-9000-f884-cdbc-861c-b45f-61a3.ngrok.io';
export default {
  components:{
    DoctorNavBar,
    pdf
  },
  name: "PDFPrescription",
  data: () => ({
    dialog:false,
    responsePDF:'',
    pdfsrc: null
  }),
  created() {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      responseType: 'blob',
      body: JSON.stringify({pk: 22})
    };
    axios.post(API_URL, requestOptions).then(response => {
      console.log("Success", response);
      const blob = new Blob([response.data]);
      const objectUrl = URL.createObjectURL(blob);
      this.pdfsrc = objectUrl;
    })
  },
  /*async beforeCreate(){
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      responseType: 'blob',
      body: JSON.stringify({pk: 22})
    };
    console.log(requestOptions.body);
    const response = await fetch(API_URL+"/api/prescription/pdf", requestOptions).then(async response => {
      const data = response;
      // check for error response
      if (!response.ok) {
        this.dialog=true
        // get error message from body or default to response status
        const error = (data && data.message) || response.status;
        return Promise.reject(error);
      }else{
        this.pdfsrc = window.URL.createObjectURL(new Blob([response]));
        console.log("AQUISTOI EN EL PDF"+ response);
        /*const blob = new Blob([response.data]);
        const objectUrl = URL.createObjectURL(blob);
        this.pdfsrc = objectUrl;
        //await router.push({name: 'MyPatients'})
      }
      this.postId = data.id;
    }).catch(error => {
      this.dialog=true
      this.errorMessage = error;
      console.error('There was an error!', error);
    });
  }*/
}
</script>

<style scoped>

</style>