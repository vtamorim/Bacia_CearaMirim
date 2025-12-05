<template>
  <footer class="site-footer" role="contentinfo">
    <!-- background usando URL importada -->
    <div
      class="footer-bg"
      :style="{
        backgroundImage: FooterWaveUrl ? `url(${FooterWaveUrl})` : 'none'
      }"
      aria-hidden="true"
    ></div>

    <div class="footer-inner">
      <div class="footer-col footer-left">
        <img class="footer-logo" :src="Logotipo" alt="Logo" />
      </div>

      <nav class="footer-col footer-nav" aria-label="Footer navigation">
        <ul class="nav-list">
          <li><a href="#home" :class="{ active: isActive('home') }">A Bacia</a></li>
          <li><a href="#comite" :class="{ active: isActive('comite') }">Comitê</a></li>
          <li><a href="#ods" :class="{ active: isActive('ods') }">ODS</a></li>
          <li><a href="#midias" :class="{ active: isActive('midias') }">Mídias</a></li>
          <li><a href="#cartilha" :class="{ active: isActive('cartilha') }">Cartilha</a></li>
          <li><a href="#jogos" :class="{ active: isActive('jogos') }">Jogos</a></li>
          <li><a href="#contato" :class="{ active: isActive('contato') }">Contato</a></li>
        </ul>
      </nav>

      <div class="footer-col footer-right">
        <div class="copyright">© 2025 Company, Inc</div>
        <div class="social">
          <img :src="Instagram" alt="instagram" style="width:28px;height:28px" />
          <img :src="Youtube" alt="youtube" style="width:28px;height:28px" />
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Instagram from '@/assets/images/Footer/Instagram.svg'
import Youtube from '@/assets/images/Footer/YouTube.svg'
import Logotipo from '@/assets/images/logotipo.svg'

// VITE: força import retornar URL do asset
// Se o seu arquivo tem espaço no nome, mantenha exatamente o nome ou prefira renomear para Group-63.svg
import FooterWaveUrlRaw from '@/assets/images/Footer/Group-63.svg?url'
const FooterWaveUrl = FooterWaveUrlRaw || ''

const hashPage = ref('home')
const isActive = (page) => {
  return (
    hashPage.value === page ||
    (page === 'home' && (hashPage.value === 'home' || hashPage.value === 'bacia'))
  )
}
const updateHash = () => {
  hashPage.value = window.location.hash.slice(1) || 'home'
}
onMounted(() => {
  updateHash()
  window.addEventListener('hashchange', updateHash)
  // debug rápido: descomente se precisar ver a URL no console
  // console.log('FooterWaveUrl =', FooterWaveUrl)
})
</script>

<style scoped>
:root {
  --footer-max-width: 1100px;
  --text-color: rgba(255, 255, 255, 0.95);
  --muted: rgba(255,255,255,0.45);
  --line: rgba(255,255,255,0.12);
}

/* container */
.site-footer {
  position: relative;
  width: 100%;
  overflow: hidden;
  color:white;
  background-color: #0A142F; /* fallback por baixo do background SVG */
  min-height: clamp(160px, 28vh, 260px);
  display: flex;
  height: auto;
  justify-content: center;
  align-items: flex-end;
}

/* DIV que recebe o SVG como background-image */
.footer-bg {
  position: absolute;
  inset: 0 0 auto 0; /* top:0, left:0, right:0, bottom:auto */
  height: 48%; /* controla visual do "céu + onda" – ajuste se precisar */
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  background-repeat: no-repeat;
  /* evita cortes ao dar zoom lateral extremo */
  background-size: 140% auto; /* largura maior que 100% evita recortes nas laterais */
  background-position: top center; /* fixa a parte superior/onda onde queremos */
  pointer-events: none;
  z-index: 0;
  will-change: background-position;
}

/* conteúdo sobre a imagem */
.footer-inner {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: var(--footer-max-width);
  margin: 0 auto;
  padding: clamp(14px, 3.5vw, 40px) clamp(18px, 4vw, 36px);
  
  display: flex;
  flex-direction: column;   /* <-- vira coluna */
  justify-content: center;
  align-items: center;      /* <-- centraliza tudo */
  gap: 1.2rem;
  text-align: center;
}

/* layout */
.footer-col {   width: 100%;
  display: flex;
  justify-content: center;  /* <-- garante centralização interna */
  align-items: center;}
.footer-left { flex:0 0 auto; }
.footer-logo { height: clamp(36px, 2.6vw, 52px); width:auto; display:block; }

/* nav central */
.footer-nav { flex:1 1 auto; display:flex; justify-content:center; position:relative; }
.nav-list { display:flex; gap: clamp(12px, 2.2vw, 28px); list-style:none; margin:0; padding:0; z-index:2; align-items:center; }
.nav-list a { color:var(--text-color); text-decoration:none; font-size:clamp(12px,1.05vw,14px); padding:6px 2px; white-space:nowrap; }

/* decorative line */
.footer-nav::before {
  content: "";
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: calc(50% - 18px);
  width: 65%;
  height: 1px;
  background: var(--line);
  z-index: 0;
}

/* right */
.footer-right {   flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 8px; }
copyright, .copyright { color: var(--muted); font-size: clamp(11px, 0.9vw, 13px); }
.social { display:flex; gap:10px; align-items:center; }

/* responsive tweaks */
@media (max-width: 820px) {
  .footer-inner { flex-direction:column; align-items:center; padding-top: clamp(18px, 6vh, 48px); padding-bottom: clamp(14px,4vh,32px); text-align:center; }
  .footer-nav { order:2; width:100%; }
  .footer-right { align-items:center; text-align:center; }
  .nav-list { flex-wrap:wrap; gap:10px; justify-content:center; }
  .footer-bg { background-size: 180% auto; }
}
@media (max-width:420px) {
  .footer-inner { padding:16px; }
  .footer-bg { background-size: 220% auto; }
}
</style>