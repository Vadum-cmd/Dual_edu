<template>
<div>
  <h1>Click to verify your email</h1>
  <setting-button @click="sendToken">Verify</setting-button>
</div>

</template>

<script>
import axios from "axios";
import SettingButton from "@/components/UI/SettingButton.vue";
export default {
  name: "Verifi-cation",
  components: {SettingButton},
  data() {
    return {


      token:'',
      url:process.env.VUE_APP_URL
    }
  },
  methods:{
    sendToken() {
      const data = {
        token: this.token,
      }
      axios.post(this.url + '/verify', data)
    }
  },

  mounted() {
    this.token = window.location.href.split('token=')[1];
    console.log(this.token);

  }
}

</script>

<style scoped>

</style>