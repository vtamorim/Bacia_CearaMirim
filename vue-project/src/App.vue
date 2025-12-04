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
    <Carousel />
    <main class="main-content">
      <!-- Home / A Bacia -->
      <section v-show="currentPage === 'home' || currentPage === 'bacia'" id="bacia">
        <div style="padding:  40px 20px;">
        <apresentacao />
        
        <Parcerias />
      </div>
      </section>

      <!-- Jogos (Quiz) -->
      <section v-show="currentPage === 'jogos'" id="jogos">
        <div style="padding: 40px 20px;">
          <h2 style="text-align: center; margin-bottom: 30px;">Jogos</h2>
          <Quiz />
        </div>
      </section>

      <!-- Placeholder para outras páginas -->
      <section v-show="currentPage === 'comite'" id="comite" style="padding: 60px 20px; text-align: center;">
        <Comite/>
      </section>

      <section v-show="currentPage === 'ods'" id="ods" style="padding: 60px 20px; text-align: center;">
        <ODS/>
      </section>

      <section v-show="currentPage === 'midias'" id="midias" style="padding: 60px 20px; text-align: center;">
        <h2>Mídias</h2>
        <p>Página em desenvolvimento</p>
      </section>

      <section v-show="currentPage === 'cartilha'" id="cartilha" style="padding: 60px 20px; text-align: center;">
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

    * { 
        margin: 0;
        padding: 0;
        box-sizing: border-box; font-family: 'Poppins', sans-serif; }

    /* Layout to keep footer at bottom on short pages */
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
</style>
<style scoped>

</style>
