<template>
  <section class="games-page">
    <!-- TÍTULO -->
    <div class="section-header">
      <h1>Jogos Educativos</h1>
      <p>Aprenda sobre a Bacia Cearamirím de forma divertida!</p>
    </div>

    <!-- CARROSSEL -->
    <div class="carousel-container">
      <div class="carousel">
        <div 
          class="carousel-track" 
          :style="{ transform: `translateX(-${currentIndex * 100}%)` }"
        >
          <div 
            class="carousel-item"
            v-for="game in games"
            :key="game.id"
            @click="selectGame(game)"
            @keydown.enter="selectGame(game)"
            tabindex="0"
            role="button"
          >
            <div 
              class="slide-placeholder"
              :style="{ backgroundColor: game.color }"
            >
              <div class="game-info">
                <h3>{{ game.name }}</h3>
                <p>{{ game.description }}</p>
              </div>
            </div>
          </div>
        </div>

        <button class="nav prev" @click="prev" aria-label="Anterior">‹</button>
        <button class="nav next" @click="next" aria-label="Próximo">›</button>
      </div>

      <!-- Indicadores de slides -->
      <div class="carousel-indicators">
        <button 
          v-for="(_, index) in games"
          :key="index"
          :class="['indicator', { active: index === currentIndex }]"
          @click="currentIndex = index"
          :aria-label="`Slide ${index + 1}`"
        ></button>
      </div>
    </div>

    <!-- MODAL -->
    <div v-if="showModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <button class="modal-close" @click="closeModal" aria-label="Fechar">✕</button>
        
        <div class="modal-game-info">
          <div 
            class="modal-game-icon"
            :style="{ backgroundColor: selectedGame.color }"
          >
            <span class="game-emoji">{{ selectedGame.emoji }}</span>
          </div>
          
          <h2>{{ selectedGame.name }}</h2>
          <p class="game-description">{{ selectedGame.fullDescription }}</p>
          
          <div class="game-details">
            <div class="detail">
              <span class="label">Dificuldade:</span>
              <span class="value">{{ selectedGame.difficulty }}</span>
            </div>
            <div class="detail">
              <span class="label">Tempo:</span>
              <span class="value">{{ selectedGame.duration }}</span>
            </div>
          </div>

          <button class="play-button" @click="playGame">
            🎮 Jogar Agora
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

const games = [
  {
    id: 1,
    name: "Fluxo da Água",
    description: "Entenda o ciclo",
    fullDescription: "Descubra como a água flui pela Bacia Cearamirím. Aprenda sobre rios, afluentes e a importância da preservação hídrica.",
    emoji: "💧",
    color: "#99ccff",
    difficulty: "Médio",
    duration: "10-15 min",
    route: "fluxo-agua"
  },
  {
    id: 2,
    name: "Protetor do Ecossistema",
    description: "Salve a natureza",
    fullDescription: "Proteja os ecossistemas da bacia. Identifique plantas e animais nativos e aprenda sobre conservação ambiental.",
    emoji: "🌿",
    color: "#99ff99",
    difficulty: "Fácil",
    duration: "8-12 min",
    route: "protetor-ecossistema"
  },
  {
    id: 3,
    name: "Qualidade da Água",
    description: "Teste seus conhecimentos",
    fullDescription: "Desafie-se a monitorar e melhorar a qualidade da água. Conheça os parâmetros de potabilidade e sustentabilidade.",
    emoji: "🧪",
    color: "#ffcc99",
    difficulty: "Difícil",
    duration: "15-20 min",
    route: "qualidade-agua"
  }
];

const currentIndex = ref(0);
const showModal = ref(false);
const selectedGame = ref(null);

function next() {
  currentIndex.value = (currentIndex.value + 1) % games.length;
}

function prev() {
  currentIndex.value = (currentIndex.value - 1 + games.length) % games.length;
}

function selectGame(game) {
  selectedGame.value = game;
  showModal.value = true;
}

function closeModal() {
  showModal.value = false;
}

function playGame() {
  // Navegar para a página do jogo usando hash
  window.location.hash = `#jogos/${selectedGame.value.route}`;
 
}
</script>
<style scoped>
/* LAYOUT GERAL */
.games-page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3rem;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

/* HEADER */
.section-header {
  text-align: center;
  max-width: 800px;
  margin-bottom: 1rem;
}

