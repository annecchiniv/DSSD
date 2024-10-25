<template>
    <div>
      <div class="container" v-for="recolector in recolectores.recolectores" v-bind:key=recolector.id>
            <div class="round">
                <router-link :to="'/me/recolectores/recolector'+ recolector.id">
                    <b> Recolector: </b> {{recolector.name}} {{recolector.lastname}} - <b>DNI:</b> {{recolector.doc_number}}
                </router-link>
            </div>
        </div> 
    </div>
</template>

<script>
import { apiService } from '@/api';
export default ({
  name: "Recolector-Index",  
  data() {
    return { 
        page:this.$route.params.page,
        members: [] };
    },
  async created(){
        await apiService.get('/me/recolectores/')
            .then((response) => (this.recolectores = response.data));

    }
    });
    
</script>