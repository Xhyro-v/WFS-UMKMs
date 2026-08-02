<script setup>
import { ref } from "vue";
import { login } from "@/services/auth_service";

const email = ref("");
const password = ref("");

async function handleLogin() {
  try {
    const result = await login(
      email.value,
      password.value
    );

    console.log(result);
  }

  catch (err) {
    console.error(err);
  }
}
</script>

<template>

<h1>Login</h1>

<input
v-model="email"
placeholder="Email"
/>

<input
type="password"
v-model="password"
placeholder="Password"
/>

<button @click="handleLogin">
Login
</button>

</template>