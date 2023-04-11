<template>
  <div class="content">
    <div class="text">
      <div class="upload">Upload your book</div>
      <download-button @change="onFileChange"/>
    </div>
    <div class="lang_choose" v-if="isNotLogin">
      <div class="select_lev">Select your english level</div>
      <select v-model="level">
        <option v-for="value in options" :key="value">{{ value }}</option>
      </select>
    </div>
    <setting-button @click="sendLevel">Submit</setting-button>
    <div v-if="loading"><i class="fa fa-spinner fa-spin"></i></div>

    <div v-if="books && books.length > 0">
      <h2>Available Books</h2>
      <ul>
        <li v-for="book in books" :key="book.id">{{ book.title }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SettingButton from "@/components/UI/SettingButton.vue";
import DownloadButton from "@/components/UI/Download button.vue";

export default {
  components: {DownloadButton, SettingButton},
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
      formData:null,
      loading: false,
      books: [],
      isNotLogin:false
    }
  },
  methods: {

    onFileChange(event) {
      this.file = event.target.files[0];
    },
    sendLevel() {
      this.formData = new FormData();
      this.formData.append('file', this.file);
      this.formData.append('level', this.level);

      this.url = 'http://192.168.1.104:8081/sendbook';
      this.loading = true;
      axios.post(this.url, this.formData)
          .then(() => {

          })
          .catch(error => {
            this.errorMessage = error.message;
            console.error("There was an error!", error);
          })
          .finally(() => {
            this.loading = false;
          });
    },
    fetchBooks() {
      const jwt = localStorage.getItem("jwt");
      axios.get(`http://192.168.1.104:8081/books?jwt=${jwt}`)
          .then(response => {
            this.books = response.data;
          })
          .catch(error => {
            console.error("There was an error!", error);
          });
    }
  },
  mounted() {
    const jwt = localStorage.getItem("jwt");
    if(jwt !== 'null' && this.isNotLogin===true){
      window.location.reload();
    }
    this.isNotLogin = jwt === 'null';

    this.fetchBooks();
  }
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

@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');

.fa {
  font-size: 24px;
  color: white;
}



</style>


