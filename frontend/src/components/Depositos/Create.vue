<template>
    <div>
        <div class="container">
            <h2>Crear Nuevo Depósito</h2>
            <form @submit.prevent="crearDeposito">
                <div class="form-group">
                    <label for="nombre">Nombre del Depósito</label>
                    <input type="text" v-model="nuevoDeposito.nombre" class="form-control" id="nombre" required />
                </div>
                <div class="form-group">
                    <label for="ubicacion">Ubicación</label>
                    <input type="text" v-model="nuevoDeposito.ubicacion" class="form-control" id="ubicacion" required />
                </div>
                <button type="submit" class="btn btn-success">Crear Depósito</button>
                <router-link to="/depositos" class="btn btn-secondary ml-2">Volver</router-link>
            </form>
        </div>
    </div>
</template>

<script>
import { apiService } from '@/api';

export default {
    name: "CrearDeposito",
    data() {
        return {
            nuevoDeposito: {
                nombre: '',
                ubicacion: ''
            }
        };
    },
    methods: {
        async verificarDepositoExistente() {
            try {
                // Verificar si ya existe un depósito con el mismo nombre o ubicación
                const response = await apiService.get('/depositos', {
                    params: {
                        nombre: this.nuevoDeposito.nombre,
                        ubicacion: this.nuevoDeposito.ubicacion
                    }
                });

                if (response.data.length > 0) {
                    // Si existe un depósito con el mismo nombre o ubicación
                    this.depositoExistente = true;
                } else {
                    this.depositoExistente = false;
                }
            } catch (error) {
                console.error('Error al verificar si el depósito ya existe:', error);
            }
        },
        async crearDeposito() {

            await this.verificarDepositoExistente();

            if (this.depositoExistente) {
                alert('Ya existe un depósito con el mismo nombre o ubicación.');
                return;
            }

            try {
                const response = await apiService.post('/depositos', this.nuevoDeposito);
                console.log('Depósito creado exitosamente:', response.data);
                this.$router.push('/depositos'); // Redirige a la lista de depósitos después de crear
            } catch (error) {
                console.error('Error al crear el depósito:', error);
            }
        }
    }
};
</script>
