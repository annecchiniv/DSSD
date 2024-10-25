<template>
    <div>
        <div class="container">
            <div v-if="ordenes.length"> <!-- Solo muestra si hay órdenes -->
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Nombre de Orden</th>
                                <th>Estado de la Orden</th>
                                <th>Nombre del Depósito</th>
                                <th>Materiales</th> <!-- Nueva columna para los materiales -->
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="orden in ordenes" :key="orden.id">
                                <td>{{ orden.nombre_orden }}</td>
                                <td>
                                    {{ orden.reserva ? 'Entregado' : 'Pendiente' }}
                                    <button @click="toggleEstado(orden.id)" class="btn btn-warning ml-2">Cambiar Estado</button>
                                </td>
                                <td>{{ orden.deposito_nombre }}</td>
                                <td>
                                    <ul>
                                        <li v-for="material in orden.materiales" :key="material.id">
                                            {{ material.nombre}} - {{ material.cantidad }}
                                        </li>
                                    </ul>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div v-else>
                <p>No hay órdenes cargadas.</p> <!-- Mensaje cuando no hay órdenes -->
            </div>
            <div class="center pbt">
                <router-link to="/ordenes/nueva" class="btn btn-success" title="Nueva Orden">
                    Crear Nueva Orden
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
    name: "OrdenList",
    data() {
        return {
            ordenes: [],  // Inicialmente es un array vacío
        };
    },
    async created() {
        await this.fetchOrdenes();
    },
    methods: {
        async fetchOrdenes() {
            try {
                const response = await apiService.get('/ordenes'); // Obtiene todas las órdenes
                this.ordenes = response.data.ordenes; // Asigna la lista de órdenes
            } catch (error) {
                console.error('Error al obtener las órdenes:', error);
                this.ordenes = []; // Mantenemos como vacío en caso de error
            }
        },
        async toggleEstado(ordenId) {
            try {
                const orden = this.ordenes.find(o => o.id === ordenId); // Encuentra la orden correspondiente
                const nuevoEstado = !orden.reserva; // Cambia el estado
                await apiService.put(`/ordenes/${ordenId}/estado`, { reserva: nuevoEstado });
                orden.reserva = nuevoEstado; // Actualiza el estado en el frontend
            } catch (error) {
                console.error('Error al cambiar el estado:', error);
            }
        },
    },
};
</script>
