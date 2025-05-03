<template>
  <div class="prompt-input">
    <textarea
      v-model="innerPrompt"
      :disabled="loading"
      placeholder="Type your prompt..."
      @input="autoResize"
      ref="textareaRef"
      style="overflow-y:auto;max-height:72px;min-height:32px;resize:none;"
    />
    <div class="buttons">
      <button
        class="create-btn"
        :class="{ active: createAnswer }"
        @click="toggleCreate"
      >
        Create Answer
      </button>
      <img
        src="@/assets/search.png"
        alt="Search"
        class="search-btn"
        @click="submit"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, nextTick } from 'vue'

const props = defineProps({
  modelValue: String,
  loading: Boolean,
  createAnswer: Boolean
})
const emit = defineEmits(['update:modelValue', 'submit', 'toggle-create'])

const innerPrompt = ref(props.modelValue || '')
const textareaRef = ref(null)

watch(
  () => props.modelValue,
  (v) => (innerPrompt.value = v)
)
watch(innerPrompt, (v) => emit('update:modelValue', v))

function submit() {
  if (!props.loading) emit('submit')
}
function toggleCreate() {
  emit('toggle-create', !props.createAnswer)
}
function autoResize() {
  nextTick(() => {
    const el = textareaRef.value
    if (el) {
      el.style.height = 'auto'
      let h = el.scrollHeight
      if (h > 72) h = 72 // 3行*24px
      el.style.height = h + 'px'
    }
  })
}
onMounted(autoResize)
</script>

<style scoped>
.prompt-input {
  
  width: 942px;
  height: 125px;
  background: rgba(167, 167, 167, 0.17);
  border-radius: 16px;
  padding: 20px 15px;
  box-sizing: border-box;
  margin: 20px auto 40px; 
}

.prompt-input textarea {
  width: 100%;
  border: none;
  background: transparent;
  resize: none;
  outline: none;
  font-family: 'Palanquin', sans-serif;
  font-size: 20px;
  line-height: 24px;
  overflow-y: auto;
  max-height: 72px;
  min-height: 32px;
}

.buttons {
  /*position: absolute;*/
  top: 8px;
  right: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}

.create-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 169px;
  height: 30px;
  background: #fff;
  border: 2px solid #fff;
  border-radius: 100px;
  font-family: 'PalanquinDark', sans-serif;
  font-size: 20px;
  color: #033F92;
  cursor: pointer;
}

.create-btn.active {
  border: 2px solid #e6f3fb;
}

.search-btn {
  width: 30px;
  height: 30px;
  cursor: pointer;
}
</style>

