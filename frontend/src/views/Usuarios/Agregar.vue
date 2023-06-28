<template>
<div class="agregar" :style="backgroundStyle"> 
    <div class="container mt-5">
        <div>
            <div class="card-header d-flex justify-content-center">
                <h4>Agregar Usuario</h4>
            </div>
            <div class="card-body d-flex flex-column align-items-center">
                <div class="mb-3">
                    <label for="">Nombre</label>
                    <input type="text" v-model="model.usuarios.nombre_completo" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">Telefono</label>
                    <input type="text" v-model="model.usuarios.telefono" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="">Mail</label>
                    <input type="text" v-model="model.usuarios.email" class="form-control" />
                </div>
                <div class="mb-3">
                    <button type="button" @click="guardarUsuario" class="btn btn-primary">Agregar</button>
                </div>
            </div>
        </div>

    </div>
</div>
</template>

<script>
import axios from 'axios';


export default {
    name: "usuariosAgregar",
    data(){
        return {
            model: {
                usuarios: {
                    nombre_completo: '',
                    telefono: '',
                    email: '',
                }
            }
        }
    },
    methods: {
        guardarUsuario(){
            axios.post('http://127.0.0.1:3000/usuarios', this.model.usuarios)
            .then(res => {

                console.log(res.data);
                alert(res.data.message);

                this.model.usuarios = {
                    nombre_completo: '',
                    telefono: '',
                    email: '',
                }
                
            })
            .catch(function (error){

                if (error.response) {

                    console.log(error.response.data);
                    console.log(error.response.status);
                    console.log(error.response.headers);
                } else if (error.request) {

                    console.log(error.request);
                } else {
                    console.log('Error', error.message);
                }

            });
        }

    },
    name: 'Agregar',
    computed: {
        backgroundStyle() {
        return {
         background: 'linear-gradient(to bottom, #ffcc00, #ff9900)',
        };
        },
    },
};



</script>




<style scoped>
.agregar {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>



