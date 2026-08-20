<template>
  <aside
    class="hidden md:flex flex-col fixed top-16 left-0 h-[calc(100vh-4rem)] w-64 bg-surface border-r border-border transition-transform duration-300 ease-in-out z-40"
    :class="props.isOpen ? 'translate-x-0' : '-translate-x-full'"
  >
    <nav class="flex-1 p-4 space-y-2 overflow-y-auto">
      <a
        v-for="item in menuItems"
        :key="item.name"
        href="#"
        class="block px-4 py-3 rounded-button text-txt-secondary hover:bg-primary-50 hover:text-primary-700 transition-colors font-medium"
      >
        {{ item.name }}
      </a>
    </nav>
  </aside>

  <div 
  v-if="props.isOpen"
  @click="emit('close')"
  class="hidden md:block fixed inset-0 bg-txt-primary/5 z-30 top-16"
></div>
</template>

<script setup>
const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['close'])

const menuItems = [
  { name: 'Dashboard', href: '/dashboard' },
  { name: 'Projects', href: '#' },
  { name: 'Analytics', href: '#' },
  { name: 'Settings', href: '#' },
]
</script>