<template>

<section>
<iframe width="560" height="315" src="https://www.youtube.com/embed/_kVRRV0b2is?si=tP04TXsGYcxTht39" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<div>
    <h1>Conheça a Bacia do Rio Ceará-Mirim</h1>
    <p>A bacia do rio Ceará-Mirim percorre diversos municípios entre Lajes, onde nasce na Serra do Feiticeiro, e Extremoz, onde deságua após 129 km de extensão. 
Ela sustenta atividades essenciais como abastecimento urbano, indústria, irrigação, agropecuária, pesca e turismo. 
Contudo, sofre com poluição, desmatamento, erosão, uso inadequado do solo e exploração excessiva da água, o que ameaça sua qualidade ambiental e a disponibilidade de recursos naturais.</p>

    <button @click="abrirSite">Saiba mais sobre a Bacia</button>
</div>   
</section>

</template>

<script setup>
        function abrirSite() {
            const url = "https://files.abrhidro.org.br/Eventos/Trabalhos/248/XXVI-SBRH1104-2-0-20250805-212923.pdf";
            window.open(url, "_blank"); // "_blank" abre em nova aba
        }
</script>
<style scoped>

    section{
        position: relative;
        gap: 4rem;
        display: flex;
        margin: 0 auto;
        max-width: 1400px;
        width: 100%;
        padding: 0 clamp(0.5rem, 3vw, 2.5rem);

        box-sizing: border-box;
        & div{
            width: 50%;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }
    }

    iframe {
        width: 100%;
        max-width: 560px;
        height: 300px;
        aspect-ratio: 16 / 9;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    h1 {
        font-size: clamp(1.5rem, 4vw, 2.2rem);
        color: #0081C7;
        margin: 0;
        font-weight: 700;
        line-height: 1.2;
    }

    p {
        font-size: clamp(0.95rem, 2vw, 1.1rem);
        color: #333;
        line-height: 1.6;
        margin: 0;

        text-align: justify;
    }

    button{
        background-color: var(--bg-but);
        color: var(--txt-but);
        width: 240px;
        height: 44px;
        border-radius: 200px;
        border: none;
        font-size: 1em;
        font-weight: bold;
        transition: all 0.2s ease;
        box-shadow: 0px 3px 3px var(--color-boxs);
        cursor: pointer;
        align-self: flex-start;
    }

    button:hover{
        background-color: #0A142F;
        transform: translateY(-2px);
        box-shadow: 0px 6px 8px var(--color-boxs);
    }

    /* Tablet (max-width 768px) */
    @media (max-width: 768px) {
        section {
            flex-direction: column;
            gap: 2rem;
            padding: 0 clamp(0.5rem, 3vw, 2.5rem);
        }
        h1{
            text-align: center;
            width: 90vw;

        }

        section & p {
            width: 100%;
        }

        section & div {
            width: 100%;
        }

        iframe {
            max-width: 100%;
        }
        button{
            width: 100%;
            max-width: 300px;
            position: relative;
            left: 50%;
            
        }
        h1 {
            font-size: clamp(1.3rem, 3.5vw, 2rem);
        }

        p {
                        font-size: clamp(0.85rem, 1.6vw, 0.95rem);
            text-align: center;
            width: 90vw;
        }
    }
    @media (max-width:1400px) {
        
    }
    @media (max-width: 1200px) {
        section{
            flex-direction: column-reverse;
            width: 100%;
            justify-content: center;
            & p{
                
                text-align: center;
                padding: 0%;
                width: 95vw;
                position: relative;
                right: 1%;

            }
            & h1{
                text-align: center;
            }

            & button{
                position: relative;
                align-self: center;
                left: 50%;
            }
            & iframe{
                position: relative;
                max-width: none;
                height: auto;
            }
        }
    }

    
    @media (max-width: 600px) {
        section {
            flex-direction: column-reverse;
            justify-content: center;

            padding: 0 clamp(0.5rem, 3vw, 2.5rem);
            margin-bottom: clamp(1.5rem, 4vw, 2.5rem);
            gap: 1.5rem;
        }

        section & p {
            width: 100%;
        }

        section & div {
            width: 100%;
            gap: 1.2rem;
        }

        iframe {
            max-width: 100%;
            height: auto;
        }

        h1 {
            font-size: clamp(1.1rem, 3vw, 1.6rem);
            line-height: 1.3;
        }

        p {
            font-size: 0.75rem;
            line-height: 1.3;
            text-align: center;

            width: 100vw;
            right: 6%;
            position: relative;
        }

        button {
            width: 100%;
            max-width: 100%;
            height: 48px;
            font-size: 0.95rem;
        }
    }

    /* Small mobile (max-width 480px) */
    @media (max-width: 480px) {
        section {
            padding: 1rem;
            margin-bottom: 1.5rem;
            gap: 1.2rem;
        }

        h1 {
            font-size: 1.1rem;
        }

        p {
            font-size: 0.85rem;
            line-height: 1.5;
            text-align: center;
            width: 100vw;
            right: 1rem;
            position: relative;

        }

        button {
            height: 40px;
            width: 100%;
            font-size: 0.6rem;
        }
    }

</style>