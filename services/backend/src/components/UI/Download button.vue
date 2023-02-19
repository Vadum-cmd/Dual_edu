<template>
  <button class="btn">
    <font-awesome-icon icon="fa-solid fa-cloud-arrow-down" />
  </button>
</template>

<script>
export default {
  name: 'download-button'
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
}
.btn:active{
  background-color: #595959;
}

</style>