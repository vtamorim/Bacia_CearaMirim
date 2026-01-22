<template>
    <div class="page-inner">
        <main class="quizstart card">
            <h2>Quiz</h2>
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

@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

*{
    font-family: 'Poppins',sans-serif;
}
main{
    position: relative;
    top: 10vh;
    width: 50vw;
    left: 5vw;
}
h2{
    font-size: 2em;
}
button{
        background-color: var(--bg-but) ;
        color: var(--txt-but);
        width: 240px;
        height: 44px;
        border-radius: 200px;
        border: none;
        font-size: 1em;
        font-weight: bold;
        transition: background-color 0.1s ease-in;
        box-shadow: 0px 3px 3px var(--color-boxs);
    &:hover{
        background-color: #0A142F;
    }
    
    }
p{
    width: 50vw;
}
</style>