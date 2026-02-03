<template>
  <div class="game-page">
    <div class="game-header">
      <router-link to="/jogos" class="back-button">← Voltar</router-link>
      <h1>Aventura por Obstáculos</h1>
      <p>Passe por obstáculos e saiba mais sobre a Bacia</p>
    </div>

    <div class="game-content">
      <section class="game-description">
        <h2>Como Jogar</h2>
        <p>Neste jogo, você terá que passar por obstáculos e descobrir informações sobre a Bacia Cearamirim.</p>
        <p v-if="!isMobile">Teclas: <strong>WASD</strong> para mover, <strong>Espaço</strong> para pular.</p>
        <p v-else>Toque: Use o <strong>D-Pad</strong> para mover e o botão <strong>Pular</strong>.</p>
      </section>

      <section class="game-area">
        <div class="unity-container">
          
          <div class="unity-wrapper" ref="unityWrapper">
            <iframe 
              ref="gameIframe"
              src="/PRIMEIRO JOGO/index.html"
              frameborder="0"
              allowfullscreen
              scrolling="no"
            ></iframe>

            <div v-if="isMobile" class="mobile-controls">
              
              <div class="d-pad-grid">
                <button 
                  class="control-btn up-btn" 
                  @touchstart.prevent="startKey('KeyW')" 
                  @touchend.prevent="stopKey('KeyW')"
                >▲</button>
                
                <button 
                  class="control-btn left-btn" 
                  @touchstart.prevent="startKey('KeyA')" 
                  @touchend.prevent="stopKey('KeyA')"
                >◀</button>
                
                <button 
                  class="control-btn right-btn" 
                  @touchstart.prevent="startKey('KeyD')" 
                  @touchend.prevent="stopKey('KeyD')"
                >▶</button>
                
                <button 
                  class="control-btn down-btn" 
                  @touchstart.prevent="startKey('KeyS')" 
                  @touchend.prevent="stopKey('KeyS')"
                >▼</button>
              </div>

              <div class="action-area">
                <button 
                  class="control-btn jump-btn" 
                  @touchstart.prevent="startKey('Space')" 
                  @touchend.prevent="stopKey('Space')"
                >
                  PULAR
                </button>
              </div>
            </div>
          </div>

          <div class="game-actions">
            <button @click="toggleFullscreen" class="fullscreen-btn">
              <span>⛶</span> {{ isMobile ? 'Expandir / Tela Cheia' : 'Jogar em Tela Cheia' }}
            </button>
          </div>

        </div>
      </section>

      <section class="game-info">
        <div class="info-card">
          <h3>📚 Aprendizado</h3>
          <p>Conheça curiosidades sobre a Bacia Cearamirim.</p>
        </div>
        <div class="info-card">
          <h3>⏱️ Tempo</h3>
          <p>Tempo Estimado: 5-10 min</p>
        </div>
        <div class="info-card">
          <h3>🎯 Dificuldade</h3>
          <p>Nível Médio - Para quem curte plataforma</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const unityWrapper = ref(null)
const gameIframe = ref(null)
const isMobile = ref(false)

// Mapeamento de Teclas
const keyMap = {
  'KeyW': 87,
  'KeyA': 65,
  'KeyS': 83,
  'KeyD': 68,
  'Space': 32
}

// Detecção de Mobile
const checkMobile = () => {
  isMobile.value = window.matchMedia("(pointer: coarse)").matches || window.innerWidth <= 768;
}

// Simulação de Teclas para o Iframe
const simulateKey = (code, type) => {
  const iframe = gameIframe.value;
  if (!iframe || !iframe.contentWindow) return;

  iframe.contentWindow.focus();

  const keyCode = keyMap[code];
  const event = new KeyboardEvent(type, {
    key: code === 'Space' ? ' ' : code.replace('Key', '').toLowerCase(),
    code: code,
    keyCode: keyCode,
    which: keyCode,
    bubbles: true,
    cancelable: true
  });

  iframe.contentWindow.dispatchEvent(event);
}

const startKey = (code) => simulateKey(code, 'keydown');
const stopKey = (code) => simulateKey(code, 'keyup');

// Lógica de Tela Cheia Robusta
const toggleFullscreen = async () => {
  const elem = unityWrapper.value
  if (!elem) return

  try {
    if (!document.fullscreenElement && !document.webkitFullscreenElement) {
      // Entrar em tela cheia
      if (elem.requestFullscreen) await elem.requestFullscreen();
      else if (elem.webkitRequestFullscreen) await elem.webkitRequestFullscreen();
      
      // Tentar travar em paisagem no mobile
      if (isMobile.value && screen.orientation && screen.orientation.lock) {
        try {
          await screen.orientation.lock('landscape');
        } catch (e) {
          console.log('Bloqueio de orientação não suportado');
        }
      }
    } else {
      // Sair da tela cheia
      if (document.exitFullscreen) await document.exitFullscreen();
      else if (document.webkitExitFullscreen) await document.webkitExitFullscreen();
    }
  } catch (err) {
    console.error("Erro no fullscreen:", err);
  }
}

