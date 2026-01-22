<script setup>
  import { ref, onMounted } from 'vue';
  import Header from './components/layout/Header.vue';
  import Carousel from './components/layout/Carousel.vue';



  import Footer from './components/layout/Footer.vue';


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
    <Header />
    <Carousel :currentPage="currentPage" v-show="currentPage != 'jogos'"/>
    <main class="main-content">
      <router-view />
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
