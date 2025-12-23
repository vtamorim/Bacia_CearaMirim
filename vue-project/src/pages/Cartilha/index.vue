<template>
    <section id="origem_instrumento">
        <div>
            <div>
                <h2>Origem dessa Cartilha Interativa</h2>
                <hr>
                <p>A elaboração da cartilha interativa sobre a bacia hidrográfica do rio Ceará-Mirim surgiu da necessidade de difundir informações bem como fortalecer o conhecimento da população local sobre a importância da gestão integrada dos recursos hídricos, promovendo maior conscientização e engajamento comunitário na preservação do rio e de seus afluentes.</p>
            </div>
            <figure>
                <img v-bind:src="fru1" alt="">
            </figure>
        </div>
        <div>  
            <div>
                <h2>Instrumento de Apoio à Educação e à Gestão Ambiental</h2>
                <hr>
                <p>A elaboração da cartilha interativa sobre a bacia hidrográfica do rio Ceará-Mirim surgiu da necessidade de difundir informações bem como fortalecer o conhecimento da população local sobre a importância da gestão integrada dos recursos hídricos, promovendo maior conscientização e engajamento comunitário na preservação do rio e de seus afluentes.</p>
            </div>
                <figure>
                    <img v-bind:src="fru2" alt="">
                </figure>
        </div>
    </section>

  <section id="section_publicoalvo">
    <h2>Público-Alvo</h2>

    <div class="publico-line">
        <div class="line-center"></div>
    </div>

    <ul class="publico-list">

        <li class="publico-item">
            <span class="marker"></span>
            <div class="box" style="--bg: #BAEFFF;">
                <img v-bind:src="Teacher" alt="">
                <span class="label">Professores</span>
            </div>
        </li>

        <li class="publico-item">
            <span class="marker"></span>
            <div class="box" style="--bg:#45ABE2">
               <img v-bind:src="Student" alt="">
                <span class="label">Estudantes</span>
            </div>
        </li>

        <li class="publico-item">
            <span class="marker"></span>
            <div class="box" style="--bg: #068BD3;">
               <img v-bind:src="Manager" alt="">
                <span class="label">Gestores Públicos</span>
            </div>
        </li>

        <li class="publico-item">
            <span class="marker"></span>
            <div class="box" style="--bg: #0182C9">
                <img v-bind:src="Member" alt="">
                <span class="label">Integrantes dos Comitês</span>
            </div>
        </li>

        <li class="publico-item">
            <span class="marker"></span>
            <div class="box" style="--bg: #0477B5;">
                <img v-bind:src="Farmer" alt="">
                <span class="label">Agricultores</span>
            </div>
        </li>

        <li class="publico-item">
            <span class="marker"></span>
            <div class="box" style="--bg: #036498">
                <img v-bind:src="Enviroment" alt="">
                <span class="label">Técnicos Ambientais</span>
            </div>
        </li>

        <li class="publico-item">
            <span class="marker"></span>
            <div class="box" style="--bg:#034E77;">
                <img v-bind:src="People" alt="">
                <span class="label">Comunidade em Geral</span>
            </div>
        </li>

    </ul>
</section>


<section id="section_objetivo">
    <h3>Objetivo da Cartilha</h3>
    <hr>
    <p>O objetivo é atingir tanto o público escolar quanto a população local, promovendo conhecimento, engajamento e ações práticas voltadas à preservação e gestão sustentável da bacia hidrográfica.</p>
</section>


</template>
<script setup>
    import Student from '@/assets/images/Cartilha/Student Male.svg';
    import Teacher from '@/assets/images/Cartilha/Teacher.svg';
    import Manager from '@/assets/images/Cartilha/Manager.svg';
    import Member from '@/assets/images/Cartilha/Member.svg';
    import Farmer from '@/assets/images/Cartilha/Farmer.svg';
    import Enviroment from '@/assets/images/Cartilha/Environmental Planning.svg';
    import People from '@/assets/images/Cartilha/People Working Together.svg';

    import fru1 from '@/assets/images/Cartilha/fru 1.png';
    import fru2 from '@/assets/images/Cartilha/fru 2.png';

