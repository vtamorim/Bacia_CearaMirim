<template>
  <img :src="mano[index].url" alt="img" />

  <ol>

  </ol>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Importa as imagens OU usa URL import.meta.url
import img1 from '@/assets/images/Carrosel/image.-fotor-enhance-20251106124220 1.svg'
import img2 from '@/assets/images/Carrosel/Screenshot 2025-11-06 at 12-37-29 (386) Comitê da Bacia Hidrográfica Rio Ceará Mirim Documentário 2024 - YouTube.-fotor-enhance-20251106124013 1.svg'
import img3 from '@/assets/images/Carrosel/Screenshot 2025-11-06 at 12-43-43 (386) Comitê da Bacia Hidrográfica Rio Ceará Mirim Documentário 2024 - YouTube 1.svg'
// ... continue

// Array das imagens
const mano = [
  { name: "img1", url: img1 },
  { name: "img2", url: img2 },
  { name: "img3", url: img3 }
]

const index = ref(0)
let interval = null

onMounted(() => {
  interval = setInterval(() => {
    index.value = (index.value + 1) % mano.length
  }, 5000) // 5 segundos
})

onUnmounted(() => {
  clearInterval(interval)
})
</script>
