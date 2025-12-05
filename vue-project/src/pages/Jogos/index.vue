<template>
  <section class="games-page">
    <!-- CARROSSEL -->
    <div class="carousel">
      <div 
        class="carousel-track" 
        :style="{ transform: `translateX(-${currentIndex * 100}%)` }"
      >
        <div 
          class="carousel-item"
          v-for="index in slideCount"
          :key="index"
        >
          <div 
        class="slide-placeholder"
        :style="{ backgroundColor: colors[index] }"
      ></div>
        </div>
      </div>

      <button class="nav prev" @click="prev">‹</button>
      <button class="nav next" @click="next">›</button>
    </div>

  </section>
</template>

<script setup>
import { ref } from "vue";

const slideCount = 3;

const colors = [
  "#cfcfcf",  // slide 1
  "#ff9999",  // slide 2
  "#99ccff"   // slide 3
];

const currentIndex = ref(0);

function next() {
  currentIndex.value = (currentIndex.value + 1) % slideCount;
}

function prev() {
  currentIndex.value = (currentIndex.value - 1 + slideCount) % slideCount;
}
</script>
<style scoped>
.games-page {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  padding: 2rem 0;
}

.carousel {
  position: relative;
  width: 100%;
  height: 600px;
  overflow: hidden;
  border-radius: 12px;
  background: #fff;
}

.carousel-track {
  display: flex;
  transition: transform 0.5s ease;
  width: 100%;
  height: 100%;
}

.carousel-item {
  min-width: 100%;
  height: 100%;
}

.slide-placeholder {
  width: 100%;
  height: 100%;
  background: #cf0000; /* CINZA VISÍVEL */
  border-radius: 12px;
}


.nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.4);
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 24px;
  z-index: 10;
}

.nav.prev {
  left: 10px;
}

.nav.next {
  right: 10px;
}

.title {
  font-size: 26px;
  font-weight: 700;
  margin-top: 10px;
}
</style>
