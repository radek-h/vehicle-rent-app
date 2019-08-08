<template>

<div class="container">
  <nav>
    <div class="nav-wrapper">
    <strong>
      <div class="brand-logo">
          VehicleRent
      </div>
    </strong>
    <a href="#" data-target="mobile-demo" class="sidenav-trigger">
      <i class="material-icons">menu</i>
    </a>
    <ul id="nav-mobile" class="right hide-on-med-and-down">
      <li> 
        <router-link to="/" class="btn waves-effect waves-light white">
          HOME
        </router-link>
      </li>
      <li>
        <router-link to="/add-advert" class="btn waves-effect waves-light white">
          Add Advert
        </router-link>
      </li>
      <li>
        <a class="btn waves-effect waves-light white" href="/accounts/logout/">
          logout
        </a>
    </li>
    </ul>
    </div>
  </nav>

  <ul class="sidenav" id="mobile-demo">
    <li><a href="sass.html">Sass</a></li>
    <li><a href="badges.html">Components</a></li>
    <li><a href="collapsible.html">Javascript</a></li>
    <li><a href="mobile.html">Mobile</a></li>
  </ul>

</div>
</template>

<script>
// $(document).ready(function(){
//     $('.sidenav').sidenav();
//   });
</script>

<script>
export default {
    name: "NavbarComponent"
}
</script>

<style scoped>
nav a {
  color: black;
}
nav ul a.btn{
  margin-left: 0px;
}
nav {
  background-color:white;
  margin-top: 20px;
  border: 1px solid lightgray;
  border-radius: 10px;
  box-shadow: none;
    
}
.brand-logo{
  color: gray;
  margin-left: 15px;
  cursor: default;
}

li > a{
  color: black;
  box-shadow: none;
  border: 1px solid lightgray;
  border-radius: 10px;
}
li:nth-child(1) > a:hover{ /* home */
  border: 1px solid #26a69a;
  color: #26a69a;
}
li:nth-child(2) > a:hover{ /* add advert */
  border: 1px solid #eea92a;
  color: #eea92a;
}
li:nth-child(3) > a:hover{ /* logout */
  border: 1px solid red;
  color: red;
}
</style>


