<template>
  <div class="radar-card">
    <div class="chart-container">
      <Radar :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { Radar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
} from 'chart.js'
ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
)

import { computed } from 'vue'

const props = defineProps({
  scores: {
    type: Object,
    default: () => ({
      clarity: 7,
      controllability: 5,
      goal_specificity: 6,
      ambiguity: 8,
      readability: 6
    })
  }
})

const labels = [
  'Controllability',
  'Clarity',
  'Goal Specificity',
  'Ambiguity',
  'Readability'
]

const dataValues = computed(() =>
  labels.map((lbl) => {
    const key = lbl.toLowerCase().replace(' ', '_')
    return props.scores[key] ?? 0
  })
)

const chartData = computed(() => ({
  labels,
  datasets: [
    {
      data: dataValues.value,
      backgroundColor: 'rgba(13, 180, 253,0.3)',
      borderColor: 'rgba(13, 180, 253,0.5)',
      borderWidth: 1,
      pointBackgroundColor: 'rgba(255,165,0,0)',
      pointBorderColor: 'rgba(255,165,0,0)',
      pointRadius: 0
    }
  ]
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    r: {
      min: 0,
      max: 10,
      beginAtZero: true,
      angleLines: { color: '#222', lineWidth: 0.5 },
      grid: { color: '#ddd', circular: true },
      pointLabels: { 
        color: '#003366', 
        font: { size: 14, family: 'PalanquinDark' } 
      },
      ticks: { 
        display: true, 
        stepSize: 2, 
        color: '#222', 
        font: { size: 12, family: 'PalanquinDark' },
        backdropColor: 'transparent'
      }
    }
  },
  plugins: {
    legend: { display: false },
    tooltip: { enabled: false }
  }
}
</script>

<style scoped>
.radar-card {
  position: relative;
  width: 424px;
  height: 400px;
  background: #fff;
  padding: 0;
  text-align: center;
  border-radius: 8px;
  /*box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);*/
}

.chart-container {
  position: relative;
  height: 100%;
  width: 100%;
}
</style>