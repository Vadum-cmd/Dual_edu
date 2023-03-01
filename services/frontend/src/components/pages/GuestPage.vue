<template>
  <div class="content">
    <div class="text">
      <div class="upload">Upload your book</div>
      <input type="file" @change="onFileChange">
    </div>
    <div class="lang_choose" v-if="true">
      <div class="select_lev">Select your english level</div>
      <select v-model="level">
        <option v-for="value in options" :key="value">{{ value }}</option>
      </select>
    </div>
    <button @click="SendLevel">Submit</button>
  </div>
</template>

<script>

import axios from "axios";
export default {
  data() {
    return {
      options: [
        'A1',
        'A2',
        'B1',
        'B2',
        'C1',
        'C2'
      ],
      level: null,
      url:'',
      file:null,
      formData:null
    }
  },
  methods: {
    onFileChange(event) {
      this.file = event.target.files[0];
    },
    SendLevel() {
      this.formData = new FormData();
      this.formData.append('file', this.file);
      this.formData.append('level', this.level);
    
      this.url = 'http://192.168.0.163:8081/sendbook'
      axios.post(this.url, this.formData)
          .catch(error => {
            this.errorMessage = error.message;
            console.error("There was an error!", error);
          });
    }
  },



}
</script>

<style scoped>
.content {
  display: flex;
  height: 100%;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.upload{
  font-size: 30px;
  font-family: 'Times New Roman', serif;
  color: white;
  margin-right: 10px;

}
input{
  color: white;

}
.text{
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  margin-left: 120px;
}
.select_lev{
  font-size: 30px;
  font-family: 'Times New Roman', serif;
  color: white;
  margin-right: 10px;
}
.lang_choose{
  display: flex;
  align-items: center;
}
select{
  height: 30px;
  font-family: "Times New Roman", serif;
  background-color: #595959;
  color: white;
}
</style>
