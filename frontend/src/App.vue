<template>
  <router-view />
</template>

<script setup>
</script>

<style>

/* 重置body样式，应用Palanquin字体 */
body {
  margin: 0;
  font-family: 'Palanquin', 'sans-serif';
  background-color: #f4f6f8;
}

/* 统一按钮和输入框默认字体 */
button, input, select, textarea {
  font-family: 'Palanquin', 'sans-serif';
}

/* 加粗用PalanquinDark */
.bold-text {
  font-family: 'PalanquinDark', 'sans-serif';
  font-weight: bold;
}
</style>

  