<template>
  <div class="login-wrapper">
    <div class="login-card">
      <h1 class="bold-text">🔐 SmartPrompt</h1>
      <p>Please enter your OpenAI API Key to begin</p>

      <input
        type="password"
        v-model="apiKey"
        placeholder="sk-..."
        class="api-input"
      />

      <button @click="submitKey" :disabled="!apiKey">Continue</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const apiKey = ref('')

function submitKey() {
  sessionStorage.setItem('openai_api_key', apiKey.value)
  router.push('/dashboard')
}
</script>

<style scoped>
@import '../assets/fonts/fonts.css'; /* 引入你的字体 */

.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #f4f6f8;
}

.login-card {
  background: #ffffff;
  padding: 40px 30px;
  border-radius: 10px;
  width: 400px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  text-align: center;
  font-family: 'Palanquin', sans-serif;
}

h1 {
  margin-bottom: 16px;
  font-size: 24px;
  color: #2f80ed;
}

.api-input {
  width: 100%;
  padding: 12px;
  margin: 20px 0;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

button {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  background-color: #2f80ed;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s ease;
  font-family: 'Palanquin', sans-serif;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
