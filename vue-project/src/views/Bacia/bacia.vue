<template>
    <div class="bacia-container">
          
          <mapa />


          <apresentacao />
          
       
          <Parcerias />
        </div>
</template>
<script setup>
    import apresentacao from './apresentacao.vue';
    import Parcerias from './parcerias.vue';
    import mapa from './mapa.vue';
</script>
<style scoped>
    .bacia-container{
        display: flex;
        gap: 5em;
    }
</style>