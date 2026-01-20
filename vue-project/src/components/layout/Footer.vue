<template>
  <footer class="site-footer" role="contentinfo">
    <!-- background usando URL importada -->

    <div class="footer-inner">
      <div class="footer-col footer-left">
        <img class="footer-logo" :src="Logotipo" alt="Logo" />
      </div>

      <div id="col-outlogo">
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
        <div style="display:flex; gap:5px;">
        <div class="social">
          <img :src="Instagram" alt="instagram" />
        </div>
        <div class="social">
                    <img :src="Youtube" alt="youtube"  />
        </div>
        </div>
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

<style scoped>:root {
  --footer-max-width: 1200px;
  --text-color: rgba(255, 255, 255, 0.95);
  --muted: rgba(255,255,255,0.55);
}

#col-outlogo{
  display: flex;
  flex-direction: column;
  gap: 10px;
}
/* container */
.site-footer {
  position: relative;
  width: 100%;
  background-color: #0A142F;
  color: white;
}


.footer-inner {
  max-width: 1400px; /* igual ao header */
  width: 100%;
  margin: 0 auto;

  padding: clamp(1.5rem, 3vw, 2.5rem); /* mesmo padrão */
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* colunas */
.footer-col {
  display: flex;
  align-items: center;
}


.footer-left img {
  height: 44px;
}

.footer-nav {
  flex: 1;
  justify-content: center;
  border-bottom:  1px solid #6EA7C7;
}

.nav-list {
  display: flex;
  gap: 100px;
  list-style: none;
  padding: 0;
  margin: 0;
  flex-wrap: wrap;
  justify-content: center;
}

.nav-list a {
  color: var(--text-color);
  text-decoration: none;
  font-size: 14px;
  white-space: nowrap;
}

.nav-list a:hover {
  opacity: 0.8;
}

.footer-right {
  flex-direction: column;
  align-items: flex-end;
  gap: 6px;
}

.copyright {
  font-size: 13px;
  color: var(--muted);
}

.social {
  border: 1px solid #6EA7C7;
  display:flex;
  justify-content: center;
  align-items: center;
  width:1.6rem;
  height: 1.6rem;
  border-radius: 50%;

}

.social img {
  width: 18px;
  height: 18px;
  cursor: pointer;
}

@media (max-width:1052px) {

 .nav-list{
  gap: 50px;
 }
}
@media (max-width: 900px) {
  .footer-inner {
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 20px;
    padding: 32px 20px;
  }

  .footer-left img {
    height: 40px;
  }

  .footer-nav {
    width: 100%;
  }

  .nav-list {
    gap: 14px 18px;
  }

  .nav-list a {
    font-size: 13px;
  }

  .footer-right {
    align-items: center;
    gap: 10px;
  }
}
</style>