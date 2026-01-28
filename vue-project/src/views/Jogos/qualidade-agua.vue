<template>
  <div class="game-page">
    <div class="game-header">
      <router-link to="/jogos" class="back-button">← Voltar</router-link>
      <h1>🧪 Qualidade da Água</h1>
      <p>Monitore e melhore a qualidade da água</p>
    </div>

    <div class="game-content">
      <section class="game-description">
        <h2>Como Jogar</h2>
        <p>Seja um especialista em monitoramento de qualidade da água! Teste amostras de água e ajuste os parâmetros para atingir os padrões de potabilidade.</p>
        <p>Aprenda sobre pH, turbidez, contaminantes e como manter a água segura para consumo.</p>
      </section>

      <section class="game-area">
        <h2>Jogo em Desenvolvimento</h2>
        <div class="placeholder">
          <iframe 
      src="public/TERCEIRO JOGO/index.html" 
      frameborder="0" 
      style="width: 800px; height: 600px;"
      allowfullscreen>
    </iframe>
        </div>
      </section>

      <section class="game-info">
        <div class="info-card">
          <h3>📚 Aprendizado</h3>
          <p>Você aprenderá sobre parâmetros de qualidade de água e sustentabilidade.</p>
        </div>
        <div class="info-card">
          <h3>⏱️ Tempo</h3>
          <p>Tempo estimado: 15-20 minutos</p>
        </div>
        <div class="info-card">
          <h3>🎯 Dificuldade</h3>
          <p>Nível Difícil - Para usuários avançados</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
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
