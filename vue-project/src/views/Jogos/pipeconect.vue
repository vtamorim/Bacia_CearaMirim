<template>
  <div class="game-page">
    <div class="game-header">
      <router-link to="/jogos" class="back-button">← Voltar</router-link>
      <h1>Caminho das Águas</h1>
      <p>Conecte os dutos para levar a água até o destino final.</p>
    </div>

    <div class="game-content">
      <section class="game-description">
        <h2>Como Jogar</h2>
        <p>A água precisa fluir do topo (esquerda) até a saída (direita/fundo).</p>
        <p>Clique nos blocos para <strong>girar os canos</strong>. Tente fazer com o menor número de movimentos!</p>
      </section>

      <section class="game-area">
        <div class="pipe-game-container">
          
          <div class="game-stats">
            <span>Movimentos: <strong>{{ moves }}</strong></span>
          </div>

          <div class="board-wrapper">
            <div class="connector start">
              <div class="pipe-stub">
                <div class="water-flow" :class="{ 'active': flatGrid[0]?.filled }"></div>
              </div>
            </div>

            <div class="board" :style="gridStyle">
              <div
                v-for="(cell, index) in flatGrid"
                :key="index"
                class="tile-cell"
                @click="rotate(index)"
                :class="{ 'is-filled': cell.filled }"
              >
                <div class="tile-face"></div>
                <svg viewBox="0 0 100 100" class="pipe-svg">
                  <g :style="{ transform: `rotate(${cell.rotation}deg)`, transformOrigin: '50% 50%', transition: 'transform 0.3s ease' }">
                    <template v-if="cell.type === 'straight'">
                      <line x1="50" y1="-10" x2="50" y2="110" class="p-outline" />
                    </template>
                    <template v-else>
                      <path d="M50 -10 V50 H110" class="p-outline" fill="none" />
                    </template>
                    <template v-if="cell.type === 'straight'">
                      <line x1="50" y1="-5" x2="50" y2="105" class="p-body" />
                    </template>
                    <template v-else>
                      <path d="M50 -5 V50 H105" class="p-body" fill="none" />
                    </template>
                    <template v-if="cell.type === 'straight'">
                      <line x1="50" y1="0" x2="50" y2="100" class="p-hollow" />
                    </template>
                    <template v-else>
                      <path d="M50 0 V50 H100" class="p-hollow" fill="none" />
                    </template>
                    <g class="water-layer" :class="{ 'flowing': cell.filled }">
                      <template v-if="cell.type === 'straight'">
                        <line x1="50" y1="0" x2="50" y2="100" class="p-water" />
                      </template>
                      <template v-else>
                        <path d="M50 0 V50 H100" class="p-water" fill="none" />
                      </template>
                    </g>
                  </g>
                </svg>
              </div>
            </div>

            <div class="connector end">
              <div class="pipe-stub">
                <div class="water-flow" :class="{ 'active': win }"></div>
              </div>
            </div>
            
          </div>

          <div class="game-actions">
            <button @click="resetGame" class="action-btn">
              <span>↻</span> Reiniciar
            </button>
          </div>

        </div>
      </section>

      <section class="game-info">
        <div class="info-card">
          <h3>🧩 Raciocínio</h3>
          <p>Lógica espacial.</p>
        </div>
        <div class="info-card">
          <h3>⏱️ Tempo</h3>
          <p>Rápido: 1-3 min</p>
        </div>
        <div class="info-card">
          <h3>🎯 Dificuldade</h3>
          <p>Médio</p>
        </div>
      </section>
    </div>

    <Transition name="pop">
      <div v-if="win" class="win-modal-overlay">
        <div class="modal-content">
          <h1>💦 Conectado!</h1>
          <p>Você completou em {{ moves }} movimentos.</p>
          <button @click="resetGame" class="modal-btn">Jogar Novamente</button>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const rows = 4;
const cols = 4;
const grid = ref([]);
const moves = ref(0);
const win = ref(false);

const flatGrid = computed(() => grid.value.flat());
const gridStyle = computed(() => ({
  display: 'grid',
  gridTemplateColumns: `repeat(${cols}, 1fr)`,
  width: '100%',
  gap: '0px'
}));

