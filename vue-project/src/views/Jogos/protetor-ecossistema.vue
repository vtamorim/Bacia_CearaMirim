<template>
  <div class="game-page">
    <div class="game-header">
      <router-link to="/jogos" class="back-button">← Voltar</router-link>
      <h1>🌿 Protetor do Ecossistema</h1>
      <p>Salve a biodiversidade da Bacia Cearamirím</p>
    </div>

    <div class="game-content">
      <section class="game-description">
        <h2>Como Jogar</h2>
        <p>Proteja os ecossistemas nativos identificando corretamente os animais e plantas. Cada resposta correta ajuda a preservar a biodiversidade.</p>
        <p>Descubra espécies endêmicas, aprenda sobre habitat e conheça a importância da conservação ambiental.</p>
      </section>

      <section class="game-area">
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
      </section>

      <section class="game-info">
        <div class="info-card">
          <h3>📚 Aprendizado</h3>
          <p>Você aprenderá sobre a biodiversidade local e espécies protegidas.</p>
        </div>
        <div class="info-card">
          <h3>⏱️ Tempo</h3>
          <p>Tempo estimado: 8-12 minutos</p>
        </div>
        <div class="info-card">
          <h3>🎯 Dificuldade</h3>
          <p>Nível Fácil - Perfeito para iniciantes</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()



export default {
  data() {
    return {
      icons: ['🐶','🐱','🦊','🐼','🐸','🐵','🐷','🐰'],
      cards: [],
      flippedCards: [],
      lock: false
    }
  },

  mounted() {
    this.startGame()
  },

  methods: {
    startGame() {
      const duplicated = [...this.icons, ...this.icons]

      this.cards = duplicated
        .sort(() => Math.random() - 0.5)
        .map(icon => ({
          icon,
          flipped: false,
          matched: false
        }))
    },

    flipCard(card) {
      if (this.lock || card.flipped || card.matched) return

      card.flipped = true
      this.flippedCards.push(card)

      if (this.flippedCards.length === 2) {
        this.checkMatch()
      }
    },

    checkMatch() {
      this.lock = true
      const [c1, c2] = this.flippedCards

      setTimeout(() => {
        if (c1.icon === c2.icon) {
          c1.matched = true
          c2.matched = true
        } else {
          c1.flipped = false
          c2.flipped = false
        }

        this.flippedCards = []
        this.lock = false
      }, 800)
    }
  }
}
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

.placeholder {
  text-align: center;
  padding: 4rem 2rem;
  background: #f0f4f8;
  border-radius: 12px;
  border: 2px dashed #ddd;
}

.placeholder .emoji {
  font-size: 4rem;
  display: block;
  margin-bottom: 1rem;
}

.placeholder p {
  color: #999;
  font-size: 1.1rem;
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

@media (max-width: 768px) {
  .game-page {
    padding: 1.5rem;
  }

  .game-header h1 {
    font-size: 1.8rem;
  }

  section {
    padding: 1.5rem;
  }

  .info-card {
    padding: 1rem;
  }
}
</style>
