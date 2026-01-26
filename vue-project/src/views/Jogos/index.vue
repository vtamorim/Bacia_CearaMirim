<template>
  <section class="games-page">



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
              :style="{ backgroundImage: `url(${game.color})` }"
              style="background-size: cover; background-position: center;"
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

    <div v-if="showModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <button class="modal-close" @click="closeModal" aria-label="Fechar">✕</button>
        
        <div class="modal-game-info">
          <div 
            class="modal-game-icon"
            :style="{ backgroundColor: selectedGame.color }"
          >
            <img :src="selectedGame.emoji" alt="imagem do jogo" v-if="selectedGame.emoji" class="imagem_jogo"/>
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
            Jogar Agora
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from 'vue-router';
import foto_quiz from '@/assets/images/Jogos/quiz.png'
import capa_quiz from '@/assets/images/Jogos/imagem_quiz.png'
import foto_obstaculo from '@/assets/images/Jogos/foto_obstaculo.png'
import foto_quebracabeca from '@/assets/images/Jogos/foto_quebracabeca.png'
import foto_qc from '@/assets/images/Jogos/imagem_qc.png'
import foto_memoria from '@/assets/images/Jogos/foto_memoria.png'
import pipeconect from '@/assets/images/Jogos/pipeconect.png'

const games = [
  {
    id: 1,
    name: "Aventura na Bacia Hidrográfica",
    description: "Passar por obstáculos, saber mais sobre a Bacia Hidrográfica",
    fullDescription: "Uma jornada em que o jogador precisa pecorrer e superar obstáculos e plataformas para que possa ter uma grande vitória no final.",
    emoji: foto_obstaculo,
    color: "#99ccff",
    difficulty: "Médio",
    duration: "10-15 min",
    route: "fluxo-agua"
  },
  {
    id: 2,
    name: "Jogo da Memória",
    description: "Jogo de memória para testar sua habilidade",
    fullDescription: "Teste sua memória combinando pares de cartas relacionadas à Bacia Ceara-mirím e à preservação dos recursos hídricos.",
    emoji: foto_memoria,
    color: "#99ff99",
    difficulty: "Médio",
    duration: "10 min",
    route: "jogo-memoria"
  },
  {
    id: 3,
    name: "Quiz",
    description: "Teste seus conhecimentos",
    fullDescription: "Perguntas para testar o seu conhecimento sobre a Bacia Ceara-mirím e a importância da preservação dos recursos hídricos.",
    emoji: foto_quiz,
    color: capa_quiz,
    difficulty: "Difícil",
    duration: "5-10 min",
    route: "quiz"
  },{
    id: 4,
    name : "Quebra-cabeça",
    description: "Resolva o que pode quebrar a sua cabeça",
    fullDescription: "Monte o quebra-cabeça relacionado à Bacia Ceara-mirím, aprendendo sobre seus elementos enquanto se diverte.",
    emoji: foto_qc, 
    color: foto_quebracabeca,
    difficulty:"Médio",
    duration: "5 min",
    route: null

},
{
    id : 5,
    name : "Conexão de tubo",
    description: "Conecte os canos para levar a água ao seu destino",
    fullDescription: "Conecte os canos corretamente para garantir que a água flua do ponto de origem até o destino final, evitando vazamentos e desperdícios.",
    emoji: pipeconect,
    color : "nada",
    difficulty: "Fácil",
    duration: "3-5 min",
    route: null


}
];

const currentIndex = ref(0);
const showModal = ref(false);
const selectedGame = ref(null);
const router = useRouter();

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
  if (!selectedGame.value) return;
  router.push({ name: selectedGame.value.route });
}
</script>
<style scoped>

.games-page {
  width: 100%;
  min-height: calc(100vh - 200px);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: clamp(1.5rem, 4vw, 3rem);
  padding: clamp(1.5rem, 4vw, 3rem) clamp(0.75rem, 3vw, 2rem);
}


.imagem_jogo{
  width: 60%;
  height: 60%;
  object-fit: contain;
}



.carousel-container {
  width: 100%;
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}


.carousel {
  position: relative;
  width: 100%;
  height: clamp(200px, 55vw, 500px);
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
    background: linear-gradient(
    to bottom,
    rgba(0,0,0,0.35),
    rgba(0,0,0,0.55)
  );
  transition: background 0.3s ease;
}


.carousel-item:focus {
  outline: 3px solid #1e3c72;
  outline-offset: -3px;
}
.game-info {
  position: relative;
  z-index: 2;
  text-align: center;
  color: white;
  padding: clamp(1rem, 3vw, 2rem);
}

.game-info h3 {
  font-size: clamp(1.2rem, 3.5vw, 2rem);
  margin-bottom: 0.5rem;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  line-height: 1.2;
}

