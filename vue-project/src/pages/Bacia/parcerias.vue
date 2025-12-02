<template>
  <section>
    <div>
      <figure><img :src="ANA" alt="ANA Logotipo"></figure>
    </div>
    <div>
      <figure><img :src="IFRN" alt="IFRN Logotipo"></figure>
    </div>
    <div>
      <figure><img :src="GOVERNO" alt="GOVERNO Logotipo"></figure>
    </div>
    <div>
      <figure><img :src="IGARN" alt="IGARN Logotipo"></figure>
    </div>
    <div>
      <figure><img :src="NEPPSA" alt="NEPPSA Logotipo"></figure>
    </div>
  </section>
</template>


<script setup>
import ANA from '@/assets/images/Parcerias/ANA.svg'
import IFRN from '@/assets/images/Parcerias/IFRN.svg'
import IGARN from '@/assets/images/Parcerias/IGARN.svg'
import GOVERNO from '@/assets/images/Parcerias/GOVERNO.svg'
import NEPPSA from '@/assets/images/Parcerias/NEPPSA.svg'






</script>
<style scoped>


@keyframes pulseGlow {
  0%, 100% {
    box-shadow: 0 4px 12px rgba(0, 129, 199, 0.15);
  }
  50% {
    box-shadow: 0 8px 20px rgba(0, 129, 199, 0.3);
  }
}


section {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  max-width: 1200px;
  margin: 0 auto;
  gap: clamp(12px, 4vw, 30px);
  padding: clamp(20px, 5vw, 40px) 20px;
  place-items: center;
}

div {
  width: 100%;
  max-width: 340px;
  aspect-ratio: 3 / 1.4;
  min-height: 8rem;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 129, 199, 0.15);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  cursor: pointer;
}

/* Delay escalonado para cada card */
div:nth-child(1) { animation-delay: 0.1s; }
div:nth-child(2) { animation-delay: 0.2s; }
div:nth-child(3) { animation-delay: 0.3s; }
div:nth-child(4) { animation-delay: 0.25s; }
div:nth-child(5) { animation-delay: 0.35s; }

/* Hover: elevação + glow */
div:hover {
  transform: translateY(-12px) scale(1.05);
  box-shadow: 0 12px 28px rgba(0, 129, 199, 0.35);
  animation: none;
}

figure {
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  padding: 10px;
}

img {
  max-width: 90%;
  max-height: 90%;
  object-fit: contain;
  transition: filter 0.3s ease;
}

div:hover img {
  filter: brightness(1.1);
}

/* Responsividade */
@media (max-width: 900px) {
  section {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }
}

@media (max-width: 600px) {
  section {
    grid-template-columns: 1fr;
    padding: 20px 12px;
  }
  
  div:hover {
    transform: translateY(-8px) scale(1.02);
  }
}
</style>