const initGrid = () => {
  const newGrid = [];
  for (let r = 0; r < rows; r++) {
    const row = [];
    for (let c = 0; c < cols; c++) {
      row.push({
        type: Math.random() > 0.4 ? 'curve' : 'straight',
        rotation: Math.floor(Math.random() * 4) * 90,
        filled: false
      });
    }
    newGrid.push(row);
  }
  grid.value = newGrid;
  checkFlow();
};

const rotate = (index) => {
  if (win.value) return;
  const r = Math.floor(index / cols);
  const c = index % cols;
  grid.value[r][c].rotation += 90;
  moves.value++;
  checkFlow();
};

const getConnections = (cell) => {
  const rot = (cell.rotation % 360 + 360) % 360;
  if (cell.type === 'straight') {
    return (rot === 0 || rot === 180) ? ['top', 'bottom'] : ['left', 'right'];
  }
  const curveMap = { 0: ['top', 'right'], 90: ['right', 'bottom'], 180: ['bottom', 'left'], 270: ['left', 'top'] };
  return curveMap[rot];
};

const checkFlow = () => {
  grid.value.forEach(row => row.forEach(c => c.filled = false));
  const stack = [];
  
  if (getConnections(grid.value[0][0]).includes('top')) {
    grid.value[0][0].filled = true;
    stack.push([0, 0]);
  }

  while (stack.length > 0) {
    const [r, c] = stack.pop();
    const conns = getConnections(grid.value[r][c]);
    conns.forEach(dir => {
      let nr = r, nc = c, opp;
      if (dir === 'top') { nr--; opp = 'bottom'; }
      if (dir === 'bottom') { nr++; opp = 'top'; }
      if (dir === 'left') { nc--; opp = 'right'; }
      if (dir === 'right') { nc++; opp = 'left'; }
      if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
        const nextCell = grid.value[nr][nc];
        if (!nextCell.filled && getConnections(nextCell).includes(opp)) {
          nextCell.filled = true;
          stack.push([nr, nc]);
        }
      }
    });
  }
  
  const lastCell = grid.value[rows-1][cols-1];
  win.value = lastCell.filled && getConnections(lastCell).includes('bottom');
};

const resetGame = () => { moves.value = 0; win.value = false; initGrid(); };
onMounted(initGrid);
</script>

<style scoped>
/* ESTILOS GERAIS */
.game-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.game-header, .game-content {
  max-width: 900px;
  margin: 0 auto;
  width: 100%;
}

