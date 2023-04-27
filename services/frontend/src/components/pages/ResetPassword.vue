<template>
  <div v-if="!success">
    <h1>Reset Password</h1>
    <form @submit.prevent="resetPassword">
      <div>
        <label for="password">New Password:</label>
        <input class="password" type="password" id="password" v-model="password" required>
      </div>
      <setting-button type="submit">Reset Password</setting-button>
    </form>
  </div>
  <div v-else>
    <h1>You can finally login</h1>
    <setting-button @click="loginRedirect">Login</setting-button>
  </div>
</template>

<script>
import axios from "axios";
import router from "@/components/router/index.js";
import SettingButton from "@/components/UI/SettingButton.vue";
export default {
  components: {SettingButton},
  data() {
    return {
      password: '',
      success: false,
      url: process.env.VUE_APP_URL,
      token: ''
    }
  },
  methods: {
    resetPassword() {
      const data = {
        password: this.password,
        token: this.token
      }
      axios.post(this.url + '/reset-password', data)
          .then(response => {
            if (response.status === 200) {
              this.success = true;
            } else {
              alert("Something went wrong. Please try again.");
            }
          })
    },
    loginRedirect(){
      router.push('/login');
    },
  },
  mounted() {
    this.token = window.location.href.split('token=')[1];

  }
}
</script>
<style scoped>
div{
  color:white;

}
.password{
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>