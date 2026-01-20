<template>
    <section id="apresentar_comite">
        <figure><img v-bind:src="img1" alt="Foto do Comitê"></figure>
        <p> {{ apresentacao_comite }}</p>
    </section>
       <div class="subsection-title-wrapper">
        <h2>Objetivos</h2>
    </div>
    <section id="objetivos_comite">
        
        <div v-for="(num, index) in 3"
      :key="num"
      class="objectives">
        <img v-bind:src="imagens[index]" alt="">
        <h3>{{ content[index].titulo }}</h3>
         <p>{{ content[index].p }}</p>
        </div>
    </section>

    <div class="subsection-title-wrapper">
        <h2>Gestão Atual</h2>
    </div>
    <section class="gestao-atual">
        <div>
            <figure>
                <img :src="ceres" alt="">
            </figure>
            <div id="ceres_desc">
                <h3>Ceres Dantas</h3>
                <p>Presidente</p>
            </div>
        </div>

    </section>

    <div class="subsection-title-wrapper">
        <h2>Gestões Anteriores</h2>
    </div>
    <section class="gestoes_ant">
        <div v-for="(num,index) in 3" style="">
            <figure>
                <img :src="imagens_pessoas[index]" alt="">
            </figure>
            <div>
                <div id="pessoas_desc">
                    <h3>{{ nome_pessoas[index] }}</h3>
            </div>
            </div>
        </div>
    </section>

    
</template>
<script setup>
    import img1 from '@/assets/images/Comite/Screenshot 2026-01-19 at 15-29-41 BLOG CBH DO RIO CEARÁ-MIRIM.png'
    import objetivo1 from '@/assets/images/Comite/Group 60.svg'
    import objetivo2 from '@/assets/images/Comite/Group 61.svg'
    import objetivo3 from '@/assets/images/Comite/Group 62.svg'

    import wagna from '@/assets/images/Comite/Foto Wagna 1.png'
    import maria from '@/assets/images/Comite/WhatsApp Image 2025-11-18 at 13.35.26 1.png'
    import fabio from '@/assets/images/Comite/WhatsApp Image 2025-11-18 at 13.12.22 1.png'

    import ceres from '@/assets/images/Comite/Group 55.png'

    const content = [ {"titulo":"Gestão","p":"Promover a gestão integrada dos recursos hídricos no território da bacia, assegurando a participação de múltiplos atores sociais no processo decisório;"},
    {"titulo":"Mediação","p":"Elaborar e aprovar o plano de bacia, mediar conflitos entre usuários, e definir os critérios para a cobrança pelo uso da água;"},
    {"titulo":"Acompanhamento","p":"Acompanhar a implementação das políticas públicas no âmbito da bacia hidrográfica;"}      
    ]
    const imagens_pessoas = [wagna,maria,fabio]
    const imagens = [objetivo1,objetivo2,objetivo3]
    const apresentacao_comite = "O Comitê da Bacia Hidrográfica do Rio Ceará-Mirim (CBH-CM) foi criado em 2010 por decreto estadual, integrando o Sistema de Gestão dos Recursos Hídricos do Rio Grande do Norte. Ele atua como órgão colegiado de apoio à Política Estadual de Recursos Hídricos e é formado por representantes da sociedade civil, do poder público e dos usuários de água. O comitê possui 40 vagas, sendo 20 titulares e 20 suplentes, distribuídas conforme as necessidades da bacia."

    const nome_pessoas = ["Maria Wagna","Maria Lucimar","Fábio Góis"]


</script>
<style scoped>

.subsection-title-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 0;
}

.subsection-title-wrapper h2 {
  width: 100%;
  max-width: 1400px;
  box-sizing: border-box;
}

h2 {
      font-size: clamp(1rem, 2vw, 1.5rem);
      color: #0081C7;
      text-align: left;
      font-weight: 700;
      margin: 0 0 1rem 0;
      max-width: 1400px;
      width: 100%;
      padding: 0 clamp(0.5rem, 3vw, 2.5rem);
      box-sizing: border-box;
      position: relative;
      

  &::after {
    content: '';
    position: absolute;
    bottom: -0.8rem;
    left: clamp(0.5rem, 3vw, 2.5rem);
    width: 120px;
    height: 20px;
    background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 120 20" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs><linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:%230081C7;stop-opacity:1" /><stop offset="100%" style="stop-color:%232196F3;stop-opacity:1" /></linearGradient></defs><path d="M0,10 Q30,0 60,10 T120,10" stroke="url(%23waveGrad)" stroke-width="3" fill="none" stroke-linecap="round"/></svg>') no-repeat center;
    background-size: contain;
  }
}

