<template>
  <DashboardAdminLayoutMobile v-if="isMobile" />
  <DashboardAdminLayout v-else />
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

import DashboardAdminLayout from './DashboardAdminLayout.vue'
import DashboardAdminLayoutMobile from './DashboardAdminLayoutMobile.vue'

const isMobile = ref(false)

function checkScreen() {
  isMobile.value = window.innerWidth < 768
}

onMounted(() => {
  checkScreen()
  window.addEventListener('resize', checkScreen)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkScreen)
})
</script>