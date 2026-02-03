<template>
  <section class="game-page">
    <div class="game-header">
      <router-link to="/jogos" class="back-button">← Voltar</router-link>
      <h1>Jogo da Memória</h1>
      <p>Encontre os pares e conheça as belezas da região</p>
    </div>

    <div class="game-content">
      <section class="game-description">
        <h2>Como Jogar</h2>
        <p>O objetivo é encontrar todos os pares de imagens idênticas.</p>
        <p>Clique/Toque em uma carta para virá-la e tente memorizar sua posição. Se acertar o par, elas permanecem viradas!</p>
      </section>

      <section class="game-area">
        <div class="memory-game-container">
          
          <div class="board">
            <div
              v-for="(card, index) in cards"
              :key="index"
              class="card"
              :class="{ flipped: card.flipped || card.matched }"
              @click="flipCard(card)"
            >
              <img
                v-if="card.flipped || card.matched"
                :src="card.image"
                alt="card"
              />
              <div v-else class="back"></div>
            </div>
          </div>

          <div class="game-actions">
            <button @click="startGame" class="action-btn">
              <span>↻</span> Reiniciar Jogo
            </button>
          </div>

        </div>
      </section>

      <section class="game-info">
        <div class="info-card">
          <h3>🧠 Aprendizado</h3>
          <p>Estimula a memória visual e o reconhecimento de padrões.</p>
        </div>
        <div class="info-card">
          <h3>⏱️ Tempo</h3>
          <p>Tempo Estimado: 1-3 min</p>
        </div>
        <div class="info-card">
          <h3>🎯 Dificuldade</h3>
          <p>Nível Fácil - Para todas as idades</p>
        </div>
      </section>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'


import imagem_1 from '@/assets/images/Jogos/Memória/imagem_1.jpeg';
import imagem_2 from '@/assets/images/Jogos/Memória/imagem_2.jpeg';
import imagem_3 from '@/assets/images/Jogos/Memória/imagem_3.jpeg';
import imagem_4 from '@/assets/images/Jogos/Memória/imagem_4.jpeg';
import imagem_5 from '@/assets/images/Jogos/Memória/imagem_5.jpeg';
import imagem_6 from '@/assets/images/Jogos/Memória/imagem_6.jpeg';
import imagem_7 from '@/assets/images/Jogos/Memória/imagem_7.jpeg';
import imagem_8 from '@/assets/images/Jogos/Memória/imagem_8.jpeg';

const router = useRouter()

const images = [
  imagem_1, imagem_2, imagem_3, imagem_4,
  imagem_5, imagem_6, imagem_7, imagem_8
]

const cards = ref([])
const flippedCards = ref([])
const lock = ref(false)

function startGame() {
  const duplicated = [...images, ...images]

  cards.value = duplicated
    .sort(() => Math.random() - 0.5)
    .map(image => ({
      image,
      flipped: false,
      matched: false
    }))
    
  flippedCards.value = []
  lock.value = false
}

function flipCard(card) {
  if (lock.value || card.flipped || card.matched) return

  card.flipped = true
  flippedCards.value.push(card)

  if (flippedCards.value.length === 2) {
    checkMatch()
  }
}

function checkMatch() {
  lock.value = true
  const [c1, c2] = flippedCards.value

  setTimeout(() => {
    if (c1.image === c2.image) {
      c1.matched = true
      c2.matched = true
    } else {
      c1.flipped = false
      c2.flipped = false
    }

    flippedCards.value = []
    lock.value = false
  }, 800)
}

onMounted(startGame)
</script>

<style scoped>

.game-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.game-header, .game-content {
  max-width: 1000px;
  margin: 0 auto;
  width: 100%;
}

.game-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
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


.game-area {
  background: #f8f9fa; 
  padding: 2rem;
  display: flex;
  justify-content: center;
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



.memory-game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.board {
  display: grid;

  grid-template-columns: repeat(4, 150px);
  gap: 20px;
  justify-content: center;
  margin-bottom: 2rem;
}

.card {
  width: 150px;
  height: 150px;
  background: #333;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: transform 0.3s ease;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.card.flipped {
    transform: rotateY(180deg);
}

.card img {
  width: 100%;
  height: 100%;
  object-fit: cover;   
  border-radius: 8px;
  transform: rotateY(180deg); 
}

.back {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #555, #222);
  border-radius: 8px;
}

.game-actions {
  display: flex;
  justify-content: center;
}

.action-btn {
  background: #1e3c72;
  color: white;
  border: none;
  padding: 10px 25px;
  border-radius: 50px;
  cursor: pointer;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(30, 60, 114, 0.3);
  display: flex;
  align-items: center;
  gap: 8px;
}

.action-btn:hover {
  background: #2e5090;
  transform: translateY(-2px);
  box-shadow: 0 6px 15px rgba(30, 60, 114, 0.4);
}


@media (max-width: 768px) {
  .game-page {
    padding: 1rem;
  }
  
  .game-area {
    padding: 1rem;
  }

  .board {
    grid-template-columns: repeat(4, 1fr); 
    gap: 10px;
    width: 100%;
  }

  .card {

    width: auto; 
    height: auto;
    aspect-ratio: 1 / 1; 
  }
  
  .game-header h1 {
    font-size: 1.8rem;
  }
}
</style>