<template>
  <div>
    <h1>Reset Password</h1>
    <form @submit.prevent="resetPassword">
      <div>
        <label for="password">New Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Reset Password</button>
    </form>
    <div v-if="successMessage">{{ successMessage }}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      password: '',
      successMessage: '',
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
      axios.post(this.url + '/reset-password', data);
    }
  },
  mounted() {
    this.token = window.location.href.split('token=')[1];
    console.log(this.token);

  }
}
</script>