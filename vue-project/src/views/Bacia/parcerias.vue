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
  max-width: 1400px;
  margin: 0 auto;

  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-areas:
    "a a b b c c"
    ". d d e e .";

  gap: 32px;
  position: relative;
  left:-30px;
  padding: 40px 24px;
  place-items: center;
}
section > div:nth-child(1) { grid-area: a; }
section > div:nth-child(2) { grid-area: b; }
section > div:nth-child(3) { grid-area: c; }
section > div:nth-child(4) { grid-area: d; }
section > div:nth-child(5) { grid-area: e; }

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
}

div {
  height: 140px;
  max-width: 340px;
  width: 100%;
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
  height: 70%;
  width: auto;
  max-width: 80%;
  object-fit: contain;
}
img[alt*="GOVERNO"] { height: 100%; }
img[alt*="NEPPSA"]  { height: 100%; }
img[alt*="IGARN"]   { height: 100%; }
div:hover img {
  filter: brightness(1.1);
}
@media (max-width:1400px) {
  section{
    right: 0;
  }
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
@media (max-width : 480px){
  section{
    position: relative;
    left: 0%;
  }
    div{
      width: 90%;
        min-height: 6rem;
    }

}

@media (max-width: 900px) {
  section {
    grid-template-columns: repeat(2, 1fr);
    grid-template-areas:
      "a b"
      "c d"
      "e e";
  }
}

@media (max-width: 600px) {
  section {
    grid-template-columns: 1fr;
    grid-template-areas:
      "a"
      "b"
      "c"
      "d"
      "e";
  }
}
</style>