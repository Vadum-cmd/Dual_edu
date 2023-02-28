<template>
  <div class="content">
    <div class="text">
      <div class="upload" @click="selectFile()">Upload your book</div>
      <download-button @file-selected="onFileSelected"></download-button>
    </div>
    <div class="lang_choose" v-if="true">
      <div class="select_lev">Select your english level</div>
      <select>
        <option v-for="value in options" :key="value">
          {{ value }}
        </option>
      </select>
    </div>
    <div class="submit_btn">
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>
<script>
import DownloadButton from "@/components/UI/Download button.vue";

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
      file: null,
      downloadUrl: null,
    }
  },
  components: {DownloadButton},
  methods: {
    selectFile() {
      const input = document.createElement("input");
      input.type = "file";
      input.onchange = (e) => {
        this.file = e.target.files[0];
      };
      input.click();
    },
    onFileSelected(file) {
      this.file = file;
    },
    submitFile() {
      if (!this.file) {
        return; // file not selected, do nothing
      }
      const formData = new FormData();
      formData.append("file", this.file);
      formData.append("level", this.value);
      fetch("http://localhost:8080/sendbook", {
        method: "POST",
        body: formData,
      })
          .then((response) => response.json())
          .then((data) => {
            this.downloadUrl = data.downloadUrl;
          })
          .catch((error) => {
            console.error("Error:", error);
          });
    },
  },
};
</script>

<style scoped>
.content {
  display: flex;
  height: 100%;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.upload {
  font-size: 30px;
  font-family: 'Times New Roman', serif;
  color: white;
  margin-right: 10px;
}

.text {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.select_lev {
  font-size: 30px;
  font-family: 'Times New Roman', serif;
  color: white;
  margin-right: 10px;
}

.lang_choose {
  display: flex;
  align-items: center;
}

select {
  height: 30px;
  font-family: "Times New Roman", serif;
  background-color: #595959;
  color: white;
}

.submit_btn button {
  background-color: #595959;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  color: white;
  font-size: 20px;
  cursor: pointer;
}

.submit_btn button:hover {
  background-color: #6c757d;
}
</style>
