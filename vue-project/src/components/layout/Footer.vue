<template>
    <footer>
        <img class="footer-wave" :src="FooterWave" alt="" aria-hidden="true" />
        <div class="footer-inner">
            <div class="footer-left">
                <img :src="Logotipo" alt="Logo" />
            </div>

            <nav class="footer-nav">
                
                <ul>
                    <li><a href="#home" :class="{ active: isActive('home') }">A Bacia</a></li>
                    <li><a href="#comite" :class="{ active: isActive('comite') }">Comitê</a></li>
                    <li><a href="#ods" :class="{ active: isActive('ods') }">ODS</a></li>
                    <li><a href="#midias" :class="{ active: isActive('midias') }">Mídias</a></li>
                    <li><a href="#cartilha" :class="{ active: isActive('cartilha') }">Cartilha</a></li>
                    <li><a href="#jogos" :class="{ active: isActive('jogos') }">Jogos</a></li>
                    <li><a href="#contato" :class="{ active: isActive('contato') }">Contato</a></li>
                </ul>
                <hr>
            </nav>

            <div class="footer-right">
                <div class="copyright">© 2025 Company, Inc</div>
                <div class="socials">
                    <a class="social" href="#" aria-label="instagram"></a>
                    <a class="social" href="#" aria-label="facebook"></a>
                </div>
            </div>
        </div>
    </footer>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import Logotipo from '@/assets/images/logotipo.svg'
import FooterWave from '@/assets/images/Footer/Vector 58(1).svg'

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

footer {
    position: relative;
    width: 100%;

    padding: 0; /* internal spacing handled by .footer-inner */
    box-sizing: border-box;
    background: none;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: clamp(10rem, 20vh, 18rem); /* reserve vertical space so content centers */
}

.footer-wave{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: auto;
    pointer-events: none;
    z-index: 1;
    transform: translateY(-2%);
}

.footer-inner{
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center; /* centralize content horizontally */
    gap: 1rem;
    padding: clamp(1rem, 3.5vw, 2.2rem);
    padding-bottom: clamp(1rem, 2.5vw, 2rem);
    position: relative;
    top: 20vh;
    z-index: 2;
    text-align: center;
}
.footer-left img{
    display: block;
    margin: 0 auto;
    width: clamp(3rem, 6vw, 5rem);
    height: auto;
}

.footer-nav ul{
    width: auto;
    margin: 0;
    padding: 0;
    list-style: none;
    display: flex;
    gap: clamp(0.5rem, 2.5vw, 1.2rem);
    align-items: center;
    justify-content: center;
}

footer nav ul li{
    display: flex;
    align-items: center;
    justify-content: center;
}

.footer-nav ul li{
    height: 100%;
}

.footer-nav ul li a{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    color: white;
    padding: 0.6rem 0.8rem;
    border-radius: 6px;
    font-size: clamp(0.85rem, 1.6vw, 1rem);
    height: 100%;
}


.footer-right{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
}

.footer-right .copyright{
    color: #e6eef6;
    font-size: clamp(0.75rem, 1.2vw, 0.95rem);
}

.socials{
    display: flex;
    gap: 0.5rem;
}

.social{
    display: inline-block;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: rgba(230,238,246,0.08);
}

/* Responsive footer stack */
@media (max-width: 900px){
    .footer-inner{
        padding-left: 1rem;
        padding-right: 1rem;
    }
}

@media (max-width: 600px){
    .footer-inner{
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: 0.75rem;
    }

    .footer-right{ align-items: center; }

    .footer-nav ul{ flex-wrap: wrap; justify-content: center; }
}

/* Reduce wave overlap on very small heights (when zoomed very large) */
@media (max-height: 500px){
    footer{ min-height: clamp(8rem, 18vh, 14rem); }
}



</style>