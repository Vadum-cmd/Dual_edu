<template>
  <Navigation/>
  <div class="app">

    <content>
      <router-view/>
    </content>
    <footer>

    </footer>
  </div>
</template>

<script>

import Navigation from "@/components/Navigation.vue";

export default {
  components: {Navigation}
}
</script>

<style >
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Raleway", sans-serif;
  font-weight: 400;
}
.app{
  background-image: url("../src/components/materials/hero-bg.png");
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>