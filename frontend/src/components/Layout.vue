<template>
  <div>
    <nav class="navbar navcolor">
   <router-link to="/" class="navbar-brand" style="margin-left: 30px">
     <img
       src="/logo.png"
       class="logosize"
       alt="Logo"
     />
     <span style="color: white"> Ecocycle</span>
     </router-link>

     <ul class="nav nav-pills mb-3" role="tablist">
         <li class="nav-item dropdown">
          <button class="nav-link dropbtn custom-name-btn">{{ authUser ? `${authUser.lastname} ${authUser.name}` : 'Cuenta' }}</button>
             <div class="dropdown-content">
              <a href="/" @click.prevent="cerrarSesion">Cerrar Sesion</a>
             </div>
         </li>
     </ul>
 </nav>
 <div class="topnav" id=myTopnav>
      <router-link to="/">Inicio</router-link>
      <router-link to="/ordenes">Ordenes</router-link> 
      <router-link to="/depositos">Depósitos</router-link> 
      <router-link to="/materiales/material/new">Plan de material</router-link>
    </div>
  </div>
  <div class="contentrouter">
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: "App",  
  computed: {
    ...mapGetters({
      authUser: 'auth/user',
      isLoggedIn: 'auth/isLoggedIn'
    })
  },
  mounted() {
    const userFromStorage = localStorage.getItem('user');
    if (userFromStorage) {
      this.$store.commit('auth/setUser', JSON.parse(userFromStorage));
    }
  },

  methods: {
    myFunction() {
      var x = document.getElementById("myTopnav");
      if (x.className === "topnav") {
        x.className += " responsive";
      } else {
        x.className = "topnav";
      }
    },
    cerrarSesion() {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      this.$router.push('/iniciar-sesion');
      window.location.reload(); 
    },
    async loadUser() {
      try {
        await this.$store.dispatch('auth/loadUser'); 
      } catch (error) {
        console.error('Error cargando el usuario:', error);
      }
    }
  }
};
</script>
<style>
  .custom-name-btn {
    max-width: 200px; 
    white-space: nowrap; 
    overflow: hidden;
    text-overflow: ellipsis; 
}
</style>