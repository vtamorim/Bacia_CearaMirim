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

.page-inner {
    width: 100%;
    padding: clamp(1rem, 4vw, 3rem) clamp(0.5rem, 3vw, 2rem);
}

.contact-wrapper {
    width: 100%;
    max-width: 700px;
    margin: 0 auto;
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    margin-bottom: 2rem;
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
    font-weight: 500;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: clamp(0.6rem, 2vw, 0.9rem);
    font-size: clamp(0.85rem, 1.6vw, 0.95rem);
    border: 2px solid #0081c7;
    border-radius: 8px;
    font-family: 'Poppins', sans-serif;
    background: #f9f9f9;
    color: #333;
    transition: border-color 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
    min-height: 44px;
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
    resize: vertical;
    min-height: 120px;
}

/* Botão Enviar */
.btn-send {
    align-self: flex-start;
    font-size: clamp(0.95rem, 1.6vw, 1.05rem);
    font-weight: 600;
    color: white;
    background: #21A6EE;
    border: none;
    border-radius: 200px;
    cursor: pointer;
    height: 44px;
    width: 100%;
    max-width: 250px;
    transition: all 0.3s ease;
    box-shadow: 0px 3px 8px rgba(33, 166, 238, 0.3);
}

.btn-send:hover:not(:disabled) {
    background: #0066a1;
    transform: translateY(-2px);
    box-shadow: 0px 6px 12px rgba(33, 166, 238, 0.4);
}

.btn-send:active:not(:disabled) {
    transform: translateY(0);
}

.btn-send:disabled {
    opacity: 0.7;
    cursor: not-allowed;
}

/* Feedback messages */
.feedback {
    margin: 1rem 0;
    min-height: 1.5rem;
}

.feedback p {
    margin: 0;
    font-size: clamp(0.85rem, 1.6vw, 0.95rem);
    font-weight: 500;
    animation: slideIn 0.3s ease;
}

.feedback .enviando { 
    color: #0077cc; 
}

.feedback .sucesso { 
    color: #22c55e; 
}

.feedback .erro { 
    color: #ef4444; 
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Seção de emails */
.emails-section {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: clamp(1rem, 3vw, 2rem);
    margin-top: 2rem;
}

.email-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: clamp(1rem, 2vw, 1.5rem);
    border: 2px solid #0081c7;
    border-radius: 8px;
    background: #f9f9f9;
    transition: all 0.3s ease;
    min-height: 70px;
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
    width: 36px;
    height: 36px;
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
    word-break: break-word;
    margin: 0;
    font-weight: 500;
}

/* Tablet (768px and down) */
@media (max-width: 768px) {
    .page-inner {
        padding: 1.5rem 1rem;
    }

    .contact-wrapper {
        max-width: 100%;
    }

    .form-row {
        grid-template-columns: 1fr;
        gap: 1.2rem;
    }

    .btn-send {
        width: 100%;
        max-width: none;
    }

    .emails-section {
        grid-template-columns: 1fr;
    }
}

/* Mobile (600px and down) */
@media (max-width: 600px) {
    .page-inner {
        padding: 1rem 0.75rem;
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

    input[type="text"],
    input[type="email"],
    textarea {
        padding: 0.7rem;
        font-size: 16px; /* Prevents zoom on iOS */
        min-height: 44px;
    }

    textarea {
        min-height: 100px;
    }

    .btn-send {
        height: 48px;
        width: 100%;
    }

    .email-card {
        padding: 1rem;
        gap: 0.75rem;
    }

    .email-icon {
        width: 32px;
        height: 32px;
    }

    .feedback p {
        font-size: 0.9rem;
    }
}

/* Extra Small devices (480px and down) */
@media (max-width: 480px) {
    .page-inner {
        padding: 0.75rem 0.5rem;
    }

    .contact-form {
        gap: 0.8rem;
    }

    .form-group {
        gap: 0.3rem;
    }

    label {
        font-size: 0.85rem;
    }

    input[type="text"],
    input[type="email"],
    textarea {
        padding: 0.6rem;
        font-size: 16px;
    }

    textarea {
        min-height: 90px;
    }

    .btn-send {
        height: 44px;
        font-size: 0.9rem;
    }

    .email-card {
        flex-direction: column;
        text-align: center;
        min-height: auto;
    }

    .email-icon {
        width: 28px;
        height: 28px;
    }

    .email-card p {
        font-size: 0.8rem;
    }
}

/* Landscape orientation */
@media (max-height: 600px) {
    textarea {
        min-height: 80px;
    }
}
</style>
