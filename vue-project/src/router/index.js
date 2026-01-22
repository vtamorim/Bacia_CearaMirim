import { createRoute, createWebHistory } from "vue-router";

import Comite from '@/views/Sobre o Comite/index.vue';
import Quiz from '@/views/Quiz/index.vue';
import ODS from '@/views/ODS/index.vue';
import Jogos from '@/views/Jogos/index.vue';
import Contato from '@/views/Contato/index.vue';
import Cartilha from '@/views/Cartilha/index.vue';

const routes = [
    { path:'/',name: 'Comitê', component : Comite},
    { path : '/quiz', name: 'Quiz', component : Quiz},
    { path : '/ods', name: 'ODS', component : ODS},
    { path : 'jogos', name : 'Jogos', component : Jogos},
    { }
]