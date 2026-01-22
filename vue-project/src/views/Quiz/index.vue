<script setup>
import { ref } from 'vue'

import QuizStart from '@/views/Quiz/quizstart.vue'
import QuizPerguntas from '@/views/Quiz/quizperguntas.vue'

const teladisplay = ref('apresentar')
</script>

<template>
  <QuizStart 
    v-if="teladisplay === 'apresentar'" 
    @trocarTela="teladisplay = 'perguntas'"
  />

  <QuizPerguntas 
    v-if="teladisplay === 'perguntas'"
  />
</template>

<style scoped></style>
