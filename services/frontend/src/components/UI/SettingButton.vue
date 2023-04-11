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
  height: 35px;
  width: 90px;
  background-color: #4b4b4b;
  color: #ffffff;
  border-radius: 40px;
  border: none;
}
</style>
