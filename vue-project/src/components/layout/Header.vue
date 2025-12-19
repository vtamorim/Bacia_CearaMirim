<template>
    <header>
        <div class="header-inner">
            <a href="#home">
            <img :src="Logotipo" alt="Logo" />
            </a>
            <nav>
                <ul>
                    <li><a href="#home" :class="{ active: isActive('home') }">A Bacia</a></li>
                    <li><a href="#comite" :class="{ active: isActive('comite') }">Comitê</a></li>
                    <li><a href="#ods" :class="{ active: isActive('ods') }">ODS</a></li>
                    <li id="midias"><a href="#midias" :class="{ active: isActive('midias') }" >Mídias</a></li>
                    <li><a href="#cartilha" :class="{ active: isActive('cartilha') }">Cartilha</a></li>
                    <li><a href="#jogos" :class="{ active: isActive('jogos') }">Jogos</a></li>
                    <li><a href="#contato" :class="{ active: isActive('contato') }">Contato</a></li>
                </ul>
            </nav>
        </div>
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
            width: 100%;
            background-color: var(--cor-bg);
            display: flex;
            align-items: center;
            min-height: 4.2rem;
            justify-content: center;
        }

        .header-inner{
            max-width: 1400px;
            width: 100%;
            padding: 0 clamp(0.5rem, 3vw, 2.5rem);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2rem;
        }

        header a img{
            height: 3rem;
            display: block;
            width: auto;
        }

        header nav{
            flex: 1;
        }

        header nav > ul{
            height: 4.2rem;
            align-items: center;
            display: flex;
            list-style-type: none;
            justify-content: flex-end;
            gap: 0;
        }

        header nav > ul li{
            display: flex;
            align-items: center;
            justify-content: center;
            height: 4.2rem;
            flex: 0.1 auto;
            box-sizing: border-box;
        }

        header nav > ul li a{
            height: 100%;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            color: white;
            font-size: clamp(0.9rem, 1.6vw, 1rem);
            white-space: nowrap;
        }

        header nav > ul li a:hover,
        header nav > ul li a.active{
                background-color: #014D83;
        }

        /* Responsive tweaks */
        @media (max-width: 900px) {
            header{
                padding: 0 clamp(0.5rem, 4vw, 1.5rem);
            }

            header nav > ul{
                gap: 0.5rem;
            }
        }

        #midias > a{
            color: rgb(146, 146, 146) !important;
            background:transparent !important;
        }

        @media (max-width: 600px) {
            header{
                padding: 0.5rem 1rem;
                flex-direction: column;
                height: auto;
                gap: 0.5rem;
                padding-top: 0.6rem;
                padding-bottom: 0.6rem;
            }

            header nav > ul{
                width: 100%;
                flex-wrap: wrap;
                justify-content: center;
                gap: 0.5rem;
            }

            header nav > ul li{
                min-width: unset;
                flex: 0 1 auto;
            }

            header nav > ul li a{
                padding: 0.4rem 0.6rem;
                font-size: 0.95rem;
                white-space: normal;
            }
        }

    
    

</style>