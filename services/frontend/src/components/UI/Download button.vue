<template>
  <div class="btn">
    <button @click="openFileMenu()">
      <font-awesome-icon icon="fa-solid fa-cloud-arrow-down" style="scale: 240%; color: darkgray;"/>
    </button>
    <input ref="fileInput" type="file" @change="onFileSelected" style="display: none;">
  </div>

</template>

<script>
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

export default {
  name: 'download-button',
  components: {FontAwesomeIcon},
  data() {
    return {
      selectedFile: null,
    };
  },
  methods: {
    openFileMenu() {
      this.$refs.fileInput.click();
    },
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
      this.$emit('file-selected', this.selectedFile);
    },
  },
}

</script>

<style scoped>
.btn {
  height: 45px;
  width: 45px;
  background-color: #727272;
  color: #ffffff;
  border-radius: 50%;
  border: none;
  font-size: 30px;
  text-align: center;

}

.btn:active {
  background-color: #595959;
}

</style>
