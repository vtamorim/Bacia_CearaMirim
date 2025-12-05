<template>
  <section class="ods-section">
  <h2>Objetivos de Desenvolvimento Sustentável</h2>

  <ul class="ods-grid">
    <li
      v-for="(num, index) in 17"
      :key="num"
      class="box"
      :style="{ backgroundImage: `url(${getImg(num)})` }"
    >
      <h3>{{ lista_texto[index].title }}</h3>
      <p>{{ lista_texto[index].text }}</p>
    </li>
  </ul>
</section>

</template>

<script setup>
function getImg(num) {
  return new URL(`../../assets/images/ODS/${num}.png`, import.meta.url).href;
}

const lista_texto = [
    {"title":"Erradicação da Pobreza","text": "A gestão adequada dos recursos hídricos garante disponibilidade para a produção agrícola e atividades econômicas, reduzindo desigualdades e fortalecendo comunidades vulneráveis."},
    
    {"title":"Fome Zero e Agricultura Sustentável","text": "O uso eficiente do recurso hídrico em bacias hidrográficas é essencial para a irrigação sustentável, assegurando alimentos e produtividade agrícola sem degradar o ambiente."}   ,
    
    {"title":"Saúde e Bem-Estar","text": "A qualidade da água influencia diretamente a saúde pública, prevenindo doenças de veiculação hídrica e promovendo bem-estar nas comunidades."},
    
    {"title":"Educação de Qualidade","text": "A gestão dos recursos hídricos favorece ações de educação ambiental e planejamento territorial, despertando consciência ecológica e cidadania."},
    
    {"title":"Igualdade de Gênero","text": "Projetos participativos de gestão dos recursos hídricos fortalecem o protagonismo feminino em decisões comunitárias e na liderança ambiental."},
    
    {"title":"Água Potável e Saneamento","text": "A gestão dos recursos hídricos na bacia assegura abastecimento, saneamento básico e conservação dos corpos hídricos."},
    
    {"title":"Energia Limpa e Acessível","text": "A água é essencial para a geração hidrelétrica e outras formas de energia limpa, sendo sua gestão eficiente fundamental para a sustentabilidade energética."},
    
    {"title":"Trabalho Decente e Crescimento Econômico","text": " O manejo sustentável da água impulsiona atividades econômicas como agricultura, pesca e turismo, gerando empregos e renda local."},
    
    {"title":"Indústria, Inovação e Infraestrutura:","text": "O planejamento hídrico garante água para processos industriais e incentiva tecnologias inovadoras de reaproveitamento e tratamento."},
    
    {"title":"Redução das Desigualdades","text": "A gestão participativa da bacia promove equidade no acesso à água, fortalecendo comunidades rurais e populações mais vulneráveis."},
    
    {"title":"Cidades e Comunidades Sustentáveis","text": " O gerenciamento das águas urbanas reduz enchentes, melhora o saneamento e torna as cidades mais resilientes e seguras."},
    
    {"title":"Consumo e Produção Responsáveis","text": " O uso racional da água incentiva práticas sustentáveis de consumo, reciclagem e reaproveitamento nos diversos setores produtivos."},
    
    {"title":"Ação Contra a Mudança Global do Clima","text": "A gestão da bacia contribui para mitigar os efeitos das mudanças climáticas por meio da conservação de nascentes e aumento da resiliência hídrica."},
   
    {"title":"Vida na Água","text":" Uma gestão adequada da bacia evita poluição e degradação dos rios, beneficiando ecossistemas aquáticos e preservando a biodiversidade."},
    
    {"title":"Vida Terrestre","text": "O manejo correto da água mantém solos férteis, protege florestas e promove equilíbrio entre ecossistemas terrestres e aquáticos."},
    
    {"title":"Paz, Justiça e Instituições Eficazes","text": "A governança participativa da água fortalece instituições locais, incentiva a cooperação e reduz conflitos pelo uso dos recursos naturais."},
    
    {"title":"Parcerias e Meios de Implementação","text": "A gestão integrada de bacias depende da união entre governos, sociedade civil e setor privado, promovendo parcerias sustentáveis."}
]


</script>




<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* { 
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

/* ---- GRID RESPONSIVO ---- */
ul.ods-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    place-items: center;
    list-style-type: none;
    gap: 70px;
    row-gap: 110px;
}

/* Tablet */
@media (max-width: 1024px) {
    ul.ods-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 55px;
        row-gap: 90px;
    }
}

/* Celular */
@media (max-width: 600px) {
    ul.ods-grid {
        grid-template-columns: 1fr;
        gap: 40px;
        row-gap: 65px;
    }
}

/* ---- CARD ---- */
.box {
    position: relative;
    width: 100%;
    max-width: 330px;
    height: 350px;

    background-size: cover;
    background-position: center;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(17, 13, 13, 0.1);
    z-index: 1;
}

/* Ajuste automático em tela pequena */
@media (max-width: 600px) {
    .box {
        max-width: 290px;
        height: 320px;
    }
}

/* ---- TEXTO ---- */
.box h3 {
    color: white;
    position: relative;
    top: 78%;
    max-width: 90%;
    text-align: center;
    margin: 0 auto;
    text-transform: uppercase;
    font-size: clamp(1rem, 2.5vw, 1.25rem);
    z-index: 3;
    transition: 0.45s cubic-bezier(.2,.9,.2,1);
}

.box p {
    color: white;
    z-index: 2;
    font-size: clamp(0.85rem, 2vw, 1rem);
    position: relative;
    top: 50%;
    max-width: 90%;
    text-align: center;
    margin: 0 auto;
    opacity: 0;
    transform: translateY(0.6rem);
    transition: opacity 0.35s ease, transform 0.45s ease;
}

/* ---- EFEITOS ---- */
.box::before {
    content: "";
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
    transition: transform 0.7s cubic-bezier(0.19, 1, 0.22, 1);
    z-index: 0;
}

.box::after {
    content: "";
    position: absolute;
    inset: 0;
    height: 200%;
    transform: translateY(-50%);
    transition: transform 1.2s cubic-bezier(0.19, 1, 0.22, 1);
    z-index: 1;
    pointer-events: none;
}

/* ANIMAÇÕES NO HOVER */
.box:hover::before {
    transform: translateY(-4%);
}

.box:hover::after {
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.5);
}

.box:hover h3 {
    transform: translateY(-14rem);
}

.box:hover p {
    opacity: 1;
    transform: translateY(-7rem);
}

/* Ajuste do hover no celular (não some da tela) */
@media (max-width: 600px) {

    .box:hover h3 {
        transform: translateY(-11rem);
    }

    .box:hover p {
        transform: translateY(-5rem);
    }

}

</style>
