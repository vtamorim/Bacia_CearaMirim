<template>
  <div class="carousel-container">
    <div class="carousel-wrapper">

      <img :src="mano[index].url" :alt="mano[index].name" class="carousel-image"  />
      <!-- Overlay title sobre a imagem -->
      <div class="carousel-overlay">
        <h2 class="carousel-title">Bacia Hidrográfica Rio Ceará-mirim</h2>
      </div>
      <!-- Navegação por setas removida (auto-play + dots permanecem) -->
    </div>

    <!-- Indicadores (dots) -->
    <ol class="carousel-dots">
      <li
        v-for="(_, i) in mano"
        :key="i"
        :class="{ active: i === index }"
        @click="goToSlide(i)"
        class="dot"
      ></li>
    </ol>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Importa as imagens OU usa URL import.meta.url
import img1 from '@/assets/images/Carrosel/image.-fotor-enhance-20251106124220 1.svg'
import img2 from '@/assets/images/Carrosel/Screenshot 2025-11-06 at 12-37-29 (386) Comitê da Bacia Hidrográfica Rio Ceará Mirim Documentário 2024 - YouTube.-fotor-enhance-20251106124013 1.svg'
import img3 from '@/assets/images/Carrosel/Screenshot 2025-11-06 at 12-43-43 (386) Comitê da Bacia Hidrográfica Rio Ceará Mirim Documentário 2024 - YouTube 1.svg'
import img4 from '@/assets/images/Carrosel/Screenshot 2025-11-06 at 12-59-03 (386) Comitê da Bacia Hidrográfica Rio Ceará Mirim Documentário 2024 - YouTube.-fotor-enhance-20251106125945 1.svg'
import img5 from '@/assets/images/Carrosel/Screenshot 2025-11-06 at 13-01-08 (386) Comitê da Bacia Hidrográfica Rio Ceará Mirim Documentário 2024 - YouTube.-fotor-enhance-2025110613135 1.svg'
import img6 from '@/assets/images/Carrosel/Screenshot 2025-11-06 at 13-02-50 (386) Comitê da Bacia Hidrográfica Rio Ceará Mirim Documentário 2024 - YouTube 1.svg'
import img7 from '@/assets/images/Carrosel/Screenshot 2025-11-06 at 13-04-05 (386) Comitê da Bacia Hidrográfica Rio Ceará Mirim Documentário 2024 - YouTube.-fotor-enhance-2025110613432 1.svg'
import img8 from '@/assets/images/Carrosel/Screenshot 2025-11-06 at 13-07-50 (386) Comitê da Bacia Hidrográfica Rio Ceará Mirim Documentário 2024 - YouTube 1.svg'
// Array das imagens
const mano = [
  { name: "img1", url: img1 },
  { name: "img2", url: img2 },
  { name: "img3", url: img3 },
  { name: "img4", url: img4 },
  { name: "img5", url: img5 },
  { name: "img6", url: img6 },
  { name: "img7", url: img7 },
  { name: "img8", url: img8 }
]

const index = ref(0)
let interval = null

const nextSlide = () => {
  index.value = (index.value + 1) % mano.length
  resetInterval()
}

const prevSlide = () => {
  index.value = (index.value - 1 + mano.length) % mano.length
  resetInterval()
}

const goToSlide = (i) => {
  index.value = i
  resetInterval()
}

const resetInterval = () => {
  clearInterval(interval)
  startAutoPlay()
}

const startAutoPlay = () => {
  interval = setInterval(() => {
    index.value = (index.value + 1) % mano.length
  }, 2500)
}

onMounted(() => {
  startAutoPlay()
})

onUnmounted(() => {
  clearInterval(interval)
})
</script>

<style scoped>
  
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');


*{
  font-family: 'Poppins',sans-serif;
}
  @keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* slideIn keyframes removed (no arrow buttons) */

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.15);
  }
}

.carousel-container {
  width: 100%;
  margin: 0 auto;
  position: relative;

}

.carousel-wrapper {
  position: relative;
  width: 100%;
  overflow: hidden;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
  height: clamp(220px, 35vh, 520px);
}

.carousel-image {
  width: 100%;
  height: 100%;

  display: block;
  animation: fadeIn 0.6s ease-in-out;
  object-fit: cover;
  object-position: center;

}

/* Overlay com título sobre a imagem */
.carousel-overlay {
  position: absolute;
  inset: 0; /* ocupa toda a área do wrapper */
  display: flex;
  align-items: center;
  padding-left: clamp(3.5rem, 6vw, 5rem);
  justify-content: flex-start; /* alinhar à esquerda como na referência */
  pointer-events: none; /* não bloqueia interações */
}

.carousel-title {
  color: #ffffff;
  font-size: clamp(1.1rem, 3.6vw, 2.6rem);
  margin: 0;
  text-shadow: 0 6px 18px rgba(0,0,0,0.55);
  max-width: 70%;
  position: relative;
  line-height: 1.1;
  pointer-events: none;
  transform: translateY(8px);
  opacity: 0;
  animation: titleIn 0.8s ease-out 0.2s forwards;
  padding-right: 0%;
}

/* Camada preta semitransparente sobre a imagem (entre img e texto) */
.carousel-overlay::before{
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.45); /* ajuste o último valor (0.45) para controlar a opacidade */
  z-index: 1;
}

.carousel-title{ z-index: 2; }

@keyframes titleIn {
  to { transform: translateY(0); opacity: 1; }
}

/* Arrow buttons removed */

/* Indicadores (dots) */
.carousel-dots {
  list-style: none;
  padding: 0;
  margin: 20px 0 0;
  display: flex;
  justify-content: center;
  gap: 12px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #d1d5db;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.dot:hover {
  background: #9ca3af;
  transform: scale(1.2);
}

.dot.active {
  background: #0081c7;
  animation: pulse 0.6s ease-in-out;
  width: 32px;
  border-radius: 6px;
}


@media (max-width: 480px) {
  .carousel-container {
    padding: 20px 10px;
  }
  .carousel-dots {
    gap: 8px;
  }

  .dot {
    width: 8px;
    height: 8px;
  }

  .dot.active {
    width: 24px;
  }
}

@media (max-width: 900px) {
  .carousel-wrapper{
    height: clamp(220px, 30vh, 360px);
  }

  .carousel-title{
    font-size: clamp(1rem, 3.2vw, 2rem);
    max-width: 80%;
    padding-right: 10%;
  }
}

@media (max-width: 600px) {
  .carousel-wrapper{
    height: clamp(180px, 28vh, 300px);
  }

  .carousel-overlay{
    padding-left: 4%;
    justify-content: center;
  }

  .carousel-title{
    font-size: clamp(0.95rem, 3.5vw, 1.25rem);
    text-align: center;
    max-width: 95%;
  }
}
</style>