section {
  padding: clamp(1rem, 3vw, 2rem);
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  box-sizing: border-box;
}

#apresentar_comite {
  display: flex;
  gap: clamp(1.5rem, 2vw, 3rem);
  position: relative;
  justify-content: center;
  align-items: flex-start;
  flex-wrap: wrap;
  margin-bottom: clamp(2rem, 4vw, 3rem);
}

#apresentar_comite figure {
  flex: 1;
  min-width: 250px;
  max-width: 400px;
  margin: 0;
  padding: 0;
}

#apresentar_comite img {
  width: 100%;
  height: 15rem;
  display: block;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

#apresentar_comite > p {
  text-align: justify;
  flex: 1;
  min-width: 250px;
  font-size: clamp(0.9rem, 2vw, 1rem);
  color: #034E77;
  line-height: 1.6;
  margin: 0;
  max-width:550px;
}

#objetivos_comite {
  display: grid;
  position:relative;
  z-index:1;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: clamp(1.5rem, 3vw, 2.5rem);
  padding: clamp(2rem, 4vw, 3rem);
  justify-items: center;
  align-items: center;
  width: 100%;
  height:50rem;
  max-width: 1400px;
  min-height: auto;
}

#objetivos_comite> div:nth-child(1){
  justify-self: flex-start;
}
#objetivos_comite> div:nth-child(2){
  justify-self: center;
}
#objetivos_comite> div:nth-child(3){
  justify-self: flex-end;
}
#objetivos_comite::before{
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100vw;
  background-image: url('@/assets/images/Comite/Vector 69.png');
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  z-index: -1;
  left: 50%;
  transform: translateX(-50%);
  pointer-events: none;
}
.objectives {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  max-width: 280px;
}

.objectives img {
  width: clamp(60px, 10vw, 100px);
  height: auto;
  margin-bottom: 1rem;
  display: block;
}

.objectives h3 {
  font-size: clamp(1.3rem, 3.5vw, 1.5rem);
  color: #034E77;
  margin: 0.5rem 0;
  font-weight: 700;
  line-height: 1.2;
}

.objectives p {
  font-size: clamp(0.9rem, 2vw, 1rem);
  color: #034E77;
  line-height: 1.5;
  margin: 0;
  text-align: center;
}

/* GESTÃO ATUAL */
section > div {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: clamp(1rem, 2vw, 1.5rem);
}

section figure {
  width: 100%;
  max-width: 300px;
  margin: 0;
  padding: 0;
}

section figure img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 8px;
}

#ceres_desc {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  width: 100%;
  max-width: 265px;
  background-color: white;
  box-shadow: 0px 3px 3px 0px rgba(0, 129, 199, 0.15);
  margin-top: -50px;
  z-index: 1;
  padding: clamp(1rem, 2vw, 1.5rem);
  min-height: auto;
}

#ceres_desc h3 {
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: #034E77;
  margin: 0.5rem 0;
  font-weight: 700;
}

#ceres_desc p {
  font-size: clamp(0.85rem, 1.6vw, 0.95rem);
  color: #0081C7;
  margin: 0;
}

/* GESTÕES ANTERIORES */
.gestoes_ant {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(180px, 100%), 1fr));
  gap: clamp(1rem, 3vw, 2rem);
  justify-items: center;
  margin: 0 auto;
  max-width: 1440px;
  padding: 0 clamp(0.5rem, 2vw, 1rem);
}

.gestoes_ant > div {
  width: 100%;
  max-width: 220px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.gestoes_ant figure {
  width: 100%;
  max-width: 200px;
  margin: 0;
  padding: 0;
}

.gestoes_ant figure img {
  width: 100%;
  aspect-ratio: 3 / 4;
  object-fit: cover;
  border-radius: 10px;
}

#pessoas_desc {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  width: 100%;
  max-width: 200px;
  background-color: white;
  box-shadow: 0px 3px 3px 0px rgba(0, 129, 199, 0.15);
  margin-top: -50px;
  z-index: 1;
  padding: clamp(0.75rem, 1.5vw, 1rem);
  min-height: auto;
}

