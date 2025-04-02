<template>
  <div id="app">
    <InterfaceWeb />
  </div>
</template>

<script>
import InterfaceWeb from "./components/InterfaceWeb.vue";

export default {
  name: "App",
  components: {
    InterfaceWeb,
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 20px;
}
</style>
