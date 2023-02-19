<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'game-button'
}
</script>

<style scoped>
.btn {
  height: 85px;
  width: 220px;
  background-color: #d9d9d9;
  color: #000000;
  border-radius: 20px;
  border: none;
  transition:0.5s ease-out;
}
.btn:hover{
  background-color: #807c7c;
}
</style>