<template>
  <div class="language-page">
    <h1>Language Settings</h1>
    <form v-if="!editing" @submit.prevent="saveSettings">
      <div class="form-group">
        <label for="username">Username:</label>
        <input class="username" id="username" v-model="username" :disabled="!editing">
      </div>


      <div class="form-group">
        <label for="english-level">English Level:</label>
        <select id="english-level" v-model="englishLevel" :disabled="!editing">
          <option value="A1">A1 - Beginner</option>
          <option value="A2">A2 - Elementary</option>
          <option value="B1">B1 - Intermediate</option>
          <option value="B2">B2 - Upper Intermediate</option>
          <option value="C1">C1 - Advanced</option>
          <option value="C2">C2 - Proficient</option>
        </select>
      </div>
      <div class="form-group">
        <label for="target-level">Target Level of English:</label>
        <select id="target-level" v-model="targetLevel" :disabled="!editing">
          <option value="A1">A1 - Beginner</option>
          <option value="A2">A2 - Elementary</option>
          <option value="B1">B1 - Intermediate</option>
          <option value="B2">B2 - Upper Intermediate</option>
          <option value="C1">C1 - Advanced</option>
          <option value="C2">C2 - Proficient</option>
        </select>
      </div>
      <div class="form-group">
        <label for="native-language">Native Language:</label>
        <select id="native-language" v-model="nativeLanguage" :disabled="!editing">
          <option value="Spanish">Spanish</option>
          <option value="Ukrainian">Ukrainian</option>

        </select>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="!editing">Save Settings</button>
      <button @click.prevent="editSettings" class="btn btn-secondary" :disabled="editing">Edit Settings</button>
    </form>
    <form v-if="editing" @submit.prevent="saveSettings">

      <div class="form-group">
        <label for="username">Username:</label>
        <input class="username" id="username" v-model="username">
      </div>
      <div class="form-group">
        <label for="english-level">English Level:</label>
        <select id="english-level" v-model="englishLevel">
          <option value="A1">A1 - Beginner</option>
          <option value="A2">A2 - Elementary</option>
          <option value="B1">B1 - Intermediate</option>
          <option value="B2">B2 - Upper Intermediate</option>
          <option value="C1">C1 - Advanced</option>
          <option value="C2">C2 - Proficient</option>
        </select>
      </div>
      <div class="form-group">
        <label for="target-level">Target Level of English:</label>
        <select id="target-level" v-model="targetLevel">
          <option value="A1">A1 - Beginner</option>
          <option value="A2">A2 - Elementary</option>
          <option value="B1">B1 - Intermediate</option>
          <option value="B2">B2 - Upper Intermediate</option>
          <option value="C1">C1 - Advanced</option>
          <option value="C2">C2 - Proficient</option>
        </select>
      </div>
      <div class="form-group">
        <label for="native-language">Native Language:</label>
        <select id="native-language" v-model="nativeLanguage">
          <option value="Spanish">Spanish</option>
          <option value="Ukrainian">Ukrainian</option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Save Settings</button>
      <button @click.prevent="cancelEdit" class="btn btn-secondary">Cancel</button>
    </form>
  </div>
</template>
<script>

export default {
  data() {
    return {
      editing: false,
      targetLevel: 'A1',
      username: '',
      englishLevel: 'A1',
      nativeLanguage: 'English',
      savedSettings: null,
      url: process.env.VUE_APP_URL
    }
  },
  created() {
    const jwt = localStorage.getItem("jwt");
    fetch(this.url + '/settings', {
      method: 'GET',
      headers: {
        'Cookie': jwt,

      },
      credentials: 'include',
    })
        .then(response => response.json())
        .then(data => {
          this.savedSettings = data
          this.targetLevel = data.goal_level.toUpperCase()
          this.username = data.user_name
          this.englishLevel = data.user_level.toUpperCase()
          this.nativeLanguage = data.native_language
        })
        .catch(error => console.error(error))


  },
  methods: {
    editSettings() {
      this.editing = true
    },
    cancelEdit() {
      this.editing = false
    },
    async saveSettings() {
      const jwt = localStorage.getItem("jwt");
      const data = {
        user_name: this.username,
        user_level: this.englishLevel.toLowerCase(),
        goal_level: this.targetLevel.toLowerCase(),
        native_language: this.nativeLanguage,
      };

      try {
        const response = await fetch(`${this.url}/settings`, {
          method: 'PUT',
          headers: {
            'Accept-Language': 'en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,uk;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Cookie': jwt,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'accept': 'application/json'
          },
          body: JSON.stringify(data),
          credentials: 'include',
        });

        if (response.ok) {
          this.savedSettings = data;
          this.editing = false;
        } else {
          throw new Error('Failed to save settings');
        }
      } catch (error) {
        console.error(error);
        alert('Failed to save settings');
      }
    }

  }
}

</script>
<style scoped>
.language-page {
  max-width: 700px;
  margin: 0 auto;
  padding: 2rem;
  background-color: white;
  color: #444;
  border-radius: 40px;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #666;
}

.username {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 3px;
  background-color: #f9f9f9;
  color: #444;
}

select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 3px;
  background-color: #f9f9f9;
  color: #444;
}

select:disabled {
  background-color: #f3f3f3;
}

.btn {
  padding: 0.5rem 1rem;
  border-radius: 3px;
  border: none;
  cursor: pointer;
}

.btn-primary {
  background-color: #464646;
  color: white;
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-secondary {
  background-color: #464646;
  color: white;
  margin-left: 1rem;
}

.btn-secondary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

</style>
