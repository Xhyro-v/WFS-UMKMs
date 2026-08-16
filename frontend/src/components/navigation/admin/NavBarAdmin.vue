<template>
    <header class="bg-surface border-b border-border h-16 sticky top-0 z-50 shadow-sm">
      <div class="flex items-center justify-between h-full px-4 md:px-page">
        <!-- Bagian Kiri: Hamburger & Brand -->
        <div class="flex items-center gap-4">
          <button
  @click="emit('toggle')"
  class="p-2 rounded-button text-txt-secondary hover:text-txt-primary hover:bg-canvas transition-colors focus:outline-none focus:ring-2 focus:ring-primary-500"
  aria-label="Toggle Menu"
>
            <!-- Ikon Hamburger -->
            <svg
              v-if="!isOpen"
              class="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
            <!-- Ikon Close (X) -->
            <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>

          <span class="font-bold text-lg text-txt-primary tracking-wide">BrandLogo</span>
        </div>

        <!-- Bagian Kanan: Aksi (Contoh) -->
        <div class="flex items-center gap-4">
          <button
            class="px-5 py-2 bg-primary-500 text-surface rounded-button font-medium hover:bg-primary-600 transition-colors shadow-sm"
          >
            Masuk
          </button>
        </div>
      </div>
    </header>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  isOpen: {
    type: Boolean,
    default: false,
  },
})

// State untuk mengatur buka/tutup menu
const emit = defineEmits(['toggle'])

</script>
