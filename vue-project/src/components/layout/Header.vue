<template>
    <header>
        <img :src="Logotipo" alt="Logo" />
        <nav>
            <ul>
                <li><a href="#home" :class="{ active: isActive('home') }">A Bacia</a></li>
                <li><a href="#comite" :class="{ active: isActive('comite') }">Comitê</a></li>
                <li><a href="#ods" :class="{ active: isActive('ods') }">ODS</a></li>
                <li><a href="#midias" :class="{ active: isActive('midias') }">Mídias</a></li>
                <li><a href="#cartilha" :class="{ active: isActive('cartilha') }">Cartilha</a></li>
                <li><a href="#jogos" :class="{ active: isActive('jogos') }">Jogos</a></li>
                <li><a href="#contato" :class="{ active: isActive('contato') }">Contato</a></li>
            </ul>
        </nav>
    </header>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import Logotipo from '@/assets/images/logotipo.svg'

const hashPage = ref('home');

const isActive = (page) => {
  return hashPage.value === page || (page === 'home' && (hashPage.value === 'home' || hashPage.value === 'bacia'));
};

const updateHash = () => {
  hashPage.value = window.location.hash.slice(1) || 'home';
};

onMounted(() => {
  updateHash();
  window.addEventListener('hashchange', updateHash);
});
</script>
<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    * { 
        margin: 0;
        padding: 0;
        box-sizing: border-box; font-family: 'Poppins', sans-serif; }
    header{
        width: 100vw;
        background-color: var(--cor-bg);
        padding: 0rem 10rem 0rem 10rem;
        display: flex;
        height: 67px;
        justify-content: space-between;

        & nav>ul{
            width: 50vw;
            height: 100%;
            align-items: center;
            display: flex;
            list-style-type: none;
            justify-content: space-around;
            
            & li{

                height: 100%;
                width: 100%;
                justify-content: center;
                display: flex;
                align-items: center;
            }
            & a:hover{
                background-color: #014D83;
            }
            
            & a{
                height: 100%;
                width: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                text-decoration: none;
                color: white;
            }

            & a.active{
                background-color: #014D83;
            }
        }
    }

    
    

</style>