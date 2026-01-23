<template>
  <div class="container">
    <h1>Jogo da Memória</h1>

    <div class="board">
      <div
        v-for="(card, index) in cards"
        :key="index"
        class="card"
        :class="{ flipped: card.flipped || card.matched }"
        @click="flipCard(card)"
      >
        <span v-if="card.flipped || card.matched">
          {{ card.icon }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()


const icons = ['🐶','🐱','🦊','🐼','🐸','🐵','🐷','🐰']

const cards = ref([])
const flippedCards = ref([])
const lock = ref(false)

function startGame() {
  const duplicated = [...icons, ...icons]

  cards.value = duplicated
    .sort(() => Math.random() - 0.5)
    .map(icon => ({
      icon,
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
    if (c1.icon === c2.icon) {
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
  font-family: Arial, sans-serif;
}

.board {
  display: grid;
  grid-template-columns: repeat(4, 80px);
  gap: 10px;
  justify-content: center;
  margin-top: 20px;
}

.card {
  width: 80px;
  height: 80px;
  background: #444;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 32px;
  color: black;
}

.card.flipped {
  background: #fff;
}
</style>
