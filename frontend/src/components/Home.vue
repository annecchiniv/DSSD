<template>
  <div>
    <div class="cardContainer">

      <div class="card">
        
        <router-link class="link" to="/depositos">
          <h3 class="title"><b>Administrar Red de Depositos</b></h3>
          <img class="img-card" src="/materiales.png" alt="ilustracion de materiales">
        </router-link>
      </div>

      <div class="card">
        <router-link class="link" to="/ordenes">
          <h3 class="title"><b>Administrar Ordenes de los Depositos</b></h3>
          <img class="img-card" src="/recolector.png" alt="ilustracion de recolectores">
        </router-link>
      </div>

    </div>
  </div>
</template>
  
<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters({
      authUser: 'auth/user',
      isLoggedIn: 'auth/isLoggedIn'
    })
  },
  name: "Home-Component",
  components: {},

};
</script>
  