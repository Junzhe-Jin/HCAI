<template>
  <div class="suggestions">
    <div
      v-for="(sug, idx) in suggestions"
      :key="idx"
      class="suggestion"
    >
      <span class="label">Suggestion {{ idx + 1 }}: </span><span class="suggestion-text">{{ sug }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  suggestions: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.suggestions {
  margin-top: 24px;
  margin-bottom: 12px;
}

.suggestion {
  color: #0db4fd;
  font-weight: bold;
  font-size: 18px;
  margin-bottom: 6px;
  line-height: 1.7;
  font-family: "Palanquin Dark";
}

.label {
  color: #0db4fd;
  font-weight: 900;
  font-size: 18px;
}

.suggestion-text {
  color: #033f92;
  font-size: 16px;
  line-height: 1.7;
  font-family: "Palanquin";
}
</style>

