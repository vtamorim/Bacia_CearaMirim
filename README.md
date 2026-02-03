# Bacia do Rio Ceará-Mirim

Este projeto é uma aplicação web desenvolvida em Vue.js para apresentar informações sobre a Bacia Hidrográfica Ceará-Mirim, localizada no Rio Grande do Norte, Brasil. O site inclui seções sobre a bacia, comitê, ODS (Objetivos de Desenvolvimento Sustentável), cartilhas, contato, jogos educacionais e quiz.

## Funcionalidades

- **Página Inicial**: Visão geral da bacia.
- **Sobre o Comitê**: Informações sobre o comitê responsável.
- **ODS**: Conteúdo relacionado aos Objetivos de Desenvolvimento Sustentável.
- **Cartilha**: Materiais educacionais.
- **Contato**: Formulário de contato com integração via EmailJS.
- **Jogos**: Jogos interativos como aventura, quebra-cabeça,quiz, pipe connect e jogo da memória.

## Tecnologias Utilizadas

- **Vue.js 3**: Framework JavaScript para a interface.
- **Vite**: Ferramenta de build e desenvolvimento.
- **Vue Router**: Roteamento da aplicação.
- **Leaflet**: Biblioteca para mapas interativos.
- **EmailJS**: Serviço para envio de emails.
- **Docker**: Containerização para fácil deployment.

## Pré-requisitos

- Node.js (versão ^20.19.0 ou >=22.12.0)
- Docker (opcional, para execução via container)

## Instalação e Execução

### Via Node.js

1. Navegue até a pasta do projeto:
   ```bash
   cd vue-project
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Execute o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```

4. Abra o navegador em `http://localhost:5173` (ou a porta indicada).

### Via Docker

1. Certifique-se de que o Docker está instalado e em execução.

2. Execute o comando:
   ```bash
   docker-compose up
   ```

3. A aplicação estará disponível em `http://localhost:8080` (ou conforme configurado no docker-compose.yml).

## Build para Produção

Para gerar os arquivos de produção:

```bash
npm run build
```

Os arquivos serão gerados na pasta `dist/`.

## Estrutura do Projeto

```
vue-project/
├── src/
│   ├── components/     # Componentes reutilizáveis (Header, Footer, Carousel)
│   ├── views/          # Páginas da aplicação
│   ├── router/         # Configuração de rotas
│   └── assets/         # Recursos estáticos
├── public/             # Arquivos públicos
├── Dockerfile          # Configuração Docker
├── docker-compose.yml  # Orquestração Docker
└── package.json        # Dependências e scripts
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto é de código aberto. Verifique o arquivo de licença para mais detalhes.