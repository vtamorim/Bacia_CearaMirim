<template>
    <section id="apresentar_comite">
        <figure><img v-bind:src="img1" alt="Foto do Comitê"></figure>
        <p> {{ apresentacao_comite }}</p>
    </section>
    
    <h2>Objetivos</h2>
    <section id="objetivos_comite">
        
        <div v-for="(num, index) in 3"
      :key="num"
      class="objectives">
        <img v-bind:src="imagens[index]" alt="">
        <h3>{{ content[index].titulo }}</h3>
         <p>{{ content[index].p }}</p>
        </div>
    </section>


    <h2>Gestão Atual</h2>
    <section>
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

    <h2>Gestões Anteriores</h2>
    <section>
        <div v-for="(num,index) in 3">

        </div>
        <p>bla bla bla bla bla</p>
    </section>

    
</template>
<script setup>
    import img1 from '@/assets/images/Comite/fotocomite.png'
    import objetivo1 from '@/assets/images/Comite/Group 60.svg'
    import objetivo2 from '@/assets/images/Comite/Group 61.svg'
    import objetivo3 from '@/assets/images/Comite/Group 62.svg'

    import ceres from '@/assets/images/Comite/Group 55.png'
    const content = [ {"titulo":"Gestão","p":"Promover a gestão integrada dos recursos hídricos no território da bacia, assegurando a participação de múltiplos atores sociais no processo decisório;"},
    {"titulo":"Mediação","p":"Elaborar e aprovar o plano de bacia, mediar conflitos entre usuários, e definir os critérios para a cobrança pelo uso da água;"},
    {"titulo":"Acompanhamento","p":"Acompanhar a implementação das políticas públicas no âmbito da bacia hidrográfica;"}      
    ]

    const imagens = [objetivo1,objetivo2,objetivo3]
    const apresentacao_comite = "O comitê da bacia hidrográfica do rio Ceará-Mirim (CBH-CM) foi criado pelo Decreto de N° 21.779, de 07 de julho de 2010, sancionado pelo Governo do Estado do Rio Grande do Norte, integrando-o formalmente ao Sistema Integrado de Gestão dos Recursos Hídricos (SIGERH) do Estado, consolidando-o como instância colegiada de apoio à implementação da Política Estadual de Recursos Hídricos. O CBH-CM é composto por representações da sociedade civil, poder público e usuários de água, conforme estabelecido pela Política Nacional de Recursos Hídricos. O número de vagas é disposto de forma a trazer à tona as principais necessidades da bacia hidrográfica, o que resulta em um total de 40 vagas, sendo 20 representantes titulares e 20 suplentes."



</script>
<style scoped>

    #apresentar_comite{
        display: flex;
        gap: 20px;
        justify-content: center;
}
    #objetivos_comite{
        background-image: url('@/assets/images/Comite/Vector 69.png');
        
        display: flex;
        height: 856px;
        justify-content: center;
        align-items: center;

        width: 100%;

    & p{
        width: 50%;
        font-size: 18px;
        color: #034E77;
    }

    & h3{
        font-size: 20px;
        color: #034E77;
    }

    & div{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;   
        width: 40em;
        gap: 32px;
        height: 30em;
    }
    
    }
    
    #ceres_desc{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
        margin: 0 auto;
        width: 265px;
        background-color: transparent;
        position: relative;
        background-color: white;
        box-shadow: 0px 3px 3px 0px rgba(0,129, 199, 0.15);
        bottom: 50px;
        z-index: 0;
        height: 104px;
    }
    
    #apresentar_comite >p{
        text-align: justify;
        width: 30%;
        
    }
</style>