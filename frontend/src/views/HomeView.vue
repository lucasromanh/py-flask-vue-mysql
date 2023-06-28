<template>
  <main>
    <div class="inicio" :style="backgroundStyle">
      <div class="container">
        <h1 class="titulo">TRABAJO FINAL INTEGRADOR - 2023</h1>
        <div class="row justify-content-center">
          <div class="col-md-6 d-flex justify-content-center">
            <div class="card carta w-50">
              <div class="card-header">
                <h5 class="card-title">Lucas Roman</h5>
              </div>
              <div class="card-body">
                <p class="card-text">Salta</p>
                <p class="card-text">3874404472</p>
              </div>
            </div>
          </div>
          <div class="col-md-6 d-flex justify-content-center">
            <div class="card carta w-50">
              <div class="card-header">
                <h5 class="card-title">Jorge Rios</h5>
              </div>
              <div class="card-body">
                <p class="card-text">Buenos Aires</p>
                <p class="card-text">11 5990-7483</p>
              </div>
            </div>
          </div>
          <div class="col-md-6 d-flex justify-content-center">
            <div class="card carta w-50">
              <div class="card-header">
                <h5 class="card-title">Mauricio Gutierrez</h5>
              </div>
              <div class="card-body">
                <p class="card-text">Santa Fe</p>
                <p class="card-text">342 438-0832</p>
              </div>
            </div>
          </div>
          <div class="col-md-6 d-flex justify-content-center">
            <div class="card carta w-50">
              <div class="card-header">
                <h5 class="card-title">Angela Saturnino</h5>
              </div>
              <div class="card-body">
                <p class="card-text">Buenos Aires - GBA</p>
                <p class="card-text">11 3428-4790</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: 'Inicio',
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
.inicio {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.titulo {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.carta {
  margin-bottom: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #f8f9fa;
}

.metalico {
  background-color: #c0c0c0;
}

.card {
  display: flex;
  flex-direction: column;
}

.card-header {
  background-color: #ffffff;
  border-bottom: none;
  padding: 10px 15px;
  border-radius: 10px 10px 0 0;
}

.card-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 0;
}

.card-body {
  padding: 15px;
}

.card-text {
  font-size: 14px;
  margin-bottom: 5px;
}

</style>
