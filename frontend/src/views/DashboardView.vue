<script setup>
import Button from '@/components/Button.vue'
import { ref, onMounted } from 'vue'
import { getSummary } from '@/services/dashboard_service'

const summary = ref(null)
const loading = ref(true)
const error = ref(null)

async function loadDashboard() {
  try {
    summary.value = await getSummary()
  } catch (err) {
    error.value = err
    console.error(err)
  } finally {
    loading.value = false
  }
}

onMounted(loadDashboard)
</script>

<template>
  <div>
    <main
      class="p-section md:p-page transition-all duration-300"
      :class="isOpen ? 'md:ml-64' : 'ml-0'"
    >
      <div class="bg-surface p-6 rounded-card shadow-card border border-border mt-4">
        <h1 class="text-2xl font-bold text-txt-primary mb-2">Desktop Dashboard Admin</h1>
        <p class="text-txt-secondary">
          Cobalah me-resize browsermu (Desktop / Mobile) dan klik tombol Hamburger di atas. Desain
          ini sudah disesuaikan dengan Tailwind config khusus milikmu (menggunakan warna
          <code>bg-canvas</code>, <code>bg-surface</code>, dll).
        </p>
      </div>
    </main>
  </div>
</template>