.back-button {
  display: inline-block;
  margin-bottom: 0.5rem;
  padding: 0.4rem 0.8rem;
  background: #1e3c72;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}
.back-button:hover { background: #2e5090; transform: translateX(-4px); }

.game-header h1 { font-size: 2rem; color: #1e3c72; margin-bottom: 0.5rem; }
.game-header p { font-size: 1rem; color: #666; }

section {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  margin-bottom: 1.5rem;
}
section h2 { color: #1e3c72; margin-bottom: 0.8rem; font-size: 1.3rem; }
section p { color: #555; line-height: 1.5; margin-bottom: 0.5rem; font-size: 0.95rem; }

/* ÁREA DO JOGO */
.game-area {
  background: #f8f9fa;
  padding: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* --- CONTROLE DE TAMANHO AQUI --- */
.pipe-game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 340px; /* <--- DIMINUÍDO DE 450PX PARA 340PX */
}

.game-stats {
  margin-bottom: 1rem;
  font-size: 1.1rem;
  color: #1e3c72;
}

.board-wrapper {
  position: relative;
  width: 100%;
  margin: 20px 0; 
}

.board {
  background: #dfe6e9;
  padding: 5px; /* Padding menor */
  border-radius: 10px;
  box-shadow: 0 6px 15px rgba(0,0,0,0.15);
  position: relative;
  z-index: 2;
  border: 3px solid #b2bec3;
}

/* --- CONECTORES AJUSTADOS --- */
/* --- CONECTORES (AJUSTE DE CENTRALIZAÇÃO) --- */
.connector {
  position: absolute;
  width: 46px; 
  height: 30px;
  display: flex;
  justify-content: center;
  z-index: 1;
}

/* Explicação:
   O board tem 4 colunas. 100% / 4 = 25% por coluna.
   O centro da 1ª coluna está em 12.5% (25 / 2).
   Usamos calc() para considerar os 5px de padding e 3px de border do board.
*/

.connector.start {
  top: -24px; 
  /* Centraliza na 1ª coluna descontando as bordas do board */
  left: calc(12.5% + 4px); 
  transform: translateX(-50%);
}

.connector.end {
  bottom: -24px; 
  /* Centraliza na última coluna (87.5%) descontando as bordas */
  right: calc(12.5% + 4px); 
  transform: translateX(50%);
}
.pipe-stub {
  width: 30px; /* Largura interna menor */
  height: 100%;
  background: #72cc42;
  border-left: 5px solid #468e28;
  border-right: 5px solid #468e28;
  position: relative;
}

.water-flow { width: 100%; height: 100%; background: #2c3e50; transition: background 0.3s; opacity: 0.8; }
.water-flow.active { background: #00a8ff; box-shadow: 0 0 8px #00a8ff; opacity: 1; }

.connector.start .pipe-stub { border-radius: 4px 4px 0 0; border-top: 5px solid #468e28; }
.connector.end .pipe-stub { border-radius: 0 0 4px 4px; border-bottom: 5px solid #468e28; }

/* CÉLULAS */
.tile-cell {
  position: relative; width: 100%; aspect-ratio: 1/1; cursor: pointer;
  background: #ecf0f1; border: 1px solid #bdc3c7; overflow: hidden;
}
.tile-cell:hover { background: #fff; }
.tile-face {
  position: absolute; inset: 0; pointer-events: none; z-index: 10;
  box-shadow: inset 2px 2px 4px rgba(255,255,255,0.8), inset -2px -2px 4px rgba(0,0,0,0.05);
}

.pipe-svg { width: 100%; height: 100%; display: block; }
.p-outline { stroke: #468e28; stroke-width: 50; }
.p-body { stroke: #72cc42; stroke-width: 38; }
.p-hollow { stroke: #2d3436; stroke-width: 20; }
.p-water { stroke: #00a8ff; stroke-width: 20; opacity: 0; transition: opacity 0.4s ease; }
.water-layer.flowing .p-water { opacity: 1; }

/* AÇÕES */
.game-actions { margin-top: 1.5rem; }
.action-btn {
  background: #1e3c72; color: white; border: none; padding: 8px 20px;
  border-radius: 50px; cursor: pointer; font-weight: 600; font-size: 0.95rem;
  transition: all 0.3s; box-shadow: 0 3px 10px rgba(30, 60, 114, 0.3);
  display: flex; align-items: center; gap: 6px;
}
.action-btn:hover { background: #2e5090; transform: translateY(-2px); }

/* INFO GRID */
.game-info {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* Força 3 colunas para ficar compacto */
  gap: 1rem;
  padding: 0; background: transparent; box-shadow: none; margin-bottom: 0;
}
.info-card {
  background: white; padding: 1rem; border-radius: 10px;
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08); text-align: center;
}
.info-card h3 { color: #1e3c72; margin-bottom: 0.4rem; font-size: 1rem; }
.info-card p { color: #666; font-size: 0.85rem; margin: 0; }

/* MODAL */
.win-modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.6); z-index: 100;
  display: flex; justify-content: center; align-items: center; backdrop-filter: blur(4px); padding: 20px;
}
.modal-content { 
  background: white; padding: 2rem; border-radius: 16px; text-align: center; 
  max-width: 350px; width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
.modal-content h1 { color: #1e3c72; margin-bottom: 1rem; font-size: 1.8rem; }
.modal-btn {
  background: #1e3c72; color: white; border: none; padding: 10px 24px;
  border-radius: 8px; font-size: 1rem; cursor: pointer; font-weight: bold;
}

@media (max-width: 600px) {
  .game-info { grid-template-columns: 1fr; } /* Empilha infos no mobile */
  .game-page { padding: 1rem; }
}
</style>