<template>
  <div class="amb-viewer">
    <h2 class="amb-title">Ambiguous Analysis</h2>
    <div class="text-box">
      <span
        v-for="(word, idx) in tokens"
        :key="idx"
        :class="{ highlight: ambiguousWords.includes(word.text) }"
      >
        {{ word.text }}&nbsp;
      </span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  tokens: {
    type: Array,
    default: () => []
  },
  ambiguousWords: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.amb-viewer {
  margin-top: 32px;
  margin-bottom: 0;
}

.amb-title {
  font-size: 20px;
  font-weight: bold;
  color: #033f92;
  margin-bottom: 8px;
}

.text-box {
  width: 100%;
  min-height: 32px;
  background: #F5F5F5;
  border-radius: 8px;
  padding: 12px 16px;
  font-size: 18px;
  color: #333;
  line-height: 1.7;
}

.highlight {
  color: #D7263D;
  font-weight: bold;
}
</style>
