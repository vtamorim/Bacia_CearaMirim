<template>

<section>
<iframe width="560" height="315" src="https://www.youtube.com/embed/_kVRRV0b2is?si=tP04TXsGYcxTht39" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<div>
    <h1>Conheça a Bacia do Rio Ceará-Mirim</h1>
    <p>A bacia do rio Ceará-Mirim percorre diversos municípios entre Lajes, onde nasce na Serra do Feiticeiro, e Extremoz, onde deságua após 129 km de extensão. 
Ela sustenta atividades essenciais como abastecimento urbano, indústria, irrigação, agropecuária, pesca e turismo. 
Contudo, sofre com poluição, desmatamento, erosão, uso inadequado do solo e exploração excessiva da água, o que ameaça sua qualidade ambiental e a disponibilidade de recursos naturais.</p>

    <button onclick="">Saiba mais sobre a Bacia</button>
</div>   
</section>



</template>

<script setup></script>
<style scoped>

    section{
        position: relative;
        top: 1rem;
        gap: 4rem;
        display: flex;
        margin: 0 auto;
        max-width: 1440px;
        justify-content: center;
        & div{
            width: 50%;
            display: flex;
            flex-direction: column;
            gap: 2.2rem;
        }
    }
    button{
        background-color: var(--bg-but) ;
        color: var(--txt-but);
        width: 240px;
        height: 44px;
        border-radius: 200px;
        border: none;
        font-size: 1em;
        font-weight: bold;
        transition: background-color 0.1s ease-in;
        box-shadow: 0px 3px 3px var(--color-boxs);
    &:hover{
        background-color: #0A142F;
    }
    
    }



@media (max-width: 900px) {
  section {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }
}

@media (max-width: 600px) {
  section {
    flex-direction: column;
    padding: 20px 12px;
    & div{
        width: 100%;
    
    }
    
}

  
}
</style>