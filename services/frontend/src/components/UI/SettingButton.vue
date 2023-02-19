<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'setting-button'
}
</script>

<style scoped>
.btn {
  height: 45px;
  width: 120px;
  background-color: #716eff;
  color: #ffffff;
  border-radius: 40px;
  border: none;
}
</style>