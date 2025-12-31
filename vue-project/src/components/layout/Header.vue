<template>
    <header>
        <div class="header-inner">
            <a href="#home" class="logo-link">
            <img :src="Logotipo" alt="Logo" />
            </a>
            
            <!-- Hamburger Menu Button (Mobile) -->
            <button class="hamburger" :class="{ active: menuAberto }" @click="menuAberto = !menuAberto" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            
            <!-- Navigation -->
            <nav :class="{ 'menu-ativo': menuAberto }">
                <ul>
                    <li><a href="#home" :class="{ active: isActive('home') }" @click="fecharMenu">A Bacia</a></li>
                    <li><a href="#comite" :class="{ active: isActive('comite') }" @click="fecharMenu">Comitê</a></li>
                    <li><a href="#ods" :class="{ active: isActive('ods') }" @click="fecharMenu">ODS</a></li>
                    <li id="midias"><a href="#midias" :class="{ active: isActive('midias') }" @click="fecharMenu">Mídias</a></li>
                    <li><a href="#cartilha" :class="{ active: isActive('cartilha') }" @click="fecharMenu">Cartilha</a></li>
                    <li><a href="#jogos" :class="{ active: isActive('jogos') }" @click="fecharMenu">Jogos</a></li>
                    <li><a href="#contato" :class="{ active: isActive('contato') }" @click="fecharMenu">Contato</a></li>
                </ul>
            </nav>
        </div>
    </header>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import Logotipo from '@/assets/images/logotipo.svg'

const hashPage = ref('home');
const menuAberto = ref(false);

const isActive = (page) => {
  return hashPage.value === page || (page === 'home' && (hashPage.value === 'home' || hashPage.value === 'bacia'));
};

const updateHash = () => {
  hashPage.value = window.location.hash.slice(1) || 'home';
};

const fecharMenu = () => {
  menuAberto.value = false;
};

// Fechar menu quando navegar
watch(hashPage, () => {
  fecharMenu();
});

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




    * { 
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Poppins', sans-serif;
    }

    header {
        width: 100%;
        background-color: var(--cor-bg);
        display: flex;
        align-items: center;
        min-height: 4.2rem;
        justify-content: center;
        position: relative;
        z-index: 100;
    }

    .header-inner {
        max-width: 1400px;
        width: 100%;
        padding: 0 clamp(0.5rem, 3vw, 2.5rem);
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 2rem;
    }

    .logo-link {
        display: flex;
        align-items: center;
        flex-shrink: 0;
        z-index: 101;
    }

    header a img {
        height: 3rem;
        display: block;
        width: auto;
    }

    .hamburger {
        display: none;
        flex-direction: column;
        background: none;
        border: none;
        cursor: pointer;
        padding: 0.5rem;
        z-index: 101;
        gap: 0.4rem;
    }

    .hamburger span {
        width: 25px;
        height: 2.5px;
        background-color: white;
        border-radius: 2px;
        transition: all 0.3s ease;
        display: block;
    }

    .hamburger.active span:nth-child(1) {
        transform: rotate(45deg) translate(8px, 8px);
    }

    .hamburger.active span:nth-child(2) {
        opacity: 0;
    }

    .hamburger.active span:nth-child(3) {
        transform: rotate(-45deg) translate(7px, -6px);
    }

    /* Navigation */
    header nav {
        flex: 1;
    }

    header nav > ul {
        height: 4.2rem;
        align-items: center;
        display: flex;
        list-style-type: none;
        justify-content: flex-end;
        gap: 0;
        margin: 0;
        padding: 0;
    }

    header nav > ul li {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 4.2rem;
        flex: 0.1 auto;
        box-sizing: border-box;
        margin: 0;
    }

    header nav > ul li a {
        height: 100%;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: white;
        font-size: clamp(0.9rem, 1.6vw, 1rem);
        white-space: nowrap;
        transition: all 0.2s ease;
    }

    header nav > ul li a:hover,
    header nav > ul li a.active {
        background-color: #014D83;
    }

    #midias > a {
        color: rgb(146, 146, 146) !important;
        background: transparent !important;
    }

    /* Desktop - 900px and up */
    @media (min-width: 901px) {
        header nav {
            display: block;
        }

        header nav > ul {
            flex-direction: row;
        }
    }

    /* Tablet - 768px to 900px */
    @media (max-width: 900px) {
        header {
            padding: 0 clamp(0.5rem, 4vw, 1.5rem);
        }

        header nav > ul {
            gap: 0.5rem;
        }
    }

    /* Mobile Menu - 768px and down */
    @media (max-width: 768px) {
        .hamburger {
            display: flex;
        }

        .header-inner {
            padding: 0 clamp(0.75rem, 3vw, 1.5rem);
        }

        header nav {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background-color: var(--cor-bg);
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
            z-index: 99;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        header nav.menu-ativo {
            max-height: 600px;
        }

        header nav > ul {
            height: auto;
            flex-direction: column;
            align-items: stretch;
            justify-content: flex-start;
            gap: 0;
            padding: 0.5rem 0;
        }

        header nav > ul li {
            height: auto;
            flex: none;
            width: 100%;
        }

        header nav > ul li a {
            height: auto;
            padding: clamp(0.8rem, 2vw, 1.2rem) clamp(1rem, 3vw, 1.5rem);
            justify-content: flex-start;
            white-space: normal;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            font-size: clamp(0.9rem, 1.5vw, 1rem);
        }

        header nav > ul li a:hover,
        header nav > ul li a.active {
            background-color: #014D83;
            padding-left: clamp(1.2rem, 4vw, 2rem);
        }

        #midias > a {
            color: rgb(146, 146, 146) !important;
            background: transparent !important;
        }

        #midias > a:hover {
            background: transparent !important;
            padding-left: clamp(1.2rem, 4vw, 2rem);
        }
    }

    /* Small Mobile - 600px and down */
    @media (max-width: 600px) {
        header {
            min-height: 3.5rem;
        }

        header a img {
            height: 2.5rem;
        }

        .header-inner {
            padding: 0 clamp(0.5rem, 2vw, 1rem);
            gap: 1rem;
        }

        header nav > ul li a {
            padding: 0.75rem clamp(0.8rem, 2vw, 1.2rem);
        }

        header nav > ul li a:hover,
        header nav > ul li a.active {
            padding-left: clamp(1rem, 3vw, 1.5rem);
        }
    }

    /* Extra Small - 480px and down */
    @media (max-width: 480px) {
        header {
            min-height: 3.25rem;
        }

        header a img {
            height: 2.2rem;
        }

        .hamburger {
            padding: 0.4rem;
        }

        .hamburger span {
            width: 22px;
            height: 2px;
        }

        header nav > ul li a {
            padding: 0.7rem 1rem;
            font-size: 0.9rem;
        }
    }
</style>