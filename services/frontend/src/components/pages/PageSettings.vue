<template>
  <div class="language-page">
    <h1>Language Settings</h1>
    <form v-if="!editing" @submit.prevent="saveSettings">
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
        <label for="email">Email Address:</label>
        <input type="email" id="email" v-model="email" :disabled="!editing">
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
        <label for="native-language">Native Language:</label>
        <select id="native-language" v-model="nativeLanguage" :disabled="!editing">
          <option value="English">English</option>
          <option value="Spanish">Spanish</option>
          <option value="French">French</option>
          <option value="German">German</option>
          <option value="Ukrainian">Ukrainian</option>
          <option value="Arabic">Arabic</option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="!editing">Save Settings</button>
      <button @click.prevent="editSettings" class="btn btn-secondary" :disabled="editing">Edit Settings</button>
    </form>
    <form v-if="editing" @submit.prevent="saveSettings">
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
        <label for="email">Email Address:</label>
        <input type="email" id="email" v-model="email">
      </div>
      <div class="form-group">
        <label

            for="english-level">English Level:</label>
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
        <label for="native-language">Native Language:</label>
        <select id="native-language" v-model="nativeLanguage">
          <option value="English">English</option>
          <option value="Spanish">Spanish</option>
          <option value="French">French</option>
          <option value="German">German</option>
          <option value="Ukrainian">Ukrainian</option>
          <option value="Arabic">Arabic</option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Save Settings</button>
      <button @click.prevent="cancelEditing" class="btn btn-secondary">Cancel Editing</button>
    </form>

  </div>
</template>
<script>
export default {
  data() {
    return {
      targetLevel: "",
      email: "",
      englishLevel: "",
      nativeLanguage: "",
      editing: false,
      savedSettings: {
        targetLevel: "",
        email: "",
        englishLevel: "",
        nativeLanguage: "",
      },
    };
  },
  methods: {
    saveSettings() {
      this.savedSettings.targetLevel = this.targetLevel;
      this.savedSettings.email = this.email;
      this.savedSettings.englishLevel = this.englishLevel;
      this.savedSettings.nativeLanguage = this.nativeLanguage;
      this.editing = false;
    },
    editSettings() {
      this.editing = true;
    },
    cancelEditing() {
      this.targetLevel = this.savedSettings.targetLevel;
      this.email = this.savedSettings.email;
      this.englishLevel = this.savedSettings.englishLevel;
      this.nativeLanguage = this.savedSettings.nativeLanguage;
      this.editing = false;
    },
  },
  mounted() {
    this.savedSettings.targetLevel = this.targetLevel;
    this.savedSettings.email = this.email;
    this.savedSettings.englishLevel = this.englishLevel;
    this.savedSettings.nativeLanguage = this.nativeLanguage;
  },
};
</script>
<style scoped>
.language-page {
  max-width: 700px;
  margin: 0 auto;
  padding: 2rem;
  background-color: white;
  color: #444;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #666;
}

input[type="email"],
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
