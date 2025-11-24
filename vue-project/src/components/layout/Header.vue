<template>
    <header>
        <img :src="Logotipo" alt="Logo" />
        <nav>
            <ul>
                <li><a href="#" id="paginaatual">A Bacia</a></li>
                <li><a href="#">Comitê</a></li>
                <li><a href="#">ODS</a></li>
                <li><a href="#">Mídias</a></li>
                <li><a href="#">Cartilha</a></li>
                <li><a href="#">Jogos</a></li>
                <li><a href="#">Contato</a></li>
            </ul>
        </nav>
    </header>
</template>
<script setup>

    import Logotipo from '@/assets/images/logotipo.svg'
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
        border-bottom-left-radius: 8px ;
        border-bottom-right-radius: 8px;

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
        }
    }
    #paginaatual{
        background-color: #014D83;
    }
    
    

</style>