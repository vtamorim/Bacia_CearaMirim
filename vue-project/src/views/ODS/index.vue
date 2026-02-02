<template>
  <section class="ods-section">
    <ul class="ods-grid">
      <li
        v-for="(num, index) in 17"
        :key="num"
        class="box"
        :style="{ '--bg-img': `url(${getImg(num)})` }"
      >
        <div class="overlay"></div>
        <div class="content">
          <h3>{{ lista_texto[index].title }}</h3>
          <p>{{ lista_texto[index].text }}</p>
        </div>
      </li>
    </ul>
  </section>
</template>

<script setup>
function getImg(num) {
  // Certifique-se de que este caminho está correto para o seu projeto
  return new URL(`../../assets/images/ODS/${num}.png`, import.meta.url).href;
}

const lista_texto = [
    {"title":"Erradicação da Pobreza","text": "A gestão adequada dos recursos hídricos garante disponibilidade para a produção agrícola e atividades econômicas, reduzindo desigualdades e fortalecendo comunidades vulneráveis."},
    {"title":"Fome Zero e Agricultura Sustentável","text": "O uso eficiente do recurso hídrico em bacias hidrográficas é essencial para a irrigação sustentável, assegurando alimentos e produtividade agrícola sem degradar o ambiente."},
    {"title":"Saúde e Bem-Estar","text": "A qualidade da água influencia diretamente a saúde pública, prevenindo doenças de veiculação hídrica e promovendo bem-estar nas comunidades."},
    {"title":"Educação de Qualidade","text": "A gestão dos recursos hídricos favorece ações de educação ambiental e planejamento territorial, despertando consciência ecológica e cidadania."},
    {"title":"Igualdade de Gênero","text": "Projetos participativos de gestão dos recursos hídricos fortalecem o protagonismo feminino em decisões comunitárias e na liderança ambiental."},
    {"title":"Água Potável e Saneamento","text": "A gestão dos recursos hídricos na bacia assegura abastecimento, saneamento básico e conservação dos corpos hídricos."},
    {"title":"Energia Limpa e Acessível","text": "A água é essencial para a geração hidrelétrica e outras formas de energia limpa, sendo sua gestão eficiente fundamental para a sustentabilidade energética."},
    {"title":"Trabalho Decente e Crescimento Econômico","text": "O manejo sustentável da água impulsiona atividades econômicas como agricultura, pesca e turismo, gerando empregos e renda local."},
    {"title":"Indústria, Inovação e Infraestrutura","text": "O planejamento hídrico garante água para processos industriais e incentiva tecnologias inovadoras de reaproveitamento e tratamento."},
    {"title":"Redução das Desigualdades","text": "A gestão participativa da bacia promove equidade no acesso à água, fortalecendo comunidades rurais e populações mais vulneráveis."},
    {"title":"Cidades e Comunidades Sustentáveis","text": "O gerenciamento das águas urbanas reduz enchentes, melhora o saneamento e torna as cidades mais resilientes e seguras."},
    {"title":"Consumo e Produção Responsáveis","text": "O uso racional da água incentiva práticas sustentáveis de consumo, reciclagem e reaproveitamento nos diversos setores produtivos."},
    {"title":"Ação Contra a Mudança Global do Clima","text": "A gestão da bacia contribui para mitigar os efeitos das mudanças climáticas por meio da conservação de nascentes e aumento da resiliência hídrica."},
    {"title":"Vida na Água","text":"Uma gestão adequada da bacia evita poluição e degradação dos rios, beneficiando ecossistemas aquáticos e preservando a biodiversidade."},
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

.ods-section {
    padding: 2rem 1rem;
    display: flex;
    justify-content: center;
    background-color: #f4f4f9; /* Cor de fundo suave */
}

ul.ods-grid {
    display: grid;
    /* Cria colunas automaticamente. Cada card terá no mínimo 300px. */
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    max-width: 1400px;
    width: 100%;
    list-style: none;
}

/* ---- CARD ---- */
.box {
    position: relative;
    width: 100%;
    /* Define uma proporção fixa para o card (largura / altura) */
    aspect-ratio: 4 / 5;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    /* Flexbox para alinhar o conteúdo na parte inferior */
    display: flex;
    align-items: flex-end;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Imagem de Fundo */
.box::before {
    content: "";
    position: absolute;
    inset: 0; /* Ocupa todo o espaço do pai */
    /* Usa a variável CSS definida no HTML */
    background-image: var(--bg-img);
    background-size: cover;
    background-position: center;
    transition: transform 0.5s ease;
    z-index: 0;
}

/* Overlay Gradiente */
.overlay {
    position: absolute;
    inset: 0;
    /* Gradiente de transparente para preto para melhorar a leitura do texto */
    background: linear-gradient(to top, rgba(0, 0, 0, 0.8) 0%, rgba(0, 0, 0, 0.2) 60%, rgba(0, 0, 0, 0) 100%);
    z-index: 1;
}

/* ---- CONTEÚDO (TEXTO) ---- */
.content {
    position: relative;
    z-index: 2; /* Fica acima da imagem e do overlay */
    padding: 1.5rem;
    color: white;
    width: 100%;
}

.box h3 {
    font-size: 1.25rem;
    font-weight: 700;
    text-transform: uppercase;
    line-height: 1.3;
    margin-bottom: 0.5rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
}

.box p {
    font-size: 0.95rem;
    line-height: 1.5;
    /* Esconde o parágrafo inicialmente */
    opacity: 0;
    max-height: 0;
    overflow: hidden;
    transition: all 0.4s ease-in-out;
}

/* ---- EFEITOS DE HOVER ---- */
/* Levanta ligeiramente o card */
.box:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

/* Zoom na imagem de fundo */
.box:hover::before {
    transform: scale(1.1);
}

/* Mostra o parágrafo */
.box:hover p {
    opacity: 1;
    max-height: 200px; /* Altura suficiente para o texto */
}

/* ---- RESPONSIVIDADE ---- */
/* Ajustes para telas menores, se necessário */
@media (max-width: 600px) {
    .ods-section {
        padding: 1rem 0rem;
        width: 100vw;
    }
    ul.ods-grid {
        gap: 1rem;
        padding: 0 0rem;
        align-items: center;
        justify-content: center;
    }
    .box {
        align-self: center;
        justify-self: center;
        /* Em telas muito pequenas, pode ser melhor um card mais baixo */
        min-height: 450px;
        max-width: 90vw;
    }
    .content {
        padding: 1.2rem;
    }
    .box h3 {
        font-size: 1.1rem;
    }
    .box p {
        font-size: 0.9rem;
    }
}
@media (max-width: 400px) {
    .box {
        min-height: 400px;
    }
}
@media (max-width: 320px) {
    .box {
        min-height: 300px;
    }
}
@media (max-width: 300px) {
    .box {
        min-height: 270px;
    }
}

</style>