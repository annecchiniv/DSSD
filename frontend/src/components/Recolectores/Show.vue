<template>
    <div>
        <div class="container">
            <div class="table-responsive">
                <table class="table">
                    <tbody>
                        <tr>
                            <th scope="row">Nombre</th>
                            <td> {{ recolector.name }} </td>
                        </tr>
                        <tr>
                            <th scope="row">Apellido</th>
                            <td> {{ recolector.lastname }} </td>
                        </tr>
                        <tr>
                            <th scope="row">{{ member.doc_type }}</th>
                            <td> {{ recolector.doc_number }} </td>
                        </tr>
                        <tr>
                            <th scope="row">Número de télefono</th>
                            <td> {{ recolector.phone_number }} </td>
                        </tr>
                        <tr>
                            <th scope="row">Email</th>
                            <td> {{ recolector.email }} </td>
                        </tr>
                        <tr>
                            <th scope="row">Estado</th>
                            <td>{{ recolector.state }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="center pbt">
                <router-link :to="'materiales/new'+ material.id" class="btn btn-success" title="Nueva carga de material">
                    Nueva carga de material
                </router-link>
                <router-link to="/me/members" class="btn btn-primary" title="Volver">
                    Volver
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from '@/api';
export default ({
    name: "Recolector-Show",
    data() {
        return {
            page: this.$route.params.page,
            id: this.$route.params.id,
            member: []
        };
    },
    async created() {
        await apiService.get('/ordenes/' + this.id)
            .then((response) => (this.member = response.data.member));

    }
});
</script>