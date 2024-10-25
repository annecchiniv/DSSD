<template>
    <div class="container">
      <h2>Crear Nueva Orden</h2>
      <form @submit.prevent="crearOrden">
  
        <!-- Campo para Nombre de la Orden -->
        <div class="form-group">
          <label for="nombre_orden">Nombre de la Orden</label>
          <input
            type="text"
            id="nombre_orden"
            v-model="orden.nombre_orden"
            class="form-control"
            placeholder="Ingresa el nombre de la orden"
            required
          />
        </div>
        <!-- Campo para seleccionar Depósito -->
        <div class="form-group">
          <label for="deposito_id">Depósito</label>
          <select
            id="deposito_id"
            v-model="orden.deposito_id"
            class="form-control"
            required
          >
            <option v-for="deposito in depositos" :key="deposito.id" :value="deposito.id">
              {{ deposito.nombre }}
            </option>
          </select>
        </div>
  
        <!-- Campo para seleccionar Materiales y su Cantidad -->
        <div class="form-group">
          <h4>Materiales</h4>
          <div v-for="(material, index) in orden.materiales" :key="index" class="form-material">
            <div class="form-row">
              <div class="col">
                <label for="material_id">Material</label>
                <select v-model="material.material_id" class="form-control" required>
                  <option v-for="m in materiales" :key="m.id" :value="m.id">
                    {{ m.nombre }}
                  </option>
                </select>
              </div>
              <div class="col">
                <label for="cantidad">Cantidad</label>
                <input
                  type="number"
                  v-model="material.cantidad"
                  class="form-control"
                  placeholder="Cantidad"
                  required
                />
              </div>
              <div class="col-auto">
                <button type="button" @click="removeMaterial(index)" class="btn btn-danger">Quitar</button>
              </div>
            </div>
          </div>
          <button type="button" @click="addMaterial" class="btn btn-secondary mt-2">Agregar Material</button>
        </div>
        
        <button type="submit" class="btn btn-primary mt-4 btncreate">Crear Orden</button>
        <br>
        <br>
        <router-link to="/ordenes" class="btn btn-primary" title="Volver">
            Volver
        </router-link>
           
      </form>
      
    </div>
  </template>
  
  <script>
  import { apiService } from '@/api';
  
  export default {
    name: 'CrearOrden',
    data() {
      return {
        orden: {
          nombre_orden: '',
          reserva: true,
          deposito_id: null,
          materiales: [
            { material_id: null, cantidad: 1 }  // Al menos un material al inicio
          ]
        },
        depositos: [],
        materiales: []  // Lista de materiales disponibles
      };
    },
    async created() {
      await this.fetchDepositos();
      await this.fetchMateriales();
    },
    methods: {
      // Obtener depósitos
      async fetchDepositos() {
        try {
          const response = await apiService.get('/depositos');
          this.depositos = response.data.depositos;
        } catch (error) {
          console.error('Error al cargar los depósitos:', error);
        }
      },
      // Obtener lista de materiales
      async fetchMateriales() {
        try {
          const response = await apiService.get('/materiales');
          this.materiales = response.data.materiales;
        } catch (error) {
          console.error('Error al cargar los materiales:', error);
        }
      },
      // Añadir un nuevo material
      addMaterial() {
        this.orden.materiales.push({ material_id: null, cantidad: 1 });
      },
      // Quitar material de la lista
      removeMaterial(index) {
        this.orden.materiales.splice(index, 1);
      },
      // Crear la orden con los materiales seleccionados
      async crearOrden() {
        try {
            await apiService.post('/ordenes', this.orden);  // Ya no necesitamos almacenar el `response`
            this.$router.push('/ordenes');  // Redirige a la lista de órdenes tras crearla
        } catch (error) {
            console.error('Error al crear la orden:', error);
        }
        }
    }
  };
  </script>
  
  <style scoped>
  
  .form-material {
    margin-bottom: 10px;
  }
  </style>
  