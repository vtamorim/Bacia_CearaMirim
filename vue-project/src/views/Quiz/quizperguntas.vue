<template>
<div class="page-inner">

  <!-- QUIZ -->
  <div v-if="!finished" class="quizperguntas card">
    <h2>{{ Lista[index] }}</h2>
    <p>Questão {{ index + 1 }}/<span class="total">{{ Lista.length }}</span></p>

    <ul>
      <li v-for="(alt, i) in Alternativas[index]" :key="i">
        <button
          class="alternativas"
          :class="buttonClass(i)"
          :disabled="answered"
          @click="choose(i)"
        >
          {{ alt }}
        </button>
      </li>
    </ul>

    <div class="controls">
      <button id="proximo" @click="proximo" :disabled="!answered">
        Próximo
      </button>
    </div>
  </div>

  <!-- RESULTADO -->
  <div v-else class="quizperguntas card resultado-final" >
    <h2>Quiz finalizado 🎉</h2>
    <p>Você acertou <strong>{{ certas }}</strong> de {{ Lista.length }}</p>
    <button id="reiniciar" @click="reiniciar">Refazer quiz</button>
  </div>

</div>
</template>

<script setup>
import { ref, computed } from 'vue';

/* estado */
const certas = ref(0);
const index = ref(0);
const questoes = ref(6); // você pode sincronizar com Lista.length depois
const Lista = ref([
  'Em qual município nasce o rio Ceará-Mirim?',
  'Em qual município localiza-se a foz do rio Ceará-Mirim?',
  'Por quantos municípios o rio Ceará-Mirim passa ao longo do seu percurso?',
  'Em qual município o rio é represado?',
  'Cite pelo menos 3 usuários da bacia do rio Ceará-Mirim?',
  'Como é composto o comitê da bacia hidrográfica do rio Ceará-Mirim?'
]);

const Alternativas_certas = ref([
  'Lajes',
  'Extremoz',
  '14',
  'Poço Branco',
  'Abastecimento urbano, indústria e mineração, irrigação e uso agropecuário, aquicultura e pesca, turismo e lazer.',
  'Representações da sociedade civil, poder público e usuários de água'
]);

// Cada item deve ser um array com as alternativas da pergunta
const Alternativas = ref([
  ['Ceará-Mirim','Lajes','João Câmara','Poço Branco'], // pergunta 1
  ['Extremoz','Natal','Guamaré','Parazinho'], // exemplo substitua se quiser
  ['12','13','14','15'],
  ['Poço Branco','Lagoa Nova','Assu','São Gonçalo do Amarante'],
  ['Abastecimento urbano, indústria e mineração, irrigação e uso agropecuário, aquicultura e pesca, turismo e lazer.','Uso apenas doméstico e recreativo, sem fins produtivos','Somente navegação fluvial e transporte de cargas','Apenas geração de energia elétrica e transporte hidroviário'],
  ['Representações da sociedade civil, poder público e usuários de água','Somente representantes do governo estadual','Apenas organizações não governamentais ambientais','Somente representantes de empresas privadas e indústrias']
]);


const answered = ref(false);
const selectedIndex = ref(null); 
const finished = ref(false);

const currentCorrect = computed(() => Alternativas_certas.value[index.value]);

function choose(i) {
  if (answered.value) return;
  selectedIndex.value = i;
  answered.value = true;

  const selectedText = Alternativas.value[index.value][i]?.trim();
  const correctText = currentCorrect.value?.trim();

  if (selectedText === correctText) {
    certas.value++;
  }
}

function buttonClass(i) {
  if (!answered.value) return '';
  const text = Alternativas.value[index.value][i]?.trim();
  const correctText = currentCorrect.value?.trim();

  if (text === correctText) return 'certa';
  if (selectedIndex.value === i && text !== correctText) return 'errada';
  return 'desativada'; 
}

function proximo() {
  if (index.value >= Lista.value.length - 1) {
    finished.value = true;
    return;
  }
  index.value++;
  answered.value = false;
  selectedIndex.value = null;
}

function reiniciar() {
  index.value = 0;
  certas.value = 0;
  answered.value = false;
  selectedIndex.value = null;
  finished.value = false;
}
</script>

<style scoped>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* {
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

.page-inner {
  display: flex;
  justify-content: center;
  padding: 1rem;
}
#reiniciar{
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
/* CARD PRINCIPAL */
.quizperguntas {
  width: 100%;
  max-width: 640px;
  min-height: 26em;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: stretch;
  justify-content: center;
}

/* TÍTULOS */
h2 {
  text-align: left;
  margin: 0;
  font-size: 1.25rem;
}

.total {
  color: gray;
}

/* LISTA */
ul {
  display: flex;
  flex-direction: column;
  list-style: none;
  gap: 14px;
  padding: 0;
  margin: 0;
}

/* BOTÕES DE ALTERNATIVA */
.alternativas {
  width: 100%;
  min-height: 44px;
  padding: 12px 16px;
  text-align: left;
  background-color: #E9F9FC;
  border: 1px solid #014D83;
  border-radius: 8px;
  line-height: 1.4;
  white-space: normal;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.alternativas:not(:disabled):hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.06);
}

/* ESTADOS */
.alternativas.certa {
  background: rgba(86,192,43,0.22);
  border-color: #56C02B;
}

.alternativas.errada {
  background: rgba(255,0,0,0.14);
  border-color: #FF0000;
}

.alternativas.desativada {
  opacity: 0.85;
}

/* CONTROLES */
.controls {
  display: flex;
  justify-content: center;
}

#proximo {
  background-color: var(--bg-but);
  color: var(--txt-but);
  width: 100%;
  max-width: 260px;
  height: 44px;
  border-radius: 200px;
  border: none;
  font-size: 1em;
  font-weight: bold;
  transition: background-color 0.15s ease;
  box-shadow: 0px 3px 3px var(--color-boxs);
}

#proximo:hover {
  background-color: #0A142F;
}

#proximo[disabled] {
  opacity: 0.5;
  cursor: not-allowed;
}

/* RESULTADO FINAL */
.resultado {
  margin-top: 1rem;
  padding: 12px;
  border-radius: 8px;
  background: #f3f7fb;
  border: 1px solid #d6e5f3;
  text-align: center;
}


/* 📱 MOBILE */
@media (max-width: 480px) {
  h2 {
    font-size: 1.1rem;
  }

  .alternativas {
    font-size: 0.95rem;
  }
}


</style>