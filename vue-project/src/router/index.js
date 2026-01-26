import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('@/views/Bacia/bacia.vue') },
  { path: '/bacia', name: 'bacia', component: () => import('@/views/Bacia/bacia.vue') },
  { path: '/comite', name: 'comite', component: () => import('@/views/Sobre o Comite/index.vue') },
  { path: '/ods', name: 'ods', component: () => import('@/views/ODS/index.vue') },
  { path: '/cartilha', name: 'cartilha', component: () => import('@/views/Cartilha/index.vue') },
  { path: '/contato', name: 'contato', component: () => import('@/views/Contato/index.vue') },
  { path: '/jogos', name: 'jogos', component: () => import('@/views/Jogos/index.vue') },
  { path: '/jogos/fluxo-agua', name: 'fluxo-agua', component: () => import('@/views/Jogos/fluxo-agua.vue') },
  { path: '/jogos/protetor-ecossistema', name: 'protetor-ecossistema', component: () => import('@/views/Jogos/protetor-ecossistema.vue') },
  { path: '/jogos/qualidade-agua', name: 'qualidade-agua', component: () => import('@/views/Jogos/qualidade-agua.vue') },
  { path: '/quiz', name: 'quiz', component: () => import('@/views/Quiz/index.vue') },
  { path: '/:pathMatch(.*)*', redirect: '/' },
  { path: '/jogos/jogo-memoria', name: 'jogomemoria', component: () => import('@/views/Jogos/jogo-memoria.vue') }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router