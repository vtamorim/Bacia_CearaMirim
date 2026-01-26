<template>
    <div class="bacia-container">
          
          <que />

          <div class="section-title-wrapper">
            <h2 class="section-title">Apresentação</h2>
          </div>
          <apresentacao />
          
       
          <div class="section-title-wrapper">
            <h2 class="section-title">Parcerias</h2>
          </div>
          <Parcerias />
        </div>
</template>
<script setup>
    import apresentacao from './apresentacao.vue';
    import Parcerias from './parcerias.vue';
    import mapa from './mapa.vue';
    import que from './que.vue';
</script>
