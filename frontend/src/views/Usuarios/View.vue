<template>
    <div class="ver" :style="backgroundStyle">
    <div class="container">
      <div class="card">
        <div class="card-header bg-success">
            <h4 style="color:aliceblue">
                Usuarios
                <RouterLink class="btn btn-primary float-end"  to="/usuarios/agregar">Agregar Usuario</RouterLink>
            </h4>
        </div>
        <div class="card-body">

            <table class="table table-bordered border-primary">
                <thead>
                    <tr style="text-align: center;">
                        <th>ID</th>
                        <th>Nombre completo</th>
                        <th>Telefono</th>
                        <th>Mail</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody v-if="this.usuarios.length > 0">
                    <tr v-for="(usuarios, index) in this.usuarios" :key="index">
                        <td>{{ usuarios.id }}</td>
                        <td>{{ usuarios.nombre_completo }}</td>
                        <td>{{ usuarios.telefono }}</td>
                        <td>{{ usuarios.email }}</td>
                        <td class="d-flex justify-content-around">
                            <RouterLink :to="{path: '/usuarios/'+usuarios.id }"  class="btn btn-success">
                                Editar
                            </RouterLink>
                            <button type="button" @click="eliminarUsuario(usuarios.id)" class="btn btn-danger">
                                Eliminar
                            </button>
                        </td>

                    </tr>
                </tbody>
                <tbody v-else>
                    <tr>
                        <td colspan="6">Cargando .....</td>
                    </tr>
                </tbody>
            </table>
        </div>
      </div>
    </div>
</div>
  </template>
  
<script>
import axios from 'axios';


export default{
    name: 'usuarios',
    data(){
        return {
            usuarios: []
        }
    },
    mounted(){

        this.getUsuarios();


    },
    methods: {
        getUsuarios(){

            axios.get('http://127.0.0.1:3000/usuarios').then(res => {
                this.usuarios = res.data;
                 console.log(this.usuarios);

            } );
        },

        eliminarUsuario(usuariosId){

            if(confirm("Tas segurisisismo que quieres Eliminar este Usuario??")){

                axios.delete(`http://127.0.0.1:3000/usuarios/${usuariosId}`)
                .then(res => {

                    alert(res.data.message);
                    this.getUsuarios();
                })
                
            }
        },

    },
    name: 'Ver',
    computed: {
        backgroundStyle() {
        return {
         background: 'linear-gradient(to bottom, #ffcc00, #ff9900)',
        };
        },
    },
}


</script>

<style scoped>
.ver {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>