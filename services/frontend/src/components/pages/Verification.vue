<template>
<div v-if="isNotVerificated">

  <h1>Click to verify your email</h1>
  <setting-button @click="sendToken">Verify</setting-button>
</div>
<div v-else>
  <h1>You can finally login</h1>
  <setting-button @click="loginRedirect">Login</setting-button>
</div>
</template>

<script>
import axios from "axios";
import SettingButton from "@/components/UI/SettingButton.vue";
import router from "@/components/router/index.js";
export default {
  name: "Verifi-cation",
  components: {SettingButton},
  data() {
    return {

      isNotVerificated:true,
      token:'',
      url:process.env.VUE_APP_URL
    }
  },
  methods:{
    sendToken() {
      const data = {
        token: this.token,
      }
      const response = axios.post(this.url + '/verify', data)
      if(response.ok){
        this.isNotVerificated=false;
      }
    },
    loginRedirect(){
      router.push('/login');
    }

  },

  mounted() {
    this.token = window.location.href.split('token=')[1];
    console.log(this.token);

  }
}

</script>

<style scoped>
div{
  color:white;
}
</style>