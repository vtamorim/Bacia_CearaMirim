<template>
    <section>
        <div>
            <div>
                <h2>Origem dessa Cartilha Interativa</h2>
                <hr>
                <p></p>
            </div>
            <figure>
                <img src="" alt="">
            </figure>
        </div>
        <div>  
            <div>
                <h2>Instrumento de Apoio à Educação e à Gestão Ambiental</h2>
                <hr>
                <p>A elaboração da cartilha interativa sobre a bacia hidrográfica do rio Ceará-Mirim surgiu da necessidade de difundir informações bem como fortalecer o conhecimento da população local sobre a importância da gestão integrada dos recursos hídricos, promovendo maior conscientização e engajamento comunitário na preservação do rio e de seus afluentes.</p>
            </div>
                <figure>
                    <img src="" alt="">
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



</script>
<style scoped>
/* SEÇÃO PÚBLICO-ALVO — IGUAL AO MODELO DA IMAGEM */


#section_objetivo{
    
    height: 30rem;
    & p{
        text-align: left;
        width: 35%;
    }
    & h3{
        text-align: left;
    }

    & hr{
        border: 1px solid #006DA8;
        width: 35%;
        color: #006DA8;
    }
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    padding-top: 10rem;
    padding-left: 15rem;
}



.publico-line {
    width: 986px;
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

/* Linha central curta */
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
    padding: 0;
    display: grid;
    grid-template-columns: repeat(7, minmax(0,1fr));
    gap: 0;
    max-width: 1150px;
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
    height: 120px;
    padding: 1rem 0.6rem;
    display: flex;
    background-color: var(--bg);
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 0;
    color: #fff;
}

.box img {
    width: 42px;
    height: auto;
    margin-bottom: 0.35rem;
}

.label {
    font-size: 0.95rem;
    font-weight: 700;
}

/* RESPONSIVIDADE */
@media (max-width: 900px) {
    .publico-list {
        grid-template-columns: repeat(4, 1fr);
    }
    .publico-item::before {
        display: none;
    }
    .publico-item .marker {
        display: none;
    }
}

@media (max-width: 600px) {
    .publico-list {
        grid-template-columns: repeat(2, 1fr);
    }
}

</style>