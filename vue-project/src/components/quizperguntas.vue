<template>
    <div class="quizperguntas">
        <h2>{{ Lista[index] }}</h2>
        <p>Questão {{ index+1 }}/<span style="color: gray;">{{ questoes }}</span></p>
        <ul>
            <li v-for="(alt, i) in Alternativas[index]" :key="i">
                <button
                    type="button"
                    class="alternativas"
                    @click="mostrarresposta($event)"
                >
                    {{ alt }}
                </button>
            </li>
        </ul>
        <button type="button" id="proximo" @click="proximo">Próximo</button>
    </div>
</template>

<script setup>
import { ref } from 'vue';

let certas = ref(0);
let index = ref(0);
let questoes = ref(6);
const Lista = ref([
  'Em qual município nasce o rio Ceará-Mirim?',
  'Em qual município localiza-se a foz do rio Ceará-Mirim?',
  'Por quantos municípios o rio Ceará-Mirim passa ao longo do seu percurso?',
  'Em qual município o rio é represado?',
  'Cite pelo menos 3 usuários da bacia do rio Ceará-Mirim?',
  'Como é composto o comitê da bacia hidrográfica do rio Ceará-Mirim?'
]);

// alternativa certa por pergunta (texto igual ao da alternativa correta)
const Alternativas_certas = ref([
  'Lajes',
  'Extremos',
  '14',
  'Poço Branco',
  'Abastecimento urbano, indústria e mineração, irrigação e uso agropecuário, aquicultura e pesca, turismo e lazer.',
  'Representações da sociedade civil, poder público e usuários de água'
]);

// IMPORTANT: cada item aqui deve ser um array com as 4 (ou N) alternativas daquela pergunta.
// No seu exemplo original só tinha as alternativas da primeira pergunta — complete os outros arrays.
const Alternativas = ref([
  ['Ceará-Mirim','Lajes','João Câmara','Poço Branco','Pedro Avelino'], // pergunta 1
  ['Extremos','Outra','Outra2','Outra3'], // pergunta 2 (exemplo; substitua)
  ['12','13','14','15'], // pergunta 3
  ['Poço Branco','Outra','Outra2','Outra3'], // pergunta 4
  ['Abastecimento urbano, indústria e mineração, irrigação e uso agropecuário, aquicultura e pesca, turismo e lazer.','Opção B','Opção C','Opção D'], // pergunta 5
  ['Representações da sociedade civil, poder público e usuários de água','Opção B','Opção C','Opção D'] // pergunta 6
]);

const answered = ref(false);

function mostrarresposta(event) {
    // evita múltiplos cliques na mesma pergunta
    if (answered.value) return;

    // preferir currentTarget (botão) para garantir que pegamos o elemento correto
    const btn = event.currentTarget;
    const correct = Alternativas_certas.value[index.value];

    // pega todos os botões daquela lista (pergunta atual)
    const ul = btn.closest('ul');
    const buttons = ul.querySelectorAll('button.alternativas');

    // pinta todos: a correta de verde, as demais ficam normais (ou serão marcadas vermelhas se forem o clique errado)
    buttons.forEach(b => {
        // desabilita para não aceitar mais cliques
        b.disabled = true;

        if (b.innerText.trim() === correct.trim()) {
            b.style.background = 'rgba(86,192,43,0.22)'; // verde para a certa
            b.style.borderColor = '#56C02B';
        }
    });

    // se a resposta clicada for a correta, soma; se não, pinta ela de vermelho
    if (btn.innerText.trim() === correct.trim()) {
        certas.value++;
        // já pintamos a correta acima; opcionalmente adicionar algum efeito
    } else {
        btn.style.background = 'rgba(255,0,0,0.22)'; // vermelho para a errada clicada
        btn.style.borderColor = '#FF0000';
    }

    answered.value = true;
}

function proximo() {
    // avança apenas se houver próxima pergunta
    if (index.value < Lista.value.length - 1) {
        index.value++;
        answered.value = false;
        
    } else {
        alert(`Quiz finalizado! Acertos: ${certas.value}`);
    
    }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

*{
    font-family: 'Poppins',sans-serif;
}


    h2{
        text-align: left;
    }
    .quizperguntas{
        margin: 0 auto;
        width: 40em;
        height: 30em;
        align-self: center;
        justify-self: center;
    }
    ul{
        display: flex;
        flex-direction: column;
        list-style-type: none;
        gap: 14px;
    }
    .alternativas{
        width: 544px;
        height: 40px;
        text-align: left;
        padding-left: 15px;
        background-color: #E9F9FC;
        border: 1px solid #014D83;
        border-radius: 8px;
    }
    #proximo{
                background-color: var(--bg-but) ;
        color: var(--txt-but);
        width: 240px;
        height: 44px;
        border-radius: 200px;
        border: none;
        font-size: 0.8em;
        font-weight: bold;
        transition: background-color 0.1s ease-in;
        box-shadow: 0px 3px 3px var(--color-boxs);
    &:hover{
        background-color: #0A142F;
    }}</style>