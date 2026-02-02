<template>
  <div class="game">
    <h2>Pipe Connect 💧</h2>

    <div class="grid">
      <div
        v-for="(cell, index) in grid.flat()"
        :key="index"
        class="cell"
        @click="rotate(index)"
      >
        <svg viewBox="0 0 100 100"
             :style="{ transform: `rotate(${cell.rotation}deg)` }">

          <!-- CANO RETO -->
          <line v-if="cell.type === 'straight'"
                x1="50" y1="0" x2="50" y2="100"
                :class="cell.filled ? 'water' : 'pipe'" />

          <!-- CANO CURVA -->
          <path v-if="cell.type === 'curve'"
                d="M50 100 V50 H100"
                fill="none"
                :class="cell.filled ? 'water' : 'pipe'" />

        </svg>
      </div>
    </div>

    <p v-if="win">🎉 Água conectada!</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rows: 4,
      cols: 4,
      win: false,
      grid: [
        [
          { type: 'straight', rotation: 0, filled: false },
          { type: 'curve', rotation: 90, filled: false },
          { type: 'straight', rotation: 0, filled: false },
          { type: 'curve', rotation: 180, filled: false }
        ],
        [
          { type: 'curve', rotation: 0, filled: false },
          { type: 'straight', rotation: 90, filled: false },
          { type: 'curve', rotation: 270, filled: false },
          { type: 'straight', rotation: 0, filled: false }
        ],
        [
          { type: 'straight', rotation: 0, filled: false },
          { type: 'curve', rotation: 90, filled: false },
          { type: 'straight', rotation: 0, filled: false },
          { type: 'curve', rotation: 180, filled: false }
        ],
        [
          { type: 'curve', rotation: 0, filled: false },
          { type: 'straight', rotation: 90, filled: false },
          { type: 'curve', rotation: 270, filled: false },
          { type: 'straight', rotation: 0, filled: false }
        ]
      ]
    }
  },

  methods: {
    rotate(index) {
      const r = Math.floor(index / this.cols)
      const c = index % this.cols

      this.grid[r][c].rotation = (this.grid[r][c].rotation + 90) % 360
      this.checkFlow()
    },

    getConnections(cell) {
      const map = {
        straight: {
          0: ['top', 'bottom'],
          90: ['left', 'right'],
          180: ['top', 'bottom'],
          270: ['left', 'right']
        },
        curve: {
          0: ['bottom', 'right'],
          90: ['bottom', 'left'],
          180: ['top', 'left'],
          270: ['top', 'right']
        }
      }
      return map[cell.type][cell.rotation]
    },

    checkFlow() {
      // reset
      this.grid.flat().forEach(c => c.filled = false)

      const stack = [[0, 0]]
      this.grid[0][0].filled = true

      while (stack.length) {
        const [r, c] = stack.pop()
        const cell = this.grid[r][c]
        const conns = this.getConnections(cell)

        for (const dir of conns) {
          let nr = r, nc = c, opposite

          if (dir === 'top') { nr--; opposite = 'bottom' }
          if (dir === 'bottom') { nr++; opposite = 'top' }
          if (dir === 'left') { nc--; opposite = 'right' }
          if (dir === 'right') { nc++; opposite = 'left' }

          if (
            this.grid[nr]?.[nc] &&
            !this.grid[nr][nc].filled &&
            this.getConnections(this.grid[nr][nc]).includes(opposite)
          ) {
            this.grid[nr][nc].filled = true
            stack.push([nr, nc])
          }
        }
      }

      this.win = this.grid[this.rows - 1][this.cols - 1].filled
    }
  },

  mounted() {
    this.checkFlow()
  }
}
</script>

<style>
body {
  font-family: sans-serif;
}

.game {
  text-align: center;
}

.grid {
  display: grid;
  grid-template-columns: repeat(4, 80px);
  gap: 8px;
  justify-content: center;
}

.cell {
  width: 80px;
  height: 80px;
  background: #eee;
  cursor: pointer;
}

svg {
  width: 100%;
  height: 100%;
  transition: transform 0.2s;
}

.pipe {
  stroke: #555;
  stroke-width: 14;
  stroke-linecap: round;
}

.water {
  stroke: dodgerblue;
  stroke-width: 14;
  stroke-linecap: round;
}
</style>
