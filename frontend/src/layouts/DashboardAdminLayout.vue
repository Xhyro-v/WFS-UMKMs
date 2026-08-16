<template>
  <NavBarAdmin
    :is-open="isOpen"
    @toggle="isOpen = !isOpen"
  />

  <SideBarAdmin
    :is-open="isOpen"
    @close="isOpen = false"
  />

  <main>
    <RouterView />
  </main>
</template>

<script setup>
import { ref } from 'vue'

import NavBarAdmin from '@/components/navigation/admin/NavBarAdmin.vue'
import SideBarAdmin from '@/components/navigation/admin/SideBarAdmin.vue'

const isOpen = ref(false)
</script>