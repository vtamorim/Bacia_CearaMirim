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
  <div class="game-page">
    <div class="game-content">
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

            <div v-if="isMobile && !isPlaying" class="game-overlay">
              <div class="overlay-content">
                <span class="rotate-icon">↻</span>
                <h3>Modo Imersivo</h3>
                <p>Para a melhor experiência, este jogo requer tela cheia.</p>
                <button class="start-btn" @click="enterImmersiveMode">
                  ▶ JOGAR AGORA
                </button>
              </div>
            </div>

            <div v-if="isMobile && isPlaying" class="mobile-controls">
              <div class="d-pad-grid">
                  <button class="control-btn up-btn" @touchstart.prevent="startKey('KeyW')" @touchend.prevent="stopKey('KeyW')">▲</button>
                  <button class="control-btn left-btn" @touchstart.prevent="startKey('KeyA')" @touchend.prevent="stopKey('KeyA')">◀</button>
                  <button class="control-btn right-btn" @touchstart.prevent="startKey('KeyD')" @touchend.prevent="stopKey('KeyD')">▶</button>
                  <button class="control-btn down-btn" @touchstart.prevent="startKey('KeyS')" @touchend.prevent="stopKey('KeyS')">▼</button>
               </div>
               <div class="action-area">
                  <button class="control-btn jump-btn" @touchstart.prevent="startKey('Space')" @touchend.prevent="stopKey('Space')">PULAR</button>
               </div>
            </div>

          </div>
          
          <div class="game-actions" v-if="!isMobile">
            <button @click="toggleFullscreen" class="fullscreen-btn">
              <span>⛶</span> Jogar em Tela Cheia
            </button>
          </div>
        </div>
      </section>

      </div>
  </div>
</div>
            </div>
          <div class="game-actions">
            <button @click="toggleFullscreen" class="fullscreen-btn">
              <span>⛶</span> {{ isMobile ? 'Expandir' : 'Jogar em Tela Cheia' }}
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
const isPlaying = ref(false) // Novo estado para controlar o overlay

// ... (Seu keyMap e simulateKey continuam iguais) ...


// Função Poderosa: Entra em Tela Cheia E Tenta Travar em Paisagem
const enterImmersiveMode = async () => {
  const elem = unityWrapper.value;
  if (!elem) return;

  try {
    // 1. Solicita Tela Cheia
    if (elem.requestFullscreen) {
      await elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) {
      await elem.webkitRequestFullscreen();
    }
    
    // 2. Tenta Travar Orientação (Funciona bem no Android/Chrome, Safari ignora às vezes)
    if (screen.orientation && screen.orientation.lock) {
      try {
        await screen.orientation.lock('landscape');
      } catch (err) {
        console.log('Bloqueio de orientação não suportado pelo navegador');
      }
    }

    // 3. Ativa os controles
    isPlaying.value = true;
    
  } catch (err) {
    console.error("Erro ao entrar em tela cheia:", err);
  }
}

// Monitora se o usuário saiu da tela cheia pelo botão "Voltar" do celular
const handleFullscreenChange = () => {
  if (!document.fullscreenElement && !document.webkitFullscreenElement) {
    // Se saiu da tela cheia no mobile, volta a mostrar o overlay
    if (isMobile.value) {
      isPlaying.value = false;
    }
  }
}
// Mapeamento de Códigos de Tecla para Unity
const keyMap = {
  'KeyW': 87, // W
  'KeyA': 65, // A
  'KeyS': 83, // S
  'KeyD': 68, // D
  'Space': 32 // Barra de Espaço
}

// Detecção de Mobile
const checkMobile = () => {
  isMobile.value = window.matchMedia("(pointer: coarse)").matches || window.innerWidth <= 768;
  // Se virou desktop, libera o jogo
  if (!isMobile.value) isPlaying.value = true; 
}

// Lógica de Simulação de Teclas
const simulateKey = (code, type) => {
  const iframe = gameIframe.value;
  if (!iframe || !iframe.contentWindow) return;

  // Garante foco no iframe para receber o input
  iframe.contentWindow.focus();

  const keyCode = keyMap[code];
  
  // Cria o evento de teclado
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

const toggleFullscreen = () => {
  const elem = unityWrapper.value
  if (!elem) return

  if (!document.fullscreenElement) {
    if (elem.requestFullscreen) elem.requestFullscreen()
    else if (elem.webkitRequestFullscreen) elem.webkitRequestFullscreen()
  } else {
    document.exitFullscreen()
  }
}

onMounted(() => {
  checkMobile();
  window.addEventListener('resize', checkMobile);
  document.addEventListener('fullscreenchange', handleFullscreenChange);
  document.addEventListener('webkitfullscreenchange', handleFullscreenChange);
})

onUnmounted(() => {
  window.removeEventListener('resize', checkMobile);
  document.removeEventListener('fullscreenchange', handleFullscreenChange);
  document.removeEventListener('webkitfullscreenchange', handleFullscreenChange);
})
</script>

<style scoped>
/* SEUS ESTILOS EXISTENTES MANTIDOS ABAIXO */
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
  transition: all 0.3s ease;
  font-weight: 600;
}

.back-button:hover {
  background: #2e5090;
  transform: translateX(-4px);
}

.game-header h1 {
  font-size: 2.5rem;
  color: #1e3c72;
  margin-bottom: 0.5rem;
}

