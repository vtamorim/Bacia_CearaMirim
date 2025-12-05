<template>
  <footer class="site-footer" role="contentinfo">
    <!-- Background SVG (keeps its aspect and scales) -->
    <img class="footer-bg" v-bind:src="FooterWave" alt="" aria-hidden="true" />

    <div class="footer-inner">
      <!-- Left: logo -->
      <div class="footer-col footer-left">
        <!-- Replace this with your real logo -->
        <img class="footer-logo" src="@/assets/images/logotipo.svg" alt="Logo" />
      </div>

      <!-- Center: navigation -->
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

      <!-- Right: copyright + social -->
      <div class="footer-col footer-right">
        <div class="copyright">© 2025 Company, Inc</div>
        <div class="social">
          <button class="icon" aria-label="Instagram" title="Instagram" v-html="instagramSvg"></button>
          <button class="icon" aria-label="YouTube" title="YouTube" v-html="youtubeSvg"></button>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>

import Instagram from '@/assets/images/Footer/Instagram.svg'
import Youtube from '@/assets/images/Footer/YouTube.svg'
import { ref, onMounted } from 'vue'
import Logotipo from '@/assets/images/logotipo.svg'
import FooterWave from '@/assets/images/Footer/group.svg'

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
})
</script>

<style scoped>
:root {
  /* tweakable tokens */
  --footer-max-width: 1100px;
  --footer-bg-color: #081329; /* fallback background */
  --text-color: rgba(255, 255, 255, 0.95);
  --muted: rgba(255,255,255,0.45);
  --line: rgba(255,255,255,0.12);
}

/* Container */
.site-footer {
  position: relative;
  width: 100%;
  overflow: hidden;
  background-color: var(--footer-bg-color); /* fallback */
  /* Make the footer height scale with viewport but keep a min and max */
  min-height: clamp(160px, 28vh, 260px);
  display: flex;
  align-items: flex-end; /* content sits visually inside the dark wave at bottom */
}

/* SVG background - absolute to allow content overlap */
.footer-bg {
  position: absolute;
  left: 50%;
  top: 0;
  transform: translateX(-50%);
  width: 140%; /* larger than viewport to avoid clipping waves at extreme zooms */
  height: auto;
  pointer-events: none;
  z-index: 0;
  user-select: none;
}

/* Inner container that holds the content */
.footer-inner {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: var(--footer-max-width);
  margin: 0 auto;
  padding: clamp(14px, 3.5vw, 40px) clamp(18px, 4vw, 36px);
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1rem;
  color: var(--text-color);
}

/* Columns */
.footer-col {
  display: flex;
  align-items: center;
}

/* Left */
.footer-left {
  flex: 0 0 auto;
}

/* Logo */
.footer-logo {
  height: clamp(36px, 2.6vw, 52px);
  width: auto;
  display: block;
  filter: drop-shadow(0 1px 0 rgba(0,0,0,0.15));
}

/* Center navigation: centered horizontally in available space */
.footer-nav {
  flex: 1 1 auto;
  display: flex;
  justify-content: center;
}

/* Decorative horizontal line behind nav (thin) */
.footer-nav::before {
  content: "";
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: calc(50% - 18px); /* shifts line roughly aligned behind nav row */
  width: 65%;
  height: 1px;
  background: var(--line);
  opacity: 1;
  pointer-events: none;
  z-index: 0;
}

/* Nav list */
.nav-list {
  display: flex;
  gap: clamp(12px, 2.2vw, 28px);
  list-style: none;
  margin: 0;
  padding: 0;
  z-index: 1; /* above the line */
  align-items: center;
}

.nav-list a {
  color: var(--text-color);
  text-decoration: none;
  font-size: clamp(12px, 1.05vw, 14px);
  letter-spacing: 0.02em;
  opacity: 0.95;
  padding: 6px 2px;
}

.nav-list a:hover {
  text-decoration: underline;
  color: #fff;
}

/* Right column */
.footer-right {
  flex: 0 0 auto;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
  text-align: right;
}

/* Copyright */
copyright, .copyright {
  color: var(--muted);
  font-size: clamp(11px, 0.9vw, 13px);
}

/* Social icons */
.social {
  display: flex;
  gap: 10px;
  align-items: center;
}

.icon {
  border: 1px solid rgba(255,255,255,0.15);
  background: rgba(0,0,0,0.08);
  width: clamp(30px, 2.6vw, 36px);
  height: clamp(30px, 2.6vw, 36px);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 4px;
  color: var(--text-color);
  cursor: pointer;
}

/* ensure inline SVG scales */
.icon svg { width: 60%; height: 60%; display:block; }

/* Responsiveness - stack columns on narrow viewports */
@media (max-width: 820px) {
  .footer-inner {
    flex-direction: column;
    align-items: center;
    padding-top: clamp(18px, 6vh, 48px);
    padding-bottom: clamp(14px, 4vh, 32px);
    text-align: center;
  }

  .footer-nav::before {
    width: 85%;
    bottom: calc(50% - 24px);
  }

  .footer-right {
    align-items: center;
    text-align: center;
  }

  .nav-list {
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
  }

  /* Reduce background width on small screens to avoid very wide scaling */
  .footer-bg { width: 180%; }
}

/* Very small screens */
@media (max-width: 420px) {
  .footer-inner { padding: 16px; }
  .footer-bg { width: 220%; }
  .nav-list { gap: 8px; font-size: 12px; }
}
</style>