import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('@/views/Bacia/bacia.vue') },
  { path: '/bacia', name: 'bacia', component: () => import('@/views/Bacia/bacia.vue') },
  { path: '/comite', name: 'comite', component: () => import('@/views/Sobre o Comite/index.vue') },
  { path: '/ods', name: 'ods', component: () => import('@/views/ODS/index.vue') },
  { path: '/cartilha', name: 'cartilha', component: () => import('@/views/Cartilha/index.vue') },
  { path: '/contato', name: 'contato', component: () => import('@/views/Contato/index.vue') },
  { path: '/jogos', name: 'jogos', component: () => import('@/views/Jogos/index.vue') },
  { path: '/quiz', name: 'quiz', component: () => import('@/views/Quiz/index.vue') },
  { path: '/:pathMatch(.*)*', redirect: '/' }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router