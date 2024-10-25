<template>
  <div class="form-wrapper">
    <div class="register-container">
      <h3>Registrarse</h3>
      <form @submit.prevent="registrar_usuario">
        <input class="register-input" type="text" v-model="user.name" placeholder="Nombre" required />
        <input class="register-input" type="text" v-model="user.lastname" placeholder="Apellido" required />
        <input class="register-input" type="email" v-model="user.email" placeholder="Email" required />
        <input class="register-input" type="password" v-model="user.password" placeholder="Contraseña" required />
        <button class="register-button" type="submit">Registrarse</button>
      </form>
      <p v-if="error" class="register-error-message">{{ errorMessage }}</p>

      <p class="link-to-login">
        ¿Ya tienes una cuenta? 
        <router-link to="/iniciar-sesion" class="login-link">Iniciar sesión</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      user: {
        name: '',
        lastname: '',
        email: '',
        password: ''
      },
      error: false,
      errorMessage: ''
    };
  },
  methods: {
    ...mapActions('auth', ['registerUser']),
    async registrar_usuario() {
      try {
        await this.registerUser(this.user);
        this.$router.push('/iniciar-sesion');
      } catch (error) {
        this.error = true;
        this.errorMessage = 'Error al registrarse. Inténtalo de nuevo.';
      }
    }
  }
};
</script>

<style scoped>
@import '../css/RegisterForm.css';
</style>

