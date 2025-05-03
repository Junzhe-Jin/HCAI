// frontend/src/api/api.js
import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  timeout: 30000,
})

export const analyzePrompt = async (prompt, createAnswer = false) => {
  // DEV 模式下使用 mock
  if (import.meta.env.DEV) {
    const { default: allMocks } = await import('@/mock/analyze_result.json')
    // 在扁平数组中找匹配 prompt 的项，找不到就返回第一条
    const match = allMocks.find(item => item.prompt.trim() === prompt.trim())
    const data = match || allMocks[0]
    return new Promise(resolve => {
      setTimeout(() => resolve({ data }), 300)
    })
  }

  // 真正环境下调用后端
  const apiKey = sessionStorage.getItem('openai_api_key')
  return instance.post('/analyze', {
    prompt,
    api_key: apiKey,
    create_answer: createAnswer
  })
}
