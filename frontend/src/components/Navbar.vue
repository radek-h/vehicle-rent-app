<template>

<div class="container">
  <nav>
    <div class="nav-wrapper">
    <strong><a href="#" class="brand-logo">VehicleRent</a></strong>
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
</div>
  
</template>

<script>
export default {
    name: "NavbarComponent"
}
</script>

<style scoped>
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
}
.brand-logo:hover{
    color: black;
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


