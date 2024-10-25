<template>
  <div class="register">
    <div class="register-left">
      <img src="/logo.png" alt="logo" />
      <h1>Bienvenido a<br>Ecocycle</h1>
    </div>

    <div class="register-right">
      <div class="tab-content" id="myTabContent">
        <h1 class="register-heading">Iniciar sesión</h1>

        <div class="row register-form">
          <div class="col-md-12 profile_card">

            <form @submit.prevent="login">
              <input type="email" class="form-input" placeholder="Escriba su email" v-model="user.email" required /><br>
              <div class="password-input-wrapper">
                <input :type="showPassword ? 'text' : 'password'" class="form-input" placeholder="Escriba su contraseña" v-model="user.password" required />
                <button type="button" class="toggle-password" @click="togglePasswordVisibility">
                  {{ showPassword ? 'Ocultar' : 'Ver' }}
                </button>
              </div>

              <div class="float-center ">
                <input style="padding: 10px 40px; font-size: 120%;" type="submit" class="btn btn-outline-light" value="Entrar" />
              </div>
            </form>

          </div>

          <router-link to="/registrar">¿No tienes una cuenta? Regístrate aquí</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: "Login-Component",
  data: () => ({
    user: {
      email: null,
      password: null
    },
    showPassword: false 
  }),
  methods: {
    ...mapActions('auth', ['loginUser']),
    
    async login() {
      try {
        await this.loginUser(this.user);
        this.user = {
          email: null,
          password: null
        };
        this.$router.push('/');
      } catch (error) {
        alert('Correo electrónico o contraseña incorrectos');
        console.error('Error en el inicio de sesión:', error);
      }
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword; 
    }
  }
};
</script>

<style>
@import "../css/login.css";
</style>