.game-header p {
  font-size: 1.1rem;
  color: #666;
}
.game-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(30, 60, 114, 0.95); /* Azul escuro quase sólido */
  z-index: 50; /* Fica acima de tudo */
  display: flex;
  justify-content: center;
  align-items: center;
  backdrop-filter: blur(5px);
}

.overlay-content {
  text-align: center;
  color: white;
  padding: 20px;
  max-width: 300px;
}

.rotate-icon {
  font-size: 3rem;
  display: block;
  margin-bottom: 10px;
  animation: rotateHint 2s infinite ease-in-out;
}

.overlay-content h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.overlay-content p {
  font-size: 0.9rem;
  opacity: 0.8;
  margin-bottom: 1.5rem;
  color: #c3cfe2;
}

.start-btn {
  background: #ff4757;
  color: white;
  border: none;
  padding: 15px 30px;
  font-size: 1.1rem;
  font-weight: bold;
  border-radius: 50px;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(255, 71, 87, 0.4);
  transition: transform 0.2s;
  animation: pulse 1.5s infinite;
}

.start-btn:active {
  transform: scale(0.95);
}

/* Animações para chamar atenção */
@keyframes rotateHint {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(-90deg); }
  75% { transform: rotate(-90deg); }
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(255, 71, 87, 0.7); }
  70% { box-shadow: 0 0 0 15px rgba(255, 71, 87, 0); }
  100% { box-shadow: 0 0 0 0 rgba(255, 71, 87, 0); }
}

/* Esconde scrollbar quando em fullscreen no mobile */
.unity-wrapper:fullscreen {
  overflow: hidden;
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

section h2 {
  color: #1e3c72;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

section p {
  color: #555;
  line-height: 1.6;
  margin-bottom: 0.5rem;
}

.game-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  padding: 0;
  background: transparent;
  box-shadow: none;
}

.info-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.info-card h3 {
  color: #1e3c72;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.info-card p {
  color: #666;
  font-size: 0.95rem;
}

.game-area {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 12px;
}

.unity-container {
  width: 100%;
  max-width: 960px;
  margin: 0 auto;
}

.unity-wrapper {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  background: #000;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  /* Previne seleção de texto ao tocar nos botões */
  user-select: none;
  -webkit-user-select: none;
}

.unity-wrapper iframe {
  width: 100%;
  height: 100%;
  border: none;
  /* Importante para que o toque não dê scroll na página */
  touch-action: none; 
}

/* === ESTILOS DOS CONTROLES MOBILE === */
.mobile-controls {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 20;
  pointer-events: none; /* Permite tocar no jogo através da área vazia */
  
  /* Removemos o display:flex aqui para usar posicionamento absoluto nos grupos */
}
.d-pad, .action-buttons {
  pointer-events: auto; /* Reativa o toque nos botões */
}

.d-pad {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  margin-bottom: 20px;
  margin-left: 10px;
}.d-pad-grid {
  pointer-events: auto;
  display: grid;
  grid-template-columns: repeat(3, 50px);
  grid-template-rows: repeat(3, 45px);
  gap: 5px;
  
  position: absolute;
  bottom: 20px;  /* Distância do fundo */
  left: 20px;    /* Distância da esquerda */
}

.d-pad-middle {
  display: flex;
  gap: 40px; /* Espaço entre Esquerda e Direita */
}




/* === MODIFICAÇÕES FINAIS === */

.unity-wrapper:fullscreen {
  width: 100vw;
  height: 100vh;
  border-radius: 0;
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
  padding: 10px 20px;
  border-radius: 50px;
  cursor: pointer;
  font-weight: 600;
}

@media (max-width: 768px) {
  /* Diminui um pouco os botões se a tela for pequena demais */
  .d-pad-grid {
    grid-template-columns: repeat(3, 45px);
    grid-template-rows: repeat(3, 40px);
    bottom: 15px;
    left: 15px;
  }
  
  .jump-btn {
    width: 70px;
    height: 70px;
    bottom: 15px;
    right: 15px;
  }
}
/* Estilo Base dos Botões */
.control-btn {
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 6px rgba(0,0,0,0.2);
  backdrop-filter: blur(4px);
  color: white;
  border-radius: 10px;
  font-size: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

/* Feedback Visual ao Tocar */
.control-btn:active {
  background: rgba(255, 255, 255, 0.4);
  transform: scale(0.95);
}
/* Área de Ação (Direita) */
.action-area {
  pointer-events: auto;
  position: absolute;
  bottom: 30px;  /* Um pouco mais alto para o dedão */
  right: 20px;   /* Distância da direita */
}

.jump-btn {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: rgba(255, 71, 87, 0.5); /* Vermelho semitransparente */
  border: 2px solid rgba(255, 71, 87, 0.8);
  font-size: 0.9rem;
  font-weight: 800;
  text-transform: uppercase;
}
.jump-btn:active {
  background: rgba(255, 71, 87, 0.8);
}

/* === AJUSTES PARA TELAS PEQUENAS E PAISAGEM === */
@media (max-height: 500px) {
  /* Se a tela for muito "baixa" (modo paisagem no celular) */
  .mobile-controls {
    padding: 10px 30px;
  }
  
  .d-pad-grid {
    grid-template-columns: repeat(3, 50px);
    grid-template-rows: repeat(3, 45px);
  }
  
  .control-btn {
    font-size: 1.2rem;
  }

  .jump-btn {
    width: 75px;
    height: 75px;
    font-size: 0.8rem;
  }
}
</style>