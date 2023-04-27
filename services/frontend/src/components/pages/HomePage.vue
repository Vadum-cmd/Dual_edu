<template>
  <div class="content">
    <div class="text">
      <div class="upload">Upload your book</div>
      <download-button @change="onFileChange"/>
    </div>
    <setting-button @click="sendLevel">Submit</setting-button>
    <div v-if="loading"><i class="fa fa-spinner fa-spin"></i></div>
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
      base_url:process.env.VUE_APP_URL,
      file:null,
      formData:null,
      loading: false,
      books: [],
      isNotLogin:true,
      level:null,
    }
  },
  methods: {

    onFileChange(event) {
      this.file = event.target.files[0];
    },
    sendLevel() {
      const jwt = localStorage.getItem('jwt');
      this.formData = new FormData();

      this.formData.append('file', this.file);
      this.url = this.base_url+ `/sendbook?level=${this.level}`;
      this.loading = true;
      axios.post(this.url, this.formData,{
        headers:{
          'Cookie':jwt
        },
        withCredentials:true,
      })
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
  },
  mounted() {
    const jwt = localStorage.getItem("jwt");
    setTimeout(() => {
      if(jwt != null && this.isNotLogin===true){
        location.reload();
      }
    }, 50);

    this.isNotLogin = jwt === null;
    axios.get(this.base_url+`/home`,{
      headers:{
        'Cookie':jwt
      },
      withCredentials:true,
    })
        .then(response => {
          const data= response.data;
          this.level= data.user_level;
        })


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