</script>

<style scoped>
/* SEÇÃO PÚBLICO-ALVO — IGUAL AO MODELO DA IMAGEM */

section {
  padding: clamp(1rem, 3vw, 2rem);
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  box-sizing: border-box;
}

#section_publicoalvo {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: auto;
  margin-top: clamp(2rem, 4vw, 4rem);
}

#origem_instrumento {
  position: relative;
  z-index: 1;
  display: flex;
  flex-wrap: wrap;
  min-height: auto;
  justify-content: center;
  gap: clamp(1.5rem, 4vw, 2rem);

  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: clamp(2rem, 4vw, 3rem) clamp(1rem, 3vw, 2rem);

  & div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;   
    width: 100%;
    max-width: 40em;
    position: relative;
    top: 4%;
    gap: clamp(1.5rem, 3vw, 2rem);
    min-height: auto;
    height: 40rem;
  }

  & figure {
    width: 100%;
    max-width: 400px;
    margin: 0;
    padding: 0;
    display: flex;
        justify-content: center;
    align-items: center;
  }

  & figure img {
    width: 50%;
    height: auto;
    display: block;
    border-radius: 8px;
  }

  & h2 {
    font-size: clamp(1.3rem, 3.5vw, 1.5rem);
    color: #034E77;
    width: 100%;
    text-align: center;
    line-height: 1.2;
  }

  & hr {
    border: 2px solid #006DA8;
    width: 50%;
    color: #006DA8;
  }

  & p {
    font-size: clamp(0.9rem, 2vw, 1rem);
    color: #034E77;
    text-align: center;
    line-height: 1.6;
  }
}

#origem_instrumento::before {
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

#section_objetivo {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: clamp(2rem, vw, 4rem) clamp(1rem, 3vw, 2rem);

  & h3 {
    text-align: left;
    font-size: clamp(1.2rem, 3vw, 1.5rem);
    color: #034E77;
  }

  & hr {
    border: 1px solid #006DA8;
    width: 100%;
    color: #006DA8;
  }

  & p {
    text-align: left;
    font-size: clamp(0.9rem, 1.8vw, 1rem);
    color: #034E77;
    line-height: 1.6;
  }
}

/* PÚBLICO-ALVO LINE */
.publico-line {
  width: 100%;
  max-width: 1200px;
  display: flex;
  justify-content: center;
  margin: 0 auto 2.2rem auto;
  position: relative;
}

.publico-line::before {
  content: "";
  position: absolute;
  top: 50%;
  width: 100%;
  height: 2px;
  background: #9ecde4;
  z-index: 0;
}

.publico-line .line-center {
  width: 140px;
  height: 2px;
  background: transparent;
  position: relative;
  z-index: 2;
}

/* GRID DE ITENS */
.publico-list {
  list-style: none;
  margin: 0 auto;
  padding: 0 clamp(0.5rem, 2vw, 1rem);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: clamp(0.5rem, 1.5vw, 1rem);
  max-width: 1200px;
  width: 100%;
}

/* Cada item */
.publico-item {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Linha vertical + bolinha */
.publico-item::before {
  content: "";
  position: absolute;
  top: -36px;
  width: 2px;
  height: 22px;
  background: #9ecde4;
}

.publico-item .marker {
  position: absolute;
  top: -10px;
  width: 10px;
  height: 10px;
  background: #1d82b9;
  border-radius: 50%;
  box-shadow: 0 0 0 4px #d3eaf5;
  z-index: 2;
}

/* BOX DOS ITENS */
.box {
  width: 100%;
  height: auto;
  min-height: 100px;
  padding: clamp(0.5rem, 1.5vw, 1rem);
  display: flex;
  background-color: var(--bg);
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  color: #fff;
  transition: all 0.3s ease;
}

.box img {
  width: clamp(30px, 5vw, 42px);
  height: auto;
  margin-bottom: 0.35rem;
}

.label {
  font-size: clamp(0.75rem, 1.5vw, 0.95rem);
  font-weight: 700;
  text-align: center;
  line-height: 1.2;
}

/* RESPONSIVIDADE */

/* Tablet (1100px and down) */
@media (max-width: 1100px) {
  #origem_instrumento {
    gap: 2rem;
    padding: 2rem;
  }

  #origem_instrumento div {
    max-width: 35em;
  }

  #section_objetivo {
    padding: 2.5rem 1.5rem;
  }

  .publico-line {
    max-width: 100%;
  }

  .publico-list {
    grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
  }
}

