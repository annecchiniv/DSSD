<template>
    <div>
        <div class="container">
            <div class="table-responsive">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Nombre del Depósito</th>
                            <th>Ubicacion</th>
                            <th>Lista de proveedores a los que pertenece</th>
                            <th>Cantidad de Órdenes</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="deposito in depositos" :key="deposito.id">
                            <td>{{ deposito.nombre }}</td>
                            <td>{{ deposito.ubicacion }}</td>
                            <td>
                                <ul v-if="deposito.materiales && deposito.materiales.length">
                                    <li v-for="material in deposito.materiales" :key="material.id">
                                        {{ material.nombre }}
                                    </li>
                                </ul>
                                <p v-else>No está en ninguna lista de proveedores.</p>
                            </td>
                            <td>{{ deposito.cantidad_ordenes }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="center pbt">
                <router-link to="/deposito/nueva" class="btn btn-success" title="Registrar nuevo depósito">
                    Registrar nuevo depósito
                </router-link>
                <router-link to="/" class="btn btn-primary" title="Volver">
                    Volver
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from '@/api';

export default {
    name: "DepositoList",
    data() {
        return {
            depositos: []  // Lista de depósitos con materiales y cantidad de órdenes
        };
    },
    async created() {
        await this.fetchDepositos();
    },
    methods: {
        async fetchDepositos() {
            try {
                const response = await apiService.get('/depositos'); // Llamada a la API para obtener depósitos
                this.depositos = response.data.depositos;
            } catch (error) {
                console.error('Error al obtener los depósitos:', error);
            }
        }
    }
};
</script>
