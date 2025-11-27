<template>
  <div class="carousel-container">
    <div class="carousel-wrapper">
      <img :src="mano[index].url" :alt="mano[index].name" class="carousel-image" />
      
      <!-- Botões de navegação -->
      <button class="carousel-btn prev" @click="prevSlide" aria-label="Slide anterior">
        ❮
      </button>
      <button class="carousel-btn next" @click="nextSlide" aria-label="Próximo slide">
        ❯
      </button>
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
  }, 5000)
}

onMounted(() => {
  startAutoPlay()
})

onUnmounted(() => {
  clearInterval(interval)
})
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

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

}

.carousel-wrapper {
  position: relative;
  width: 100%;
  overflow: hidden;
  border-radius: 16px;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
  height: 400px;
}

.carousel-image {
  width: 100%;
  height: 100%;
  display: block;
  animation: fadeIn 0.6s ease-in-out;
  object-fit: cover;
  object-position: center;
}

/* Botões de navegação */
.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 129, 199, 0.8);
  color: white;
  border: none;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  font-size: 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 10;
}

.carousel-btn:hover {
  background: rgba(0, 129, 199, 1);
  transform: translateY(-50%) scale(1.1);
  box-shadow: 0 6px 20px rgba(0, 129, 199, 0.4);
}

.carousel-btn.prev {
  left: 20px;
  animation: slideInLeft 0.5s ease-out;
}

.carousel-btn.next {
  right: 20px;
  animation: slideInRight 0.5s ease-out;
}

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

/* Responsividade */
@media (max-width: 768px) {
  .carousel-btn {
    width: 40px;
    height: 40px;
    font-size: 18px;
  }

  .carousel-btn.prev {
    left: 10px;
  }

  .carousel-btn.next {
    right: 10px;
  }
}

@media (max-width: 480px) {
  .carousel-container {
    padding: 20px 10px;
  }

  .carousel-btn {
    width: 36px;
    height: 36px;
    font-size: 16px;
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
</style>