#pessoas_desc h3 {
  font-size: clamp(0.95rem, 1.8vw, 1.1rem);
  color: #034E77;
  margin: 0;
  font-weight: 700;
  text-align: center;
}
.gestao-atual > div {
  display: flex;
  flex-direction: column;
  align-items: center;
}
/* RESPONSIVIDADE */
@media (max-width: 937px) {
    .objectives {
  max-width: none;
}


#objetivos_comite::before{

  background-image: none;
  background-color: rgba(0, 129, 199,0.15);
  background-position: center;
  background-repeat: no-repeat;}
}
/* Tablet (900px and down) */
@media (max-width: 900px) {



  #apresentar_comite {
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    height: auto;
  }

  #apresentar_comite figure {
    max-width: 70%;
    width: 70%;
    height: 20rem;
  }
  #apresentar_comite img{
        height: 18rem;
  }

  #apresentar_comite > p {
    width: 100%;
  }

  #objetivos_comite {
    gap: 1.5rem;
    padding: 2rem;
    height: 50rem;
  }

  .gestoes_ant {
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1.5rem;
  }
}
@media (max-width:700px) {
  #apresentar_comite img{
    height:15rem;
    width: 100%;
  }
  #apresentar_comite figure{
    width: 100%;
  }
  h2{
    font-size: 1.1rem;
  }
}
/* Mobile (600px and down) */
@media (max-width: 600px) {
  h2 {
    font-size: 1.1rem;
    margin: 1.25rem 0 1rem;
  }

  section {
    padding: clamp(0.75rem, 2vw, 1rem);
  }

  #apresentar_comite {
    gap: 1rem;
    margin-top: 1.5rem;
  }

  #apresentar_comite figure {
    max-width: 100%;
  }
  #apresentar_comite img{
    height: 100%;
  }

  #apresentar_comite > p {
    font-size: 0.9rem;
  }

  #objetivos_comite {
    gap: 1rem;
    padding: 1.5rem 0.75rem;
    grid-template-columns: 1fr;
  }

  .objectives {
    max-width: 100%;
  }

  .objectives img {
    width: clamp(50px, 8vw, 80px);
  }

  .objectives h3 {
    font-size: 1.1rem;
  }

  .objectives p {
    font-size: 0.85rem;
  }

  #ceres_desc {
    max-width: 50%;
    margin-top: -40px;
    padding: 0.75rem;
  }

  #ceres_desc h3 {
    font-size: 1rem;
  }

  #ceres_desc p {
    font-size: 0.85rem;
  }

  .gestoes_ant {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1.2rem;
    padding: 0 0.5rem;
  }

  .gestoes_ant figure {
    max-width: 100%;
  }

  #pessoas_desc {
    max-width: 100%;
    margin-top: -40px;
    padding: 0.6rem;
  }

  #pessoas_desc h3 {
    font-size: 0.95rem;
  }
}

/* Extra Small (480px and down) */
@media (max-width: 480px) {
  h2 {
    font-size: 1.1rem;
    margin: 1rem 0 0.75rem;
    position: relative;
    left: 0;
  }

  section {
    padding: 0.5rem;
  }

  #apresentar_comite {
    gap: 0.75rem;
    margin-bottom: 1.25rem;
    position: relative;
  }

  #apresentar_comite > p {
    text-align: center;
    font-size: 0.85rem;
  }

  #objetivos_comite {
    gap: 0.75rem;
    padding: 1rem 0.5rem;
        background-color: transparent;
    background-image: none;
  }

  .objectives img {
    width: 50px;
  }

  .objectives h3 {
    font-size: 1rem;
  }

  .objectives p {
    font-size: 0.8rem;
  }
  p{
    font-size: 0.1rem;
    text-align: center;
  }

  .gestoes_ant {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 0;
  }

  #ceres_desc,
  #pessoas_desc {
    margin-top: -35px;
    padding: 0.5rem;
  }

  #ceres_desc h3,
  #pessoas_desc h3 {
    font-size: 0.9rem;
  }

  #ceres_desc p {
    font-size: 0.8rem;
  }
  .gestoes_ant > div {
    max-width: 180px;
    width: 80%;
  }
  #ceres_desc {
    max-width: 225px;
    width: 100%;
  }

}

/* Landscape */
@media (max-height: 600px) {
  section {
    padding: clamp(0.5rem, 1.5vw, 1rem);
  }

  h2 {
    margin: 0.75rem 0 0.5rem;
  }
}
</style>