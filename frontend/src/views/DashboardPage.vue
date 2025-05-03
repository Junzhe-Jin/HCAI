<template>
  <div class="container">
    <!-- 左侧 -->
    <aside class="left-panel">
      <img src="@/assets/logo.png" class="logo" />

      <RadarChart :scores="scores" />

      <select v-model="selectedDimension" class="dimension-select palanquindark-20">
        <option
          v-for="dim in dimensions"
          :key="dim"
          :value="dim"
        >{{ dim }}</option>
      </select>

      <div class="reason-box palanquin-20">
        {{ reason[selectedDimension.toLowerCase().replace(' ', '_')] }}
      </div>
    </aside>

    <!-- 右侧 -->
    <section class="right-panel">
      <div class="top-bar">
        <img src="@/assets/justified-text.png" class="settings-btn" @click="showSettings = !showSettings" />
        <img src="@/assets/user.png" class="avatar" />
        <div v-if="showSettings" class="settings-dropdown">
          <div @click="toggleTheme">切换亮度</div>
          <div @click="logout">退出系统</div>
        </div>
      </div>
      <div class="separator"></div>

      <div class="content-area">
        <div class="right-align">
          <div v-if="prompt" class="prompt-bubble">{{ prompt }}</div>
        </div>
        <div v-if="createAnswer && modelResponse" class="model-bubble">{{ modelResponse }}</div>
        <div v-if="createAnswer && modelResponse" class="divider"></div>
        <Suggestions :suggestions="suggestions" />
      </div>
      <div class="amb-container">
        <AmbiguityViewer
          :tokens="tokens"
          :ambiguousWords="ambiguousWords"
        />
      </div>
      <PromptInput
        v-model="prompt"
        :loading="loading"
        :createAnswer="createAnswer"
        @submit="onSubmit"
        @toggle-create="onToggleCreate"
      />

      <div v-if="loading" class="loading-overlay">
        <div class="spinner"></div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import RadarChart from '@/components/RadarChart.vue'
import ModelResponse from '@/components/ModelResponse.vue'
import Suggestions from '@/components/Suggestions.vue'
import AmbiguityViewer from '@/components/AmbiguityViewer.vue'
import PromptInput from '@/components/PromptInput.vue'
import { analyzePrompt } from '@/api/api'

import { useRouter } from 'vue-router'

const router = useRouter()

const prompt = ref('')
const loading = ref(false)
const tokens = ref([])
const scores = ref({
  clarity: 0,
  controllability: 0,
  goal_specificity: 0,
  ambiguity: 0,
  readability: 0
})
const reason = ref({})
const suggestions = ref([])
const modelResponse = ref('')
const ambiguousWords = ref([])

const createAnswer = ref(false)
const dimensions = [
  'Clarity',
  'Controllability',
  'Goal Specificity',
  'Ambiguity',
  'Readability'
]
const selectedDimension = ref('Clarity')
const showSettings = ref(false)
const isDark = ref(false)

function onToggleCreate(val) {
  createAnswer.value = val
}

async function onSubmit() {
  if (!prompt.value) return
  loading.value = true
  try {
    const res = await analyzePrompt(prompt.value, createAnswer.value)
    tokens.value = res.data.tokens
    scores.value = res.data.scores
    reason.value = res.data.reason
    suggestions.value = res.data.suggestions
    ambiguousWords.value = res.data.keywords || []
    modelResponse.value = res.data.model_response || ''
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}

function toggleTheme() {
  isDark.value = !isDark.value
  document.body.style.filter = isDark.value ? 'brightness(0.7)' : 'brightness(1)'
}

function logout() {
  router.push('/')
}
</script>

<style scoped>
@import '@/assets/fonts/fonts.css';

.container {
  display: flex;
  width: 1440px;
  height: 1024px;
  background-color: #e6f3fb;
}
.amb-container{
  width:910px;
    height: 75px;
    position: relative;
    left: -15px;
    border-radius: 16px;
    box-sizing: border-box;
    margin: 20px auto 40px;
}
.left-panel {
  position: relative;
  top: -70px;
  height: 700px;

  padding: 40px 15px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.logo {
  position: relative;
  left: -140px;
  width: 207px;
  height: 102px;
}

.radar-card {
  position: relative;
}

.dimension-select {
  width: 430px;
  height: 40px;
  margin-top: 12px;
  padding-left: 8px;
  font-size: 18px;
  border-radius: 6px;
  border: none;
  color: #033f92;
}

.reason-box {
  width: 406px;
  height: 325px;
  background: #fff;
  margin-top: 12px;
  padding: 12px;
  border-radius: 6px;
  overflow-y: auto;
  font-size: 18px;
  line-height: 32px;
  color: #4d77b2;
}

.right-panel {
  flex: 1;
  position: relative;
  background: #fff;
  display: flex;
  flex-direction: column;
}
.top-bar {
  position: relative;
  height: 45px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: 16px 20px;
}
.settings-btn {
  width: 45px;
  height: 45px;
  margin-right: 23px;
  cursor: pointer;
}
.avatar {
  width: 35px;
  height: 35px;
  margin-right: 23px;
}

.separator {
  height: 3px;
  background: #F8F4F4;
  width: 980px;
}
.content-area {
  flex: 1;
  margin: 0 60px;
  padding:  0 20px;
  overflow-y: auto;
}
.divider {
  height: 3px;
  background: rgba(0,0,0,0.54);
  margin: 16px 0;
}

.loading-overlay {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: rgba(255,255,255,0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
}
.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #00ADFD;
  border-radius: 50%;
  width: 40px; height: 40px;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}

.palanquin-20 { font-family: 'Palanquin', sans-serif; font-size: 20px; }

.right-align {
  width: 100%;
  text-align: right;
}

.prompt-bubble {
  background: #E6F3FB;
  color: #333;
  border-radius: 16px;
  padding: 12px 20px;
  display: inline-block;
  margin-top: 10px;
  margin-bottom: 8px;
  font-family: 'Palanquin', sans-serif;
  font-size: 18px;
}
.model-bubble {
  color: #000;
  border-radius: 16px;
  max-width: 100%;
  align-self: flex-start;
  margin-bottom: 8px;
  font-family: 'Palanquin', sans-serif;
  font-size: 18px;
}
.settings-dropdown {
  position: absolute;
  top: 60px; right: 40px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  z-index: 10;
  font-family: 'Palanquin', sans-serif;
  font-size: 18px;
}
.settings-dropdown > div {
  padding: 12px 24px;
  cursor: pointer;
}
.settings-dropdown > div:hover {
  background: #E6F3FB;
}
::-webkit-scrollbar {
  width: 8px;
  background: #F0F0F0;
}
::-webkit-scrollbar-thumb {
  background: #B0B0B0;
  border-radius: 4px;
}
</style>
