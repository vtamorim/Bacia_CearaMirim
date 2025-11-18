<script setup>
    
    import { ref } from 'vue';
    import quizstart from '@/components/quizstart.vue';
    import quizperguntas from '@/components/quizperguntas.vue';


    const teladisplay = ref('apresentar')
</script>
<template>

    <quizstart v-if="teladisplay === 'apresentar'" @trocarTela="teladisplay = 'perguntas'"/>
    <quizperguntas v-if="teladisplay === 'perguntas'"/>

</template>
<style scoped></style>