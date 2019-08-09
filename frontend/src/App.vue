<template>
  <div id="app">
<<<<<<< HEAD
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
=======
    <NavbarComponent />
>>>>>>> vuejs
    <router-view />
  </div>
</template>

<<<<<<< HEAD
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
=======
<script>
import NavbarComponent from "@/components/Navbar.vue";

export default {
  name: "App",
  components: {
    NavbarComponent
  }
};
</script>

<style>
html,
body {
  height: 100%;
  font-family: "Lato", sans-serif !important;
>>>>>>> vuejs
}
</style>
