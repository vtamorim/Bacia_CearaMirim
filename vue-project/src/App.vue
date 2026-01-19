<script setup>
  import { ref, onMounted } from 'vue';
  import Header from './components/layout/Header.vue';
  import Carousel from './components/layout/Carousel.vue';
  import Parcerias from './pages/Bacia/parcerias.vue';
  import Quiz from './pages/Quiz/index.vue';
  import ODS from './pages/ODS/index.vue';
  import Comite from './pages/Sobre o Comite/index.vue';
  import Footer from './components/layout/Footer.vue';
  import Contato from './pages/Contato/index.vue';
  import apresentacao from './pages/Bacia/apresentacao.vue';
  import Cartilha from './pages/Cartilha/index.vue';
  import mapa from './pages/Bacia/mapa.vue';
  import Jogos from './pages/Jogos/index.vue';
  const currentPage = ref('home');



  const updatePage = () => {
    currentPage.value = window.location.hash.slice(1) || 'home';
  };

  onMounted(() => {
    updatePage();
    window.addEventListener('hashchange', updatePage);
  });
</script>

<template>
  <div id="app-root">
  <div class="page-container">
    <Header />
    <Carousel :currentPage="currentPage" v-show="currentPage != 'jogos'"/>
  </div>
    <main class="main-content">
      <!-- Home / A Bacia -->
      <section v-show="currentPage === 'home' || currentPage === 'bacia'" id="bacia">
        <div class="bacia-container">
          <!-- Título do Mapa -->
          <div class="section-title-wrapper">
            <h2 class="section-title">Mapa Interativo</h2>
          </div>
          <mapa class="mapa-bg" />
          
          <!-- Título da Apresentação -->
          <div class="section-title-wrapper">
            <h2 class="section-title">Apresentação</h2>
          </div>
          <apresentacao />
          
          <!-- Título das Parcerias -->
          <div class="section-title-wrapper">
            <h2 class="section-title">Parcerias</h2>
          </div>
          <Parcerias />
        </div>
      </section>

      <!-- Jogos (Quiz) -->
<section v-show="currentPage === 'jogos'" id="jogos">
  <div style="padding: 40px 20px;">

    <Jogos /> 
  </div>
</section>
      <!-- Placeholder para outras páginas -->
      <section v-show="currentPage === 'comite'" id="comite">
        <div class="comite-container">
          <Comite/>
        </div>
      </section>

      <section v-show="currentPage === 'ods'" id="ods" style="padding: 60px 20px; text-align: center;">
        <ODS/>
      </section>

      <section v-show="currentPage === 'midias'" id="midias" style="padding: 60px 20px; text-align: center;">
        <h2>Mídias</h2>
        <p>Página em desenvolvimento</p>
      </section>

      <section v-show="currentPage === 'cartilha'" id="cartilha" style=" text-align: center;">
        <Cartilha/>
      </section>

      <section v-show="currentPage === 'contato'" id="contato" style="padding: 60px 20px; text-align: center;">
        <Contato/>
      </section>
    </main>

    <Footer />
  </div>
</template>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    body{
      background-color: #F1FAFC;
    }

    html, body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}
    * { 
        margin: 0;
        padding: 0;
        box-sizing: border-box; font-family: 'Poppins', sans-serif; }

    #app-root{
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    .main-content{
      flex: 1 0 auto;
    }

    footer{
      flex-shrink: 0;
    }

    .bacia-container {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

    .comite-container {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 3rem;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 clamp(0.5rem, 3vw, 2.5rem);
  box-sizing: border-box;
}
    .section-title-wrapper {
      width: 100%;
      display: flex;
      justify-content: center;
      padding: 0.5rem 0 0 0;
    }

    .section-title {
      font-size: clamp(1rem, 2vw, 1.5rem);
      color: #0081C7;
      text-align: left;
      font-weight: 700;
      margin: 0 0 1rem 0;
      max-width: 1400px;
      width: 100%;
      padding: 0 clamp(0.5rem, 3vw, 2.5rem);
      box-sizing: border-box;
      position: relative;
      
      &::after {
        content: '';
        position: absolute;
        bottom: -1rem;
        left: clamp(0.5rem, 3vw, 2.5rem);
        width: 120px;
        height: 20px;
        background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 120 20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs><linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:%230081C7;stop-opacity:1" /><stop offset="100%" style="stop-color:%232196F3;stop-opacity:1" /></linearGradient></defs><path d="M0,10 Q30,0 60,10 T120,10" stroke="url(%23waveGrad)" stroke-width="3" fill="none" stroke-linecap="round"/></svg>') no-repeat center;
        background-size: contain;
      }
    }
    .mapa-bg {
    position: absolute;
    top: 0;
    left: 0;
  
    width: 100%;
    height: 100%;

    z-index: -1; 
    pointer-events: none;
    
    max-height: 600px;
    object-fit: cover;
  }

    .container{
      position:relative;
    }
    
</style>
<style scoped>

</style>