onMounted(() => {
  checkMobile();
  window.addEventListener('resize', checkMobile);
})

onUnmounted(() => {
  window.removeEventListener('resize', checkMobile);
})
</script>

<style scoped>
/* Layout Geral */
.game-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.game-header {
  max-width: 1000px;
  margin: 0 auto;
  width: 100%;
}

.back-button {
  display: inline-block;
  margin-bottom: 1rem;
  padding: 0.5rem 1rem;
  background: #1e3c72;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: transform 0.2s;
}

.back-button:hover {
  transform: translateX(-4px);
}

.game-content {
  max-width: 1000px;
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

section {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.game-area {
  background: #f8f9fa;
  padding: 1rem;
}

/* Container do Jogo */
.unity-wrapper {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  background: #000;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  user-select: none;
  -webkit-user-select: none;
}

.unity-wrapper iframe {
  width: 100%;
  height: 100%;
  border: none;
  touch-action: none; 
}

/* === CONTROLES MOBILE === */
.mobile-controls {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 20;
  pointer-events: none; /* Permite ver o jogo, mas deixa clicar nos botões abaixo */
}

/* Estilo Base dos Botões */
.control-btn {
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 4px 6px rgba(0,0,0,0.3);
  backdrop-filter: blur(4px);
  color: white;
  border-radius: 12px;
  font-size: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  pointer-events: auto; /* Reativa o clique */
  -webkit-tap-highlight-color: transparent;
  touch-action: none; /* Impede scroll ao tocar */
}

.control-btn:active {
  background: rgba(255, 255, 255, 0.5);
  transform: scale(0.95);
}

/* --- GRID DAS SETAS (CORREÇÃO) --- */
.d-pad-grid {
  position: absolute;
  bottom: 20px;
  left: 20px;
  display: grid;
  /* Cria 3 colunas e 3 linhas */
  grid-template-columns: 60px 60px 60px;
  grid-template-rows: 55px 55px 55px;
  gap: 5px;
}

/* Posicionamento Correto na Grade 3x3 */
.up-btn    { grid-column: 2; grid-row: 1; }
.left-btn  { grid-column: 1; grid-row: 2; }
.right-btn { grid-column: 3; grid-row: 2; }
.down-btn  { grid-column: 2; grid-row: 3; }

/* --- BOTÃO DE AÇÃO (PULAR) --- */
.action-area {
  position: absolute;
  bottom: 30px;
  right: 30px;
  pointer-events: auto;
}

.jump-btn {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  background: rgba(255, 71, 87, 0.6);
  border: 2px solid rgba(255, 71, 87, 0.9);
  font-size: 1rem;
  font-weight: 800;
  text-transform: uppercase;
}
.jump-btn:active {
  background: rgba(255, 71, 87, 0.9);
}

/* === FULLSCREEN & RESPONSIVIDADE === */
.unity-wrapper:fullscreen {
  border-radius: 0;
  width: 100vw;
  height: 100vh;
}

.game-actions {
  display: flex;
  justify-content: center;
  margin-top: 15px;
}

.fullscreen-btn {
  background: #1e3c72;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 50px;
  cursor: pointer;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
}

.game-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.info-card {
  text-align: center;
  padding: 1.5rem;
}

/* Ajustes para Celulares em Paisagem (Landscape) */
@media (max-height: 500px) and (orientation: landscape) {
  .game-page {
    padding: 0; /* Remove padding para focar no jogo */
  }
  
  .d-pad-grid {
    bottom: 15px;
    left: 15px;
    transform: scale(0.8); /* Diminui um pouco para não cobrir tudo */
    transform-origin: bottom left;
  }
  
  .action-area {
    bottom: 15px;
    right: 15px;
    transform: scale(0.8);
    transform-origin: bottom right;
  }
}

/* Ajustes para telas muito pequenas em Retrato */
@media (max-width: 480px) {
  .d-pad-grid {
    grid-template-columns: 50px 50px 50px;
    grid-template-rows: 45px 45px 45px;
    bottom: 10px;
    left: 10px;
  }
  
  .jump-btn {
    width: 70px;
    height: 70px;
    font-size: 0.8rem;
  }
}
</style>