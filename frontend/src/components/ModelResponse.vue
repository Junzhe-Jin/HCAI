<template>
    <div class="response">
      <p>{{ response }}</p>
    </div>
  </template>
  
  <script setup>
  defineProps({
    response: String
  });
  </script>
  
  <style scoped>
  .response {
    font-family: 'PalanquinDark';
    font-size: 20px;
    line-height: 1.7;
  }
  </style>
  