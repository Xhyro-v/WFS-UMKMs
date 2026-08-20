<script setup>
import { ref } from "vue";
import Button from "@/components/Button.vue";
import { login } from "@/services/auth_service";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const router = useRouter();
const authStore = useAuthStore();
  
async function handleLogin() {
    try {
        const result = await login(email.value, password.value);

        authStore.setToken(result.access_token);

        router.push("/dashboard");
    } catch (err) {
        console.error(err);
    }
}
</script>

<template>
    <main
        class="min-h-screen flex items-center justify-center bg-canvas p-page font-sans"
    >
        <section
            class="w-full max-w-md bg-surface border border-border rounded-card shadow-card p-page"
        >
            <header class="text-center mb-6">
                <h1 class="text-2xl font-bold tracking-tight text-txt-primary">
                    Sign In
                </h1>
            </header>

            <form
                @submit.prevent="handleLogin"
                class="flex flex-col gap-section"
            >
                <div>
                    <label
                        for="email"
                        class="block text-sm font-medium text-txt-primary mb-1.5"
                        >Email</label
                    >
                    <input
                        v-model="email"
                        id="email"
                        type="email"
                        autocomplete="email"
                        required
                        class="w-full rounded-button border border-border bg-surface px-3.5 py-2 text-txt-primary placeholder:text-txt-secondary focus:outline-none focus:ring-2 focus:ring-primary-focus"
                    />
                </div>

                <div>
                    <label
                        for="password"
                        class="block text-sm font-medium text-txt-primary mb-1.5"
                        >Password</label
                    >
                    <input
                        v-model="password"
                        id="password"
                        type="password"
                        autocomplete="current-password"
                        required
                        class="w-full rounded-button border border-border bg-surface px-3.5 py-2 text-txt-primary placeholder:text-txt-secondary focus:outline-none focus:ring-2 focus:ring-primary-focus"
                    />
                </div>

                <div class="mt-2">
                    <Button type="submit">
                        Sign in
                    </Button>
                </div>
            </form>
        </section>
    </main>
</template>
