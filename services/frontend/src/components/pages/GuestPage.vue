<template>
  <div class="content">
    <div class="text">
      <div class="upload">Upload your book</div>
      <download-button></download-button>
    </div>
    <div class="lang_choose" v-if="true">
      <div class="select_lev">Select your english level</div>
      <select>
        <option v-for="value in options" :key="value">
          {{ value }}
        </option>
      </select>
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
      ]
    }
  },
  components: {DownloadButton}

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

</style>