/* Mobile (768px and down) */
@media (max-width: 768px) {
  #origem_instrumento {
    flex-direction: column;
    gap: 1.5rem;
    padding: 1.5rem 1rem;
  }

  #origem_instrumento div {
    width: 100%;
    max-width: 100%;
  }

  #origem_instrumento h2 {
    font-size: 1.3rem;
  }

  #origem_instrumento p {
    font-size: 0.95rem;
  }

  #section_objetivo {
    padding: 2rem 1rem;
  }

  #section_objetivo h3 {
    font-size: 1.25rem;
  }

  .publico-list {
    grid-template-columns: repeat(3, 1fr);
    gap: 0.75rem;
    padding: 0 0.75rem;
  }

  .box {
    min-height: 90px;
    padding: 0.6rem 0.4rem;
  }

  .publico-item::before,
  .publico-item .marker {
    display: none;
  }

  .publico-line {
    display: none;
  }
}

/* Small Mobile (600px and down) */
@media (max-width: 600px) {
  section {
    padding: clamp(0.75rem, 2vw, 1rem);
  }

  

  #origem_instrumento {
    padding: 1.25rem 0.75rem;
    gap: 0.1rem;
  }
  #origem_instrumento > div >div{
    gap: 1rem;

    
  }
  figure > img{
    position: relative;
    bottom: 2rem;
  }
  #origem_instrumento::before{
    background-image: none;
  }

  #origem_instrumento h2 {
    font-size: 1.15rem;
  }

  #origem_instrumento p {
    font-size: 0.9rem;
  }

  #section_objetivo {
    padding: 1.5rem 0.75rem;
  }

  #section_objetivo h3 {
    font-size: 1.1rem;
    text-align: center;
  }

  #section_objetivo p {
    font-size: 0.9rem;
    text-align: center;
  }

  .publico-list {
    grid-template-columns: repeat(2, 1fr);
    gap: 0.5rem;
    padding: 0 0.5rem;
  }

  .box {
    min-height: 80px;
    padding: 0.5rem 0.3rem;
  }

  .box img {
    width: clamp(24px, 4vw, 30px);
    margin-bottom: 0.2rem;
  }

  .label {
    font-size: 0.7rem;
  }
}

/* Extra Small (480px and down) */
@media (max-width: 480px) {
  #origem_instrumento {
    padding: 1rem 0.5rem;
    margin-left: 0;
    width: 100%;
    background-image: none;
    background-color: transparent;
  }

  #origem_instrumento h2 {
    font-size: 1rem;
  }

  #origem_instrumento p {
    font-size: 0.85rem;
  }

  #section_objetivo {
    padding: 1.25rem 0.5rem;
  }

  #section_objetivo h3 {
    font-size: 1rem;
  }

  .publico-list {
    grid-template-columns: 1fr;
    gap: 0.4rem;
    padding: 0;
  }

  .box {
    min-height: 75px;
    padding: 0.5rem;
  }

  .box img {
    width: 20px;
  }

  .label {
    font-size: 0.65rem;
  }
}

/* Landscape */
@media (max-height: 600px) and (orientation: landscape) {
  #origem_instrumento {
    padding: 1rem;
  }

  #section_objetivo {
    padding: 1rem;
  }
}
</style>