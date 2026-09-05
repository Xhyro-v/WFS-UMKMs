<script setup>
import { computed, onMounted, ref } from 'vue'
import {
  BadgeCheck,
  CircleCheck,
  Clock3,
  CupSoda,
  LayoutList,
  Utensils,
} from '@lucide/vue'
import { getSummary } from '@/services/dashboard_service'

const summary = ref(null)
const loading = ref(true)
const error = ref(null)

const menuSummary = computed(() => summary.value?.menu ?? null)

const menuMetrics = computed(() => [
  {
    label: 'Total menu',
    value: menuSummary.value?.total,
    icon: LayoutList,
    tone: 'bg-primary-50 text-primary-700',
  },
  {
    label: 'Menu makanan',
    value: menuSummary.value?.makanan?.total,
    icon: Utensils,
    tone: 'bg-amber-50 text-amber-700',
  },
  {
    label: 'Menu minuman',
    value: menuSummary.value?.minuman?.total,
    icon: CupSoda,
    tone: 'bg-sky-50 text-sky-700',
  },
  {
    label: 'Sudah dipublikasi',
    value: menuSummary.value?.published,
    icon: BadgeCheck,
    tone: 'bg-emerald-50 text-emerald-700',
  },
])

const publicationMetrics = computed(() => [
  {
    label: 'Makanan',
    published: menuSummary.value?.makanan?.published,
    unpublished: menuSummary.value?.makanan?.unpublished,
    icon: Utensils,
  },
  {
    label: 'Minuman',
    published: menuSummary.value?.minuman?.published,
    unpublished: menuSummary.value?.minuman?.unpublished,
    icon: CupSoda,
  },
])

function displayValue(value) {
  return value === undefined || value === null ? 'Hubungkan backend' : value
}

async function loadDashboard() {
  loading.value = true
  error.value = null

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
  <main class="p-section md:p-page transition-all duration-300">
    <header class="mb-6">
      <p class="text-sm font-semibold uppercase tracking-wide text-primary-600">Admin</p>
      <h1 class="mt-1 text-2xl font-bold text-txt-primary md:text-3xl">Dashboard</h1>
      <p class="mt-2 text-txt-secondary">Ringkasan menu makanan dan minuman.</p>
    </header>

    <section class="bg-surface p-5 rounded-card shadow-card border border-border md:p-6">
      <div class="flex flex-col gap-2 border-b border-border pb-5 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <h2 class="text-xl font-bold text-txt-primary">Ringkasan menu</h2>
          <p class="mt-1 text-sm text-txt-secondary">Data terbaru dari katalog menu.</p>
        </div>
        <span
          class="w-fit rounded-full bg-primary-50 px-3 py-1 text-xs font-semibold text-primary-700"
        >
          {{ loading ? 'Memuat data' : error ? 'Belum terhubung' : 'Terhubung' }}
        </span>
      </div>

      <div v-if="loading" class="mt-5 grid grid-cols-1 gap-3 sm:grid-cols-2 xl:grid-cols-4">
        <div
          v-for="index in 4"
          :key="index"
          class="h-28 animate-pulse rounded-button border border-border bg-canvas"
        ></div>
      </div>

      <div v-else class="mt-5">
        <div class="grid grid-cols-1 gap-3 sm:grid-cols-2 xl:grid-cols-4">
          <article
            v-for="metric in menuMetrics"
            :key="metric.label"
            class="rounded-button border border-border p-4"
          >
            <div class="flex items-start justify-between gap-3">
              <div class="flex min-w-0 items-center gap-2">
                <span
                  :class="['flex h-8 w-8 shrink-0 items-center justify-center rounded-button', metric.tone]"
                >
                  <component :is="metric.icon" :size="16" :stroke-width="2" aria-hidden="true" />
                </span>
                <p class="text-sm font-medium text-txt-secondary">{{ metric.label }}</p>
              </div>
            </div>
            <p class="mt-4 break-words text-2xl font-bold text-txt-primary">
              {{ displayValue(metric.value) }}
            </p>
          </article>
        </div>

        <div class="mt-6 border-t border-border pt-5">
          <h3 class="text-sm font-bold text-txt-primary">Status publikasi</h3>
          <div class="mt-3 grid grid-cols-1 gap-3 md:grid-cols-2">
            <article
              v-for="metric in publicationMetrics"
              :key="metric.label"
              class="rounded-button bg-canvas p-4"
            >
              <div class="flex items-center gap-2">
                <component
                  :is="metric.icon"
                  :size="18"
                  :stroke-width="2"
                  class="text-txt-secondary"
                  aria-hidden="true"
                />
                <p class="font-semibold text-txt-primary">{{ metric.label }}</p>
              </div>
              <div class="mt-3 flex flex-wrap gap-x-5 gap-y-2 text-sm">
                <span class="flex items-center gap-1.5 text-emerald-700">
                  <CircleCheck :size="15" :stroke-width="2" aria-hidden="true" />
                  Dipublikasi: <strong>{{ displayValue(metric.published) }}</strong>
                </span>
                <span class="flex items-center gap-1.5 text-amber-700">
                  <Clock3 :size="15" :stroke-width="2" aria-hidden="true" />
                  Belum dipublikasi: <strong>{{ displayValue(metric.unpublished) }}</strong>
                </span>
              </div>
            </article>
          </div>
        </div>
      </div>

      <div v-if="error" class="mt-4 flex flex-col gap-3 rounded-button bg-red-50 p-4 sm:flex-row sm:items-center sm:justify-between">
        <p class="text-sm text-red-700">Data belum dapat dimuat. Hubungkan backend untuk melihat angka menu.</p>
        <button
          type="button"
          class="rounded-button bg-primary-600 px-4 py-2 text-sm font-semibold text-white hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
          @click="loadDashboard"
        >
          Coba lagi
        </button>
      </div>
    </section>
  </main>
</template>
