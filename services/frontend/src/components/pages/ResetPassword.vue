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
export default {
  data() {
    return {
      password: '',
      successMessage: ''
    }
  },
  methods: {
    async resetPassword() {
      try {
        const response = await fetch('/api/reset_password', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            password: this.password
          })
        })
        const data = await response.json()
        this.successMessage = data.message
        this.email = ''
        this.password = ''
      } catch (error) {
        console.error(error)
        // Handle error and display error message to user
      }
    }
  }
}
</script>