.game-info p {
  font-size: clamp(0.9rem, 2vw, 1.1rem);
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

.nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: clamp(0.5rem, 2vw, 1rem);
  border-radius: 8px;
  cursor: pointer;
  font-size: clamp(1.2rem, 3vw, 1.5rem);
  z-index: 10;
  transition: all 0.3s ease;
  min-width: 44px;
  min-height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav:hover {
  background: rgba(0, 0, 0, 0.7);
  transform: translateY(-50%) scale(1.1);
}

.nav.prev {
  left: clamp(0.5rem, 2vw, 1rem);
}

.nav.next {
  right: clamp(0.5rem, 2vw, 1rem);
}


.carousel-indicators {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  padding: 0 1rem;
}

.indicator {
  width: 14px;
  height: 14px;
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
  overflow-y: auto;
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
  padding: clamp(1.25rem, 3vw, 2rem);
  max-width: 500px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: slideUp 0.3s ease;
  position: relative;
  margin: auto;
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
  font-size: clamp(1.2rem, 2vw, 1.5rem);
  cursor: pointer;
  color: #666;
  transition: color 0.3s ease;
  padding: 0.5rem;
  min-width: 40px;
  min-height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-close:hover {
  color: #000;
}

.modal-game-info {
  text-align: center;
}

.modal-game-icon {
  width: clamp(70px, 15vw, 100px);
  height: clamp(70px, 15vw, 100px);
  margin: 0 auto 1.5rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: clamp(2rem, 5vw, 3rem);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.modal-content h2 {
  font-size: clamp(1.3rem, 3.5vw, 1.8rem);
  color: #1e3c72;
  margin-bottom: 1rem;
  font-weight: 700;
  line-height: 1.2;
  max-height: 90vh;
  overflow-y: auto;
}

.game-description {
  font-size: clamp(0.9rem, 1.8vw, 1rem);
  color: #555;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.game-details {
  display: flex;
  gap: clamp(1rem, 2vw, 2rem);
  justify-content: center;
  margin-bottom: 2rem;
  padding: 1rem 0;
  border-top: 1px solid #eee;
  border-bottom: 1px solid #eee;
  flex-wrap: wrap;
}

.detail {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.detail .label {
  font-size: clamp(0.75rem, 1.4vw, 0.85rem);
  color: #999;
  font-weight: 600;
}

.detail .value {
  font-size: clamp(0.9rem, 1.6vw, 1rem);
  color: #1e3c72;
  font-weight: 700;
}

.play-button {
  width: 100%;
  padding: clamp(0.75rem, 2vw, 1rem);
  background: linear-gradient(135deg, #1e3c72 0%, #2e5090 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: clamp(0.95rem, 1.8vw, 1.1rem);
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  min-height: 44px;
}

.play-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(30, 60, 114, 0.3);
}

.play-button:active {
  transform: translateY(0);
}

@media (max-width: 768px) {
  .games-page {
    padding: clamp(1rem, 3vw, 1.5rem);
    gap: clamp(1rem, 3vw, 2rem);
  }

  .modal-overlay {
    padding: 1rem;
  }

  .modal-content {
    max-width: 90vw;
  }
}

@media (max-width: 600px) {
  .games-page {
    padding: clamp(0.75rem, 2vw, 1.25rem);
    gap: 1.2rem;
  }

  .section-header h1 {
    font-size: 1.5rem;
  }

  .carousel {
    height: clamp(180px, 60vw, 300px);
  }

  .game-info {
    padding: 1rem;
  }

  .game-info h3 {
    font-size: 1.1rem;
  }

  .game-info p {
    font-size: 0.85rem;
  }

  .nav {
    padding: 12px 16px;
    font-size: 22px;
    min-width: 36px;
    min-height: 36px;
  }

  .nav.prev {
    left: 0.5rem;
  }

  .nav.next {
    right: 0.5rem;
  }

  .modal-overlay {
    padding: 0.75rem;
  }

  .modal-content {
    padding: 1rem;
    max-width: 95vw;
  }

  .modal-game-icon {
    width: 70px;
    height: 70px;
    font-size: 2rem;
  }

  .game-details {
    gap: 0.75rem;
    flex-direction: column;
    padding: 0.75rem 0;
  }
  .indicator{
    width: 16px;
    height: 16px;
  }
}
@media (hover: hover) {
  .carousel-item:hover {
    transform: scale(1.02);
  }

  .carousel-item:hover .slide-placeholder::before {
    background: rgba(0, 0, 0, 0.1);
  }
}
@media (max-width: 480px) {
  .games-page {
    padding: 0.75rem 0.5rem;
    gap: 1rem;
  }

  .section-header h1 {
    font-size: 1.3rem;
  }

  .section-header p {
    font-size: 0.9rem;
  }

  .carousel {
      aspect-ratio: 16 / 9;
  max-height: 480px;
  min-height: 220px;
  }

  .game-info h3 {
    font-size: 1rem;
  }

  .game-info p {
    font-size: 0.8rem;
  }

  .nav {
    padding: 0.4rem 0.6rem;
    min-width: 32px;
    min-height: 32px;
    font-size: 0.9rem;
  }

  .indicator {
    width: 10px;
    height: 10px;
  }

  .modal-content {
    padding: 0.9rem;
  }

  .modal-close {
    top: 0.75rem;
    right: 0.75rem;
  }

  .modal-game-icon {
    width: 60px;
    height: 60px;
    font-size: 1.75rem;
  }

  .modal-content h2 {
    font-size: 1.2rem;
  }

  .game-description {
    font-size: 0.85rem;
  }

  .play-button {
    padding: 0.6rem;
    font-size: 0.9rem;
    min-height: 40px;
  }
}
</style>