.section-header h1 {
  font-size: 2.5rem;
  color: #1e3c72;
  margin-bottom: 0.5rem;
  font-weight: 800;
}

.section-header p {
  font-size: 1.1rem;
  color: #555;
  line-height: 1.6;
}

/* CARROSSEL CONTAINER */
.carousel-container {
  width: 100%;
  max-width: 1000px;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* CARROSSEL */
.carousel {
  position: relative;
  width: 100%;
  height: 55vw;
  max-height: 500px;
  min-height: 200px;
  overflow: hidden;
  border-radius: 16px;
  background: #fff;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}

.carousel-track {
  display: flex;
  transition: transform 0.5s ease;
  width: 100%;
  height: 100%;
}

.carousel-item {
  min-width: 100%;
  height: 100%;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.carousel-item:hover {
  transform: scale(1.02);
}

.slide-placeholder {
  width: 100%;
  height: 100%;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.slide-placeholder::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.2);
  transition: background 0.3s ease;
}

.carousel-item:hover .slide-placeholder::before {
  background: rgba(0, 0, 0, 0.1);
}

.game-info {
  position: relative;
  z-index: 2;
  text-align: center;
  color: white;
  padding: 2rem;
}

.game-info h3 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.game-info p {
  font-size: 1.1rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

/* BOTÕES NAVEGAÇÃO */
.nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 24px;
  z-index: 10;
  transition: all 0.3s ease;
}

.nav:hover {
  background: rgba(0, 0, 0, 0.7);
  transform: translateY(-50%) scale(1.1);
}

.nav.prev {
  left: 15px;
}

.nav.next {
  right: 15px;
}

/* INDICADORES */
.carousel-indicators {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
}

.indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid #1e3c72;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
}

.indicator.active {
  background: #1e3c72;
  transform: scale(1.2);
}

/* MODAL */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.modal-content {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: slideUp 0.3s ease;
  position: relative;
}

@keyframes slideUp {
  from {
    transform: translateY(30px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.modal-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #666;
  transition: color 0.3s ease;
}

.modal-close:hover {
  color: #000;
}

.modal-game-info {
  text-align: center;
}

.modal-game-icon {
  width: 100px;
  height: 100px;
  margin: 0 auto 1.5rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.modal-content h2 {
  font-size: 1.8rem;
  color: #1e3c72;
  margin-bottom: 1rem;
  font-weight: 700;
}

.game-description {
  font-size: 1rem;
  color: #555;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.game-details {
  display: flex;
  gap: 2rem;
  justify-content: center;
  margin-bottom: 2rem;
  padding: 1rem 0;
  border-top: 1px solid #eee;
  border-bottom: 1px solid #eee;
}

.detail {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.detail .label {
  font-size: 0.85rem;
  color: #999;
  font-weight: 600;
}

.detail .value {
  font-size: 1rem;
  color: #1e3c72;
  font-weight: 700;
}

.play-button {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(135deg, #1e3c72 0%, #2e5090 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
}

.play-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(30, 60, 114, 0.3);
}

.play-button:active {
  transform: translateY(0);
}

/* RESPONSIVIDADE */
@media (max-width: 768px) {
  .games-page {
    padding: 2rem 1rem;
    gap: 2rem;
  }

  .section-header h1 {
    font-size: 2rem;
  }

  .section-header p {
    font-size: 1rem;
  }

  .game-info h3 {
    font-size: 1.5rem;
  }

  .game-info p {
    font-size: 0.95rem;
  }

  .modal-content {
    padding: 1.5rem;
  }

  .modal-content h2 {
    font-size: 1.5rem;
  }
}

@media (max-width: 600px) {
  .games-page {
    padding: 1.5rem 1rem;
    gap: 1.5rem;
  }

  .section-header h1 {
    font-size: 1.75rem;
  }

  .carousel {
    height: 70vw;
    min-height: 180px;
  }

  .nav {
    padding: 8px 12px;
    font-size: 20px;
  }

  .game-info {
    padding: 1rem;
  }

  .game-info h3 {
    font-size: 1.2rem;
  }

  .game-info p {
    font-size: 0.9rem;
  }

  .modal-overlay {
    padding: 1rem;
  }

  .modal-content {
    padding: 1.25rem;
  }

  .modal-game-icon {
    width: 80px;
    height: 80px;
    font-size: 2.5rem;
  }

  .game-details {
    gap: 1rem;
    flex-direction: column;
  }
}
</style>
