<template>
  <div class="page-inner">
    <div class="contact-wrapper">
    <form class="contact-form" @submit.prevent="enviarContato">
      <!-- Nomes em duas colunas -->
      <div class="form-row">
        <div class="form-group">
          <label for="pri_nome">Primeiro Nome</label>
          <input type="text" id="pri_nome" placeholder="Primeiro nome" v-model="pri_nome" required>
        </div>
        <div class="form-group">
          <label for="ult_nome">Último Nome</label>
          <input type="text" id="ult_nome" placeholder="Último nome" v-model="ult_nome" required>
        </div>
      </div>

      <!-- Email full-width -->
      <div class="form-group form-full">
        <label for="email">E-mail</label>
        <input type="email" id="email" placeholder="E-mail" v-model="email" required>
      </div>

      <!-- Mensagem full-width -->
      <div class="form-group form-full">
        <label for="mensagem">Mensagem</label>
        <textarea id="mensagem" placeholder="Escreva sua mensagem" rows="6" v-model="mensagem" required></textarea>
      </div>

      <!-- Feedback -->
      <div class="feedback">
        <p v-if="status === 'enviando'" class="enviando">Enviando...</p>
        <p v-if="status === 'sucesso'" class="sucesso">{{ mensagemStatus }}</p>
        <p v-if="status === 'erro'" class="erro">{{ mensagemStatus }}</p>
      </div>

      <!-- Botão Enviar -->
      <button type="submit" class="btn-send" :disabled="status === 'enviando'">
        {{ status === 'enviando' ? 'Enviando...' : 'Enviar' }}
      </button>
    </form>

    <!-- Emails abaixo -->
    <div class="emails-section">
      <div class="email-card">
        <figure class="email-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M20 6L12 12L4 6" stroke="currentColor" stroke-width="2" fill="none"/>
          </svg>
        </figure>
        <p>cbhdocearamirim@gmail.com</p>
      </div>
      <div class="email-card">
        <figure class="email-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M20 6L12 12L4 6" stroke="currentColor" stroke-width="2" fill="none"/>
          </svg>
        </figure>
        <p>neppsadiaren@gmail.com</p>
      </div>
    </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const pri_nome = ref('')
const ult_nome = ref('')
const email = ref('')
const mensagem = ref('')


const status = ref('') 
const mensagemStatus = ref('')

async function enviarContato() {
  status.value = 'enviando'
  mensagemStatus.value = ''

  try {
    const response = await fetch('http://127.0.0.1:5000/api/contato', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        pri_nome: pri_nome.value,
        ult_nome: ult_nome.value,
        email: email.value,
        mensagem: mensagem.value
      })
    })

    const data = await response.json()

    if (data.success) {
      status.value = 'sucesso'
      mensagemStatus.value = data.message
      // Limpar formulário
      pri_nome.value = ''
      ult_nome.value = ''
      email.value = ''
      mensagem.value = ''
    } else {
      status.value = 'erro'
      mensagemStatus.value = data.error
    }
  } catch (err) {
    status.value = 'erro'
    mensagemStatus.value = 'Erro ao conectar com o servidor.'
  }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

.contact-wrapper {
    width: 100%;
    max-width: 619px;
    margin: 0 auto;
    padding: clamp(1.5rem, 5vw, 3rem);
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: clamp(0.5rem, 1vw, 0.2rem);
    margin-bottom: clamp(1rem, 2vw, 1rem);
}

/* Form row para 2 colunas */
.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: clamp(1rem, 3vw, 2rem);
    width: 100%;
}

/* Form group */
.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.form-group.form-full {
    grid-column: 1 / -1;
}

/* Labels */
label {
    font-size: clamp(0.9rem, 1.8vw, 1rem);  
    color: #1a1a1a;
    text-align: left;
}
input[type="text"],input[type="email"]{
    width: 100%;
    height: 2.5rem;

}





input[type="text"],
input[type="email"],
textarea {
    padding: clamp(0.6rem, 2vw, 0.9rem);
    font-size: clamp(0.85rem, 1.6vw, 0.95rem);
    border: 2px solid #0081c7;
    border-radius: 8px;
    font-family: 'Poppins', sans-serif;
    background: #f9f9f9;
    box-sizing: border-box;
    color: #333;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

input[type="text"]:focus,
input[type="email"]:focus,
textarea:focus {
    outline: none;
    border-color: #014d83;
    box-shadow: 0 0 8px rgba(1, 129, 199, 0.2);
    background-color: #F3FBFF;

}

textarea {
    resize: none;
    min-height: 120px;
}

/* Botão Enviar */
.btn-send {
    align-self: flex-start;
    font-size: clamp(0.9rem, 1.8vw, 1rem);
    font-weight: 600;
    color: white;
    background: #21A6EE;
    border: none;
    border-radius: 200px;
    cursor: pointer;
    height: 44px;
    width: 15rem;
    transition: background 0.3s ease, transform 0.2s ease;
}

.btn-send:hover {
    background: #0066a1;
    transform: translateY(-2px);
}

.btn-send:active {
    transform: translateY(0);
}

/* Seção de emails */
.emails-section {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: clamp(1rem, 3vw, 2rem);
}

.email-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    height: 60px;
    padding: clamp(0.6rem, 2vw, 0.9rem);
    border: 2px solid #0081c7;
    border-radius: 8px;
    background: #f9f9f9;
    transition: all 0.3s ease;
}

.email-card:hover {
    box-shadow: 0 4px 12px rgba(1, 129, 199, 0.15);
    transform: translateY(-2px);
    background-color: #F3FBFF;
}

.email-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    flex-shrink: 0;
    color: #0081c7;
    margin: 0;
}

.email-icon svg {
    width: 100%;
    height: 100%;
}

.email-card p {
    font-size: clamp(0.85rem, 1.6vw, 0.95rem);
    color: #0081c7;
    text-decoration: none;
    word-break: break-all;
}

/* Responsividade mobile */
@media (max-width: 768px) {
    .contact-wrapper {
        padding: 1rem;
    }

    .form-row {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }

    .btn-send {
        align-self: center;
        width: 100%;
    }

    .emails-section {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    .contact-wrapper {
        padding: 0.75rem;
    }

    .contact-form {
        gap: 1rem;
    }

    .form-group {
        gap: 0.4rem;
    }

    label {
        font-size: 0.9rem;
    }

    input,
    textarea {
        padding: 0.6rem;
        font-size: 0.85rem;
    }

    textarea {
        min-height: 100px;
    }

    .email-card {
        gap: 0.75rem;
        padding: 1rem;
    }

    .email-icon {
        width: 28px;
        height: 28px;
    }
}

/* Suporte a zoom */
@media (max-height: 600px) {
    textarea {
        min-height: 80px;
    }
}


.feedback .enviando { color: #0077cc; }
.feedback .sucesso { color: green; }
.feedback .erro { color: red; }
</style>
