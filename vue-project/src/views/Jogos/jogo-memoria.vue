<template>
  <section class="container">
    <h1>Jogo da Memória</h1>

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
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import imagem_1 from '@/assets/images/Jogos/Memória/imagem_1.jpeg';
import imagem_2 from '@/assets/images/Jogos/Memória/imagem_2.jpeg';
import imagem_3 from '@/assets/images/Jogos/Memória/imagem_3.jpeg';
import imagem_4 from '@/assets/images/Jogos/Memória/imagem_4.jpeg';
import imagem_5 from '@/assets/images/Jogos/Memória/imagem_5.jpeg';
import imagem_6 from '@/assets/images/Jogos/Memória/imagem_6.jpeg';
import imagem_7 from '@/assets/images/Jogos/Memória/imagem_7.jpeg';
import imagem_8 from '@/assets/images/Jogos/Memória/imagem_8.jpeg';

const images = [
  imagem_1,
  imagem_2,
  imagem_3,
  imagem_4,
  imagem_5,
  imagem_6,
  imagem_7,
  imagem_8
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
.container {
  text-align: center;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  height: 50rem;
}

.board {
  display: grid;
  grid-template-columns: repeat(4, 90px);
  gap: 12px;
  justify-content: center;
  margin-top: 20px;
}

.card {
  width: 90px;
  height: 90px;
  background: #333;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card img {
  width: 100%;
  height: 100%;
  object-fit: cover;   
  border-radius: 8px;
}

.back {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #555, #222);
  border-radius: 8px;
}
</style>
