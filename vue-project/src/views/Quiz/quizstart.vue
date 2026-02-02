<template>
    <div class="page-inner">
        <main class="quizstart card">
            <p>{{ apresentacao }}</p>
            <button type="button" @click="trocarTela" class="cta">Começar</button>
        </main>
    </div>
</template>
<script setup>
import { ref } from 'vue'


const emit = defineEmits(['trocarTela'])

const apresentacao = ref(
  'Bem-vindo ao Quiz sobre a Bacia Hidrográfica do Rio Ceará-Mirim. Este questionário tem como objetivo avaliar seus conhecimentos sobre aspectos geográficos, ambientais e sociais relacionados à bacia. Leia atentamente e boa realização.'
)


function trocarTela() {
  emit('trocarTela')
}
</script>
<style>
    body{
 background-color: var(--bg-body);      
    }
</style>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* {
  font-family: 'Poppins', sans-serif;
  box-sizing: border-box;
}

.page-inner {
  display: flex;
  justify-content: center;
  padding: 1.5rem;
}

main {
  width: 100%;
  max-width: 600px;
  margin-top: 10vh;
  padding: 2rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: center;
  justify-content: center;
}

p {
  width: 100%;
  text-align: center;
  font-size: 1rem;
  line-height: 1.6;
}

button {
  background-color: var(--bg-but);
  color: var(--txt-but);
  width: 100%;
  max-width: 260px;
  height: 44px;
  border-radius: 200px;
  border: none;
  font-size: 1em;
  font-weight: bold;
  transition: background-color 0.15s ease-in;
  box-shadow: 0px 3px 3px var(--color-boxs);
}

button:hover {
  background-color: #0A142F;
}
@media (max-width: 768px) {
  main {
    margin-top: 5vh;
    padding: 1.5rem 1rem;
  }

  p {
    font-size: 0.95rem;
  }
}


</style>