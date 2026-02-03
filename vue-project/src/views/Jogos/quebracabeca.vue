<template>
  <div class="game-page">
    <div class="game-header">
      <router-link to="/jogos" class="back-button">← Voltar</router-link>
      <h1>Quebra-cabeça</h1>
      <p>Monte as peças do quebra-cabeça para formar a imagem completa da Bacia Cearamirim.</p> 
    </div>
<Transition name="fade">
  <div v-if="showRotateWarning" class="rotate-notice">
    <div class="notice-content">
      <div class="phone-icon">🔄</div>
      <p>Gire o celular para uma melhor experiência</p>
      <button @click="showRotateWarning = false" class="close-notice">Continuar assim</button>
    </div>
  </div>
</Transition>

<div class="game-content">
  </div>
    <div class="game-content">
      <section class="game-description">
        <h2>Como Jogar</h2>
        <p>Neste jogo, você terá que montar as peças do quebra-cabeça para formar a imagem completa da Bacia Cearamirim.</p>
      </section>

      <section class="game-area">
        <div class="unity-container">
          <div class="unity-wrapper" ref="unityWrapper">
            <iframe 
              src="/SEGUNDO JOGO/index.html"
              frameborder="0"
              allowfullscreen
              scrolling="no"
            ></iframe>
          </div>
        </div>
      </section>

      <section class="game-info">
        <div class="info-card">
          <h3>📚 Aprendizado</h3>
          <p>Desenvolva habilidades de resolução de problemas e atenção aos detalhes ao montar o quebra-cabeça da Bacia Cearamirim.</p>
        </div>
        <div class="info-card">
          <h3>⏱️ Tempo</h3>
          <p>Tempo Estimado: 5-10 min</p>
        </div>
        <div class="info-card">
          <h3>🎯 Dificuldade</h3>
          <p>Nível Médio - Para quem curte quebra-cabeça</p>
        </div>
      </section>
    </div>
  </div>
</template>
<script setup>import { ref, onMounted, onUnmounted } from 'vue'

const unityWrapper = ref(null)
const showRotateWarning = ref(false)

const checkOrientation = () => {
  const isMobile = window.matchMedia("(pointer: coarse)").matches
  const isLandscape = window.innerWidth > window.innerHeight
  
  // Avisa para girar se o celular estiver DEITADO, pois o jogo é VERTICAL
  showRotateWarning.value = isMobile && isLandscape
}
onMounted(() => {
  checkOrientation()
  window.addEventListener('resize', checkOrientation)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkOrientation)
})

const toggleFullscreen = () => {
  const elem = unityWrapper.value
  if (!elem) return
  if (!document.fullscreenElement) {
    elem.requestFullscreen?.() || elem.webkitRequestFullscreen?.()
  } else {
    document.exitFullscreen()
  }
}

</script>

<script>
  const isMobile =
    window.matchMedia("(pointer: coarse)").matches ||
    window.matchMedia("(max-width: 768px)").matches;

  if (isMobile) {
    document.body.classList.add("is-mobile");
  }
</script>

<style scoped>

:root {
  --primary: #1e3c72;
  --bg-gradient: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}


.game-page {
  min-height: 100vh;
  background: var(--bg-gradient);
  padding: clamp(1rem, 5vw, 2rem);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4rem;
}

.game-header,
.game-content {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;

  max-width: 1100px;
}

/* =======================
   HEADER
======================= */
.back-button {
  display: inline-block;
  margin-bottom: 1rem;
  padding: 0.5rem 1rem;
  background: var(--primary);
  color: #fff;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.back-button:hover {
  background: #2e5090;
  transform: translateX(-4px);
}

.game-header h1 {
  font-size: 2.5rem;
  color: var(--primary);
}

.game-header p {
  color: #666;
}

/* =======================
   SEÇÕES
======================= */
section {
  background: #fff;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
}

section h2 {
  color: var(--primary);
  margin-bottom: 1rem;
}

section p {
  color: #555;
  line-height: 1.6;
}

/* =======================
   UNITY / JOGO
======================= */
.game-area {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 12px;
}

.unity-container {
  width: 100%;
  margin: 0 auto;
}

.unity-wrapper {
  position: relative;
  width: 100%;
  max-width: 960px;
  aspect-ratio: 16 / 9;
  background: #000;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.unity-wrapper iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: none;
  object-fit: contain;
}

/* =======================
   FULLSCREEN
======================= */
.unity-wrapper:fullscreen,
.unity-wrapper:-webkit-full-screen {
  width: 100vw;
  height: 100vh;
  aspect-ratio: auto;
  border-radius: 0;
}

/* =======================
   BOTÃO FULLSCREEN
======================= */
.game-actions {
  display: flex;
  justify-content: center;
  margin-top: 1rem;
}

.fullscreen-btn {
  background: var(--primary);
  color: #fff;
  border: none;
  padding: 12px 24px;
  border-radius: 50px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.3s;
}

.fullscreen-btn:hover {
  background: #2e5090;
  transform: translateY(-2px);
}

/* =======================
   INFO CARDS
======================= */
.game-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.info-card {
  background: #fff;
  padding: 1.5rem;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
}

/* =======================
   MOBILE
======================= */
@media (max-width: 768px) {
  .game-header h1 {
    font-size: 1.8rem;
  }

  .unity-wrapper {
    aspect-ratio: 4 / 3;
    border-radius: 8px;
  }

  .fullscreen-btn {
    width: 100%;
    max-width: 300px;
    padding: 15px;
  }

  .game-actions {
    position: sticky;
    bottom: 20px;
    z-index: 10;
  }
}

</style>