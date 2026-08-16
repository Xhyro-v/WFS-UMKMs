<template>
  <div class="min-h-screen bg-canvas text-txt-primary font-sans relative overflow-x-hidden">
    <!-- ================= NAVBAR ================= -->
    <header class="bg-surface border-b border-border h-16 sticky top-0 z-50 shadow-sm">
      <div class="flex items-center justify-between h-full px-4 md:px-page">
        <!-- Bagian Kiri: Hamburger & Brand -->
        <div class="flex items-center gap-4">
          <button
            @click="isOpen = !isOpen"
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
  </div>
  <transition
    enter-active-class="transition ease-out duration-200"
    enter-from-class="opacity-0 -translate-y-4 scale-95"
    enter-to-class="opacity-100 translate-y-0 scale-100"
    leave-active-class="transition ease-in duration-150"
    leave-from-class="opacity-100 translate-y-0 scale-100"
    leave-to-class="opacity-0 -translate-y-2 scale-95"
  >
    <div
      v-if="isOpen"
      class="md:hidden absolute top-20 left-4 w-56 bg-surface border border-border shadow-card rounded-card z-40 overflow-hidden"
    >
      <nav class="flex flex-col p-2 space-y-1">
        <a
          v-for="item in menuItems"
          :key="item.name"
          href="#"
          class="block px-4 py-2.5 rounded-button text-txt-secondary hover:bg-primary-50 hover:text-primary-700 transition-colors font-medium text-sm"
        >
          {{ item.name }}
        </a>
      </nav>
    </div>
  </transition>
  <div v-if="isOpen" @click="isOpen = false" class="md:hidden fixed inset-0 z-30"></div>
</template>

<script setup>
import { ref } from 'vue'
const isOpen = ref(false)
const menuItems = ref([
  { name: 'Dashboard' },
  { name: 'Menu' },
  { name: 'Content' },
  { name: 'Gallery' },
])
</script>
